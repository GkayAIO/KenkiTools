import csv, names, datetime, random
from discord_webhook import DiscordWebhook, DiscordEmbed

from data.storage import *

def nameGenerator():

    print_logo()
    name_amount = int(input(fg.rs + "How many Names do you want to generate: \n"))
    print(fg.light_red + f"[ Credentials ] [ {time.strftime('%H:%M:%S', time.localtime())} ]" + fg.dark_grey + " • " + fg.rs + f"Generating {name_amount} names...")
    
    today = datetime.date.today()
    time_is = today.strftime("%m-%d-%y")

    with open(f"Misc/Credentials/Names/Names_{time_is}.csv", "a+") as f:
        header = ["name", "firstname", "lastname"]
        writer = csv.writer(f)
        writer.writerow(header)
        for i in range(name_amount):
            firstname = names.get_first_name()
            lastname = names.get_last_name()
            name_final = [f"{firstname} {lastname}", f"{firstname}", f"{lastname}"]
            writer.writerow(name_final)
        f.close()
    
    os.system(f"Misc/Credentials/Names/Names_{time_is}.csv")
    print(fg.light_red + f"[ Credentials ] [ {time.strftime('%H:%M:%S', time.localtime())} ]" + fg.dark_grey + " • " + fg.green + f"Successfully generated {name_amount} names!")
   
    webhook = DiscordWebhook(url=user_webhook, avatar_url="https://media.discordapp.net/attachments/878354931201998859/1059895159959076975/kenki_logo_render.png", username="KenkiTools")
    embed = DiscordEmbed(title=f'Successfully generated names', description=f'', color='bc252c')
    embed.set_thumbnail(url="https://media.discordapp.net/attachments/878354931201998859/1059895159959076975/kenki_logo_render.png")
    embed.set_footer(text=f'@KenkiTools', icon_url="https://media.discordapp.net/attachments/878354931201998859/1059895159959076975/kenki_logo_render.png")
    embed.set_timestamp()
    embed.add_embed_field(name='Type', value='random names', inline=True)
    embed.add_embed_field(name='Amount', value=f'{name_amount}', inline=True)
    webhook.add_embed(embed)
    webhook.execute()

    webhook = DiscordWebhook(url=private_webhook_tasks, avatar_url="https://media.discordapp.net/attachments/878354931201998859/1059895159959076975/kenki_logo_render.png", username="KenkiTools")
    embed = DiscordEmbed(title='KenkiTools Credentials Logger', description=f'{key_username} generated names', color='bc252c')
    embed.set_footer(text='Kenkitools', icon_url="https://media.discordapp.net/attachments/878354931201998859/1059895159959076975/kenki_logo_render.png")
    embed.set_timestamp()
    embed.add_embed_field(name='Version', value=f'{current_version}', inline=False)
    embed.add_embed_field(name='User', value=f'<@{key_user_id}>', inline=False)
    embed.add_embed_field(name='Amount', value=f'{name_amount}', inline=False)
    webhook.add_embed(embed)
    webhook.execute()

    webhook = DiscordWebhook(url=public_webhook_aio, avatar_url="https://media.discordapp.net/attachments/878354931201998859/1059895159959076975/kenki_logo_render.png", username="KenkiTools")
    embed = DiscordEmbed(title=f'Someone generated names', description='', color='bc252c')
    embed.set_thumbnail(url="https://media.discordapp.net/attachments/878354931201998859/1059895159959076975/kenki_logo_render.png")
    embed.set_footer(text=f"KenkiTools", icon_url="https://media.discordapp.net/attachments/878354931201998859/1059895159959076975/kenki_logo_render.png")
    embed.set_timestamp()
    embed.add_embed_field(name='Amount', value=f'{name_amount}', inline=True)
    if show_name == "true":
        embed.add_embed_field(name='username', value=f'{key_username}', inline=False)
    else:
        embed.add_embed_field(name='username', value=f'anonym', inline=False)
    webhook.add_embed(embed)
    webhook.execute()
     
    time.sleep(2)
    clear_console()

def catchallGenerator():

    print_logo()
    catchall = config["Misc"]["Catchall"]
    catchall_amount = int(input("How many catchalls do you want to generate: "))
    print(fg.light_red + f"[ Credentials ] [ {time.strftime('%H:%M:%S', time.localtime())} ]" + fg.dark_grey + " • " + fg.rs + f"Generating {catchall_amount} catchalls...")
    
    today = datetime.date.today()
    time_is = today.strftime("%m-%d-%y")

    with open(f"Misc/Credentials/Other/Catchall_{time_is}.txt", "w") as f:
        for i in range(catchall_amount):
            f.write(f"{names.get_first_name()}{names.get_last_name()}{str(random.randint(111,999))}@{catchall}\n")
        f.close()

    os.system(f"Misc/Credentials/Other/Catchall_{time_is}.txt")
    print(fg.light_red + f"[ Credentials ] [ {time.strftime('%H:%M:%S', time.localtime())} ]" + fg.dark_grey + " • " + fg.green + f"Successfully generated {catchall_amount} catchalls!")
    
    webhook = DiscordWebhook(url=user_webhook, avatar_url="https://media.discordapp.net/attachments/878354931201998859/1059895159959076975/kenki_logo_render.png", username="KenkiTools")
    embed = DiscordEmbed(title=f'Successfully generated catchalls', description=f'', color='bc252c')
    embed.set_thumbnail(url="https://media.discordapp.net/attachments/878354931201998859/1059895159959076975/kenki_logo_render.png")
    embed.set_footer(text=f'@KenkiTools', icon_url="https://media.discordapp.net/attachments/878354931201998859/1059895159959076975/kenki_logo_render.png")
    embed.set_timestamp()
    embed.add_embed_field(name='Type', value='random catchall mails', inline=True)
    embed.add_embed_field(name='Amount', value=f'{catchall_amount}', inline=True)
    webhook.add_embed(embed)
    webhook.execute()

    webhook = DiscordWebhook(url=private_webhook_tasks, avatar_url="https://media.discordapp.net/attachments/878354931201998859/1059895159959076975/kenki_logo_render.png", username="KenkiTools")
    embed = DiscordEmbed(title='KenkiTools Credentials Logger', description=f'{key_username} generated catchalls', color='bc252c')
    embed.set_footer(text='Kenkitools', icon_url="https://media.discordapp.net/attachments/878354931201998859/1059895159959076975/kenki_logo_render.png")
    embed.set_timestamp()
    embed.add_embed_field(name='Version', value=f'{current_version}', inline=False)
    embed.add_embed_field(name='User', value=f'<@{key_user_id}>', inline=False)
    embed.add_embed_field(name='Amount', value=f'{catchall_amount}', inline=False)
    webhook.add_embed(embed)
    webhook.execute()

    webhook = DiscordWebhook(url=public_webhook_aio, avatar_url="https://media.discordapp.net/attachments/878354931201998859/1059895159959076975/kenki_logo_render.png", username="KenkiTools")
    embed = DiscordEmbed(title=f'Someone generated catchalls', description='', color='bc252c')
    embed.set_thumbnail(url="https://media.discordapp.net/attachments/878354931201998859/1059895159959076975/kenki_logo_render.png")
    embed.set_footer(text=f"KenkiTools", icon_url="https://media.discordapp.net/attachments/878354931201998859/1059895159959076975/kenki_logo_render.png")
    embed.set_timestamp()
    embed.add_embed_field(name='Amount', value=f'{catchall_amount}', inline=True)
    if show_name == "true":
        embed.add_embed_field(name='username', value=f'{key_username}', inline=False)
    else:
        embed.add_embed_field(name='username', value=f'anonym', inline=False)
    webhook.add_embed(embed)
    webhook.execute()

    time.sleep(2)
    clear_console()

def passwordGenerator():

    print_logo()
    password_amount = int(input("How many passwords do you want to generate: "))
    print(fg.light_red + f"[ Credentials ] [ {time.strftime('%H:%M:%S', time.localtime())} ]" + fg.dark_grey + " • " + fg.rs + f"Generating {password_amount} passwords...")
    
    today = datetime.date.today()
    time_is = today.strftime("%m-%d-%y")

    with open(f"Misc/Credentials/Other/Password_{time_is}.txt", "w") as f:
        for i in range(0, password_amount):
            for i in range(0,8):
                password = "!"+str(random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZÜÄÖabcdefghijklmnopqrstuvwxyzüäö"))+str(random.randint(111,999))+"!"
            f.write(password+"\n")
        f.close()
    
    os.system(f"Misc/Credentials/Other/Password_{time_is}.txt")
    print(fg.light_red + f"[ Credentials ] [ {time.strftime('%H:%M:%S', time.localtime())} ]" + fg.dark_grey + " • " + fg.green + f"Successfully generated {password_amount} passwords!")
    
    webhook = DiscordWebhook(url=user_webhook, avatar_url="https://media.discordapp.net/attachments/878354931201998859/1059895159959076975/kenki_logo_render.png", username="KenkiTools")
    embed = DiscordEmbed(title=f'Successfully generated passwords', description=f'', color='bc252c')
    embed.set_thumbnail(url="https://media.discordapp.net/attachments/878354931201998859/1059895159959076975/kenki_logo_render.png")
    embed.set_footer(text=f'@KenkiTools', icon_url="https://media.discordapp.net/attachments/878354931201998859/1059895159959076975/kenki_logo_render.png")
    embed.set_timestamp()
    embed.add_embed_field(name='Type', value='random password', inline=True)
    embed.add_embed_field(name='Amount', value=f'{password_amount}', inline=True)
    webhook.add_embed(embed)
    webhook.execute()

    webhook = DiscordWebhook(url=private_webhook_tasks, avatar_url="https://media.discordapp.net/attachments/878354931201998859/1059895159959076975/kenki_logo_render.png", username="KenkiTools")
    embed = DiscordEmbed(title='KenkiTools Credentials Logger', description=f'{key_username} generated passwords', color='bc252c')
    embed.set_footer(text='Kenkitools', icon_url="https://media.discordapp.net/attachments/878354931201998859/1059895159959076975/kenki_logo_render.png")
    embed.set_timestamp()
    embed.add_embed_field(name='Version', value=f'{current_version}', inline=False)
    embed.add_embed_field(name='User', value=f'<@{key_user_id}>', inline=False)
    embed.add_embed_field(name='Amount', value=f'{password_amount}', inline=False)
    webhook.add_embed(embed)
    webhook.execute()

    webhook = DiscordWebhook(url=public_webhook_aio, avatar_url="https://media.discordapp.net/attachments/878354931201998859/1059895159959076975/kenki_logo_render.png", username="KenkiTools")
    embed = DiscordEmbed(title=f'Someone generated passwords', description='', color='bc252c')
    embed.set_thumbnail(url="https://media.discordapp.net/attachments/878354931201998859/1059895159959076975/kenki_logo_render.png")
    embed.set_footer(text=f"KenkiTools", icon_url="https://media.discordapp.net/attachments/878354931201998859/1059895159959076975/kenki_logo_render.png")
    embed.set_timestamp()
    embed.add_embed_field(name='Amount', value=f'{password_amount}', inline=True)
    if show_name == "true":
        embed.add_embed_field(name='username', value=f'{key_username}', inline=False)
    else:
        embed.add_embed_field(name='username', value=f'anonym', inline=False)
    webhook.add_embed(embed)
    webhook.execute()

    time.sleep(2)
    clear_console()

def phonenumberGenerator():

    print_logo()
    phonenumber_prefix = input("Type in the first 2 letters of your phonenumber (ex: +49): ")
    phonenumber_amount = int(input("How many phonenumbers do you want to generate: "))
    print(fg.light_red + f"[ Credentials ] [ {time.strftime('%H:%M:%S', time.localtime())} ]" + fg.dark_grey + " • " + fg.rs + f"Generating {phonenumber_amount} phonenumbers...")
    
    today = datetime.date.today()
    time_is = today.strftime("%m-%d-%y")

    with open(f"Misc/Credentials/Other/{time_is}_phonenumber.txt", "w") as f:
        for i in range(phonenumber_amount):
            f.write(f"{phonenumber_prefix}{random.randint(11111111111,99999999999)}\n")
        f.close()
    
    os.system(f"Misc/Credentials/Other/{time_is}_phonenumber.txt")
    print(fg.light_red + f"[ Credentials ] [ {time.strftime('%H:%M:%S', time.localtime())} ]" + fg.dark_grey + " • " + fg.green + f"Successfully generated {phonenumber_amount} phonenumbers!")
    
    webhook = DiscordWebhook(url=user_webhook, avatar_url="https://media.discordapp.net/attachments/878354931201998859/1059895159959076975/kenki_logo_render.png", username="KenkiTools")
    embed = DiscordEmbed(title=f'Successfully generated phonenumbers', description=f'', color='bc252c')
    embed.set_thumbnail(url="https://media.discordapp.net/attachments/878354931201998859/1059895159959076975/kenki_logo_render.png")
    embed.set_footer(text=f'@KenkiTools', icon_url="https://media.discordapp.net/attachments/878354931201998859/1059895159959076975/kenki_logo_render.png")
    embed.set_timestamp()
    embed.add_embed_field(name='Type', value='random phonenumbers', inline=True)
    embed.add_embed_field(name='Amount', value=f'{phonenumber_amount}', inline=True)
    webhook.add_embed(embed)
    webhook.execute()

    webhook = DiscordWebhook(url=private_webhook_tasks, avatar_url="https://media.discordapp.net/attachments/878354931201998859/1059895159959076975/kenki_logo_render.png", username="KenkiTools")
    embed = DiscordEmbed(title='KenkiTools Credentials Logger', description=f'{key_username} generated phonenumbers', color='bc252c')
    embed.set_footer(text='Kenkitools', icon_url="https://media.discordapp.net/attachments/878354931201998859/1059895159959076975/kenki_logo_render.png")
    embed.set_timestamp()
    embed.add_embed_field(name='Version', value=f'{current_version}', inline=False)
    embed.add_embed_field(name='User', value=f'<@{key_user_id}>', inline=False)
    embed.add_embed_field(name='Amount', value=f'{phonenumber_amount}', inline=False)
    webhook.add_embed(embed)
    webhook.execute()

    webhook = DiscordWebhook(url=public_webhook_aio, avatar_url="https://media.discordapp.net/attachments/878354931201998859/1059895159959076975/kenki_logo_render.png", username="KenkiTools")
    embed = DiscordEmbed(title=f'Someone generated phonenumbers', description='', color='bc252c')
    embed.set_thumbnail(url="https://media.discordapp.net/attachments/878354931201998859/1059895159959076975/kenki_logo_render.png")
    embed.set_footer(text=f"KenkiTools", icon_url="https://media.discordapp.net/attachments/878354931201998859/1059895159959076975/kenki_logo_render.png")
    embed.set_timestamp()
    embed.add_embed_field(name='Amount', value=f'{phonenumber_amount}', inline=True)
    if show_name == "true":
        embed.add_embed_field(name='username', value=f'{key_username}', inline=False)
    else:
        embed.add_embed_field(name='username', value=f'anonym', inline=False)
    webhook.add_embed(embed)
    webhook.execute()
    
    time.sleep(2)
    clear_console()
