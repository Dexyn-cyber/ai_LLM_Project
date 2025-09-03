import os
from dotenv import load_dotenv
from google import genai
from google.genai import types
import sys
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-v', '--verbose', action='store_true')
parser.add_argument('prompt', help="The Prompt")
args = parser.parse_args()

if len(sys.argv) > 1:
    user_prompt = str(args.prompt)
else:
    print("You are required to give a prompt. |> uv run main.py 'Prompt here' ")
    exit(1)


load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")

messages = [
    types.Content(role="user", parts=[types.Part(test=user_prompt)])
]

client = genai.Client(api_key=api_key)
response = client.models.generate_content(
    model='gemini-2.0-flash-001', 
    contents=messages
)

print(response.text)

if args.verbose:
    print(f"Users prompt: {user_prompt}")
    print(f'Prompt tokens: {response.usage_metadata.prompt_token_count}')
    print(f'Response tokens: {response.usage_metadata.candidates_token_count}')