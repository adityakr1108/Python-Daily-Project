import os
import subprocess
import speech_recognition as sr
import pyttsx3
from googletrans import Translator, LANGUAGES
from googlesearch import search  


def initialize_tts():
    """Initializes the text-to-speech engine."""
    engine = pyttsx3.init()
    return engine


def speak(text, engine):
    """Converts text to speech."""
    engine.say(text)
    engine.runAndWait()


def open_application(app_name, engine):
    """Tries to open an application based on its name."""
    app_paths = {
        "chrome": r"C:\Program Files\Google\Chrome\Application\chrome.exe",
        "brave": r"C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe",
        "microsoft edge": r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
        "notepad": r"C:\Windows\System32\notepad.exe",
        "calculator": r"C:\Windows\System32\calc.exe",
        "microsoft word": r"C:\Program Files (x86)\Microsoft Office\root\Office16\WINWORD.EXE",
        "r studio": r"C:\Program Files\RStudio\rstudio.exe",
        "tableau": r"C:\Program Files\Tableau\Tableau 2021.2\bin\tableau.exe",
    }

    if app_name in app_paths:
        try:
            message = f"Opening {app_name}."
            print(message)
            speak(message, engine)
            subprocess.Popen(app_paths[app_name])  # Opens the application from the actual executable path
        except FileNotFoundError:
            message = f"Could not find the application: {app_name}."
            print(message)
            speak(message, engine)
    else:
        message = f"I don't know how to open {app_name}."
        print(message)
        speak(message, engine)


def system_command(command, engine):
    """Handles system commands like shutdown and restart."""
    if command == "shutdown":
        speak("Shutting down the system.", engine)
        os.system("shutdown /s /t 1")
    elif command == "restart":
        speak("Restarting the system.", engine)
        os.system("shutdown /r /t 1")


def search_web(query, engine):
    """Performs a Google search for the query using googlesearch-python."""
    speak(f"Searching for {query}", engine)
    print(f"Searching for: {query}")

    try:
        for result in search(query, num_results=5):
            print(result)
            speak(result, engine)
    except Exception as e:
        message = f"An error occurred while searching the web: {e}"
        print(message)
        speak(message, engine)


def translate_text(text, dest_lang, engine):
    """Translates text into the desired language."""
    try:
        translator = Translator()
        translation = translator.translate(text, dest=dest_lang)
        speak(f"Translation: {translation.text}", engine)
        print(f"Translation: {translation.text}")
        return translation.text
    except Exception as e:
        print(f"Translation failed: {e}")
        speak(f"Translation failed.", engine)
        return text  # Return the original text if translation fails


def stop_script(engine):
    """Stops the script."""
    message = "Stopping the script."
    print(message)
    speak(message, engine)
    return "stop"


def process_command(command, engine, recognizer, lang='en'):
    """Processes the recognized voice command."""
    
    if command in ["stop", "exit", "quit"]:
        return stop_script(engine)

    if command in ["shutdown", "restart"]:
        system_command(command, engine)
        return

    # If the command is to open an application
    if command.startswith("open"):
        app_name = command.replace("open", "").strip().lower()
        open_application(app_name, engine)
        return

    # If the command starts with "translate", perform direct translation
    if command.startswith("translate"):
        speak("Which language would you like to translate to?", engine)
        for code, name in LANGUAGES.items():
            print(f"{code}: {name}")

        lang_code = input("Enter the language code: ").strip()
        if lang_code in LANGUAGES:
            text_to_translate = command.replace("translate", "").strip()
            translate_text(text_to_translate, lang_code, engine)
        else:
            speak("Invalid language code.", engine)
        return

    # Otherwise, perform a web search
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
            if process_command(command, engine, recognizer, lang) == "stop":
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
