import sys
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-v', '--verbose', action='store_true')
parser.add_argument('prompt', help="The prompt text")
try:
    args = parser.parse_args()
except SystemExit:
    print("Invalid flag or missing prompt\n|> uv run main.py 'Prompt here' [flags]")
    sys.exit(1)


if len(sys.argv) > 1:
    prompt = args.prompt
else:
    print("You are required to give a prompt. |> uv run main.py 'Prompt here' [flags]")
    exit(1)

print(f"Prompt: {prompt}")
if args.verbose:
    print("Verbose is on")