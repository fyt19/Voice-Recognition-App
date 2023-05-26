# Voice Recognition Application

This application converts the voice that the user says from the microphone to text and runs different functions by detecting certain words.

## How Does It Work?

The application connects to the Google Speech Recognition service using the speech_recognition library and converts the voice to text. Then, it checks whether there are words such as "thief", "fire" or "help" in the text. If so, it calls the relevant alarm or help function. If not, it reports that an unrecognized word was said.

## Required Libraries

You need the speech_recognition library to run the application. You can install this library with pip:
```
pip install SpeechRecognition
```

You also need the PyAudio library to use the microphone. You can also install this library with pip:
```
pip install PyAudio
```

## Installation and Usage

After downloading the application, open a terminal in the directory where the application is located and run the following command:
```
python voice_recognition.py
```

When the application starts running, you will see the message "Please speak..." on the terminal. At this stage, you can say anything you want to the microphone. The application will try to recognize your voice and convert it to text on the terminal. If there is a certain word in the recognized text, it will call the relevant function. If there is no certain word in the recognized text, it will report that an unrecognized word was said.

You can stop the application by pressing Ctrl+C keys.

You can customize the functions according to your needs.
