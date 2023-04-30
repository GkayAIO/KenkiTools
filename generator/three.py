import csv, datetime, names
from discord_webhook import DiscordWebhook, DiscordEmbed

from data.storage import *

today = datetime.date.today()
time_is = today.strftime("%m-%d-%y")
global Successfull
Successfull = 1

def load_proxies():

    global total_proxies
    total_proxies = 0
    global proxy
    proxy = set()

    with open("proxy.txt", 'r+') as f:
        proxy_list = f.readlines()
        for line in proxy_list:
            total_proxies += 1
            proxy.add(line.strip())
        f.close()

    if total_proxies == 1:
        print(fg.light_red + f"[ Three ] [ {time.strftime('%H:%M:%S', time.localtime())} ]" + fg.dark_grey + " • " + fg.red + "No proxies loaded!")
    
    else:
        print(fg.light_red + f"[ Three ] [ {time.strftime('%H:%M:%S', time.localtime())} ]" + fg.dark_grey + " • " + fg.rs + f"Successfully loaded {total_proxies} proxies!\n")

def load_tasks():

    global tasks 
    tasks = 0
    global profiles
    profiles = []
   
    with open("Generator/Other/Three/input.csv", newline="") as f:
        csv_file = csv.reader(f)

        try:
            for row in csv_file:
                if row != ["email", "firstname", "lastname", "postcode", "address", "address2", "city"]:
                    tasks += 1
                    profiles.append((row[0], row[1], row[2], row[3], row[4], row[5], row[6]))
          
            print(fg.light_red + f"[ Three ] [ {time.strftime('%H:%M:%S', time.localtime())} ]" + fg.dark_grey + " • " + fg.rs + f"Successfully loaded {tasks} tasks!")
     
        except:
            print(fg.light_red + f"[ Three ] [ {time.strftime('%H:%M:%S', time.localtime())} ]" + fg.dark_grey + " • " + fg.red + f"Error scraping profiles")

def solve_captcha(suc, ta):

    print(fg.light_red + f"[ Three ] [ {time.strftime('%H:%M:%S', time.localtime())} ] [ {suc}/{ta} ]" + fg.dark_grey + " • " + fg.rs + "Solving captcha...")
 
    try:
        captcha = solver.hcaptcha(
            sitekey='28d6ff2e-5725-4d95-a4b8-2c0a400fd47c',
            url='https://www.three.co.uk/Support/Free_SIM/Order',
            version='v2',
            action='demo_action',
            score=0.3
        )
    
        captcha = str(captcha["code"])
        print(fg.light_red + f"[ Three ] [ {time.strftime('%H:%M:%S', time.localtime())} ] [ {suc}/{ta} ]" + fg.dark_grey + " • " + fg.green + "Successfully solved captcha!")
        return captcha
   
    except:
        print(fg.light_red + f"[ Three ] [ {time.strftime('%H:%M:%S', time.localtime())} ] [ {suc}/{ta} ]" + fg.dark_grey + " • " + fg.red + "Error solving captcha!")

def generate_account(email, firstname, lastname, postcode, address, address2, city, proxy):
    
    global Successfull
    if firstname == "RANDOM" or firstname == "Random" or firstname == "random":
        firstname = f"{names.get_first_name()}"
    if lastname == "RANDOM" or lastname == "Random" or lastname == "random":
        lastname = f"{names.get_last_name()}"
    if email.startswith("RANDOM") or email.startswith("random") or email.startswith("Random"):
        email = email.split("@")
        email = f"{firstname}{lastname}@{email[1]}"
    proxy = {"http": f"http://{proxy}"}
    
    headers = {
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'de-DE,de;q=0.9,en-US;q=0.8,en;q=0.7',
        'Connection': 'keep-alive',
        'Content-Type': 'application/json',
        'dnt': '1',
        'Host': 'www.three.co.uk',
        'Origin': 'https://www.three.co.uk',
        'Referer': 'https://www.three.co.uk/Support/Free_SIM/Order',
        'sec-ch-ua': '"Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest'
        }
 
    captcha = solve_captcha(Successfull, tasks)
 
    payload = {
        "_form_url":"",
        "_success_url":"/Support/Free_SIM/Order_Confirmation",
        "_failure_url":"",
        "hiddenField":"tr-triosim",
        "firstname":firstname,
        "surname":lastname,
        "existingContactNumber":"",
        "email":email,
        "confirmemail":email,
        "postcode":postcode,
        "street":address,
        "address2":address2,
        "town":city,
        "marketingPrefs":"Yes",
        "g-recaptcha-response":captcha,
        "h-captcha-response":captcha
    }
 
    r = requests.post('https://www.three.co.uk/cs/form/freesimreg', headers=headers, json=payload, proxies=proxy)
  
    if r.status_code == 200:
        response_text = json.loads(r.text)
        print(fg.light_red + f"[ Three ] [ {time.strftime('%H:%M:%S', time.localtime())} ] [ {Successfull}/{tasks} ]" + fg.dark_grey + " • " + fg.green + "Successfully ordered sim!\n")
        Successfull += 1
        csv_data = [f'{email}', f'{address}', f'{response_text["data"]["redirectUrl"][45:]}']
       
        with open(f'Generator/Other/Three/Output/Three_{time_is}.csv', 'a+', encoding='UTF8', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(csv_data)
      
        with open("Data/accounts", "r+") as f:
            data = f.read()
            accounts_generated = int(data.replace('\x00',''))
            accounts_generated += 1
            f.truncate(0)
            f.write(str(accounts_generated))
            f.close()
      
        try:
            webhook = DiscordWebhook(url=user_webhook, avatar_url="https://media.discordapp.net/attachments/878354931201998859/1059895159959076975/kenki_logo_render.png", username="KenkiTools")
            embed = DiscordEmbed(title=f'Successfully Ordered Sim', description='', color='bc252c')
            embed.set_thumbnail(url="https://media.discordapp.net/attachments/878354931201998859/1059895159959076975/kenki_logo_render.png")
            embed.set_footer(text=f'@KenkiTools', icon_url=f"https://media.discordapp.net/attachments/878354931201998859/1059895159959076975/kenki_logo_render.png")
            embed.set_timestamp()
            embed.add_embed_field(name='Site', value='Three', inline=False)
            embed.add_embed_field(name='Name', value=f'{firstname} {lastname}', inline=True)
            embed.add_embed_field(name='Address', value=f'||{address + " " + address2}||', inline=True)
            embed.add_embed_field(name='Email', value=f'||{email}||', inline=False)
            embed.add_embed_field(name='Order number', value=f'||{response_text["data"]["redirectUrl"][45:]}||', inline=False)
            embed.add_embed_field(name='Proxy', value=f'||{proxy}||', inline=False)
            webhook.add_embed(embed)
            webhook.execute()
            webhook = DiscordWebhook(url=public_webhook_aio, avatar_url="https://media.discordapp.net/attachments/878354931201998859/1059895159959076975/kenki_logo_render.png", username="KenkiTools")
            embed = DiscordEmbed(title=f'Successfully Ordered Sim', description=f'', color='bc252c')
            embed.set_thumbnail(url="https://media.discordapp.net/attachments/878354931201998859/1059895159959076975/kenki_logo_render.png")
            embed.set_footer(text=f'KenkiTools', icon_url="https://media.discordapp.net/attachments/878354931201998859/1059895159959076975/kenki_logo_render.png")
            embed.set_timestamp()
            embed.add_embed_field(name='Site', value='three', inline=False)
            if show_name == "true":
                embed.add_embed_field(name='username', value=f'{key_username}', inline=False)
            else:
                embed.add_embed_field(name='username', value=f'anonym', inline=False)
            webhook.add_embed(embed)
            webhook.execute()
       
        except Exception as e:
            print(e)
            print(fg.light_red + f"[ Three ] [ {time.strftime('%H:%M:%S', time.localtime())} ]" + fg.dark_grey + " • " + fg.red + "No webhook set!")
      
        webhook = DiscordWebhook(url=private_webhook_tasks, avatar_url="https://media.discordapp.net/attachments/878354931201998859/1059895159959076975/kenki_logo_render.png", username="KenkiTools")
        embed = DiscordEmbed(title=f'KenkiTools Sim Logger', description=f'{key_username} ordered three sim', color="bc252c")
        embed.set_footer(text=f"KenkiTools", icon_url="https://media.discordapp.net/attachments/878354931201998859/1059895159959076975/kenki_logo_render.png")
        embed.set_timestamp()
        embed.add_embed_field(name='Version', value=f'{current_version}', inline=False)
        embed.add_embed_field(name='User', value=f'<@{key_user_id}>', inline=False)
        embed.add_embed_field(name='Status code', value=f'{r.status_code}', inline=False)
        webhook.add_embed(embed)
        webhook.execute()
  
    else:
        print(fg.light_red + f"[ Three ] [ {time.strftime('%H:%M:%S', time.localtime())} ] [ {Successfull}/{tasks} ]" + fg.dark_grey + " • " + fg.red + f"{r.status_code} - {r.text}")

print_logo()
load_tasks()
load_proxies()

for profile in profiles:
  
    if tasks >= total_proxies:
        print(fg.light_red + f"[ Three ] [ {time.strftime('%H:%M:%S', time.localtime())} ]" + fg.dark_grey + " • " + fg.red + "Error, not enough Proxies loaded, more tasks then proxies!")
 
    else:
        print(fg.light_red + f"[ Three ] [ {time.strftime('%H:%M:%S', time.localtime())} ] [ {Successfull}/{tasks} ]" + fg.dark_grey + " • " + fg.light_yellow + "Ordering sim...")
        generate_account(profile[0], profile[1], profile[2], profile[3], profile[4], profile[5], profile[6], list(proxy)[Successfull-1])