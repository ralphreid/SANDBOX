import { loadPromptablePrompts } from "@promptable/promptable";
const run = async (args: string[]) => {
  const myPrompts = await loadPromptablePrompts({
    prompts: [
      {
        id: "cleh66so00quci7ehv1t1tyq2",
      },
    ],
  });
};

export default run;
