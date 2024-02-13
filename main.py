"""
This script processes video files to detect the presence of speech in each
second of the video.

It then visualizes the results using matplotlib.

Before running this script, make sure to install the required Python packages:
- os
- time
- speech_recognition
- moviepy
- matplotlib
- numpy

You also need to have the `audio_extract` module and the `extract_audio`
function available in your Python environment.
"""

import os
import time
import speech_recognition as sr
from moviepy.editor import AudioFileClip
import matplotlib.pyplot as plt
import numpy as np
from audio_extract import extract_audio


def transcribe_audio(audio_segment):
    """
    Transcribes an audio segment using Google Speech Recognition.

    Parameters:
    audio_segment (AudioSegment): The audio segment to transcribe.

    Returns:
    str: The transcribed text if the transcription was successful,
    otherwise an empty string.
    """
    r = sr.Recognizer()
    try:
        text = r.recognize_google(audio_segment)
        return text
    except sr.UnknownValueError:
        return ""
    except sr.RequestError:
        print("Couldn't request results from Google SR service")
        return ""


def process_video(video_path):
    """
    Processes a video file to detect speech in each second of the video.

    Parameters:
    video_path (str): The path to the video file.

    Returns:
    list: A list of binary values indicating the presence of speech in each
    second of the video.
    """
    r = sr.Recognizer()
    audio = AudioFileClip(video_path)
    duration = int(audio.duration)
    binary_outcome = [0] * duration
    for i in range(duration):
        audio_segment = audio.subclip(i, i+1)
        audio_segment.write_audiofile("temp.wav", logger=None)
        with sr.AudioFile("temp.wav") as source:
            audio_data = r.record(source)
            transcript = transcribe_audio(audio_data)
            if transcript:
                binary_outcome[i] = 1
    return binary_outcome


def process_file(file_path):
    """
    Processes an audio file to detect speech in each second of the audio.

    Parameters:
    file_path (str): The path to the audio file.

    Returns:
    list: A list of binary values indicating the presence of speech in each
    second of the audio.
    """
    binary_outcome = process_video(file_path)
    return binary_outcome


def plot_binary_outcome(binary_outcome):
    """
    Plots the binary outcome of the speech detection.

    Parameters:
    binary_outcome (list): A list of binary values indicating the presence of
    speech in each second of the audio.
    """
    plt.figure(figsize=(40, 6))
    x = np.arange(len(binary_outcome))
    plt.fill_between(x, binary_outcome, color='red', alpha=0.7,
                     where=np.array(binary_outcome) == 1)
    plt.xticks(np.arange(min(x), max(x)+1, 5))
    plt.xlabel('Time (seconds)')
    plt.ylabel('Speech Detected')
    plt.show()


def main():
    """
    Main function that processes all .mp4 files in a specified directory and
    its subdirectories.
    For each .mp4 file, it extracts the audio, detects speech in each second
    of the audio, and plots the results.
    """
    directory = '/path/to/your/directory'

    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.mp4'):
                input_file_path = os.path.join(root, file)
                new_file_path = file.replace('.mp4', '.mp3')
                output_file_path = os.path.join(root, new_file_path)
                if not os.path.isfile(output_file_path):
                    extract_audio(input_path=input_file_path,
                                  output_path=output_file_path)

                binary_outcome = process_file(output_file_path)
                plot_binary_outcome(binary_outcome)


if __name__ == "__main__":
    while True:
        try:
            main()
            break
        except ConnectionResetError:
            print("Connection reset by peer. Retrying...")
            time.sleep(5)
