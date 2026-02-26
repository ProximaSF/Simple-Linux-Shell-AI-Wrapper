#!/bin/bash

PROMPT=""
VERBOSE=false

# Check of flag
while getopts "n:v" opt; do
  case $opt in
    n) PROMPT="$OPTARG" ;;
    v) VERBOSE=true ;;
    \?) echo "Invalid option -$OPTARG" >&2; exit 1 ;;
  esac
done


shift $((OPTIND -1))

# If PROMPT is empty and -n not used, grab the first
# non-flag argument; prompt string ($1)
# NOTE: $0 is the script it self
if [ -z "$PROMPT" ] && [ -n "$1" ]; then
  PROMPT="$1"
  shift
fi

# Check if PROMPT still empty str
if [ -z "$PROMPT" ]; then
  echo "Error: A prompt is required."
  exit 1
fi


echo "Running AI..."
if [ "$VERBOSE" = true ]; then
  echo "Verbose on:"
  echo "Prompt: $PROMPT"
  echo "---"*10
fi

"/home/kali/Desktop/Python Projects/.venv/bin/python" "/home/kali/Desktop/Python Projects/main.py" "$PROMPT" "$@"