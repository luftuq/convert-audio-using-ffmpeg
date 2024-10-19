# Audio Conversion Script in python and bash 

[![wemake-python-styleguide](https://img.shields.io/badge/style-wemake-000000.svg)](https://github.com/wemake-services/wemake-python-styleguide)

[
    ![Open in Remote - Containers](
        https://xebia.com/wp-content/uploads/2023/11/v1.svg    )
](
    https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/luftuq/convert-audio-using-ffmpeg
) 

## Features

- Convert audio files from specified input formats (e.g. `m4a`, `wav`) to a desired output format (`mp3`).
- Uses `ffmpeg` for audio conversion.
- Utilizes `parallel` in bash to speed up the conversion process by handling multiple files simultaneously.
- Automatically deletes original files after successful conversion.

## Usage
Edit the INPUT_FORMATS, and OUTPUT_FORMAT variables in the script as needed.
Run the script: `./convert_audio_formats.sh`

## Acknowledgments
- ffmpeg for the audio conversion capabilities.
- GNU Parallel for parallel processing support.