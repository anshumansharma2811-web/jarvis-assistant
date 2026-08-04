import pyttsx3
import speech_recognition as sr
import psutil
import datetime

engine = pyttsx3.init()

def speak(text):
    print("JARVIS:", text)
    engine.say(text)
    engine.runAndWait()

def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)

    try:
        command = r.recognize_google(audio)
        print("You:", command)
        return command.lower()
    except:
        speak("Sorry, I didn't catch that")
        return ""

def check_time():
    time = datetime.datetime.now().strftime("%H:%M")
    speak(f"The time is {time}")

def check_devices():
    devices = psutil.disk_partitions()
    speak(f"You have {len(devices)} storage devices connected")

def check_cpu():
    cpu = psutil.cpu_percent()
    speak(f"CPU usage is {cpu} percent")

def run_jarvis():
    speak("Hello Ansh, Jarvis is online")

    while True:
        command = take_command()

        if "time" in command:
            check_time()

        elif "devices" in command:
            check_devices()

        elif "cpu" in command:
            check_cpu()

        elif "status" in command:
            check_cpu()
            check_devices()

        elif "exit" in command:
            speak("Goodbye")
            break

run_jarvis()

