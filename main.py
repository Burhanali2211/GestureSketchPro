import cvzone
import cv2
from cvzone.HandTrackingModule import HandDetector
import numpy as np
import google.generativeai as genai
from PIL import Image
import streamlit as st
import pyttsx3

# Set up the Streamlit page configuration
st.set_page_config(layout="wide")

# Add a neon blue title
st.markdown('''
    <h1 style="color: #00FFFF; text-align: center; 
              text-shadow: 0 0 5px #00FFFF, 0 0 10px #00FFFF, 
                          0 0 20px #00FFFF, 0 0 40px #00FFFF;"> 
        AI Hand Gesture Math Solver
    </h1>
''', unsafe_allow_html=True)

# Create two columns: one for the webcam and one for AI response
col1, col2 = st.columns([3, 2])

with col1:
    run = st.checkbox('CAMERA', value=True)
    FRAME_WINDOW = st.image([])

with col2:
    st.title("AI RESPONSE")
    output_text_area = st.empty()  # Update as needed to minimize updates

# Initialize Google Generative AI
genai.configure(api_key="Your_Api")
model = genai.GenerativeModel('gemini-1.5-flash')

# Initialize the webcam to capture video
if 'cap' not in st.session_state:
    st.session_state.cap = cv2.VideoCapture(0)
    st.session_state.cap.set(3, 1280)
    st.session_state.cap.set(4, 720)

# Initialize HandDetector for hand tracking
detector = HandDetector(staticMode=False, maxHands=1, modelComplexity=1, detectionCon=0.7, minTrackCon=0.5)

# Function to initialize the speech engine
def init_speech_engine():
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)
    return engine

# Function to speak the text using pyttsx3
def speak(text):
    engine = init_speech_engine()
    engine.say(text)
    engine.runAndWait()

def getHandInfo(img):
    hands, img = detector.findHands(img, draw=False, flipType=True)
    if hands:
        hand = hands[0]
        lmList = hand["lmList"]
        fingers = detector.fingersUp(hand)
        return fingers, lmList
    else:
        return None

def draw(info, prev_pos, canvas):
    fingers, lmList = info
    current_pos = None
    if fingers == [0, 1, 0, 0, 0]:
        current_pos = lmList[8][0:2]
        if prev_pos is None:
            prev_pos = current_pos
        cv2.line(canvas, current_pos, prev_pos, (0, 255, 0), 4)
    elif fingers == [1, 0, 0, 0, 0]:
        canvas = np.zeros_like(img)  # Clear canvas when thumb is up
    return current_pos, canvas

def sendToAI(model, canvas, fingers):
    if fingers == [1, 0, 0, 0, 1]:
        pil_image = Image.fromarray(canvas)
        response = model.generate_content(["Analyze the provided input and respond comprehensively, adapting to the context: solve problems, answer questions, interpret drawings, or provide relevant insights based on the content.", pil_image])
        return response.text
    return "Start Drawing anything and i will answer you especially math problem and shape identification."

# Function to display AI response if there's a new message
def display_line_by_line(text, prev_text):
    if text != prev_text:
        output_text_area.text(text)  # Show updated text
    return text

prev_pos = None
canvas = None
output_text = ""
prev_output_text = ""

# Create buttons for voice guidance aligned in one row
col_buttons = st.columns(4)

with col_buttons[0]:
    if st.button("How to Write ☝️"):
        speak("To start writing, raise your index finger and draw on the screen.")

with col_buttons[1]:
    if st.button("How to Stop Writing 👆"):
        speak("To stop writing, raise your thumb with index finger.")

with col_buttons[2]:
    if st.button("How to Get Answer 🤙"):
        speak("To send your drawing to AI, raise your pinky and thumb finger together.")

with col_buttons[3]:
    if st.button("How to Clear Screen 👍"):
        speak("To clear the screen, raise your thumb finger.")

# Start video loop and processing
if run:
    while True:
        success, img = st.session_state.cap.read()
        img = cv2.flip(img, 1)
        if canvas is None:
            canvas = np.zeros_like(img)

        info = getHandInfo(img)
        if info:
            fingers, lmList = info
            prev_pos, canvas = draw(info, prev_pos, canvas)
            output_text = sendToAI(model, canvas, fingers)

        image_combined = cv2.addWeighted(img, 0.7, canvas, 0.3, 0)
        FRAME_WINDOW.image(image_combined, channels="BGR")

        # Display AI response in column 2 if updated
        prev_output_text = display_line_by_line(output_text, prev_output_text)

        cv2.waitKey(1)
else:
    st.session_state.cap.release()
