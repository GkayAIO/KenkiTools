from discord_webhook import DiscordWebhook, DiscordEmbed

from data.storage import *

delay = 0
discord_token = ""
channel_id = ""

def retrieve_messages():
    print_logo()
    print(fg.light_red + f"[ Discord ] [ {time.strftime('%H:%M:%S', time.localtime())} ]" + fg.dark_grey + " • " + fg.rs + "Searching for invites...")
    
    while True:
        time.sleep(delay)
        num = 0
        limit = 1
        headers = {
            'authorization': discord_token
        }
        last_message_id = None
        query_parameters = f'limit={limit}'
     
        if last_message_id is not None:
            query_parameters += f'&before={last_message_id}'
     
        r = requests.get(f'https://discord.com/api/v9/channels/{channel_id}/messages?{query_parameters}', headers=headers)
        jsonn = json.loads(r.text)
      
        for value in jsonn:
            content = value['content']
            last_message_id = value['id']
            num=num+1
            final_content = content.split(" ")
        
            if "https://discord.gg/" in content:
                final_content = content[19:]
                print(fg.light_red + f"[ Discord ] [ {time.strftime('%H:%M:%S', time.localtime())} ]" + fg.dark_grey + " • " + fg.light_yellow + f'Found possible invite code: "{final_content}')
                print(fg.light_red + f"[ Discord ] [ {time.strftime('%H:%M:%S', time.localtime())} ]" + fg.dark_grey + " • " + fg.light_yellow + "Joining server...")
                start_time = time.time()
                headers = {"authorization": discord_token}
                inv_r = requests.post("https://discord.com/api/v9/invites/{}".format(final_content), headers=headers, json={})
                end_time = time.time()
            
                if inv_r.status_code == 200:
                    server_invite_code = response_text2["code"]
                    guild_id = response_text2["guild"]["id"]
                    guild_name = response_text2["guild"]["name"]
                    guild_icon = response_text2["guild"]["icon"]
                    print(fg.light_red + f"[ Discord ] [ {time.strftime('%H:%M:%S', time.localtime())} ]" + fg.dark_grey + " • " + fg.green + f'Successfully joined server "{guild_name}"')
                    webhook = DiscordWebhook(url=user_webhook, avatar_url="https://media.discordapp.net/attachments/878354931201998859/1059895159959076975/kenki_logo_render.png", username="KenkiTools")
                    embed = DiscordEmbed(title=f'Successfully joined discord server!', description=f'', color="bc252c")
                    embed.set_thumbnail(url=f'https://cdn.discordapp.com/icons/{guild_id}/{guild_icon}.png')
                    embed.add_embed_field(name='Checkout speed', value=f'{end_time-start_time}s', inline=False)
                    embed.add_embed_field(name='Server name', value=f'{guild_name}', inline=True)
                    embed.add_embed_field(name='Server invite', value=f'||{server_invite_code}||', inline=True)
                    embed.set_footer(text="@KenkiTools", icon_url="https://media.discordapp.net/attachments/878354931201998859/1059895159959076975/kenki_logo_render.png")
                    embed.set_timestamp()
                    webhook.add_embed(embed)
                    webhook.execute()
                  
                    webhook = DiscordWebhook(url=private_webhook_tasks)
                    embed = DiscordEmbed(title=f'KenkiTools Discord Logger', description=f'{key_username} j1gged address', color="bc252c")
                    webhook.add_embed(embed)
                    embed.set_footer(text=f"KenkiTools", icon_url="https://media.discordapp.net/attachments/878354931201998859/1059895159959076975/kenki_logo_render.png")
                    embed.set_timestamp()
                    embed.add_embed_field(name='Version', value=f'{current_version}', inline=False)
                    embed.add_embed_field(name='User', value=f'<@{key_user_id}>', inline=False)
                    embed.add_embed_field(name='Server invite', value=f'{final_content}', inline=False)
                    embed.add_embed_field(name='Guild name', value=f'{guild_name}', inline=False)
                    webhook.execute()
                  
                    webhook = DiscordWebhook(url=public_webhook_aio, avatar_url="https://media.discordapp.net/attachments/878354931201998859/1059895159959076975/kenki_logo_render.png", username="KenkiTools")
                    embed = DiscordEmbed(title=f'Successfully joined discord server!', description=f'', color='bc252c')
                    embed.set_thumbnail(url="https://media.discordapp.net/attachments/878354931201998859/1059895159959076975/kenki_logo_render.png")
                    embed.set_footer(text=f"KenkiTools", icon_url="https://media.discordapp.net/attachments/878354931201998859/1059895159959076975/kenki_logo_render.png")
                    embed.set_timestamp()
                    embed.add_embed_field(name='Server name', value=f'{guild_name}', inline=True)
                    if show_name == "true":
                        embed.add_embed_field(name='username', value=f'{key_username}', inline=False)
                    else:
                        embed.add_embed_field(name='username', value=f'anonym', inline=False)
                    webhook.add_embed(embed)
                    webhook.execute()
                    input("")
              
                else:
                    print("error")
          
            elif "discord.gg/" in content:
                final_content = content[11:]
                print(fg.light_red + f"[ Discord ] [ {time.strftime('%H:%M:%S', time.localtime())} ]" + fg.dark_grey + " • " + fg.light_yellow + f'Found possible invite code: "{final_content}')
                print(fg.light_red + f"[ Discord ] [ {time.strftime('%H:%M:%S', time.localtime())} ]" + fg.dark_grey + " • " + fg.light_yellow + "Joining server...")
                start_time = time.time()
                headers = {"authorization": discord_token}
                inv_r = requests.post("https://discord.com/api/v9/invites/{}".format(final_content), headers=headers, json={})
                end_time = time.time()
               
                if inv_r.status_code == 200:
                    server_invite_code = response_text2["code"]
                    guild_id = response_text2["guild"]["id"]
                    guild_name = response_text2["guild"]["name"]
                    guild_icon = response_text2["guild"]["icon"]
                    print(fg.light_red + f"[ Discord ] [ {time.strftime('%H:%M:%S', time.localtime())} ]" + fg.dark_grey + " • " + fg.green + f'Successfully joined server "{guild_name}"')
                    webhook = DiscordWebhook(url=user_webhook, avatar_url="https://media.discordapp.net/attachments/878354931201998859/1059895159959076975/kenki_logo_render.png", username="KenkiTools")
                    embed = DiscordEmbed(title=f'Successfully joined discord server!', description=f'', color="bc252c")
                    embed.set_thumbnail(url=f'https://cdn.discordapp.com/icons/{guild_id}/{guild_icon}.png')
                    embed.add_embed_field(name='Checkout speed', value=f'{end_time-start_time}s', inline=False)
                    embed.add_embed_field(name='Server name', value=f'{guild_name}', inline=True)
                    embed.add_embed_field(name='Server invite', value=f'||{server_invite_code}||', inline=True)
                    embed.set_footer(text="@KenkiTools", icon_url="https://media.discordapp.net/attachments/878354931201998859/1059895159959076975/kenki_logo_render.png")
                    embed.set_timestamp()
                    webhook.add_embed(embed)
                    webhook.execute()
                 
                    webhook = DiscordWebhook(url=private_webhook_tasks)
                    embed = DiscordEmbed(title=f'KenkiTools Discord Logger', description=f'{key_username} j1gged address', color="bc252c")
                    webhook.add_embed(embed)
                    embed.set_footer(text=f"KenkiTools", icon_url="https://media.discordapp.net/attachments/878354931201998859/1059895159959076975/kenki_logo_render.png")
                    embed.set_timestamp()
                    embed.add_embed_field(name='Version', value=f'{current_version}', inline=False)
                    embed.add_embed_field(name='User', value=f'<@{key_user_id}>', inline=False)
                    embed.add_embed_field(name='Server invite', value=f'{final_content}', inline=False)
                    embed.add_embed_field(name='Guild name', value=f'{guild_name}', inline=False)
                    webhook.execute()
                   
                    webhook = DiscordWebhook(url=public_webhook_aio, avatar_url="https://media.discordapp.net/attachments/878354931201998859/1059895159959076975/kenki_logo_render.png", username="KenkiTools")
                    embed = DiscordEmbed(title=f'Successfully joined discord server!', description=f'', color='bc252c')
                    embed.set_thumbnail(url="https://media.discordapp.net/attachments/878354931201998859/1059895159959076975/kenki_logo_render.png")
                    embed.set_footer(text=f"KenkiTools", icon_url="https://media.discordapp.net/attachments/878354931201998859/1059895159959076975/kenki_logo_render.png")
                    embed.set_timestamp()
                    embed.add_embed_field(name='Server name', value=f'{guild_name}', inline=True)
                    if show_name == "true":
                        embed.add_embed_field(name='username', value=f'{key_username}', inline=False)
                    else:
                        embed.add_embed_field(name='username', value=f'anonym', inline=False)
                    webhook.add_embed(embed)
                    webhook.execute()
                    input("")
              
                else:
                    print("error")

def manual_input():
    final_content = input("Input the code: ")
    start_time = time.time()
    headers = {
        'authorization': discord_token
    }
    inv_r = requests.post(f"https://discord.com/api/v9/invites/{final_content}", headers=headers, json={""})
    end_time = time.time()
    print(inv_r.text)
   
    if inv_r.status_code == 200:
        server_invite_code = response_text2["code"]
        guild_id = response_text2["guild"]["id"]
        guild_name = response_text2["guild"]["name"]
        guild_icon = response_text2["guild"]["icon"]
        print(fg.light_red + f"[ Discord ] [ {time.strftime('%H:%M:%S', time.localtime())} ]" + fg.dark_grey + " • " + fg.green + f'Successfully joined server "{guild_name}"')
     
        webhook = DiscordWebhook(url=user_webhook, avatar_url="https://media.discordapp.net/attachments/878354931201998859/1059895159959076975/kenki_logo_render.png", username="KenkiTools")
        embed = DiscordEmbed(title=f'Successfully joined discord server!', description=f'', color="bc252c")
        embed.set_thumbnail(url=f'https://cdn.discordapp.com/icons/{guild_id}/{guild_icon}.png')
        embed.add_embed_field(name='Checkout speed', value=f'{end_time-start_time}s', inline=False)
        embed.add_embed_field(name='Server name', value=f'{guild_name}', inline=True)
        embed.add_embed_field(name='Server invite', value=f'||{server_invite_code}||', inline=True)
        embed.set_footer(text="@KenkiTools", icon_url="https://media.discordapp.net/attachments/878354931201998859/1059895159959076975/kenki_logo_render.png")
        embed.set_timestamp()
        webhook.add_embed(embed)
        webhook.execute()
      
        webhook = DiscordWebhook(url=private_webhook_tasks)
        embed = DiscordEmbed(title=f'KenkiTools Discord Logger', description=f'{key_username} j1gged address', color="bc252c")
        webhook.add_embed(embed)
        embed.set_footer(text=f"KenkiTools", icon_url="https://media.discordapp.net/attachments/878354931201998859/1059895159959076975/kenki_logo_render.png")
        embed.set_timestamp()
        embed.add_embed_field(name='Version', value=f'{current_version}', inline=False)
        embed.add_embed_field(name='User', value=f'<@{key_user_id}>', inline=False)
        embed.add_embed_field(name='Server invite', value=f'{final_content}', inline=False)
        embed.add_embed_field(name='Guild name', value=f'{guild_name}', inline=False)
        webhook.execute()
       
        webhook = DiscordWebhook(url=public_webhook_aio, avatar_url="https://media.discordapp.net/attachments/878354931201998859/1059895159959076975/kenki_logo_render.png", username="KenkiTools")
        embed = DiscordEmbed(title=f'Successfully joined discord server!', description=f'', color='bc252c')
        embed.set_thumbnail(url="https://media.discordapp.net/attachments/878354931201998859/1059895159959076975/kenki_logo_render.png")
        embed.set_footer(text=f"KenkiTools", icon_url="https://media.discordapp.net/attachments/878354931201998859/1059895159959076975/kenki_logo_render.png")
        embed.set_timestamp()
        embed.add_embed_field(name='Server name', value=f'{guild_name}', inline=True)
        if show_name == "true":
            embed.add_embed_field(name='username', value=f'{key_username}', inline=False)
        else:
            embed.add_embed_field(name='username', value=f'anonym', inline=False)
        webhook.add_embed(embed)
        webhook.execute()
        input("")
  
    else:
        print("error")
