import face_recognition
import cv2
import os
import pyttsx3 as tts
import sys
import time

known_users = {
    "1": {
        "name": "saeed",
        "pin": "1234"
    },
    "2": {
        "name": "User 2",
        "pin": "5678"
    }
}

# Function to load known face encodings and names with error handling
def load_known_faces(known_faces_directory):
    known_face_encodings = []
    known_face_names = []
    try:
        for filename in os.listdir(known_faces_directory):
            if filename.endswith(".jpg"):
                image = face_recognition.load_image_file(os.path.join(known_faces_directory, filename))
                encoding = face_recognition.face_encodings(image)[0]
                known_face_encodings.append(encoding)
                known_face_names.append(filename.split('.')[0])
        return known_face_encodings, known_face_names
    except Exception as e:
        print(f"Error while loading known faces: {e}")
        return [], []


# Function to initialize text-to-speech with error handling
def initialize_tts():
    try:
        speaker=tts.init()
        speaker.setProperty('rate',120)
        speaker.setProperty('voice', speaker.getProperty('voices')[1].id) 
        return speaker
    except Exception as e:
        print(f"Error initializing text-to-speech: {e}")
        return None

# Function for user authentication
def authenticate_user(known_users, username):
    pin = input(known_users[username]['name']+"\nPassword: ")
    if username in known_users and pin == known_users[username].get('pin', ''):
        speaker.say(f"Identification succeeded .")
        speaker.runAndWait()
        return True
    else:
        print("Identification failed. Please try again.")
        return False


# Combined function for video capture and face recognition
def video_capture_and_recognition(camera, known_face_encodings, known_face_names, speaker,known_users):
    start_time = time.time()  # Record the start time
    exit_after = 30  # Set the desired duration for automatic exit (in seconds)
    legal=False
    while True:
        if legal:
            break
        elapsed_time = time.time() - start_time
        if elapsed_time >= exit_after:
            speaker.say(f"Identification failed, please try again.")
            speaker.runAndWait()
            break
        ret, frame = camera.read()
        if not ret:
            print("Failed to capture a frame. Exiting.")
            break

        # Detect faces using the face detection classifier
        faces = faceCascade.detectMultiScale(frame, 1.3, 5)
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        cv2.imshow('Face Recognition', frame)
        face_locations = face_recognition.face_locations(frame)
        face_encodings = face_recognition.face_encodings(frame, face_locations)
 
        for face_encoding, _ in zip(face_encodings, face_locations):
            matches = face_recognition.compare_faces(known_face_encodings, face_encoding, tolerance=0.6)
            if True in matches:
                name = known_face_names[matches.index(True)]
                legal=True
                speaker.say(f"Hello, {known_users[name]['name']}.")

    # Release the camera and close windows
    camera.release()
    cv2.destroyAllWindows()
    if legal:
        speaker.say(f"For increased security, please provide your password.")
        speaker.runAndWait()
        for i in range(3):
            if authenticate_user(known_users, name):
                break
            if(i==2):
                speaker.say(f"Identification failed. goodbye")
                speaker.runAndWait()
                break
# Main code
if __name__ == "__main__":
    # Initialize text-to-speech with error handling
    speaker = initialize_tts()
    if speaker is None:
        sys.exit("Failed to initialize text-to-speech. Exiting.")

    # Initialize the webcam and face detection classifier
    camera = cv2.VideoCapture(0)
    faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    # Load known face encodings and names with error handling
    known_face_encodings, known_face_names = load_known_faces("./known/")
    if not known_face_encodings:
        sys.exit("No known faces loaded. Exiting.")

    video_capture_and_recognition(camera, known_face_encodings, known_face_names, speaker,known_users)


