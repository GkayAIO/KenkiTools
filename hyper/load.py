import csv, threading
from discord_webhook import DiscordWebhook, DiscordEmbed

from data.storage import *

s = requests.Session()

from hyper.task import hyper
from hyper.manual import hyper_manual

print_logo()
print(fg.light_red + "   [1] Monitor Discord    [2] Manual input\n")

while True:
    try:
        mode = int(input(fg.light_red + "\n   Select a Module: "+fg.rs))
    
        if mode == 1 or mode == 2:
            break
   
        else:
            pass
  
    except:
        pass

print("")

if mode == 1:
    dashboard = input(fg.light_red + f"[ Hyper ] [ {time.strftime('%H:%M:%S', time.localtime())} ]" + fg.dark_grey + " • " + fg.rs + "Dashboard(ex. https://kenki-tools.hyper.co/): ")
    monitor_channel = input(fg.light_red + f"[ Hyper ] [ {time.strftime('%H:%M:%S', time.localtime())} ]" + fg.dark_grey + " • " + fg.rs + "Channel id: ")
 
    while True:
        paid = input(fg.light_red + f"[ Hyper ] [ {time.strftime('%H:%M:%S', time.localtime())} ]" + fg.dark_grey + " • " + fg.rs + "Is the release paid?(y/n): ")
   
        if paid == "y" or paid == "Y":
            paid = True
            break
      
        if paid == "n" or paid == "N":
            paid = False
            break
     
        else:
            print(fg.light_red + f"[ Hyper ] [ {time.strftime('%H:%M:%S', time.localtime())} ]" + fg.dark_grey + " • " + fg.red + 'Error - please only use y/n')
  
    webhook = DiscordWebhook(url=private_webhook_hyper, avatar_url="https://media.discordapp.net/attachments/878354931201998859/1059895159959076975/kenki_logo_render.png", username="KenkiTools")
    embed = DiscordEmbed(title=f'KenkiTools Hyper Logger', description=f'{key_username} Started tasks', color='bc252c')
    embed.set_footer(text=f'Kenkitools', icon_url="https://media.discordapp.net/attachments/878354931201998859/1059895159959076975/kenki_logo_render.png")
    embed.set_timestamp()
    embed.add_embed_field(name='Version', value=f'{current_version}', inline=False)
    embed.add_embed_field(name='User', value=f'<@{key_user_id}>', inline=False)
    embed.add_embed_field(name='Dashboard', value=f'{dashboard}', inline=False)
    embed.add_embed_field(name='Channel id', value=f'{monitor_channel}', inline=False)
    webhook.add_embed(embed)
    webhook.execute()
   
    print("")
    global task
    global processlist
    task = 0
    processlist = []
   
    with open('hyper/profiles/profile.csv', newline='') as input_file:
        csv_file = csv.reader(input_file)
        for row in csv_file:
        
            if row != ["discord token","email","firstname","lastname","address","address2","zip code","city","state","countrycode","cc","cvc","exp"]:
                if "@" in row[1]:
                    task += 1
                    processlist.append(threading.Thread(target=hyper, args=(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11], row[12], monitor_channel, dashboard, paid, task, )))
     
                else:
                    print(fg.light_red + f"[ Hyper ] [ {time.strftime('%H:%M:%S', time.localtime())} ]" + fg.dark_grey + " • " + fg.red + f"Something is wrong with your csv!")
   
    for t in processlist:
        t.start()

    for t in processlist:
        t.join()

if mode == 2:
    dashboard = input(fg.light_red + f"[ Hyper ] [ {time.strftime('%H:%M:%S', time.localtime())} ]" + fg.dark_grey + " • " + fg.rs + "Dashboard(ex. https://kenki-tools.hyper.co/): ")
   
    while True:
        paid = input(fg.light_red + f"[ Hyper ] [ {time.strftime('%H:%M:%S', time.localtime())} ]" + fg.dark_grey + " • " + fg.rs + "Is the release paid?(y/n): ")
   
        if paid == "y" or paid == "Y":
            paid = True
            break
   
        if paid == "n" or paid == "N":
            paid = False
            break
   
        else:
            print(fg.light_red + f"[ Hyper ] [ {time.strftime('%H:%M:%S', time.localtime())} ]" + fg.dark_grey + " • " + fg.red + 'Error - please only use y/n')
  
    webhook = DiscordWebhook(url=private_webhook_hyper, avatar_url="https://media.discordapp.net/attachments/878354931201998859/1059895159959076975/kenki_logo_render.png", username="KenkiTools")
    embed = DiscordEmbed(title=f'KenkiTools Hyper Logger', description=f'{key_username} Started tasks', color='bc252c')
    embed.set_footer(text=f'Kenkitools', icon_url="https://media.discordapp.net/attachments/878354931201998859/1059895159959076975/kenki_logo_render.png")
    embed.set_timestamp()
    embed.add_embed_field(name='Version', value=f'{current_version}', inline=False)
    embed.add_embed_field(name='User', value=f'<@{key_user_id}>', inline=False)
    embed.add_embed_field(name='Dashboard', value=f'{dashboard}', inline=False)
    embed.add_embed_field(name='Channel id', value=f'MANUAL INPUT', inline=False)
    webhook.add_embed(embed)
    webhook.execute()
    
    task = 0
    processlist = []
    
    with open('hyper/profiles/profile.csv', newline='') as input_file:
        csv_file = csv.reader(input_file)
        for row in csv_file:
            if row != ["discord token","email","firstname","lastname","address","address2","zip code","city","state","countrycode","cc","cvc","exp"]:
      
                if "@" in row[1]:
                    task += 1
                    processlist.append(threading.Thread(target=hyper_manual, args=(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11], row[12], dashboard, paid, task, )))
              
                else:
                    print(fg.light_red + f"[ Hyper ] [ {time.strftime('%H:%M:%S', time.localtime())} ]" + fg.dark_grey + " • " + fg.red + f"Something is wrong with your csv!")
  
    for t in processlist:
        t.start()

    for t in processlist:
        t.join()