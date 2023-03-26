# RuPert
RuPert is a LLM trained chatbot fine-tuned on examples and non-examples of restrictive practices as understood by the NDIS. 

To run the program download the files, and add your own API key to RuPertGUI.py, then run RuPertGUI.py :)

Information on files:
- RPExamples.JSON: first draft of restrictive practice examples in JSON format
- RuPertData2.csv: second draft of formatting prompts and completions in CSV format
- RuPertData3.csv: third draft. This file contains varied language and gives the LLM more realistic training data
- RuPertData3_prepared.jsonl: RuPertData3 transformed using OpenAI CLI tool

Images: Some screenshots of the program running

GUI: Lightweight python script to process prompts and responses