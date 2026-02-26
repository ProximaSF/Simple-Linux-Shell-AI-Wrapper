import os
import time
import json
import boto3
from dotenv import load_dotenv
from botocore.exceptions import ClientError

import sys
from argparse import ArgumentParser

load_dotenv()
API_KEY = os.getenv("AWS_BEARER_TOKEN_BEDROCK")
MODEL_ID = "deepseek.v3.2"
LOG_FILE = os.getenv("LOG_FILE")

class AI_Assistant:
    def __init__(self, prompt, token_limit):
        self.prompt = prompt
        self.token_limit = token_limit 
        self.client = boto3.client("bedrock-runtime", region_name='us-east-1') 

    def watch_log(self):
        while not os.path.exists(LOG_FILE):
            print(f"Waiting for log file '{LOG_FILE}' to be created...")
            time.sleep(0.5)

        with open(LOG_FILE, 'r', encoding='UTF-8') as f:
            f.seek(0)
            line = f.read()

            prompt = self.prompt
            formatted_prompt = [{
                "role": "user",
                "content": prompt + f" {line}"
            }]

            body = json.dumps({
                "messages": formatted_prompt,
                "max_tokens": self.token_limit,
                "temperature": 0.5,
                "top_p": 0.9,
            })
            try:
                print("Running AI...")
                # Invoke the model with the request.
                response = self.client.invoke_model(modelId=MODEL_ID, body=body)

                # Read the response body.
                model_response = json.loads(response["body"].read())

                # Extract choices.
                choices = model_response["choices"]

                # Print choices.
                #print(choices)

                return choices[0]["message"]["content"]

            except (ClientError, Exception) as e:
                print(f"ERROR: Can't invoke '{MODEL_ID}'. Reason: {e}")
                exit(1)

    def ai_content(self):
        result = self.watch_log()
        print(f"{result}\n{"**"*20}")


def main(prompt, token_limit):
    AI_Assistance_instance = AI_Assistant(prompt, token_limit)
    AI_Assistance_instance.ai_output()

def parse_args(arglist):
    parser = ArgumentParser()
    parser.add_argument("ai_prompt", help="Prompt for the AI to process")
    parser.add_argument("-tk", "--token", type=int, default=150, help="Number of tokens to generate")
    parser.add_argument("-v", "--verbose", action="store_true", help="Enable verbose output")
    return parser.parse_args()

if __name__ == "__main__":
    args = parse_args(sys.argv[1:])
    if args.verbose:
        print(f"AI Prompt: {args.ai_prompt}")
        print(f"Token Limit: {args.token}")

    main(args.ai_prompt, args.token)