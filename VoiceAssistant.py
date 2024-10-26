import os
import subprocess
import speech_recognition as sr
import pyttsx3
from googletrans import Translator, LANGUAGES
from googlesearch import search


def display_ascii():
     print("""
 _____                                                                        _____ 
( ___ )                                                                      ( ___ )
 |   |~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|   | 
 |   | ...................................................................... |   | 
 |   | ......█.....█░▓█████..██▓.....▄████▄...▒█████...███▄.▄███▓▓█████...... |   | 
 |   | .....▓█░.█.░█░▓█...▀.▓██▒....▒██▀.▀█..▒██▒..██▒▓██▒▀█▀.██▒▓█...▀...... |   | 
 |   | .....▒█░.█.░█.▒███...▒██░....▒▓█....▄.▒██░..██▒▓██....▓██░▒███........ |   | 
 |   | .....░█░.█.░█.▒▓█..▄.▒██░....▒▓▓▄.▄██▒▒██...██░▒██....▒██.▒▓█..▄...... |   | 
 |   | .....░░██▒██▓.░▒████▒░██████▒▒.▓███▀.░░.████▓▒░▒██▒...░██▒░▒████▒..... |   | 
 |   | .....░.▓░▒.▒..░░.▒░.░░.▒░▓..░░.░▒.▒..░░.▒░▒░▒░.░.▒░...░..░░░.▒░.░..... |   | 
 |   | .......▒.░.░...░.░..░░.░.▒..░..░..▒.....░.▒.▒░.░..░......░.░.░..░..... |   | 
 |   | .......░...░.....░.....░.░...░........░.░.░.▒..░......░......░........ |   | 
 |   | .........░.......░..░....░..░░.░..........░.░.........░......░..░..... |   | 
 |   | .............................░........................................ |   | 
 |   | .......................▄▄▄█████▓.▒█████............................... |   | 
 |   | .......................▓..██▒.▓▒▒██▒..██▒............................. |   | 
 |   | .......................▒.▓██░.▒░▒██░..██▒............................. |   | 
 |   | .......................░.▓██▓.░.▒██...██░............................. |   | 
 |   | .........................▒██▒.░.░.████▓▒░............................. |   | 
 |   | .........................▒.░░...░.▒░▒░▒░.............................. |   | 
 |   | ...........................░......░.▒.▒░.............................. |   | 
 |   | .........................░......░.░.░.▒............................... |   | 
 |   | ....................................░.░............................... |   | 
 |   | ...................................................................... |   | 
 |   | ........................███▄.▄███▓▓██...██▓........................... |   | 
 |   | .......................▓██▒▀█▀.██▒.▒██..██▒........................... |   | 
 |   | .......................▓██....▓██░..▒██.██░........................... |   | 
 |   | .......................▒██....▒██...░.▐██▓░........................... |   | 
 |   | .......................▒██▒...░██▒..░.██▒▓░........................... |   | 
 |   | .......................░.▒░...░..░...██▒▒▒............................ |   | 
 |   | .......................░..░......░.▓██.░▒░............................ |   | 
 |   | .......................░......░....▒.▒.░░............................. |   | 
 |   | ..............................░....░.░................................ |   | 
 |   | ...................................░.░................................ |   | 
 |   | ............█.....█░.▒█████...██▀███...██▓....▓█████▄................. |   | 
 |   | ...........▓█░.█.░█░▒██▒..██▒▓██.▒.██▒▓██▒....▒██▀.██▌................ |   | 
 |   | ...........▒█░.█.░█.▒██░..██▒▓██.░▄█.▒▒██░....░██...█▌................ |   | 
 |   | ...........░█░.█.░█.▒██...██░▒██▀▀█▄..▒██░....░▓█▄...▌................ |   | 
 |   | ...........░░██▒██▓.░.████▓▒░░██▓.▒██▒░██████▒░▒████▓................. |   | 
 |   | ...........░.▓░▒.▒..░.▒░▒░▒░.░.▒▓.░▒▓░░.▒░▓..░.▒▒▓..▒................. |   | 
 |   | .............▒.░.░....░.▒.▒░...░▒.░.▒░░.░.▒..░.░.▒..▒................. |   | 
 |   | .............░...░..░.░.░.▒....░░...░...░.░....░.░..░................. |   | 
 |   | ...............░........░.░.....░.........░..░...░.................... |   | 
 |   | ...............................................░...................... |   | 
 |   | ...................................................................... |   | 
 |___|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|___| 
(_____)                                                                      (_____)
""")
def initialize_tts():
    """Initializes the text-to-speech engine and sets it to a female voice if available."""
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    # Set to female voice if available
    for voice in voices:
        if "female" in voice.name.lower():
            engine.setProperty('voice', voice.id)
            break
    return engine

def speak(text, engine):
    """Converts text to speech."""
    engine.say(text)
    engine.runAndWait()

def open_application(app_name, engine):
    """Opens an application based on its name."""
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
        speak(f"Opening {app_name}.", engine)
        subprocess.Popen(app_paths[app_name])
    else:
        speak(f"I don't know how to open {app_name}.", engine)

def open_python_script(file_path, engine):
    """Opens a specified Python file."""
    if os.path.exists(file_path):
        speak("Opening Python file.", engine)
        subprocess.Popen(["python", file_path], shell=True)
    else:
        speak("The specified file path does not exist.", engine)

def play_game(game_name, engine):
    """Runs a specified game."""
    games = {
        "hangman": "Hangman\main.py",
        "turtle cross": "Turtle Cross\main.py",
        "ping pong": "Pong Game\pingPong\main.py",
        "snake": "Snake-Game-using-python-main\main.py",
        "blackbox": "BlackJack-Game-using-python-main\BlackJack-Game-using-python-main\blackbox.py",
        "state" : "state\main.py"
    }
    if game_name in games:
        open_python_script(games[game_name], engine)
    else:
        speak("Game not available.", engine)

def system_command(command, engine):
    """Executes system commands."""
    if command == "shutdown":
        speak("Shutting down the system.", engine)
        os.system("shutdown /s /t 1")
    elif command == "restart":
        speak("Restarting the system.", engine)
        os.system("shutdown /r /t 1")

def search_web(query, engine):
    """Performs a web search."""
    speak(f"Searching for {query}", engine)
    for result in search(query, num_results=5):
        print(result)
        speak(result, engine)

def translate_text(text, dest_lang, engine):
    """Translates text to the desired language."""
    try:
        translator = Translator()
        translation = translator.translate(text, dest=dest_lang)
        speak(f"Translation: {translation.text}", engine)
    except Exception as e:
        speak("Translation failed.", engine)

def display_menu(engine):
    """Displays the main menu options."""
    menu = """
    Please choose an option:
    1. Open an application
    2. Translate text
    3. Web search
    4. Play a game
    5. System command (shutdown, restart)
    """
    print(menu)
    speak(menu, engine)

def process_main_menu_choice(choice, engine, recognizer):
    """Processes the user choice from the main menu."""
    if choice == "open an application" or choice == "one":
        speak("Which application would you like to open?", engine)
        app_name = listen_for_command(recognizer, engine)
        open_application(app_name.lower(), engine)

    elif choice == "translate text" or choice == "two":
        speak("Which language would you like to translate to?", engine)
        for code, name in LANGUAGES.items():
            print(f"{code}: {name}")
        dest_lang = input("Enter language code: ").strip()
        speak("What text would you like to translate?", engine)
        text = listen_for_command(recognizer, engine)
        translate_text(text, dest_lang, engine)

    elif choice == "web search" or choice == "three":
        speak("What would you like to search for?", engine)
        query = listen_for_command(recognizer, engine)
        search_web(query, engine)

    elif choice == "play a game" or choice == "four":
        speak("Which game would you like to play? Options: hangman, turtle cross, ping pong, snake, state, blackbox ", engine)
        game_name = listen_for_command(recognizer, engine)
        play_game(game_name.lower(), engine)

    elif choice == "system command" or choice == "five":
        speak("Which system command would you like to perform? Options: shutdown, restart", engine)
        command = listen_for_command(recognizer, engine)
        system_command(command.lower(), engine)

    speak("Would you like to perform another action? Say yes or no.", engine)
    response = listen_for_command(recognizer, engine)
    return response.lower() == "yes"

def listen_for_command(recognizer, engine):
    """Listens for a command with an optimized setup for faster response."""
    print("\nListening for a command...")
    speak("Listening.", engine)
    with sr.Microphone() as source:
        # Adjust for ambient noise only once at the start
        audio = recognizer.listen(source, timeout=2, phrase_time_limit=5)  # Limits to a shorter duration
    try:
        command = recognizer.recognize_google(audio).lower()
        print(f"User said: {command}")
        return command
    except sr.UnknownValueError:
        speak("I did not understand. Please try again.", engine)
        return listen_for_command(recognizer, engine)
    except sr.RequestError:
        speak("Error with the speech service.", engine)
        return ""

def main():
    engine = initialize_tts()
    recognizer = sr.Recognizer()

    display_ascii()
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source, duration=0.5)

    while True:
        
        display_menu(engine)
        speak("Please say your choice.", engine)
        choice = listen_for_command(recognizer, engine)
        continue_choice = process_main_menu_choice(choice, engine, recognizer)

        if not continue_choice or choice in ["exit", "stop", "quit"]:
            speak("Exiting the program.", engine)
            break

if __name__ == "__main__":
    
    main()
