import csv
from discord_webhook import DiscordWebhook, DiscordEmbed

from data.storage import *

def meshtracker():
    clear_console()
   
    tracked = 0
    error = 0
    placed = 0
    processed = 0
    dispatched = 0
    delivered = 0
    global order
    orders = []
  
    print_logo()
    print(fg.light_red + f"[ Mesh tracker ] [ {time.strftime('%H:%M:%S', time.localtime())} ]" + fg.dark_grey + " • " + fg.rs + "Fetching information...")
   
    with open("Shipping/Mesh/input.csv", newline="") as f:
        csv_file = csv.reader(f)
     
        try:
            for row in csv_file:
                if row != ["store", "country code", "zip code", "ordernumber"]:
                    orders.append((row[0], row[1], row[2], row[3]))
  
        except:
            print(fg.light_red + f"[ Mesh tracker ] [ {time.strftime('%H:%M:%S', time.localtime())} ]" + fg.dark_grey + " • " + fg.red + "Error fetching the information")
   
    print(fg.light_red + f"[ Mesh tracker ] [ {time.strftime('%H:%M:%S', time.localtime())} ]" + fg.dark_grey + " • " + fg.rs + "Tracking orders...")
   
    for order in orders:
        params = {
            'orderNumber': order[3],
            'facia': order[0] + order[1],
            'postcode': order[2]
        }
        response = requests.get("https://data.smartagent.io/v1/jdsports/track-my-order", params=params)
        
        if response.status_code == 200:
            tracked += 1
            response = json.loads(response.text, strict=False)
            OrderNumber = response["number"]
            OrderStatus = response["message"]["text"]
          
            if OrderStatus == "Your order has been placed.":
                placed += 1
                OrderStatus = "📩 The order has been **Placed!**"
       
            if OrderStatus == "Your order is currently being processed.":
                processed += 1
                OrderStatus = "⏳ The order is currently being **Processed!**"
       
            if OrderStatus == "Your order has been despatched.":
                dispatched += 1
                OrderStatus = "📨 The order has been **Dispatched**!"
      
            if OrderStatus == "Your order has been delivered.":
                delivered += 1
                OrderStatus = "✅ The order has been **Delivered!**"
           
            OrderCourier = response["delivery"]["courier"]
            OrderTrackingURL = response["delivery"]["trackingURL"]
            ShoeName = response["vendors"][0]["items"][0]["name"]
            ShoeSize = response["vendors"][0]["items"][0]["size"]
            ShoeImage = response["vendors"][0]["items"][0]["img"]
            ShoePrice = response["vendors"][0]["items"][0]["price"]["amount"] + " " + response["vendors"][0]["items"][0]["price"]["currency"]
            print(fg.light_red + f"[ Mesh tracker ] [ {time.strftime('%H:%M:%S', time.localtime())} ]" + fg.dark_grey + " • " + fg.light_blue + f"Order {tracked} status: {OrderStatus}")
           
            webhook = DiscordWebhook(url=user_webhook, avatar_url="https://media.discordapp.net/attachments/878354931201998859/1059895159959076975/kenki_logo_render.png", username="KenkiTools")
            embed = DiscordEmbed(title=f'Successfully Tracked Order', description='', color="bc252c")
            embed.set_thumbnail(url=f"{ShoeImage}")
            embed.set_footer(text='@KenkiTools', icon_url="https://media.discordapp.net/attachments/878354931201998859/1059895159959076975/kenki_logo_render.png")
            embed.set_timestamp()
            embed.add_embed_field(name='Site', value=f'{order[0]} :flag_{order[1]}:', inline=True)
            embed.add_embed_field(name='Tracking number', value=f'||{OrderNumber}||', inline=True)
            embed.add_embed_field(name='Shoe', value=f'{ShoeName}', inline=True)
            embed.add_embed_field(name='Size', value=f'{ShoeSize}', inline=True)
            embed.add_embed_field(name='Price', value=f'{ShoePrice}', inline=True)
            embed.add_embed_field(name='Status', value=f'||{OrderStatus}||', inline=False)
            embed.add_embed_field(name='Courier', value=f'{OrderCourier}', inline=False)
            embed.add_embed_field(name='Tracking URL', value=f'||{OrderTrackingURL}||', inline=False)
            webhook.add_embed(embed)
            webhook.execute()
           
            webhook = DiscordWebhook(url=private_webhook_tasks, avatar_url="https://media.discordapp.net/attachments/878354931201998859/1059895159959076975/kenki_logo_render.png", username="KenkiTools")
            embed = DiscordEmbed(title=f'KenkiTools Shipping Logger', description=f'{key_username} tracked mesh order', color="bc252c")
            embed.set_footer(text=f"KenkiTools", icon_url="https://media.discordapp.net/attachments/878354931201998859/1059895159959076975/kenki_logo_render.png")
            embed.set_timestamp()
            embed.add_embed_field(name='Version', value=f'{current_version}', inline=False)
            embed.add_embed_field(name='User', value=f'<@{key_user_id}>', inline=False)
            webhook.add_embed(embed)
            webhook.execute()
        
        else:
            response = json.loads(response.text, strict=False)
            print(fg.light_red + f"[ Mesh tracker ] [ {time.strftime('%H:%M:%S', time.localtime())} ]" + fg.dark_grey + " • " + fg.red + f'Error tracking order - {response["message"]}')
            error += 1
 
    if tracked == 0:
        pass
  
    else:
        print(fg.light_red + f"[ Mesh tracker ] [ {time.strftime('%H:%M:%S', time.localtime())} ]" + fg.dark_grey + " • " + fg.green + f'Successfully tracked {tracked} orders, sending conclusion...')
    
        webhook = DiscordWebhook(url=user_webhook, avatar_url="https://media.discordapp.net/attachments/878354931201998859/1059895159959076975/kenki_logo_render.png", username="KenkiTools")
        embed = DiscordEmbed(title=f'Tracking Conclusion', description='', color="bc252c")
        embed.set_thumbnail(url="https://media.discordapp.net/attachments/878354931201998859/1059895159959076975/kenki_logo_render.png")
        embed.set_footer(text='@KenkiTools', icon_url="https://media.discordapp.net/attachments/878354931201998859/1059895159959076975/kenki_logo_render.png")
        embed.set_timestamp()
        embed.add_embed_field(name='Amount of packages tracked', value=f'{tracked} Packages', inline=True)
        embed.add_embed_field(name='Placed', value=f'{placed}/{tracked}', inline=False)
        embed.add_embed_field(name='Processed', value=f'{processed}/{tracked}', inline=False)
        embed.add_embed_field(name='Dispatched', value=f'{dispatched}/{tracked}', inline=False)
        embed.add_embed_field(name='Delivered', value=f'{delivered}/{tracked}', inline=False)
        embed.add_embed_field(name='Not found', value=f'{error}/{tracked}', inline=False)
        webhook.add_embed(embed)
        webhook.execute()
      
        webhook = DiscordWebhook(url=public_webhook_aio, avatar_url="https://media.discordapp.net/attachments/878354931201998859/1059895159959076975/kenki_logo_render.png", username="KenkiTools")
        embed = DiscordEmbed(title=f'Successfully Tracked Order', description='', color='bc252c')
        embed.set_thumbnail(url="https://media.discordapp.net/attachments/878354931201998859/1059895159959076975/kenki_logo_render.png")
        embed.set_footer(text="KenkiTools", icon_url="https://media.discordapp.net/attachments/878354931201998859/1059895159959076975/kenki_logo_render.png")
        embed.set_timestamp()
        embed.add_embed_field(name='Amount of packages tracked', value=f'{tracked} Packages', inline=True)
        if show_name == "true":
            embed.add_embed_field(name='username', value=f'{key_username}', inline=False)
        else:
            embed.add_embed_field(name='username', value=f'anonym', inline=False)
        webhook.add_embed(embed)
        webhook.execute()
    
    time.sleep(3)
    clear_console()