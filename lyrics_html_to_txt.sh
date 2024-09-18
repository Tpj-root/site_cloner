#!/bin/bash

# Define the path to the main movies folder
main_dir="$(pwd)/movies_sample"
echo ${main_dir}
# Check if the main directory exists
if [[ ! -d "$main_dir" ]]; then
  echo "Directory $main_dir does not exist."
  exit 1
fi

# Loop through each folder in the main directory
for folder in "$main_dir"/*/; do
  # Check if it's a directory
  if [[ -d "$folder" ]]; then
    # Get the folder name (basename of the directory)
    folder_name=$(basename "$folder")
    echo "Processing folder: $folder_name"

    # Loop through each file in the folder
    for file in "$folder"*; do
      # Check if it's a file
      if [[ -f "$file" ]]; then
        # Get the file name (basename of the file)
        file_name=$(basename "$file")
        python3 $(pwd)"/"html_to_txt.py ${file} ${file}.txt
        #echo "  File: $file_name"
      fi
    done
  fi
done

