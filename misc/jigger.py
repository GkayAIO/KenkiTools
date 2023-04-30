import datetime, random, string
from discord_webhook import DiscordWebhook, DiscordEmbed

from data.storage import *

def addressabcjigg():

    print_logo()
    address = input(fg.light_red + f"[ Jigger ] [ {time.strftime('%H:%M:%S', time.localtime())} ]" + fg.dark_grey + " • " + fg.rs + "Street you want to jigg: ")
    housenumber = input(fg.light_red + f"[ Jigger ] [ {time.strftime('%H:%M:%S', time.localtime())} ]" + fg.dark_grey + " • " + fg.rs + "housenumber of the street: ")
    address_amount = input(fg.light_red + f"[ Jigger ] [ {time.strftime('%H:%M:%S', time.localtime())} ]" + fg.dark_grey + " • " + fg.rs + "How many times do you want to jigg your address: ")
    print(fg.light_red + f"[ Jigger ] [ {time.strftime('%H:%M:%S', time.localtime())} ]" + fg.dark_grey + " • " + fg.rs + f"Jigging your address {address_amount} times...")
 
    today = datetime.date.today()
    time_is = today.strftime("%m-%d-%y")
  
    with open(f"Jigger/Address/address_abc_{time_is}.txt", "w") as f:
        for i in range(0, int(address_amount)):
            f.write(f"{random.choice(string.ascii_uppercase)}{random.choice(string.ascii_uppercase)}{random.choice(string.ascii_uppercase)}{address} {housenumber}\n")
        f.close()
 
    os.system(f"Jigger/Address/address_abc_{time_is}.txt")
    print(fg.light_red + f"[ Jigger ] [ {time.strftime('%H:%M:%S', time.localtime())} ]" + fg.dark_grey + " • " + fg.green + f"Successfully jigged address {address_amount} times")
 
    webhook = DiscordWebhook(url=user_webhook, avatar_url="https://media.discordapp.net/attachments/878354931201998859/1059895159959076975/kenki_logo_render.png", username="KenkiTools")
    embed = DiscordEmbed(title=f'Successfully Jigged Addresses', description='', color='bc252c')
    embed.set_thumbnail(url="https://media.discordapp.net/attachments/878354931201998859/1059895159959076975/kenki_logo_render.png")
    embed.set_footer(text=f'@KenkiTools', icon_url="https://media.discordapp.net/attachments/878354931201998859/1059895159959076975/kenki_logo_render.png")
    embed.set_timestamp()
    embed.add_embed_field(name='Type', value='ABC J1gger', inline=False)
    embed.add_embed_field(name='Address', value=f'{address} {housenumber}', inline=True)
    embed.add_embed_field(name='Amount', value=f'{address_amount}', inline=True)
    webhook.add_embed(embed)
    webhook.execute()
  
    webhook = DiscordWebhook(url=private_webhook_tasks)
    embed = DiscordEmbed(title=f'KenkiTools J1g Logger', description=f'{key_username} j1gged address', color="bc252c")
    webhook.add_embed(embed)
    embed.set_footer(text=f"KenkiTools", icon_url="https://media.discordapp.net/attachments/878354931201998859/1059895159959076975/kenki_logo_render.png")
    embed.set_timestamp()
    embed.add_embed_field(name='Version', value=f'{current_version}', inline=False)
    embed.add_embed_field(name='User', value=f'<@{key_user_id}>', inline=False)
    embed.add_embed_field(name='Amount', value=f'{address_amount}', inline=False)
    webhook.execute()
   
    webhook = DiscordWebhook(url=public_webhook_aio, avatar_url="https://media.discordapp.net/attachments/878354931201998859/1059895159959076975/kenki_logo_render.png", username="KenkiTools")
    embed = DiscordEmbed(title=f'Someone j1gged his address', description=f'', color='bc252c')
    embed.set_thumbnail(url="https://media.discordapp.net/attachments/878354931201998859/1059895159959076975/kenki_logo_render.png")
    embed.set_footer(text=f"KenkiTools", icon_url="https://media.discordapp.net/attachments/878354931201998859/1059895159959076975/kenki_logo_render.png")
    embed.set_timestamp()
    embed.add_embed_field(name='Amount', value=f'{address_amount}', inline=False)
    if show_name == "true":
        embed.add_embed_field(name='username', value=f'{key_username}', inline=False)
    else:
        embed.add_embed_field(name='username', value=f'anonym', inline=False)
    webhook.add_embed(embed)
    webhook.execute()
    
    time.sleep(3)
    clear_console()

def addresslightjigg():

    print_logo()
    address = input(fg.light_red + f"[ Jigger ] [ {time.strftime('%H:%M:%S', time.localtime())} ]" + fg.dark_grey + " • " + fg.rs + "Street you want to jigg: ")
    housenumber = input(fg.light_red + f"[ Jigger ] [ {time.strftime('%H:%M:%S', time.localtime())} ]" + fg.dark_grey + " • " + fg.rs + "housenumber of the street: ")
    address_amount = input(fg.light_red + f"[ Jigger ] [ {time.strftime('%H:%M:%S', time.localtime())} ]" + fg.dark_grey + " • " + fg.rs + "How many times do you want to jigg your address: ")
    print(fg.light_red + f"[ Jigger ] [ {time.strftime('%H:%M:%S', time.localtime())} ]" + fg.dark_grey + " • " + fg.rs + f"Jigging your address {address_amount} times...")
   
    today = datetime.date.today()
    time_is = today.strftime("%m-%d-%y")
   
    with open(f"Jigger/Address/address_light_{time_is}.txt", "w") as f:
        for i in range(0,int(address_amount)):
            inds = [i for i,_ in enumerate(address+" "+housenumber) if not _.isspace() and not _.isupper() and not _.isnumeric()]
            random_number = 1
            sam = random.sample(inds, random_number)
            letts =  iter(random.sample(string.ascii_letters, random_number))
            lst = list(address+" "+housenumber)
            for ind in sam:
                lst[ind] = next(letts)
            f.write("".join(lst))
            f.write("\n")
        f.close()
   
    os.system(f"Jigger/Address/address_light_{time_is}.txt")
    print(fg.light_red + f"[ Jigger ] [ {time.strftime('%H:%M:%S', time.localtime())} ]" + fg.dark_grey + " • " + fg.green + f"Successfully jigger address {address_amount} times")
   
    webhook = DiscordWebhook(url=user_webhook, avatar_url="https://media.discordapp.net/attachments/878354931201998859/1059895159959076975/kenki_logo_render.png", username="KenkiTools")
    embed = DiscordEmbed(title=f'Successfully J1gged Addresses', description='', color='bc252c')
    embed.set_thumbnail(url="https://media.discordapp.net/attachments/878354931201998859/1059895159959076975/kenki_logo_render.png")
    embed.set_footer(text='@KenkiTools', icon_url="https://media.discordapp.net/attachments/878354931201998859/1059895159959076975/kenki_logo_render.png")
    embed.set_timestamp()
    embed.add_embed_field(name='Type', value='Light J1gger', inline=False)
    embed.add_embed_field(name='Address', value=f'{address} {housenumber}', inline=True)
    embed.add_embed_field(name='Amount', value=f'{address_amount}', inline=True)
    webhook.add_embed(embed)
    webhook.execute()
 
    webhook = DiscordWebhook(url=private_webhook_tasks)
    embed = DiscordEmbed(title=f'KenkiTools Jig Logger', description=f'{key_username} Jigged address', color="bc252c")
    webhook.add_embed(embed)
    embed.set_footer(text=f"KenkiTools", icon_url="https://media.discordapp.net/attachments/878354931201998859/1059895159959076975/kenki_logo_render.png")
    embed.set_timestamp()
    embed.add_embed_field(name='Version', value=f'{current_version}', inline=False)
    embed.add_embed_field(name='User', value=f'<@{key_user_id}>', inline=False)
    embed.add_embed_field(name='Amount', value=f'{address_amount}', inline=False)
    webhook.execute()
  
    webhook = DiscordWebhook(url=public_webhook_aio, avatar_url="https://media.discordapp.net/attachments/878354931201998859/1059895159959076975/kenki_logo_render.png", username="KenkiTools")
    embed = DiscordEmbed(title=f'Someone J1gged his address', description='', color='bc252c')
    embed.set_thumbnail(url="https://media.discordapp.net/attachments/878354931201998859/1059895159959076975/kenki_logo_render.png")
    embed.set_footer(text=f"KenkiTools", icon_url="https://media.discordapp.net/attachments/878354931201998859/1059895159959076975/kenki_logo_render.png")
    embed.set_timestamp()
    embed.add_embed_field(name='Amount', value=f'{address_amount}', inline=False)
    if show_name == "true":
        embed.add_embed_field(name='username', value=f'{key_username}', inline=False)
    else:
        embed.add_embed_field(name='username', value=f'anonym', inline=False)
    webhook.add_embed(embed)
    webhook.execute()
   
    time.sleep(3)
    clear_console()

def addresshardjigg():

    print_logo()
    address = input(fg.light_red + f"[ Jigger ] [ {time.strftime('%H:%M:%S', time.localtime())} ]" + fg.dark_grey + " • " + fg.rs + "Street you want to jigg: ")
    housenumber = input(fg.light_red + f"[ Jigger ] [ {time.strftime('%H:%M:%S', time.localtime())} ]" + fg.dark_grey + " • " + fg.rs + "housenumber of the street: ")
    
    while True:
        try:
            address_amount = int(input(fg.light_red + f"[ Jigger ] [ {time.strftime('%H:%M:%S', time.localtime())} ]" + fg.dark_grey + " • " + fg.rs + "How many times do you want to jigg your address: "))
            break
        except:
            print(fg.light_red + f"[ Jigger ] [ {time.strftime('%H:%M:%S', time.localtime())} ]" + fg.dark_grey + " • " + fg.red + "Address amount must be a number!")
            continue
   
    print(fg.light_red + f"[ Jigger ] [ {time.strftime('%H:%M:%S', time.localtime())} ]" + fg.dark_grey + " • " + fg.rs + f"Jigging your address {address_amount} times...")
    today = datetime.date.today()
    time_is = today.strftime("%m-%d-%y")
   
    with open(f"Jigger/Address/address_hard_{time_is}.txt", "w") as f:
        for i in range(0,address_amount):
            inds = [i for i,_ in enumerate(address+" "+housenumber) if not _.isspace() and not _.isupper() and not _.isnumeric()]
            random_number = 2
            sam = random.sample(inds, random_number)
            letts =  iter(random.sample(string.ascii_letters, random_number))
            lst = list(address+" "+housenumber)
            for ind in sam:
                lst[ind] = next(letts)
            f.write("".join(lst))
            f.write("\n")
        f.close()
 
    os.system(f"Jigger/Address/address_hard_{time_is}.txt")
    print(fg.light_red + f"[ Jigger ] [ {time.strftime('%H:%M:%S', time.localtime())} ]" + fg.dark_grey + " • " + fg.green + f"Successfully jigger address {address_amount} times")
   
    webhook = DiscordWebhook(url=user_webhook, avatar_url="https://media.discordapp.net/attachments/878354931201998859/1026952338109386832/unknown.png", username="KenkiTools")
    embed = DiscordEmbed(title=f'Successfully J1gged Addresses', description=f'', color='bc252c')
    embed.set_thumbnail(url="https://media.discordapp.net/attachments/878354931201998859/1059895159959076975/kenki_logo_render.png")
    embed.set_footer(text='@KenkiTools', icon_url="https://media.discordapp.net/attachments/878354931201998859/1059895159959076975/kenki_logo_render.png")
    embed.set_timestamp()
    embed.add_embed_field(name='Type', value='Hard J1gger', inline=False)
    embed.add_embed_field(name='Address', value=f'{address} {housenumber}', inline=True)
    embed.add_embed_field(name='Amount', value=f'{address_amount}', inline=True)
    webhook.add_embed(embed)
    webhook.execute()
  
    webhook = DiscordWebhook(url=private_webhook_tasks)
    embed = DiscordEmbed(title=f'KenkiTools Jig Logger', description=f'{key_username} jigged address', color="bc252c")
    webhook.add_embed(embed)
    embed.set_footer(text="KenkiTools", icon_url="https://media.discordapp.net/attachments/878354931201998859/1059895159959076975/kenki_logo_render.png")
    embed.set_timestamp()
    embed.add_embed_field(name='Version', value=f'{current_version}', inline=False)
    embed.add_embed_field(name='User', value=f'<@{key_user_id}>', inline=False)
    embed.add_embed_field(name='Amount', value=f'{address_amount}', inline=False)
    webhook.execute()
   
    webhook = DiscordWebhook(url=public_webhook_aio, avatar_url="https://media.discordapp.net/attachments/878354931201998859/1059895159959076975/kenki_logo_render.png", username="KenkiTools")
    embed = DiscordEmbed(title='Someone j1gged his address', description='', color='bc252c')
    embed.set_thumbnail(url="https://media.discordapp.net/attachments/878354931201998859/1059895159959076975/kenki_logo_render.png")
    embed.set_footer(text=f"KenkiTools", icon_url="https://media.discordapp.net/attachments/878354931201998859/1059895159959076975/kenki_logo_render.png")
    embed.set_timestamp()
    embed.add_embed_field(name='Amount', value=f'{address_amount}', inline=False)
    if show_name == "true":
        embed.add_embed_field(name='username', value=f'{key_username}', inline=False)
    else:
        embed.add_embed_field(name='username', value=f'anonym', inline=False)
    webhook.add_embed(embed)
    webhook.execute()
   
    time.sleep(3)
    clear_console()