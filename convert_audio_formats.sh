#!/bin/bash

# This script converts audio files from one format to another using ffmpeg and parallel.
# It will delete the original files after conversion.

# Define the directory, input formats, and output format directly in the script
ROOT_DIR="/workspaces/convert-audio-using-ffmpeg"  # Root directory containing the audio files
INPUT_FORMATS=("m4a" "wav")                        # Input formats (e.g., m4a, wav)
OUTPUT_FORMAT="mp3"                                # Desired output format (e.g., mp3)

# Function to convert a single file from input format to output format
convert_audio_file() {
    local input_file="$1"
    local output_file="$2"
    local input_format="$3"
    local output_format="$4"
    
    # Perform the conversion using ffmpeg
    ffmpeg -i "$input_file" "$output_file" -loglevel error
    
    # Check if the conversion was successful
    if [ $? -eq 0 ]; then
        # Remove the original file
        rm -f "$input_file"
        echo "Converted and removed: $input_file"
    else
        echo "Error converting: $input_file"
    fi
}

export -f convert_audio_file

# Find audio files in the specified formats and convert them using parallel
find "$ROOT_DIR" -type f \( \
    -iname "*.${INPUT_FORMATS[0]}" \
    $(for fmt in "${INPUT_FORMATS[@]:1}"; do echo -o -iname "*.${fmt}"; done) \
\) | parallel --no-notice -j+0 \
    convert_audio_file {} "{.}.$OUTPUT_FORMAT" "{.##*.}" "$OUTPUT_FORMAT"
