#!/bin/bash

# Check if the input file is provided
if [ $# -ne 1 ]; then
  echo "Usage: ./autoqr.sh <input_file>"
  exit 1
fi

input_file="$1"

# Check if the input file exists
if [ ! -f "$input_file" ]; then
  echo "Input file not found!"
  exit 1
fi

# Read the file line by line and execute the Python script
while IFS= read -r line; do
  link=$(echo "$line" | awk '{print $1}')
  title=$(echo "$line" | awk '{$1=""; print $0}' | xargs)
  python3 pyz.py "$link" "$title"
done < "$input_file"

