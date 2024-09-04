import sys
import ctypes
import speech_recognition as sr
import os
import pyttsx3

def initialize_tts():
    """Initializes the text-to-speech engine."""
    engine = pyttsx3.init()
    # Optionally, set properties like voice, rate, and volume here
    return engine

def speak(text, engine):
    """Converts text to speech."""
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

def process_command(command, engine):
    """Processes the recognized voice command."""
    if command in ["lock my pc", "lock"]:
        lock_workstation(engine)
    elif command in ["shutdown my pc", "shutdown"]:
        shutdown_pc(engine)
        
    elif command in ["restart my pc", "restart"]:
        restart_pc(engine)
    elif command in ["sleep my pc", "sleep"]:
        sleep_pc(engine)
    elif command in ["hibernate my pc", "hibernate"]:
        hibernate_pc(engine)
    elif command in ["stop", "exit", "quit"]:
        stop_script(engine)
    else:
        invalid_command(engine)

def listen_commands(engine):
    """Listens for voice commands and processes them."""
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
            process_command(command, engine)
        except sr.UnknownValueError:
            message = "I did not understand that. Please try again."
            print(message)
            speak(message, engine)
        except sr.RequestError as e:
            message = f"Could not request results from Google Speech Recognition service; {e}"
            print(message)
            speak("There was an error with the speech recognition service.", engine)

def main():
    engine = initialize_tts()
    listen_commands(engine)

if __name__ == "__main__":
    main()
