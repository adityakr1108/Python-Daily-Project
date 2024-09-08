import sys
import ctypes
import speech_recognition as sr
import os
import pyttsx3
from googletrans import Translator, LANGUAGES

def initialize_tts():
    """Initializes the text-to-speech engine."""
    engine = pyttsx3.init()
    return engine

def speak(text, engine, lang='en'):
    """Converts text to speech."""
    # Set the voice property if needed
    engine.say(text)
    engine.runAndWait()

def lock_workstation(engine):
    """Locks the Windows workstation."""
    message = "Locking the workstation."
    print(message)
    speak(message, engine)
    ctypes.windll.user32.LockWorkStation()

def shutdown_pc(engine):
    """Shuts down the PC."""
    message = "Shutting down the PC."
    print(message)
    speak(message, engine)
    os.system("shutdown /s /t 1")

def restart_pc(engine):
    """Restarts the PC."""
    message = "Restarting the PC."
    print(message)
    speak(message, engine)
    os.system("shutdown /r /t 1")

def sleep_pc(engine):
    """Puts the PC to sleep."""
    message = "Putting the PC to sleep."
    print(message)
    speak(message, engine)
    os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")

def hibernate_pc(engine):
    """Hibernates the PC."""
    message = "Hibernating the PC."
    print(message)
    speak(message, engine)
    os.system("shutdown /h")

def stop_script(engine):
    """Stops the script."""
    message = "Stopping the script."
    print(message)
    speak(message, engine)
    sys.exit(0)

def invalid_command(engine):
    """Handles invalid commands."""
    message = "Not a valid command. Please try again."
    print(message)
    speak(message, engine)

def translate_text(text, dest_lang):
    """Translates text into the desired language."""
    translator = Translator()
    translation = translator.translate(text, dest=dest_lang)
    return translation.text

def process_command(command, engine, lang='en'):
    """Processes the recognized voice command and translates it."""
    if command in ["lock my pc", "lock"]:
        action = "lock_workstation"
    elif command in ["shutdown my pc", "shutdown"]:
        action = "shutdown_pc"
    elif command in ["restart my pc", "restart"]:
        action = "restart_pc"
    elif command in ["sleep my pc", "sleep"]:
        action = "sleep_pc"
    elif command in ["hibernate my pc", "hibernate"]:
        action = "hibernate_pc"
    elif command in ["stop", "exit", "quit"]:
        action = "stop_script"
    else:
        action = "invalid_command"

    if action in globals():
        func = globals()[action]
        func(engine)
    else:
        invalid_command(engine)

    # Translate response to selected language
    message = {
        "lock_workstation": "Locking the workstation.",
        "shutdown_pc": "Shutting down the PC.",
        "restart_pc": "Restarting the PC.",
        "sleep_pc": "Putting the PC to sleep.",
        "hibernate_pc": "Hibernating the PC.",
        "stop_script": "Stopping the script.",
        "invalid_command": "Not a valid command. Please try again."
    }.get(action, "Unknown command")

    translated_message = translate_text(message, lang)
    print(f"Translated Message: {translated_message}")
    speak(translated_message, engine)

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
            process_command(command, engine, lang)
        except sr.UnknownValueError:
            message = "I did not understand that. Please try again."
            print(message)
            speak(message, engine, lang)
        except sr.RequestError as e:
            message = f"Could not request results from Google Speech Recognition service; {e}"
            print(message)
            speak("There was an error with the speech recognition service.", engine, lang)

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
