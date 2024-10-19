"""
This module provides functionality to convert audio files between formats.

It searches through directories for audio files in specific formats,
converts them to a desired output format, and deletes the original
files after conversion.

Dependencies:
    - pydub: Required for audio format conversion.
    - os: For file operations.

Functions:
    - should_convert: Checks if a file should be converted based on its format.
    - get_output_file: Generates the output file path with the desired format.
    - process_files_in_directory: Processes all audio files in a directory.
    - convert_audio_in_directory: Walks through the directory and converts
      audio files.

Parameters:
    - root_dir (str): The root directory where audio files are located.
    - input_formats (Tuple[str]): Tuple of input formats to look for.
    - output_format (str): The desired output format to convert files to.
"""
import os
from typing import Tuple

from pydub import AudioSegment


def should_convert(filename: str, input_formats: Tuple[str, ...]) -> bool:
    """
    Check if the file has one of the supported input formats.

    Args:
        filename (str): The name of the file to check.
        input_formats (Tuple[str]): A tuple of input formats (extensions).

    Returns:
        bool: True if the file has one of the input formats, False otherwise.
    """
    return any(filename.endswith('.{0}'.format(fmt)) for fmt in input_formats)


def get_output_file(
    filename: str,
    foldername: str,
    input_format: str,
    output_format: str,
) -> str:
    """
    Generate the output file path with the desired format.

    Args:
        filename (str): The name of the input file (e.g., 'audio.m4a').
        foldername (str): The directory where the input file is located.
        input_format (str): The current format of the file (e.g., 'm4a').
        output_format (str): The format to convert the file to (e.g., 'mp3').

    Returns:
        str: The full path of the output file with the new format.
    """
    return os.path.join(
        foldername,
        filename.replace(
            '.{0}'.format(input_format),
            '.{0}'.format(output_format),
        ),
    )


def process_files_in_directory(
    foldername: str,
    filenames: Tuple[str, ...],
    input_formats: Tuple[str, ...],
    output_format: str,
) -> None:
    """
    Process each file in a directory, converting files if necessary.

    Args:
        foldername (str): The name of the folder containing the files.
        filenames (Tuple[str]): A tuple of filenames to process.
        input_formats (Tuple[str]): Tuple of input formats/extensions.
        output_format (str): The format/extension to convert files to.
    """
    for filename in filenames:
        if should_convert(filename, input_formats):
            convert_audio_file(
                os.path.join(foldername, filename),
                get_output_file(
                    filename,
                    foldername,
                    os.path.splitext(filename)[1][1:],
                    output_format,
                ),
                os.path.splitext(filename)[1][1:],
                output_format,
            )


def convert_audio_file(
    input_path: str,
    output_path: str,
    input_format: str,
    output_format: str,
) -> None:
    """
    Convert an audio file from one format to another.

    Args:
        input_path (str): The full path to the input audio file.
        output_path (str): The full path for the output audio file.
        input_format (str): The format of the input file (e.g., 'm4a', 'wav').
        output_format (str): The format for the output file (e.g., 'mp3').

    Raises:
        RuntimeError: If there is an issue loading the input file or during
                      conversion.
    """
    try:
        audio = AudioSegment.from_file(input_path, format=input_format)
    except Exception as exception:
        raise RuntimeError(
            'Failed to load audio from {0}: {1}'.format(input_path, exception),
        )
    else:
        audio.export(output_path, format=output_format)
        os.remove(input_path)


def convert_audio_in_directory(
    root_dir: str, input_formats: Tuple[str, ...], output_format: str,
) -> None:
    """
    Convert audio files in directory from input formats to output format.

    Args:
        root_dir (str): The root directory to search for audio files.
        input_formats (Tuple[str]): Tuple of input formats to search for.
        output_format (str): The format/extension to convert files to.
    """
    for foldername, _, filenames in os.walk(root_dir):
        process_files_in_directory(
            foldername,
            tuple(filenames),  # Converting filenames to tuple for type safety
            input_formats,
            output_format,
        )


if __name__ == '__main__':
    ROOT_DIRECTORY = '/workspaces/convert-audio-using-ffmpeg'
    INPUT_FORMATS = ('m4a', 'wav')
    OUTPUT_FORMAT = 'mp3'

    convert_audio_in_directory(
        ROOT_DIRECTORY,
        INPUT_FORMATS,
        OUTPUT_FORMAT,
    )
