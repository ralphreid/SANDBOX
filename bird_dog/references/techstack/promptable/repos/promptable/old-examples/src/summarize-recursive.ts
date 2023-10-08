import dotenv from "dotenv";
dotenv.config();
import fs from "fs";
import chalk from "chalk";
import { OpenAI, Templates } from "@promptable/promptable";

const apiKey = process.env.OPENAI_API_KEY || "";

/**
 * Run QA on a Document split into chunks.
 *
 * Each chunk is sent to the model as a separate request.
 *
 * @param args
 */
const run = async (args: string[]) => {
  const openai = new OpenAI(apiKey);

  // Load the file
  const filepath = "./data/startup-mistakes.txt";
  let doc = fs.readFileSync(filepath, "utf8");

  // Split the doc by the separator
  const separator = "\n\n";
  const texts = doc.split(separator);

  const chunkSize = 1000;
  const chunkOverlap = 100;

  // Create chunks to send to the model
  const chunks = texts.reduce((chunks: string[], text) => {
    let chunk = chunks.pop() || "";
    const chunkLength = openai.countTokens(chunk);
    if (chunkLength >= chunkSize + chunkOverlap) {
      chunks.push(chunk);
      chunk = "";
    }
    chunk = chunk === "" ? text : chunk + separator + text;
    chunks.push(chunk);
    return chunks;
  }, []);

  console.log(
    chalk.blue.bold("\nRunning Summarize Chunks: startup-mistakes.txt")
  );

  const summarizePromptTemplate = Templates.Summarize;

  // summarize each chunk
  const summaries = await Promise.all(
    chunks.map((chunk) => {
      const summarizePrompt = summarizePromptTemplate.build(
        {
          document: chunk,
        },
        {
          max_tokens: 1000,
        }
      );

      return openai.generate(summarizePrompt);
    })
  );

  // summarize all summaries
  const summariesStr = summaries.reduce(
    (acc, sum, i) => acc + separator + `${sum.text}`,
    ``
  );

  const { text: finalSummary } = await openai.generate(
    summarizePromptTemplate.build({
      document: summariesStr,
    })
  );

  console.log(summarizePromptTemplate.build({ document: summariesStr }));
  console.log(chalk.greenBright(finalSummary));
};

export default run;
