import os
import subprocess
import speech_recognition as sr
import pyttsx3
from googletrans import Translator, LANGUAGES
from googlesearch import search

# for chatbot
import requests 
import json

# for database
import bcrypt
import sqlite3
import getpass


def display_ascii():
    print("""
#  _____                                                                        _____ 
# ( ___ )                                                                      ( ___ )
#  |   |~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|   | 
#  |   | ...................................................................... |   | 
#  |   | ......█.....█░▓█████..██▓.....▄████▄...▒█████...███▄.▄███▓▓█████...... |   | 
#  |   | .....▓█░.█.░█░▓█...▀.▓██▒....▒██▀.▀█..▒██▒..██▒▓██▒▀█▀.██▒▓█...▀...... |   | 
#  |   | .....▒█░.█.░█.▒███...▒██░....▒▓█....▄.▒██░..██▒▓██....▓██░▒███........ |   | 
#  |   | .....░█░.█.░█.▒▓█..▄.▒██░....▒▓▓▄.▄██▒▒██...██░▒██....▒██.▒▓█..▄...... |   | 
#  |   | .....░░██▒██▓.░▒████▒░██████▒▒.▓███▀.░░.████▓▒░▒██▒...░██▒░▒████▒..... |   | 
#  |   | .....░.▓░▒.▒..░░.▒░.░░.▒░▓..░░.░▒.▒..░░.▒░▒░▒░.░.▒░...░..░░░.▒░.░..... |   | 
#  |   | .......▒.░.░...░.░..░░.░.▒..░..░..▒.....░.▒.▒░.░..░......░.░.░..░..... |   | 
#  |   | .......░...░.....░.....░.░...░........░.░.░.▒..░......░......░........ |   | 
#  |   | .........░.......░..░....░..░░.░..........░.░.........░......░..░..... |   | 
#  |   | .............................░........................................ |   | 
#  |   | .......................▄▄▄█████▓.▒█████............................... |   | 
#  |   | .......................▓..██▒.▓▒▒██▒..██▒............................. |   | 
#  |   | .......................▒.▓██░.▒░▒██░..██▒............................. |   | 
#  |   | .......................░.▓██▓.░.▒██...██░............................. |   | 
#  |   | .........................▒██▒.░.░.████▓▒░............................. |   | 
#  |   | .........................▒.░░...░.▒░▒░▒░.............................. |   | 
#  |   | ...........................░......░.▒.▒░.............................. |   | 
#  |   | .........................░......░.░.░.▒............................... |   | 
#  |   | ....................................░.░............................... |   | 
#  |   | ...................................................................... |   | 
#  |   | ........................███▄.▄███▓▓██...██▓........................... |   | 
#  |   | .......................▓██▒▀█▀.██▒.▒██..██▒........................... |   | 
#  |   | .......................▓██....▓██░..▒██.██░........................... |   | 
#  |   | .......................▒██....▒██...░.▐██▓░........................... |   | 
#  |   | .......................▒██▒...░██▒..░.██▒▓░........................... |   | 
#  |   | .......................░.▒░...░..░...██▒▒▒............................ |   | 
#  |   | .......................░..░......░.▓██.░▒░............................ |   | 
#  |   | .......................░......░....▒.▒.░░............................. |   | 
#  |   | ..............................░....░.░................................ |   | 
#  |   | ...................................░.░................................ |   | 
#  |   | ............█.....█░.▒█████...██▀███...██▓....▓█████▄................. |   | 
#  |   | ...........▓█░.█.░█░▒██▒..██▒▓██.▒.██▒▓██▒....▒██▀.██▌................ |   | 
#  |   | ...........▒█░.█.░█.▒██░..██▒▓██.░▄█.▒▒██░....░██...█▌................ |   | 
#  |   | ...........░█░.█.░█.▒██...██░▒██▀▀█▄..▒██░....░▓█▄...▌................ |   | 
#  |   | ...........░░██▒██▓.░.████▓▒░░██▓.▒██▒░██████▒░▒████▓................. |   | 
#  |   | ...........░.▓░▒.▒..░.▒░▒░▒░.░.▒▓.░▒▓░░.▒░▓..░.▒▒▓..▒................. |   | 
#  |   | .............▒.░.░....░.▒.▒░...░▒.░.▒░░.░.▒..░.░.▒..▒................. |   | 
#  |   | .............░...░..░.░.░.▒....░░...░...░.░....░.░..░................. |   | 
#  |   | ...............░........░.░.....░.........░..░...░.................... |   | 
#  |   | ...............................................░...................... |   | 
#  |   | ...................................................................... |   | 
#  |___|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|___| 
# (_____)                                                                      (_____)
                         !---Aditya Kumar Agrawal---!
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
    "hangman": r"Hangman\main.py",
    "turtle cross": r"Turtle Cross\main.py",
    "ping pong": r"Ping_Pong\pingPong\main.py",
    "snake": r"Snake-Game-using-python-main\main.py",
    "blackbox": r"BlackJack-Game-using-python-main\BlackJack-Game-using-python-main\blackbox.py",
    "state": r"state\main.py"
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
    6. Chatbot
    7. Exit
    """
    print(menu)
    speak(menu, engine)

# Starting of chatbot
# Local LM Studio API URL
LM_API_URL = "http://192.168.11.97:1234" 

def generate_ai_response(prompt):
    """Generate a response using the local LM Studio API."""
    data = {
        "model": "deepseek-ai.deepseek-r1-distill-llama-8b",  # Update with your model name if needed
        "messages": [{"role": "user", "content": prompt}]
    }

    headers = {
        "Content-Type": "application/json",
    }

    try:
        response = requests.post(f"{LM_API_URL}/v1/chat/completions", json=data, headers=headers)  # Fixed endpoint
        # print("Debug Response Status:", response.status_code)  # Debugging
        # print("Debug Response Text:", response.text)  # Debugging
        
        response_data = response.json()
        
        if 'choices' in response_data:
            return response_data['choices'][0]['message']['content']
        else:
            return "Sorry, I couldn't generate a response."
    except Exception as e:
        return f"An error occurred: {str(e)}"
    
def chatbot():
    print("🤖 AI Chatbot (Type 'exit' to quit)")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Chatbot: Goodbye! 👋")
            break

        response = generate_ai_response(user_input)
        print("Chatbot:", response)


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
    elif choice == "chatbot" or choice == "six":
        speak("Chat with Chatbot", engine)
        chatbot()
    elif choice == "exit" or choice == "seven":
        return False

    speak("Would you like to perform another action? Say yes or no.", engine)
    response = listen_for_command(recognizer, engine)
    return response.lower() == "yes"

def listen_for_command(recognizer, engine):
    """Listens for a command with extended listening time."""
    print("\nListening for a command...")
    speak("Listening. You may take your time to speak.", engine)
    with sr.Microphone() as source:
        # Adjust for ambient noise
        recognizer.adjust_for_ambient_noise(source, duration=0.5)
        # Increased timeout and phrase time limit    timeout=5: The program will wait up to 5 seconds for the user to start speaking.
        audio = recognizer.listen(source, timeout=5, phrase_time_limit=10)  # Allow 3 seconds of silence and up to 7 seconds for the user to speak
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

# Connect to SQLite database (or create one if it doesn't exist)
conn = sqlite3.connect("user.db")
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS users (username TEXT PRIMARY KEY, password BLOB)''')

# Define admin username and password (hashed for security)
admin_username = "admin"
admin_password = bcrypt.hashpw("adminpassword".encode('utf-8'), bcrypt.gensalt())


def register_user(username, password):
    # Hash the password
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    c.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, hashed_password))
    conn.commit()
    print("User registered successfully!")

def login_user(username, password):
    # Get the password for the entered username
    c.execute("SELECT password FROM users WHERE username = ?", (username,))
    result = c.fetchone()

    if result is None:
        print("Username not found!")
        return False

    stored_password = result[0]  # This is retrieved as bytes
    # Compare the hashed password with the entered one
    if bcrypt.checkpw(password.encode('utf-8'), stored_password):
        print("Login successful!")
        main()
        return True
    else:
        print("Invalid password!")
        return False
    
def admin_login(password):
    """ Check if the entered admin password is correct. """
    if bcrypt.checkpw(password.encode('utf-8'), admin_password):
        print("Admin login successful!")
        return True
    else:
        print("Invalid admin password!")
        return False
    
def show_all_users():
    """ Show all usernames and their hashed passwords (only for admin). """
    c.execute("SELECT username, password FROM users")
    users = c.fetchall()
    print("\nAll Users:")
    for user in users:
        print(f"Username: {user[0]}, Password (hashed): {user[1]}")
        
def delete_user(username):
    """ Delete a user from the database (only for admin). """
    if username == admin_username:
        print("Error: The admin account cannot be deleted!")
        return
    c.execute("DELETE FROM users WHERE username = ?", (username,))
    conn.commit()
    print(f"User {username} has been deleted successfully!")

if __name__ == "__main__":
    while True:
        action = input("Do you want to register, login, or admin login? (register/login/admin): ").strip().lower()
        if action == "register":
            username = input("Enter a username: ")
            password = getpass.getpass("Enter a password: ")  # Hide the password input
            register_user(username, password)
        elif action == "login":
            username = input("Enter your username: ")
            password = getpass.getpass("Enter your password: ")  # Hide the password input
            if login_user(username, password):
                main()
                break  # Exit the loop on successful login
        elif action == "admin":
            admin_password_input = getpass.getpass("Enter admin password: ")  # Admin password input
            if admin_login(admin_password_input):
                while True:
                    print("\nAdmin Menu: ")
                    show_all_users()  # Show all users
                    delete_option = input("Do you want to delete a user? (yes/no): ").strip().lower()
                    if delete_option == "yes":
                        username_to_delete = input("Enter the username of the user to delete: ")
                        delete_user(username_to_delete)
                    elif delete_option == "no":
                        print("Exiting admin mode...")
                        break  # Exit the admin mode
                    else:
                        print("Invalid option!")
        else:
            print("Invalid action!")
