# Audio Analysis Sandbox

This repository contains Python scripts and a Jupyter notebook for extracting and analyzing audio from video files.

## Overview

The main components of this repository are:

1. `audio_analysis_sandbox.ipynb`: A Jupyter notebook that provides a solution for extracting audio from videos. This tool is designed with two main applications in mind:
    - **Data Analysis**: In the fields of data science and machine learning, researchers often work with large datasets of videos. This notebook can be used to extract audio from these videos, which is often the first step in performing analysis or training models related to speech recognition, sentiment analysis, and more.
    - **Natural Language Processing (NLP)**: This tool can be used to extract audio for NLP tasks. By converting video content into audio, it can facilitate various NLP tasks such as transcription, translation, or sentiment analysis.

2. `main.py`: This script processes video files to detect the presence of speech in each second of the video. It then visualizes the results using matplotlib.

3. `mp4_to_mp3.py`: This script is designed to extract audio from video files in a specified directory and its subdirectories.

## Installation

Before running the scripts, make sure to install the required Python packages:

```bash
pip install os time speech_recognition moviepy matplotlib numpy
