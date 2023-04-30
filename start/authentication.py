import requests, json, time, sys
from discord_webhook import DiscordEmbed, DiscordWebhook

from data.storage import *

if license_key == "" or license_key == "KENKI-0000-0000-0000-0000":
    license_key = input(fg.light_red + f"[ Home ] [ {time.strftime('%H:%M:%S', time.localtime())} ]" + fg.dark_grey + " • " + fg.rs + "Input your license key: ")
    with open('config.json', 'r+') as f:
        data = json.load(f)
        data['License_Key'] = license_key
        f.seek(0)
        json.dump(data, f, indent=4)
        f.truncate()

print(fg.light_red + f"[ Home ] [ {time.strftime('%H:%M:%S', time.localtime())} ]" + fg.dark_grey + " • " + fg.rs + "Authenticating license key...")

payload = {
    "metadata": {
        "hardware_id": 
        hardware_id
    }
}
headers = {
    "accept": "application/json",
    "Authorization": "Bearer ",
    "content-type": "application/json",
}
authentication_response = requests.post(f"https://api.whop.com/api/v2/memberships/{license_key}/validate_license", json=payload, headers=headers)

if response.status_code == 201:
    response_text = json.loads(authentication_response.text)
    key_key = response_text["license_key"]
    key_status = response_text["status"]
    key_username = response_text["discord"]["username"]
    key_user_id = response_text["discord"]["id"]
    webhook = DiscordWebhook(url=private_webhook_authentication, avatar_url="https://media.discordapp.net/attachments/878354931201998859/1059895159959076975/kenki_logo_render.png")
    embed = DiscordEmbed(title=f'KenkiTools authentication logger', description=f'{key_username} logged into KenkiTools', color="bc252c")
    webhook.add_embed(embed)
    embed.set_footer(text=f"KenkiTools", icon_url="https://media.discordapp.net/attachments/878354931201998859/1059895159959076975/kenki_logo_render.png")
    embed.set_timestamp()
    embed.add_embed_field(name='Version', value=f'{current_version}', inline=False)
    embed.add_embed_field(name='User', value=f'<@{key_user_id}>', inline=False)
    embed.add_embed_field(name='Status', value=f'{key_status}', inline=False)
    embed.add_embed_field(name='License key', value=f'{key_key}', inline=False)
    embed.add_embed_field(name='Hardware ID', value=f'{hardware_id}', inline=False)
    response = webhook.execute()
    print(fg.light_red + f"[ Home ] [ {time.strftime('%H:%M:%S', time.localtime())} ]" + fg.dark_grey + " • " + fg.green + "Successfully authorized license key\n")
else:
    response_text = json.loads(authentication_response.text)
    webhook = DiscordWebhook(url=private_webhook_authentication, avatar_url="https://media.discordapp.net/attachments/878354931201998859/1059895159959076975/kenki_logo_render.png")
    embed = DiscordEmbed(title=f'KenkiTools authentication logger', description='', color="bc252c")
    webhook.add_embed(embed)
    embed.set_footer(text=f"KenkiTools", icon_url="https://media.discordapp.net/attachments/878354931201998859/1059895159959076975/kenki_logo_render.png")
    embed.set_timestamp()
    embed.add_embed_field(name='Status', value=f'{authentication_response.status_code} - {response_text["error"]}', inline=False)
    embed.add_embed_field(name='License key', value=f'{license_key}', inline=False)
    embed.add_embed_field(name='Hardware ID', value=f'{hardware_id}', inline=False)
    response = webhook.execute()
    input(fg.light_red + f"[ Home ] [ {time.strftime('%H:%M:%S', time.localtime())} ]" + fg.dark_grey + " • " + fg.red + f'Status Code {authentication_response.status_code} - {response_text["error"]}, press any key to exit')
    sys.exit()
