"""
Base interface that all chains should implement
"""
import logging
import time
from abc import ABC, abstractmethod
from copy import deepcopy
from typing import Any, Dict, List, Optional

from autochain.agent.base_agent import BaseAgent
from autochain.agent.message import ChatMessageHistory, MessageType
from autochain.agent.structs import AgentAction, AgentFinish
from autochain.chain import constants
from autochain.memory.base import BaseMemory
from autochain.tools.base import Tool
from pydantic import BaseModel

logger = logging.getLogger(__name__)


class BaseChain(BaseModel, ABC):
    """
    Base interface that all chains should implement.
    Chain will standardize inputs and outputs, the main entry pointy is the run function.
    """

    agent: Optional[BaseAgent] = None
    memory: Optional[BaseMemory] = None
    last_query: str = ""
    max_iterations: Optional[int] = 15
    max_execution_time: Optional[float] = None

    def prep_inputs(self, user_query: str) -> Dict[str, str]:
        """Load conversation history from memory and prep inputs."""
        inputs = {
            constants.CONVERSATION_HISTORY: ChatMessageHistory(),
            constants.INTERMEDIATE_STEPS: [],
        }
        if self.memory is not None:
            intermediate_steps = self.memory.load_memory(
                constants.INTERMEDIATE_STEPS, []
            )
            self.memory.save_conversation(
                message=user_query, message_type=MessageType.UserMessage
            )

            inputs[constants.CONVERSATION_HISTORY] = deepcopy(
                self.memory.load_conversation()
            )
            inputs[constants.INTERMEDIATE_STEPS] = deepcopy(intermediate_steps)

        return inputs

    def prep_output(
        self,
        inputs: Dict[str, str],
        output: AgentFinish,
        return_only_outputs: bool = False,
    ) -> Dict[str, Any]:
        """Save conversation into memory and prep outputs."""
        output_dict = output.format_output()
        if self.memory is not None:
            self.memory.save_conversation(
                message=output.message, message_type=MessageType.AIMessage
            )
            self.memory.save_memory(
                key=constants.INTERMEDIATE_STEPS, value=output.intermediate_steps
            )

        if return_only_outputs:
            return output_dict
        else:
            return {**inputs, **output_dict}

    def run(
        self,
        user_query: str,
        return_only_outputs: bool = False,
    ) -> Dict[str, Any]:
        """Wrapper for _run function by formatting the input and outputs

        Args:
            user_query: user query
            return_only_outputs: boolean for whether to return only outputs in the
                response. If True, only new keys generated by this chain will be
                returned. If False, both input keys and new keys generated by this
                chain will be returned. Defaults to False.

        """
        inputs = self.prep_inputs(user_query)
        logger.info(f"\n Input to agent: {inputs}")
        try:
            output = self._run(inputs)
        except (KeyboardInterrupt, Exception) as e:
            raise e

        return self.prep_output(inputs, output, return_only_outputs)

    def _run(
        self,
        inputs: Dict[str, Any],
    ) -> AgentFinish:
        """
        Run inputs including user query and past conversation with agent and get response back
        calls take_next_step function to determine what should be the next step after
        collecting all the inputs and memorized contents
        """
        # Construct a mapping of tool name to tool for easy lookup
        name_to_tool_map = {tool.name: tool for tool in self.agent.tools}

        intermediate_steps: List[AgentAction] = inputs[constants.INTERMEDIATE_STEPS]

        # Let's start tracking the number of iterations and time elapsed
        iterations = 0
        time_elapsed = 0.0
        start_time = time.time()
        # We now enter the agent loop (until it returns something).
        while self._should_continue(iterations, time_elapsed):
            logger.info(f"\n Intermediate steps: {intermediate_steps}\n")
            next_step_output = self.should_answer(inputs=inputs)

            # if next_step_output is None which means should ask agent to answer and take next
            # step
            if not next_step_output:
                next_step_output = self.take_next_step(
                    name_to_tool_map,
                    inputs,
                )

            if isinstance(next_step_output, AgentFinish):
                next_step_output.intermediate_steps = intermediate_steps
                return next_step_output

            # stores action output into the conversation as FunctionMessage, which can be used by
            # OpenAIFunctionsAgent
            if isinstance(next_step_output, AgentAction):
                self.memory.save_conversation(
                    message=str(next_step_output.tool_output),
                    name=next_step_output.tool,
                    message_type=MessageType.FunctionMessage,
                )

            intermediate_steps.append(next_step_output)
            # update inputs
            inputs[constants.INTERMEDIATE_STEPS] = intermediate_steps
            inputs[constants.CONVERSATION_HISTORY] = self.memory.load_conversation()

            iterations += 1
            time_elapsed = time.time() - start_time

        # force the termination when shouldn't continue
        output = AgentFinish(
            message="Agent stopped due to iteration limit or time limit.",
            log="",
            intermediate_steps=intermediate_steps,
        )
        return output

    @abstractmethod
    def take_next_step(
        self,
        name_to_tool_map: Dict[str, Tool],
        inputs: Dict[str, str],
    ) -> (AgentFinish, AgentAction):
        """How agent determines the next step after observing the inputs and intermediate
        steps"""

    def _should_continue(self, iterations: int, time_elapsed: float) -> bool:
        if self.max_iterations is not None and iterations >= self.max_iterations:
            return False
        if (
            self.max_execution_time is not None
            and time_elapsed >= self.max_execution_time
        ):
            return False

        return True

    def should_answer(self, inputs) -> Optional[AgentFinish]:
        """
        Let agent determines if it should continue to answer questions
        or that is the end of the conversation
        Args:
            inputs: Dict contains user query and other memorized contents

        Returns:
            None if should answer
            AgentFinish if should NOT answer and respond to user with message
        """
        output = None
        # check if agent should answer this query
        last_query = (
            inputs[constants.CONVERSATION_HISTORY].get_latest_user_message().content
        )
        if self.last_query != last_query:
            output = self.agent.should_answer(**inputs)
            self.last_query = last_query

        return output
