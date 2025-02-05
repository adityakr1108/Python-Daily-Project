import os
import speech_recognition as sr
import pyttsx3

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def run_command(query, engine):
    recognizer = sr.Recognizer()
    microphone = sr.Microphone()

    # Ask the user to choose a country
    message = "Please choose a country to play the game: India, United States, or Other"
    print(message)
    speak(message)

    with microphone as source:
        recognizer.adjust_for_ambient_noise(source)
        print("Listening...")
        speak("Listening...")

        user_input = input("In which way you want to give input, text or speech: ").lower()
        if user_input == "speech":
            audio = recognizer.listen(source)
            try:
                # Recognize speech using Google Web Speech API
                country = recognizer.recognize_google(audio).lower()
            except sr.UnknownValueError:
                message = "Sorry, I could not understand the audio."
                print(message)
                speak(message)
                return
            except sr.RequestError as e:
                message = f"Could not request results from Google Web Speech API; {e}"
                print(message)
                speak(message)
                return
        elif user_input == "text":
            country = input("Please type the country name: ").lower()
        else:
            message = "Invalid input method. Please choose either 'text' or 'speech'."
            print(message)
            speak(message)
            return

    print(f"You said: {country}")
    speak(f"You said: {country}")

    if "india" in country:
        message = "Opening and running India game..."
        print(message)
        speak(message)
        os.system("python india.py")
    elif "united states" in country or "us" in country:
        message = "Opening and running United States Map"
        print(message)
        speak(message)
        os.system("python united_states.py")
    elif "other" in country:
        message = "Opening and running Other country game..."
        print(message)
        speak(message)
        os.system("python other_country.py")
    else:
        message = "Sorry, I didn't understand that. Please choose either 'India', 'United States', or 'Other'."
        print(message)
        speak(message)

# Example usage
run_command(None, None)