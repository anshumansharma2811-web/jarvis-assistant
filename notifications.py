import requests

def get_notifications():
    # Placeholder (real apps need API or webhook)
    print("Checking notifications...")
    return ["New WhatsApp message", "Instagram notification"]

if __name__ == "__main__":
    notes = get_notifications()
    for n in notes:
        print(n)