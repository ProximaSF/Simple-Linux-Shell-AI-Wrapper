import os
import time
import boto3
from dotenv import load_dotenv
from botocore.exceptions import ClientError

import sys
from argparse import ArgumentParser

from deepseek import deepseek3_2
from claude import claude_Sonnet4_6


load_dotenv()
API_KEY = os.getenv("AWS_BEARER_TOKEN_BEDROCK")
DEFAULT_MODEL_ID = "deepseek.v3.2"
# TEST_LOG_FILE
LOG_FILE = str(os.getenv("FILE_LOG"))
MODELS_IDS = ["deepseek.v3.2", "us.anthropic.claude-sonnet-4-6"]



class AI_Assistant:
    def __init__(self, prompt, token_limit, model_id=DEFAULT_MODEL_ID):
        self.prompt = prompt
        self.token_limit = token_limit 
        self.model_id = model_id
        self.client = boto3.client("bedrock-runtime", region_name='us-east-1') 

    def check_log_file(self):
        while not os.path.exists(LOG_FILE):
            print(f"Waiting for log file '{LOG_FILE}' to be created...")
            time.sleep(0.5)

    def ai_content(self):
        is_model = [model for model in MODELS_IDS if self.model_id.lower() in model.lower()]
        if is_model:
            if self.model_id == DEFAULT_MODEL_ID:
                result = deepseek3_2((LOG_FILE), self.prompt, self.model_id, self.token_limit, self.client)
                return result
            elif "claude" in is_model[0]:
                result = claude_Sonnet4_6((LOG_FILE), self.prompt, is_model[0], self.token_limit, self.client)
                return result
        
        return f"{self.model_id} is invalid model or is unavailable."


    def output(self):
        print(f"{result}\n{"**"*20}")
        self.check_log_file()
        result = self.ai_content()
        print(f"{result}\n{"**"*20}")


def main(prompt, token_limit, model_id):
    AI_Assistance_instance = AI_Assistant(prompt, token_limit, model_id)
    AI_Assistance_instance.output()

def parse_args(arglist):
    parser = ArgumentParser()
    parser.add_argument("ai_prompt", help="Prompt for the AI to process")
    parser.add_argument("-m", "--model", type=str, default=DEFAULT_MODEL_ID, help="Model ID to use")
    parser.add_argument("-tk", "--token", type=int, default=150, help="Number of tokens to generate")
    parser.add_argument("-v", "--verbose", action="store_true", help="Enable verbose output")
    return parser.parse_args()

if __name__ == "__main__":
    args = parse_args(sys.argv[1:])
    if args.verbose:
        msg = f"""
            Verbose enabled (python):
            ------------------------------------------
            Using Model: {args.model}
            Prompt: {args.ai_prompt}
            Token Limit: {args.token}
            """
        print(f)
        print(f"Using Model: {args.model}")
        print(f"AI Prompt: {args.ai_prompt}")
        print(f"Token Limit: {args.token}")

    main(args.ai_prompt, args.token, args.model)