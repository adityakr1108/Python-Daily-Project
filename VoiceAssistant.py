import os
import subprocess
import speech_recognition as sr
import pyttsx3
from googletrans import Translator, LANGUAGES
from googlesearch import search  # To perform web searches

def initialize_tts():
    """Initializes the text-to-speech engine."""
    engine = pyttsx3.init()
    return engine

def speak(text, engine, lang='en'):
    """Converts text to speech."""
    engine.say(text)
    engine.runAndWait()

def open_application(app_name, engine):
    """Tries to open an application."""
    try:
        message = f"Opening {app_name}."
        print(message)
        speak(message, engine)
        subprocess.Popen(app_name)  # For Windows, pass the full path of the application if needed.
    except FileNotFoundError:
        message = f"Could not find the application: {app_name}."
        print(message)
        speak(message, engine)

def search_web(query, engine):
    """Performs a Google search for the query."""
    import requests

def search_web(query, engine):
    """Performs a web search using the Bing Search API."""
    speak(f"Searching for {query}", engine)
    print(f"Searching for: {query}")
    
    subscription_key = "AIzaSyB3RToH1tIzfeQJ4yULt5PbD6x0vuXSX84"  # Replace with your Bing API key
    search_url = "https://api.bing.microsoft.com/v7.0/search"
    headers = {"Ocp-Apim-Subscription-Key": subscription_key}
    params = {"q": query, "textDecorations": True, "textFormat": "HTML"}
    
    try:
        response = requests.get(search_url, headers=headers, params=params)
        response.raise_for_status()
        search_results = response.json()

        for result in search_results["webPages"]["value"]:
            print(result["url"])
            speak(result["url"], engine)

    except Exception as e:
        message = f"An error occurred while searching the web: {e}"
        print(message)
        speak(message, engine)


def stop_script(engine):
    """Stops the script."""
    message = "Stopping the script."
    print(message)
    speak(message, engine)
    return "stop"

def invalid_command(engine):
    """Handles invalid commands."""
    message = "Not a valid command. Please try again."
    print(message)
    speak(message, engine)

def translate_text(text, dest_lang):
    """Translates text into the desired language."""
    try:
        translator = Translator()
        translation = translator.translate(text, dest=dest_lang)
        return translation.text
    except Exception as e:
        print(f"Translation failed: {e}")
        return text  # Return the original text if translation fails

def process_command(command, engine, lang='en'):
    """Processes the recognized voice command."""
    if command in ["stop", "exit", "quit"]:
        return stop_script(engine)

    # If the command is to open an application
    if command.startswith("open"):
        app_name = command.replace("open", "").strip()
        open_application(app_name, engine)
        return

    # If the command is none of the above, default to web search
    search_web(command, engine)

def listen_commands(engine, lang='en'):
    """Listens for voice commands, translates them, and processes them."""
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)
        print("Voice command system is ready. Say a command.")
        speak("Voice command system is ready. Say a command.", engine)

    while True:
        with sr.Microphone() as source:
            print("\nListening for a command...")
            recognizer.adjust_for_ambient_noise(source)
            audio = recognizer.listen(source)
            print("Processing...")

        try:
            command = recognizer.recognize_google(audio).lower()
            print(f"You said: {command}")
            speak(f"You said: {command}", engine)
            if process_command(command, engine, lang) == "stop":
                break  # Stop the script if stop command is issued
        except sr.UnknownValueError:
            message = "I did not understand that. Please try again."
            print(message)
            speak(message, engine)
        except sr.RequestError as e:
            message = f"Could not request results from Google Speech Recognition service; {e}"
            print(message)
            speak("There was an error with the speech recognition service.", engine)

def display_languages():
    """Displays available languages for translation."""
    print("Available languages:")
    for code, name in LANGUAGES.items():
        print(f"{code}: {name}")

def main():
    engine = initialize_tts()
    display_languages()
    
    # Prompt user to select a language
    lang = input("Enter the language code for translation (e.g., 'es' for Spanish): ").strip()
    if lang not in LANGUAGES:
        print("Invalid language code. Using default language (English).")
        lang = 'en'

    listen_commands(engine, lang)

if __name__ == "__main__":
    main()
