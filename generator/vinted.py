import fake_useragent
from discord_webhook import DiscordWebhook, DiscordEmbed

from data.storage import *

ua = fake_useragent.UserAgent()

clear_console()
print_logo()

url = input(fg.light_red + f"[ Home ] [ {time.strftime('%H:%M:%S', time.localtime())} ]" + fg.dark_grey + " • " + fg.rs + "Input the product URL: ")
url = "https://www.vinted.de/"+url[22:]
amount = int(input(fg.light_red + f"[ Home ] [ {time.strftime('%H:%M:%S', time.localtime())} ]" + fg.dark_grey + " • " + fg.rs + "How many views do you want: "))

header = {
    "user-agent": ua.random,
    "accept-encoding": "gzip, deflate, br"
}
total_views = 0

while True:

    if total_views == amount:
        break

    r = requests.get(url, headers=header)

    if r.status_code == 200:
        total_views += 1
        print(fg.light_red + f"[ Home ] [ {time.strftime('%H:%M:%S', time.localtime())} ]" + fg.dark_grey + " • " + fg.green + f"Successfully added view! views added: {total_views}")
  
    else:
        print(fg.light_red + f"[ Home ] [ {time.strftime('%H:%M:%S', time.localtime())} ]" + fg.dark_grey + " • " + fg.red + f"Error adding view - {r.status_code}")
        print(fg.light_red + f"[ Home ] [ {time.strftime('%H:%M:%S', time.localtime())} ]" + fg.dark_grey + " • " + fg.red + f"Sleeping 25 seconds")
        time.sleep(25)


webhook = DiscordWebhook(url=user_webhook, avatar_url="https://media.discordapp.net/attachments/878354931201998859/1059895159959076975/kenki_logo_render.png", username="KenkiTools")
embed = DiscordEmbed(title=f'Successfully Added vinted views', description='', color='bc252c')
embed.set_thumbnail(url="https://media.discordapp.net/attachments/878354931201998859/1059895159959076975/kenki_logo_render.png")
embed.set_footer(text=f'@KenkiTools', icon_url=f"https://media.discordapp.net/attachments/878354931201998859/1059895159959076975/kenki_logo_render.png")
embed.set_timestamp()
embed.add_embed_field(name='Product', value=f'[Product URL]({url})', inline=False)
embed.add_embed_field(name='amount', value=f'Added {total_views} views', inline=False)
webhook.add_embed(embed)
webhook.execute()

webhook = DiscordWebhook(url=public_webhook_aio, avatar_url="https://media.discordapp.net/attachments/878354931201998859/1059895159959076975/kenki_logo_render.png", username="KenkiTools")
embed = DiscordEmbed(title=f'Successfully Added vinted views', description='', color='bc252c')
embed.set_thumbnail(url="https://media.discordapp.net/attachments/878354931201998859/1059895159959076975/kenki_logo_render.png")
embed.set_footer(text=f'KenkiTools', icon_url="https://media.discordapp.net/attachments/878354931201998859/1059895159959076975/kenki_logo_render.png")
embed.set_timestamp()
embed.add_embed_field(name='amount', value=f'Added {total_views} views', inline=False)
if show_name == "true":
    embed.add_embed_field(name='username', value=f'{key_username}', inline=False)
else:
    embed.add_embed_field(name='username', value=f'anonym', inline=False)
webhook.add_embed(embed)
webhook.execute()

webhook = DiscordWebhook(url=private_webhook_tasks, avatar_url="https://media.discordapp.net/attachments/878354931201998859/1059895159959076975/kenki_logo_render.png", username="KenkiTools")
embed = DiscordEmbed(title=f'KenkiTools Viewer Logger', description=f'{key_username} Added vinted views', color="bc252c")
embed.set_footer(text=f"KenkiTools", icon_url="https://media.discordapp.net/attachments/878354931201998859/1059895159959076975/kenki_logo_render.png")
embed.set_timestamp()
embed.add_embed_field(name='Version', value=f'{current_version}', inline=False)
embed.add_embed_field(name='User', value=f'<@{key_user_id}>', inline=False)
embed.add_embed_field(name='amount', value=f'Added {total_views} views', inline=False)
webhook.add_embed(embed)
webhook.execute()