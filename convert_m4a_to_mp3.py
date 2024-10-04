"""This module provides functionality to convert .m4a audio files to .mp3.

It searches through directories for .m4a files, converts them to .mp3,
and deletes the original .m4a file after conversion.

Dependencies:
    - pydub: Required for audio format conversion.
    - os: For file operations.

Functions:
    - convert_m4a_to_mp3: Converts a .m4a file to .mp3.
"""
import os
from pydub import AudioSegment


def convert_m4a_to_mp3(file_path: str, output_path: str) -> None:
    """
    Convert an audio file from .m4a format to .mp3 format.

    Args:
        file_path (str): The full path to the input .m4a file.
        output_path (str): The full path for the output .mp3 file.
    """
    try:  # Load and convert m4a to mp3
        audio: AudioSegment = AudioSegment.from_file(file_path, format='m4a')
        audio.export(output_path, format='mp3')
        os.remove(file_path)

    except Exception as exception:
        print(f'Failed to convert {file_path}: {exception}')


# Root directory to search for m4a files
root_dir: str = '/workspaces/mp4-to-mp3'

# Walk through all subdirectories and files
for foldername, subfolders, filenames in os.walk(root_dir):
    for filename in filenames:
        if filename.endswith('.m4a'):
            # Full path to the m4a file
            file_path: str = os.path.join(foldername, filename)
            # Replace .m4a with .mp3 for the output file name
            output_file: str = os.path.join(
                foldername,
                filename.replace('.m4a', '.mp3'),
            )
            # Convert the file and delete the original m4a
            convert_m4a_to_mp3(file_path, output_file)
