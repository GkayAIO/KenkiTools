import tls_client, random, fake_useragent
from discord_webhook import DiscordWebhook, DiscordEmbed

from data.storage import *

ua = fake_useragent.UserAgent()

def check_offers(session, token, mar):

    agent = ua.random

    while True:

        print(fg.light_red + f"[ Wethenew ] [ {time.strftime('%H:%M:%S', time.localtime())} ]" + fg.dark_grey + " • " + fg.rs + "Checking offers...")
        header = {
            'authority': "api-sell.wethenew.com",
            "method": "GET",
            "path": "/offers?skip=0&take=10",
            "scheme": "https",
            "accept": "application/json, text/plain, */*",
            "accept-encoding": "gzip, deflate",
            "accept-language": "en-GB,en-US;q=0.9,en;q=0.8",
            "authorization": f"Bearer {token}",
            "cache-control": "no-cache",
            "dnt": "1",
            "feature-policy": "microphone 'none'; geolocation 'none'; camera 'none'; payment 'none'; battery 'none'; gyroscope 'none'; accelerometer 'none';",
            "origin": "https://sell.wethenew.com",
            "pragma": "no-cache",
            "referer": "https://sell.wethenew.com/",
            "sec-ch-ua": '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": '"macOS"',
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-site",
            "user-agent": agent,
            "x-xss-protection": "0"
        }
        payload = {
            "skip": "0",
            "take": "10"
        }
        check_offers = session.get("https://api-sell.wethenew.com/offers", headers=header, params=payload)
       
        if check_offers.status_code == 200:
            check_offers_json = json.loads(check_offers.text)
       
        else:
            print(fg.light_red + f"[ Wethenew ] [ {time.strftime('%H:%M:%S', time.localtime())} ]" + fg.dark_grey + " • " + fg.red + f"Error, ratelimited - {check_offers.status_code}")
            time.sleep(60)
    
        try:
            item_id = check_offers_json["results"][0]["id"]
            item_name = check_offers_json["results"][0]["name"]
            item_variant = check_offers_json["results"][0]["variantId"]
            item_sku = check_offers_json["results"][0]["sku"]
            item_image = check_offers_json["results"][0]["image"]
            item_price = check_offers_json["results"][0]["price"]
            item_desired = check_offers_json["results"][0]["listingPrice"]
            print(fg.light_red + f"[ Wethenew ] [ {time.strftime('%H:%M:%S', time.localtime())} ]" + fg.dark_grey + " • " + fg.green + "Successfully found offer!")
        
            if int(item_price)+int(mar) >= item_desired:
                print(fg.light_red + f"[ Wethenew ] [ {time.strftime('%H:%M:%S', time.localtime())} ]" + fg.dark_grey + " • " + fg.rs + "Accepting offer...")
                input("")
                header = {
                    "accept": "application/json, text/plain, */*",
                    "authorization": f"Bearer {token}",
                    "user-agent": agent,
                    "x-xss-protection": "0"
                }
                accept_offer_1 = session.get(f"https://api-sell.wethenew.com/offers/{item_variant}", headers=header)
           
                if accept_offer_1.status_code == 200:
                    print(accept_offer_1.text)
                    payload = {"name":f"{item_id}","status":"ACCEPTED","variantId":item_variant}
                    accept_offer_2 = session.post("https://api-sell.wethenew.com/offers", headers=header, json=payload)
                    if accept_offer_2.status_code == 201:
                        status = "Accepted"
                    print(accept_offer_2.text)
                    print(accept_offer_2)
          
            else:
                print(fg.light_red + f"[ Wethenew ] [ {time.strftime('%H:%M:%S', time.localtime())} ]" + fg.dark_grey + " • " + fg.red + "declining offer...")
                status = "Declined"
                params = {
                    "variantIds[]": item_variant
                }
                header ={
                    "accept": "application/json, text/plain, */*",
                    "authorization": f"Bearer {token}",
                    "user-agent": agent,
                    "x-xss-protection": "0"
                }
                decline_offer_1 = session.get(f"https://api-sell.wethenew.com/listings/cheapest?variantIds[]={item_variant}",headers=header, json=params)
             
                if decline_offer_1.status_code == 200:
                    decline_offer_2 = session.get(f"https://api-sell.wethenew.com/offers/{item_id}", headers=header)
                  
                    if decline_offer_2.status_code == 200:
                        payload = {"name":f"{item_id}","status":"REFUSED_PRODUCT_UNAVAILABLE","isProductAvailable":"false","variantId":{item_variant}}
                        decline_offer_3 = session.post("https://api-sell.wethenew.com/offers", headers=header, json=payload)
                  
                        if decline_offer_3.status_code == 201:
                            print(fg.light_red + f"[ Wethenew ] [ {time.strftime('%H:%M:%S', time.localtime())} ]" + fg.dark_grey + " • " + fg.red + "Successfully declined offer!")
                  
                        else:
                            print("3")
                            print(decline_offer_3.text)
                 
                    else:
                        print("2")
                        print(decline_offer_2.text)
            
                else:
                    print("1")
                    print(decline_offer_1.text)
         
            input("")
            webhook = DiscordWebhook(url=user_webhook, avatar_url="https://media.discordapp.net/attachments/878354931201998859/1059895159959076975/kenki_logo_render.png", username="KenkiTools")
            embed = DiscordEmbed(title=f'New wethenew offer', description='', color='bc252c')
            embed.set_thumbnail(url=f"{item_image}")
            embed.set_footer(text=f'@KenkiTools', icon_url=f"https://media.discordapp.net/attachments/878354931201998859/1059895159959076975/kenki_logo_render.png")
            embed.set_timestamp()
            embed.add_embed_field(name='ID', value=f'{item_id}', inline=False)
            embed.add_embed_field(name='Item', value=f'{item_name}', inline=True)
            embed.add_embed_field(name='SKU', value=f'{item_sku}', inline=True)
            embed.add_embed_field(name='Offered price', value=f'{item_price}', inline=False)
            embed.add_embed_field(name='Status', value=f'{status}', inline=False)
            webhook.add_embed(embed)
            webhook.execute()
          
            webhook = DiscordWebhook(url=public_webhook_aio, avatar_url="https://media.discordapp.net/attachments/878354931201998859/1059895159959076975/kenki_logo_render.png", username="KenkiTools")
            embed = DiscordEmbed(title=f'New wethenew offer', description='', color='bc252c')
            embed.set_thumbnail(url=f"{item_image}")
            embed.set_footer(text=f'KenkiTools', icon_url="https://media.discordapp.net/attachments/878354931201998859/1059895159959076975/kenki_logo_render.png")
            embed.set_timestamp()
            embed.add_embed_field(name='Item', value=f'{item_name}', inline=True)
            embed.add_embed_field(name='SKU', value=f'{item_sku}', inline=True)
            embed.add_embed_field(name='Offered price', value=f'{item_price}', inline=False)
            embed.add_embed_field(name='Status', value='', inline=False)
            if show_name == "true":
                embed.add_embed_field(name='username', value=f'{key_username}', inline=False)
            else:
                embed.add_embed_field(name='username', value=f'anonym', inline=False)
            webhook.add_embed(embed)
            webhook.execute()
       
        except:
            print(fg.light_red + f"[ Wethenew ] [ {time.strftime('%H:%M:%S', time.localtime())} ]" + fg.dark_grey + " • " + fg.rs + "No offer detected!")
            time.sleep(random.randint(6,10))
