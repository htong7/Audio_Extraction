"""
This script is designed to extract audio from video files in a specified
directory and its subdirectories.

Before running this script, make sure to install the required Python packages:
- os
- audio_extract
You also need to have the `audio_extract` module and the `extract_audio`
function available in your Python environment.
"""
import os
from audio_extract import extract_audio


def main():
    """
    Main function that processes all .mp4 files in a specified directory and
    its subdirectories.
    For each .mp4 file, it checks if an equivalent .mp3 file exists. If not,
    it extracts the audio from the .mp4 file and saves it as an .mp3 file.
    """
    # Define the directory path where the .mp4 files are located
    directory = '/path/to/your/directory'

    # Use os.walk to go through all subdirectories of the specified directory
    for root, dirs, files in os.walk(directory):
        # For each file in the current directory
        for file in files:
            # Check if the file ends with '.mp4'
            if file.endswith('.mp4'):
                # Construct the full path of the .mp4 file
                input_file_path = os.path.join(root, file)
                # Replace the '.mp4'  with '.mp3' to create the new file name
                new_file_path = file.replace('.mp4', '.mp3')
                # Construct the full path of the .mp3 file
                output_file_path = os.path.join(root, new_file_path)
                # Check if the .mp3 file already exists
                if not os.path.isfile(output_file_path):
                    # If the .mp3 file does not exist, call the extract_audio
                    # function to convert the .mp4 file to .mp3
                    extract_audio(input_path=input_file_path,
                                  output_path=output_file_path)


if __name__ == "__main__":
    main()
