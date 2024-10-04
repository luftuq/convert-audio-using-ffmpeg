#!/bin/bash

# Directory containing the audio files
input_dir="/workspaces/mp4-to-mp3"

# Change to the directory with the audio files
cd "$input_dir" || { echo "Directory not found: $input_dir"; exit 1; }

# Function to convert a single file
convert_file() {
    input_file="$1"
    output_file="${input_file%.m4a}.mp3"  # Change the extension to .mp3

    # Run ffmpeg to convert the file
    ffmpeg -i "$input_file" -codec:a libmp3lame -qscale:a 2 "$output_file"

    # Check if conversion was successful
    if [ $? -eq 0 ]; then
        echo "Converted: $input_file to $output_file"
        # Optional: Uncomment the line below to delete the original .m4a file after conversion
        rm "$input_file"
    else
        echo "Failed to convert: $input_file"
    fi
}

export -f convert_file  # Export the function for parallel execution

# Find all .m4a files and convert them in parallel
find . -name '*.m4a' | parallel -j+0 convert_file

# Notify when done
echo "All conversions completed."
