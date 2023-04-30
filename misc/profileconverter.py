import datetime, csv
from discord_webhook import DiscordWebhook, DiscordEmbed

from data.storage import *

def profileconverter(bot, rows, header):

    print(fg.light_red + f"[ Profile ] [ {time.strftime('%H:%M:%S', time.localtime())} ]" + fg.dark_grey + " • " + fg.light_yellow + "Converting profiles...")
    today = datetime.date.today()
    time_is = today.strftime("%m-%d-%y")
   
    with open(f'Profile/output/{bot}_{time_is}.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(header)
        writer.writerow(rows)
 
    print(fg.light_red + f"[ Profile ] [ {time.strftime('%H:%M:%S', time.localtime())} ]" + fg.dark_grey + " • " + fg.green + f"Successfully converter {bot} profiles!")
   
    webhook = DiscordWebhook(url=user_webhook, avatar_url="https://media.discordapp.net/attachments/878354931201998859/1059895159959076975/kenki_logo_render.png", username="KenkiTools")
    embed = DiscordEmbed(title=f'Successfully Converted profile', description=f'', color=0xbc252c)
    embed.set_thumbnail(url="https://media.discordapp.net/attachments/878354931201998859/1059895159959076975/kenki_logo_render.png")
    embed.set_footer(text='@KenkiTools', icon_url="https://media.discordapp.net/attachments/878354931201998859/1059895159959076975/kenki_logo_render.png")
    embed.set_timestamp()
    embed.add_embed_field(name='Bot', value=f"`{bot}`", inline=False)
    webhook.add_embed(embed)
    webhook.execute()
   
    webhook = DiscordWebhook(url=private_webhook_tasks)
    embed = DiscordEmbed(title=f'{key_username} Converted Profile!', description=f'**Bot:** {bot}', color=0xbc252c)
    embed.set_thumbnail(url=f'https://media.discordapp.net/attachments/878354931201998859/1059895159959076975/kenki_logo_render.png')
    embed.set_footer(text='@KenkiTools', icon_url="https://media.discordapp.net/attachments/878354931201998859/1059895159959076975/kenki_logo_render.png")
    embed.set_timestamp()
    webhook.add_embed(embed)
    webhook.execute()
    
    webhook = DiscordWebhook(url=public_webhook_aio, avatar_url="https://media.discordapp.net/attachments/878354931201998859/1059895159959076975/kenki_logo_render.png", username="KenkiTools")
    embed = DiscordEmbed(title=f'Successfully Converted Profiles', description=f'', color=0xbc252c)
    embed.set_thumbnail(url="https://media.discordapp.net/attachments/878354931201998859/1059895159959076975/kenki_logo_render.png")
    embed.set_footer(text='@KenkiTools', icon_url="https://media.discordapp.net/attachments/878354931201998859/1059895159959076975/kenki_logo_render.png")
    embed.set_timestamp()
    embed.add_embed_field(name='Bot', value=f"`{bot}`", inline=False)
    webhook.add_embed(embed)
    webhook.execute()
   
    time.sleep(3)
    clear_console()