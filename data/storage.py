import json, requests, re, uuid, time, os
from twocaptcha import TwoCaptcha
from data.colors import *

def get_hwid() -> str:
    return ':'.join(re.findall('..', '%012x' % uuid.getnode()))

def print_logo():
    print(fg.light_red + "    _  __             _     _    _____             _")
    print(fg.light_red + "   | |/ / ___  _ __  | | _ (_)  |_   _| __   ___  | | ___ ")
    print(fg.light_red + "   | ' / / _ \| '_ \ | |/ /| |    | | / _ \ / _ \ | |/ __|")
    print(fg.light_red + "   | . \   __/| | | ||   < | |    | || (_) | (_) || |\__ \\")
    print(fg.light_red + "   |_|\_\\\\___||_| |_||_|\_\|_|    |_| \___/ \___/ |_||___/\n\n")

def clear_console():
    try:
        os.system('cls')
    except:
        os.system('clear')

public_webhook_aio = ""
public_webhook_revolut = ""
public_webhook_hyper = ""
private_webhook_authentication = ""
private_webhook_tasks = ""
private_webhook_hyper = ""
private_webhook_error = ""
private_webhook_revolut = ""
start = int(time.time())

try:
    config_file = open(r"config.json", "r")
    config = json.loads(config_file)
    version_file = open("version.json", "r")
    version_json = json.load(version_file)
    current_version = version_json["version"]
except:
    print("Error getting version")
    time.sleep(3)
try:
    license_key = config["License_Key"]
except:
    pass
try:
    user_webhook = config["Webhook"]
except:
    print("Error getting webhook")
    time.sleep(3)
try:
    show_name = config["show-username"]
except:
    with open('config.json', 'r+') as f:
        data = json.load(f)
        data['show-username'] = "true"
        f.seek(0)
        json.dump(data, f, indent=4)
        f.truncate()
try:
    api_key = config["Generator"]["2Captcha"]
    solver = TwoCaptcha(api_key)
except:
    print("Error getting 2captcha api key")

hardware_id = get_hwid()
payload = {"metadata": {"hardware_id": hardware_id}}
headers = {
    "accept": "application/json",
    "content-type": "application/json",
    "Authorization": "Bearer "
}
try:
    response = requests.post(f"https://api.whop.com/api/v2/memberships/{license_key}/validate_license", json=payload, headers=headers)
    response_text = response.text
    response_text2 = json.loads(response_text)
    key_email = response_text2["email"]
    key_key = response_text2["license_key"]
    key_status = response_text2["status"]
    key_created = response_text2["created_at"]
    key_username = response_text2["discord"]["username"]
    key_user_id = response_text2["discord"]["id"]
except:
    pass

try:
    if "https://discord.com/api/webhooks/" in user_webhook:
        pass
    else:
        user_webhook = input(fg.light_red + f"[ Home ] [ {time.strftime('%H:%M:%S', time.localtime())} ]" + fg.dark_grey + " • " + fg.rs + "Input your Webhook: ")
        with open('config.json', 'r+') as f:
            data = json.load(f)
            data['Webhook'] = user_webhook
            f.seek(0)
            json.dump(data, f, indent=4)
            f.truncate()
except:
    pass
