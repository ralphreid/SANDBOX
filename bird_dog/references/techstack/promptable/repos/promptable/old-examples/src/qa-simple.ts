import dotenv from "dotenv";
dotenv.config();
import fs from "fs";
import chalk from "chalk";
import { OpenAI, Templates } from "@promptable/promptable";

const apiKey = process.env.OPENAI_API_KEY || "";

/**
 * Run QA on a Document
 *
 * Adds the entire document to the prompt.
 *
 * @param args
 */
const run = async (args: string[]) => {
  const openai = new OpenAI(apiKey);

  // Load the file
  const filepath = "./data/beyond-smart.txt";
  let doc = fs.readFileSync(filepath, "utf8");

  // Run the Question-Answer prompt on the document.
  const question = args[0] || "What does Paul Graham mean by Beyond Smart??";

  console.log(chalk.blue.bold("\nRunning Simple QA: beyond-smart.txt"));
  console.log(chalk.white(`Question: ${question}`));

  const qaPrompt = Templates.QA.build({
    document: doc,
    question,
  });

  const tokensUsed = openai.countTokens(qaPrompt.text);

  console.log(
    `\n${doc.substring(0, 100).trim()}...\n\n...${doc.slice(-100).trim()}\n` +
      chalk.gray(`${"Tokens: " + tokensUsed}`)
  );

  const { text: answer } = await openai.generate({
    text: qaPrompt.text,
  });

  console.log(chalk.greenBright(`Answer: ${answer}`));
};

export default run;
