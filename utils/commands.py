from utils.voice import speak
from utils.system import get_cpu

def handle_command(command):
    if "cpu" in command:
        cpu = get_cpu()
        speak(f"CPU usage is {cpu} percent")