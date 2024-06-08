# Face Recognition Authentication System

  Authored by Saeed Asle
  
# Description

This project is a face recognition authentication system implemented in Python.
It uses the face_recognition library for face detection and recognition, cv2 for video capture, pyttsx3 for text-to-speech, and os for file handling.
The system authenticates users by recognizing their faces and verifying their PINs.
 
# Features

The code provides the following features:


Load Known Faces:
  * Loads known face encodings and names from a specified directory.
  * Handles errors during the loading process.
Text-to-Speech Initialization:
  * Initializes the text-to-speech engine.
  * Handles errors during the initialization process.
    
User Authentication:
  * Authenticates users by comparing entered PINs with stored PINs.
    
4.Video Capture and Face Recognition:
  * Captures video from the webcam.
  * Detects faces using the Haar cascade classifier.
  * Recognizes faces using the face_recognition library.
  * Greets recognized users and prompts for PIN verification for added security.
  * Automatically exits after a set duration if no face is recognized.
    
# How to Use

Load Known Faces:
  * The load_known_faces function reads images from the specified directory, processes them to obtain face encodings, and stores the names and encodings.
  * Example: known_face_encodings, known_face_names = load_known_faces("./known/")
    
Initialize Text-to-Speech:
  * The initialize_tts function initializes the text-to-speech engine with a specified voice and rate.
  * Example: speaker = initialize_tts()
    
User Authentication:
  * The authenticate_user function prompts the user for a PIN and checks it against stored PINs.
  * Example: authenticate_user(known_users, username)
    
Video Capture and Face Recognition:
  * The video_capture_and_recognition function captures video from the webcam, detects faces, and recognizes them using the loaded face encodings.
  * It greets recognized users and prompts for PIN verification.
  * Example: video_capture_and_recognition(camera, known_face_encodings, known_face_names, speaker, known_users)
    
# Dependencies

Make sure you have the following libraries installed:
  * face_recognition
  * opencv-python (cv2)
  * pyttsx3
  * numpy
  * PIL (Pillow)

You can install these libraries using pip:

    pip install face_recognition opencv-python pyttsx3 numpy pillow

# Directory Structure

Ensure your directory structure looks like this:

        .
    ├── face_recognition_auth.py
    ├── known/
    │   ├── user1.jpg
    │   ├── user2.jpg
    │   └── ...
    └── requirements.txt

# Output
  * Recognizes and greets known users.
  * Prompts for PIN verification for added security.
  * Outputs errors and relevant messages during execution.

