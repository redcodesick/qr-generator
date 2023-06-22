#!/bin/bash

command='python generate.py'

input_file='links.txt'

# Read each line from the input file
while IFS= read -r line; do
    # Split the line into link and title using space as the delimiter
    link=$(echo "$line" | cut -d ' ' -f 1)
    title=$(echo "$line" | cut -d ' ' -f 2-)
    
    # Execute the command with the link and title as arguments
    $command "$link" "$title"
done < "$input_file"

