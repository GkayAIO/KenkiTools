import csv, datetime
from discord_webhook import DiscordWebhook, DiscordEmbed

from data.storage import *

today = datetime.date.today()
time_is = today.strftime("%m-%d-%y")

def nikeordertracker():

    clear_console()
    print_logo()
    print(fg.light_red + f"[ Nike tracker ] [ {time.strftime('%H:%M:%S', time.localtime())} ]" + fg.dark_grey + " • " + fg.rs + 'Fetching orders...')
    global tracking_list
    tracking_list = []
 
    with open('Shipping/Nike/input.csv', newline='') as input_file:
        csv_file = csv.reader(input_file)
        next(csv_file)
        try:
            for row in csv_file:
                tracking_list.append((row[0], row[1], row[2]))
        except Exception as e:
            print(fg.light_red + f"[ Nike tracker ] [ {time.strftime('%H:%M:%S', time.localtime())} ]" + fg.dark_grey + " • " + fg.red + 'Error scraping orders')
   
    print(fg.light_red + f"[ Nike tracker ] [ {time.strftime('%H:%M:%S', time.localtime())} ]" + fg.dark_grey + " • " + fg.green + 'Successfully fetched orders\n')
    tracked_orders = {}
    tracked = 0
    webhook = DiscordWebhook(url=private_webhook_tasks, avatar_url="https://media.discordapp.net/attachments/878354931201998859/1059895159959076975/kenki_logo_render.png", username="KenkiTools")
    embed = DiscordEmbed(title=f'KenkiTools Nike Logger', description=f'{key_username} tracking orders', color="bc252c")
    embed.set_footer(text=f"KenkiTools", icon_url="https://media.discordapp.net/attachments/878354931201998859/1059895159959076975/kenki_logo_render.png")
    embed.set_timestamp()
    embed.add_embed_field(name='Version', value=f'{current_version}', inline=False)
    embed.add_embed_field(name='User', value=f'<@{key_user_id}>', inline=False)
    webhook.add_embed(embed)
    webhook.execute()
   
    for tracking in tracking_list:
        if tracking[2] != "":
            user_webhook = tracking[2]
  
        tracked += 1
        print(fg.light_red + f"[ Nike tracker ] [ {time.strftime('%H:%M:%S', time.localtime())} ]" + fg.dark_grey + " • " + fg.rs + f'Tracking order {tracked}')
        headers = {
            "authority": "api.nike.com",
            "accept": "application/json",
            "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36",
            "x-nike-visitid": "1",
            "x-nike-visitorid": str(uuid.uuid4()),
            'nike-api-caller-id': 'com.nike:sse.orders',
        }
        r = requests.get(f'https://api.nike.com/orders/summary/v1/{tracking[0]}?locale=en_us&country=US&language=en&email={tracking[1]}&timezone=Europe%2FBerlin', headers=headers)
    
        if r.status_code == 200:

            r_text1 = r.text
            r_text = json.loads(r_text1)
            order_status = r_text["group"][0]["orderItems"][0]["lineItemStatus"]["status"]
            order_price = f'{r_text["transaction"]["orderTotal"]}' + " " + f'{r_text["currency"]}'
            order_size = r_text["group"][0]["orderItems"][0]["product"]["size"]
            order_address = r_text["shipFrom"]["address"]["address1"]
            order_city = r_text["shipFrom"]["address"]["city"]
            order_country = r_text["shipFrom"]["address"]["country"]
            order_zipcode = r_text["shipFrom"]["address"]["zipCode"]
            order_name = r_text["shipFrom"]["recipient"]["firstName"] + " " + r_text["shipFrom"]["recipient"]["lastName"]
            try:
                order_shippingtracker_url = r_text["group"][0]["actions"]["trackShipment"]["webLink"]
                tracking_number = re.findall("tracking_numbers=(.*?)&locale=", order_shippingtracker_url)[0]
            except:
                order_shippingtracker_url = "None"
                tracking_number = "None"
            order_picture = r_text["group"][0]["orderItems"][0]["product"]["productImage"]
            order_product_title = r_text["group"][0]["orderItems"][0]["product"]["title"]
            order_product_category = r_text["group"][0]["orderItems"][0]["product"]["category"]
            order_product_color = r_text["group"][0]["orderItems"][0]["product"]["color"]
            tracked_orders["order{0}".format(tracked)] = order_status
          
            with open(f"Shipping/Nike/output/{time_is}_output.csv", "w") as f:
                data = [tracking[0], order_status, tracking_number]
                csv.writer(f).writerow(data)
                f.close()
         
            webhook = DiscordWebhook(url=user_webhook, avatar_url="https://media.discordapp.net/attachments/878354931201998859/1059895159959076975/kenki_logo_render.png", username="KenkiTools")
            embed = DiscordEmbed(title=f'Successfully Tracked Order', description=f'{order_product_title} / {order_product_category}\n{order_product_color}', color="bc252c")
            embed.set_thumbnail(url=f"{order_picture}")
            embed.set_footer(text='@KenkiTools', icon_url="https://media.discordapp.net/attachments/878354931201998859/1059895159959076975/kenki_logo_render.png")
            embed.set_timestamp()
            embed.add_embed_field(name='Status', value=f'{order_status}', inline=True)
            embed.add_embed_field(name='Price', value=f'{order_price}', inline=True)
            embed.add_embed_field(name='Size', value=f'{order_size}', inline=True)
            embed.add_embed_field(name='Address & country', value=f'||{order_address} :flag_{order_country.lower()}:||', inline=True)
            embed.add_embed_field(name='City & Zip', value=f'||{order_city} / {order_zipcode}||', inline=True)
            embed.add_embed_field(name='Email', value=f'||{tracking[1]}||', inline=True)
            embed.add_embed_field(name='Ordernumber', value=f'||{tracking[0]}||', inline=True)
            embed.add_embed_field(name='Tracking number', value=f'||{tracking_number}||', inline=True)
            embed.add_embed_field(name='Shipping name', value=f'||{order_name}||', inline=True)
            embed.add_embed_field(name='Tracking URL', value=f'[click here]({order_shippingtracker_url})', inline=True)
            webhook.add_embed(embed)
            webhook.execute()
          
            print(fg.light_red + f"[ Nike tracker ] [ {time.strftime('%H:%M:%S', time.localtime())} ]" + fg.dark_grey + " • " + fg.light_blue + f'Successfully tracked order "{tracking[0]}"!')
            print(fg.light_red + f"[ Nike tracker ] [ {time.strftime('%H:%M:%S', time.localtime())} ]" + fg.dark_grey + " • " + fg.light_blue + f'Status: {order_status}\n')
      
        else:
            print(fg.light_red + f"[ Nike tracker ] [ {time.strftime('%H:%M:%S', time.localtime())} ]" + fg.dark_grey + " • " + fg.red + 'Error tracking order!\n')
   
    webhook = DiscordWebhook(url=public_webhook_aio, avatar_url="https://media.discordapp.net/attachments/878354931201998859/1059895159959076975/kenki_logo_render.png", username="KenkiTools")
    embed = DiscordEmbed(title=f'Successfully Tracked Nike Order', description='', color='bc252c')
    embed.set_thumbnail(url="https://media.discordapp.net/attachments/878354931201998859/1068966965479215234/Nike_1.png")
    embed.set_footer(text=f'KenkiTools', icon_url="https://media.discordapp.net/attachments/878354931201998859/1059895159959076975/kenki_logo_render.png")
    embed.set_timestamp()
    embed.add_embed_field(name='Amount of packages tracked', value=f'{tracked}', inline=False)
    if show_name == "true":
        embed.add_embed_field(name='username', value=f'{key_username}', inline=False)
    else:
        embed.add_embed_field(name='username', value=f'anonym', inline=False)
    webhook.add_embed(embed)
    webhook.execute()
  
    while True:
  
        run24 = input(fg.light_red + f"[ Nike tracker ] [ {time.strftime('%H:%M:%S', time.localtime())} ]" + fg.dark_grey + " • " + fg.rs + 'Do you want to run 24/7 for updates (y/n): ')
        if run24 == "y" or run24 == "Y":
            run24 = True
            break
        if run24 == "n" or run24 == "N":
            run24 = False
            break
        else:
            print("wrong input, retry")
  
    if run24 == True:
        while True:
            print(fg.light_red + f"[ Nike tracker ] [ {time.strftime('%H:%M:%S', time.localtime())} ]" + fg.dark_grey + " • " + fg.light_blue + 'Sleeping for 3 hours')
            time.sleep(10800)
            tracked = 0
    
            webhook = DiscordWebhook(url=private_webhook_tasks, avatar_url="https://media.discordapp.net/attachments/878354931201998859/1059895159959076975/kenki_logo_render.png", username="KenkiTools")
            embed = DiscordEmbed(title=f'KenkiTools Nike Logger', description=f'{key_username} tracking orders', color="bc252c")
            embed.set_footer(text=f"KenkiTools", icon_url="https://media.discordapp.net/attachments/878354931201998859/1059895159959076975/kenki_logo_render.png")
            embed.set_timestamp()
            embed.add_embed_field(name='Version', value=f'{current_version}', inline=False)
            embed.add_embed_field(name='User', value=f'<@{key_user_id}>', inline=False)
            webhook.add_embed(embed)
            webhook.execute()
       
            for tracking in tracking_list:
                tracked += 1
                headers = {
                    "authority": "api.nike.com",
                    "accept": "application/json",
                    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36",
                    "x-nike-visitid": "1",
                    "x-nike-visitorid": str(uuid.uuid4()),
                    'nike-api-caller-id': 'com.nike:sse.orders',
                }
                r = requests.get(f'https://api.nike.com/orders/summary/v1/{tracking[0]}?locale=en_us&country=US&language=en&email={tracking[1]}&timezone=Europe%2FBerlin', headers=headers)
           
                if r.status_code == 200:

                    r_text1 = r.text
                    r_text = json.loads(r_text1)
                    if order_status != tracked_orders[f"order{tracked}"]:
                        order_status = r_text["group"][0]["orderItems"][0]["lineItemStatus"]["status"]
                        status_changed = True
                    else:
                        status_changed = False
                    order_price = f'{r_text["transaction"]["orderTotal"]}' + " " + f'{r_text["currency"]}'
                    order_size = r_text["group"][0]["orderItems"][0]["product"]["size"]
                    order_address = r_text["shipFrom"]["address"]["address1"]
                    order_city = r_text["shipFrom"]["address"]["city"]
                    order_country = r_text["shipFrom"]["address"]["country"]
                    order_zipcode = r_text["shipFrom"]["address"]["zipCode"]
                    order_name = r_text["shipFrom"]["recipient"]["firstName"] + " " + r_text["shipFrom"]["recipient"]["lastName"]
                    try:
                        order_shippingtracker_url = r_text["group"][0]["actions"]["trackShipment"]["webLink"]
                    except:
                        order_shippingtracker_url = "None"
                    order_picture = r_text["group"][0]["orderItems"][0]["product"]["productImage"]
                    order_product_title = r_text["group"][0]["orderItems"][0]["product"]["title"]
                    order_product_category = r_text["group"][0]["orderItems"][0]["product"]["category"]
                    order_product_color = r_text["group"][0]["orderItems"][0]["product"]["color"]
                   
                    if status_changed == True:
               
                        webhook = DiscordWebhook(url=user_webhook, avatar_url="https://media.discordapp.net/attachments/878354931201998859/1059895159959076975/kenki_logo_render.png", username="KenkiTools")
                        embed = DiscordEmbed(title=f'Successfully Tracked Order', description=f'{order_product_title} / {order_product_category}\n{order_product_color}', color="bc252c")
                        embed.set_thumbnail(url=f"{order_picture}")
                        embed.set_footer(text='@KenkiTools', icon_url="https://media.discordapp.net/attachments/878354931201998859/1059895159959076975/kenki_logo_render.png")
                        embed.set_timestamp()
                        embed.add_embed_field(name='Status', value=f'{order_status}', inline=True)
                        embed.add_embed_field(name='Price', value=f'{order_price}', inline=True)
                        embed.add_embed_field(name='Size', value=f'{order_size}', inline=True)
                        embed.add_embed_field(name='Address & country', value=f'||{order_address} :flag_{order_country.lower()}:||', inline=True)
                        embed.add_embed_field(name='City & Zip', value=f'||{order_city} / {order_zipcode}||', inline=True)
                        embed.add_embed_field(name='Email', value=f'||{tracking[1]}||', inline=True)
                        embed.add_embed_field(name='Ordernumber', value=f'||{tracking[0]}||', inline=True)
                        embed.add_embed_field(name='Shipping name', value=f'||{order_name}||', inline=True)
                        embed.add_embed_field(name='Tracking URL', value=f'[click here]({order_shippingtracker_url})', inline=True)
                        webhook.add_embed(embed)
                        webhook.execute()
                        status_changed = False
                    else:
                        print(fg.light_red + f"[ Nike tracker ] [ {time.strftime('%H:%M:%S', time.localtime())} ]" + fg.dark_grey + " • " + fg.rs + 'Order status didnt change')
                  
                    print(fg.light_red + f"[ Nike tracker ] [ {time.strftime('%H:%M:%S', time.localtime())} ]" + fg.dark_grey + " • " + fg.green + 'Successfully tracked order!')
         
            webhook = DiscordWebhook(url=private_webhook_tasks, avatar_url="https://media.discordapp.net/attachments/878354931201998859/1059895159959076975/kenki_logo_render.png", username="KenkiTools")
            embed = DiscordEmbed(title=f'Successfully Tracked Nike Order', description='', color='bc252c')
            embed.set_thumbnail(url="https://media.discordapp.net/attachments/878354931201998859/1068966965479215234/Nike_1.png")
            embed.set_footer(text=f'KenkiTools', icon_url="https://media.discordapp.net/attachments/878354931201998859/1059895159959076975/kenki_logo_render.png")
            embed.set_timestamp()
            embed.add_embed_field(name='Amount of packages tracked', value=f'{tracked}', inline=False)
            if show_name == "true":
                embed.add_embed_field(name='username', value=f'{key_username}', inline=False)
            else:
                embed.add_embed_field(name='username', value=f'anonym', inline=False)
            webhook.add_embed(embed)
            webhook.execute()
   
    if run24 == False:
        time.sleep(3)