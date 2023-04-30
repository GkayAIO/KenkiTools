import datetime, random
from discord_webhook import DiscordWebhook, DiscordEmbed

from data.storage import *

def shuffleProxies():

    today = datetime.date.today()
    time_is = today.strftime("%m-%d-%y")
    print_logo()
    print(fg.light_red + f"[ Proxy ] [ {time.strftime('%H:%M:%S', time.localtime())} ]" + fg.dark_grey + " • " + fg.rs + "Fetching proxies...")
    total_proxies = 0

    with open("Misc/Proxies/Input.txt", "r") as f:
        data = [ (random.random(), line) for line in f ]
        for line in data:
            total_proxies += 1
        f.close()

    print(fg.light_red + f"[ Proxy ] [ {time.strftime('%H:%M:%S', time.localtime())} ]" + fg.dark_grey + " • " + fg.rs + f"Shuffling {total_proxies} proxies...")
    data.sort()

    with open(f"Misc/Proxies/Output/shuffled_{time_is}", "w") as f:
        for _, line in data:
            f.write( line )
        f.close()

    print(fg.light_red + f"[ Proxy ] [ {time.strftime('%H:%M:%S', time.localtime())} ]" + fg.dark_grey + " • " + fg.green + f"Successfully shuffled {total_proxies} proxies!")
    
    webhook = DiscordWebhook(url=user_webhook, avatar_url="https://media.discordapp.net/attachments/878354931201998859/1059895159959076975/kenki_logo_render.png", username="KenkiTools")
    embed = DiscordEmbed(title=f'Successfully Shuffled Proxies', description='', color='bc252c')
    embed.set_thumbnail(url="https://media.discordapp.net/attachments/878354931201998859/1059895159959076975/kenki_logo_render.png")
    embed.set_footer(text='@KenkiTools', icon_url="https://media.discordapp.net/attachments/878354931201998859/1059895159959076975/kenki_logo_render.png")
    embed.set_timestamp()
    embed.add_embed_field(name='Type', value='Proxy Shuffler', inline=False)
    embed.add_embed_field(name='Amount', value=f'{total_proxies}', inline=False)
    webhook.add_embed(embed)
    webhook.execute()

    webhook = DiscordWebhook(url=public_webhook_aio, avatar_url="https://media.discordapp.net/attachments/878354931201998859/1059895159959076975/kenki_logo_render.png", username="KenkiTools")
    embed = DiscordEmbed(title=f'Successfully Shuffled proxies', description='', color='bc252c')
    embed.set_thumbnail(url="https://media.discordapp.net/attachments/878354931201998859/1059895159959076975/kenki_logo_render.png")
    embed.set_footer(text=f'KenkiTools', icon_url="https://media.discordapp.net/attachments/878354931201998859/1059895159959076975/kenki_logo_render.png")
    embed.set_timestamp()
    embed.add_embed_field(name='Amount', value=f'{total_proxies}', inline=False)
    if show_name == "true":
        embed.add_embed_field(name='username', value=f'{key_username}', inline=False)
    else:
        embed.add_embed_field(name='username', value=f'anonym', inline=False)
    webhook.add_embed(embed)
    webhook.execute()

    time.sleep(3)
    clear_console()