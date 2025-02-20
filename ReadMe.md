# AI Hand Gesture Math Solver

## Description
This is an AI-powered hand gesture recognition system that allows users to draw mathematical equations or shapes in the air using hand gestures, which are then interpreted and solved by an AI model. The project integrates OpenCV, Google Gemini AI, and Streamlit for an interactive experience.

## Features
- Real-time hand gesture tracking using OpenCV and `cvzone`.
- AI-powered mathematical equation solving and shape recognition using Google Gemini AI.
- Streamlit-based user interface with an interactive camera feed.
- Speech guidance for better usability.
- Ability to write, erase, and submit drawings using specific hand gestures.
- Voice output for AI responses.

## Technologies Used
- **Python** (Main programming language)
- **OpenCV & cvzone** (Hand tracking and image processing)
- **Google Gemini AI** (AI-based response generation)
- **Streamlit** (Web-based UI framework)
- **pyttsx3** (Text-to-speech functionality)

## Installation & Setup

### Prerequisites
Ensure you have Python 3.x installed along with the following dependencies:

```sh
pip install opencv-python cvzone google-generativeai streamlit numpy pyttsx3 pillow
```

### API Key Setup
To use the Google Gemini AI API, follow these steps:
1. Go to [Google AI API Console](https://ai.google.dev/)
2. Generate an API key.
3. Replace `Your_Api` in the script with your actual API key.

### Running the Project
1. Clone or download the repository.
2. Navigate to the project directory.
3. Run the following command:
   ```sh
   streamlit run GestureSketchPro.py
   ```
4. Enable the camera and interact using hand gestures.

## Hand Gesture Controls
| Gesture | Action |
|---------|--------|
| Index Finger Up | Start Writing |
| Thumb Up | Clear Screen |
| Pinky & Thumb Up | Submit Drawing to AI |
| Thumb + Index Finger Up | Stop Writing |

## Example Usage
When you start the application, follow the instructions for writing and submitting mathematical problems. The AI will provide a response, which will also be spoken out loud using the text-to-speech feature.

```
 _______  _______  _______  _______  _______  _______
|       ||       ||       ||       ||       ||       |
|   _   ||    ___||    ___||    ___||    ___||   _   |
|  | |  ||   |___ |   |___ |   |___ |   |___ |  | |  |
|  |_|  ||    ___||    ___||    ___||    ___||  |_|  |
|       ||   |___ |   |    |   |___ |   |___ |       |
|_______||_______||___|    |_______||_______||_______|

Enter the mathematical equation or draw a shape.

>> AI Response: "The answer to your equation is..."
```

## License
This project is licensed under the MIT License.
