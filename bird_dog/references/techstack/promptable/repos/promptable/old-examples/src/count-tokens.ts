import chalk from "chalk";
import { Loaders, OpenAI, Templates, Documents } from "@promptable/promptable";

const apiKey = process.env.OPENAI_API_KEY || "";

/**
 * Simple example of using the OpenAI API count the tokens used in a prompt
 */
export default async function run(args: string[]) {
  const openai = new OpenAI(apiKey);

  const loader = new Loaders.FileLoader();
  const docs = await loader.loadTexts(["./data/startup-mistakes.txt"]);

  const prompt = Templates.QA.build({
    document: docs[0].text,
    question: "",
  });

  const tokensUsed = openai.countTokens(prompt.text);

  console.log(chalk.white(`Token Count`), chalk.green(tokensUsed));
}
