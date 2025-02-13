import os
import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import subprocess as sp
import requests
from openaitest import search_on_google, youtube, find_my_ip  


def say(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language="en-in")
            print(f"User said: {query}")
            return query
        except sr.UnknownValueError:
            return "Sorry, I could not understand the audio."
        except sr.RequestError as e:
            return f"Could not request results; {e}"
        
def open_camera():
    try:
        sp.run('start microsoft.windows.camera:', shell=True, check=True)
        print("Opening camera...")
    except sp.CalledProcessError as e:
        print(f"Failed to open camera: {e}")

def close_program():
    say("Closing Program , Thankyou for using Tom A I , BYE")
    exit()
    


if __name__ == '__main__':
    say("Yes Sir, TOM A,I here")
    while True:
        query = takeCommand().lower()
        
        if "open youtube" in query:
            say("What do you want to play on YouTube, sir?")
            video = takeCommand().lower()
            if video:
                youtube(video)
        
        elif "open google" in query or "search on google" in query:
            say("What do you want to search on Google, sir?")
            search_query = takeCommand().lower()
            if search_query:
                search_on_google(search_query)

        elif "open music" in query:
            musicPath = r"C:\Users\Hp\Downloads\drift-phonk-156625.mp3"
            os.startfile(musicPath)

        elif "the time" in query:
            hour = datetime.datetime.now().strftime("%H")
            minute = datetime.datetime.now().strftime("%M")
            say(f"Sir, the time is {hour} hours and {minute} minutes.")
        
        elif "ip address" in query:
            ip_address = find_my_ip()
            say(f"Your IP address is confidential.") #{ip_address} 
            print(f"Your IP address is hidden.")


        elif "open camera" in query:
            open_camera()

        elif "close the program TOM" in query:
            close_program()


# import datetime
# import os
# import streamlit as st
# import speech_recognition as sr
# import subprocess as sp
# from openaitest import search_on_google, youtube, find_my_ip
# import webbrowser
# import requests
# from dotenv import load_dotenv
# load_dotenv()  # Loads environment variables from a .env file

# api_key = os.getenv("ELEVENLABS_API_KEY")

# if api_key is None:
#     print("Error: API key not found. Please check your .env file.")
# else:
#     print("API key loaded successfully.")
#     print("API Key:", api_key)


# def say_with_elevenlabs(text, api_key, voice_id="VR6AewLTigWG4xSOukaG"):
#     url = "https://api.elevenlabs.io/v1/text-to-speech"
#     headers = {
#         "Authorization": f"Bearer {api_key}",
#         "Content-Type": "application/json",
#     }
#     data = {
#         "voice_id": voice_id,
#         "text": text,
#         "language": "en",
#     }
#     response = requests.post(url, headers=headers, json=data)
#     if response.status_code == 200:
#         with open("output_audio.wav", "wb") as f:
#             f.write(response.content)
#         # Play the audio using the playsound module
#         import playsound
#         playsound.playsound("output_audio.wav")
#     else:
#         print(f"Error: {response.status_code}")




# def take_command():
#     r = sr.Recognizer()
#     with sr.Microphone() as source:
#         st.write("Listening...")
#         audio = r.listen(source)
#         try:
#             st.write("Recognizing...")
#             query = r.recognize_google(audio, language="en-in")
#             st.write(f"You said: {query}")
#             return query
#         except sr.UnknownValueError:
#             st.write("Sorry, I could not understand the audio.")
#             return ""
#         except sr.RequestError as e:
#             st.write(f"Could not request results; {e}")
#             return ""
        
# def youtube(video_query):
#     # Construct the search URL with the user's input
#     search_url = f"https://www.youtube.com/results?search_query={video_query.replace(' ', '+')}"
#     # Open the URL in the default web browser
#     webbrowser.open(search_url)


# def open_camera():
#     try:
#         sp.run('start microsoft.windows.camera:', shell=True, check=True)
#         st.write("Opening camera...")
#         say_with_elevenlabs("Opening Camera Sir")
#     except sp.CalledProcessError as e:
#         st.write(f"Failed to open camera: {e}")

# def close_program():
#     say_with_elevenlabs("Closing Program, Thank you for using Jarvis A I, BYE", api_key)
#     exit()

# def jarvis_ai(query):
#     if "open youtube" in query:
#         say_with_elevenlabs("What do you want to play on YouTube, sir?", api_key)
        
#         video = take_command().lower()
#         say_with_elevenlabs("Searching Sir", api_key)
#         if video:
#             youtube(video)

#     elif "open google" in query or "search on google" in query:
#         say_with_elevenlabs("What do you want to search on Google, sir?", api_key)
#         search_query = take_command().lower()
        
#         if search_query:
#             search_on_google(search_query)
            

#     elif "open music" in query:
#         music_path = r"C:\Users\Hp\Downloads\drift-phonk-phonk-2024-mix-156625.mp3"
#         say_with_elevenlabs("Music Starts, api_key")
#         os.startfile(music_path)

#     elif "the time" in query:
#         hour = datetime.datetime.now().strftime("%H")
#         minute = datetime.datetime.now().strftime("%M")
#         say_with_elevenlabs(f"Sir, the time is {hour} hours and {minute} minutes", api_key)

#     elif "ip address" in query:
#         ip_address = find_my_ip()
#         say_with_elevenlabs("Your IP address is confidential.", api_key)  # Hide the actual IP address

#     elif "open camera" in query:
#         open_camera()

# # Streamlit app interface
# st.title("Jarvis AI Assistant")
# if 'greeted' not in st.session_state:
#     say_with_elevenlabs("Hi, Jarvis A.I. here, how may I help you?", api_key)
#     st.session_state.greeted = True

# # Main loop for continuous listening
# while True:
#     query = take_command().lower()
#     if "close the program jarvis" in query:
#         close_program()  # Exit the loop and end the program
#     elif query:
#         jarvis_ai(query)  # Execute the command







# import os
# import speech_recognition as sr
# import streamlit as st
# import pyttsx3
# import datetime
# import subprocess as sp
# from openaitest import search_on_google, youtube, find_my_ip
# import time

# # Initialize the voice engine
# engine = pyttsx3.init()

# def say(text):
#     engine.say(text)
#     engine.runAndWait()

# def takeCommand():
#     r = sr.Recognizer()
#     with sr.Microphone() as source:
#         st.write("Listening...")
#         audio = r.listen(source)
#         try:
#             st.write("Recognizing...")
#             query = r.recognize_google(audio, language="en-in")
#             st.write(f"User said: {query}")
#             return query
#         except sr.UnknownValueError:
#             st.write("Sorry, I could not understand the audio.")
#             return None
#         except sr.RequestError as e:
#             st.write(f"Could not request results; {e}")
#             return None

# def open_camera():
#     try:
#         sp.run('start microsoft.windows.camera:', shell=True, check=True)
#         st.write("Opening camera...")
#     except sp.CalledProcessError as e:
#         st.write(f"Failed to open camera: {e}")

# def execute_command(query):
#     if "open youtube" in query:
#         say("What do you want to play on YouTube, sir?")
#         st.session_state.awaiting_input = "youtube"
    
#     elif "open google" in query or "search on google" in query:
#         say("What do you want to search on Google, sir?")
#         st.session_state.awaiting_input = "google"
    
#     elif "open music" in query:
#         musicPath = r"C:\Users\Hp\Downloads\drift-phonk-156625.mp3"
#         os.startfile(musicPath)
#         st.write("Playing music...")
    
#     elif "the time" in query:
#         hour = datetime.datetime.now().strftime("%H")
#         minute = datetime.datetime.now().strftime("%M")
#         say(f"Sir, the time is {hour} hours and {minute} minutes.")
#         st.write(f"The time is {hour}:{minute}.")
    
#     elif "ip address" in query:
#         ip_address = find_my_ip()
#         say("Your IP address is confidential.")
#         st.write("Your IP address is hidden.")
    
#     elif "open camera" in query:
#         open_camera()

#     # Only prompt for the next command if there’s no pending input
#     if st.session_state.awaiting_input is None:
#         say("Anything else I can do for you, sir?")

# # Streamlit App Layout
# st.title("TOM A.I. Voice Assistant")
# st.write("Hi, I am TOM A.I. How can I help you today?")

# # Initialize session state if they don't exist
# if "awaiting_input" not in st.session_state:
#     st.session_state.awaiting_input = None

# if "last_command_time" not in st.session_state:
#     st.session_state.last_command_time = time.time()

# # Main command handling loop
# if st.session_state.awaiting_input is None:
#     query = takeCommand()
#     if query:
#         execute_command(query)
#         st.session_state.last_command_time = time.time()  # Reset last command time

# # Handle follow-up commands
# if st.session_state.awaiting_input == "youtube":
#     video = takeCommand()
#     if video:
#         youtube(video)
#         st.write(f"Playing {video} on YouTube...")
#         st.session_state.awaiting_input = None  # Reset awaiting input

# elif st.session_state.awaiting_input == "google":
#     search_query = takeCommand()
#     if search_query:
#         search_on_google(search_query)
#         st.write(f"Searching Google for {search_query}...")
#         st.session_state.awaiting_input = None  # Reset awaiting input

# # Check for idle state to show "Close TOM" button
# if time.time() - st.session_state.last_command_time > 3:
#     if st.button("Close TOM", key="close_tom_button"):
#         say("Goodbye, thank you for using TOM A.I.!")

# # Debugging output
# st.write("Session State:", st.session_state)
