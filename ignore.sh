#!/bin/bash

# Check if correct number of arguments is provided
if [ "$#" -ne 2 ]; then
  echo "Usage: $0 <inputfile.txt> <output.txt>"
  exit 1
fi

inputfile=$1
outputfile=$2

# Define the words to be removed
words=("Home" "Lyrics" "Movies" "Music" "Singers" "Songs" "Album" "Artists")

# Create a pattern for grep to exclude lines containing any of the words
pattern=$(printf "|%s" "${words[@]}")
pattern=${pattern:1}

# Find the line number where the specific line is found
line_num=$(grep -n "Other Songs from" "$inputfile" | cut -d: -f1)

if [ -n "$line_num" ]; then
  # Remove lines after and including the specific line
  sed -n "1,$((line_num - 1))p" "$inputfile" | grep -vE "$pattern" > "$outputfile"
else
  # If the specific line is not found, just filter out lines with the specified words
  grep -vE "$pattern" "$inputfile" > "$outputfile"
fi

echo "Filtered lines written to $outputfile"

