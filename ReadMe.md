# AI Hand Gesture Math Solver

This project uses AI, hand gestures, and computer vision to solve math problems. The system captures hand gestures using a webcam and translates those gestures into math problems which are then sent to a Generative AI for solving.

## Features

- **Hand Gesture Detection**: Uses the OpenCV and CVZone libraries to track hand gestures.
- **AI Math Solver**: Sends the captured gesture-based input to Google's Generative AI model for solving math problems.
- **Voice Guidance**: Uses pyttsx3 to provide voice guidance for the user on how to interact with the system.
- **Streamlit Interface**: A simple and intuitive UI built using Streamlit.
- **Real-Time Canvas Drawing**: Draw math equations on the canvas in real-time and send them to AI for solving.

## Requirements

To run this project, you'll need the following Python libraries:

- `opencv-python`
- `cvzone`
- `numpy`
- `google-generativeai`
- `Pillow`
- `streamlit`
- `pyttsx3`

You can install all the dependencies by running:

```bash
pip install -r requirements.txt
