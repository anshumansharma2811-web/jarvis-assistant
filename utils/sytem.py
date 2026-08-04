import psutil

def get_cpu():
    return psutil.cpu_percent()

def get_memory():
    return psutil.virtual_memory().percent