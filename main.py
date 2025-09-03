import os
from dotenv import load_dotenv
from google import genai
from google.genai import types
import sys
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-v', '--verbose', action='store_true')
parser.add_argument('user_prompt', help="The prompt text")
try:
    args = parser.parse_args()
except SystemExit:
    print("Invalid flag or missing prompt\n|> uv run main.py 'Prompt here' [flags]")
    sys.exit(1)
    
user_prompt = args.user_prompt

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")

messages = [
    types.Content(role="user", parts=[types.Part(text=user_prompt)])
]

client = genai.Client(api_key=api_key)
response = client.models.generate_content(
    model='gemini-2.0-flash-001', 
    contents=messages
)

print(response.text)

if args.verbose:
    print(f'User prompt: {user_prompt}')
    print(f'Prompt tokens: {response.usage_metadata.prompt_token_count}')
    print(f'Response tokens: {response.usage_metadata.candidates_token_count}')