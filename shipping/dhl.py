import csv
from discord_webhook import DiscordWebhook, DiscordEmbed

from data.storage import *

def dhltracker():
    print_logo()
  
    def dhl_tracking(number):
        cookies = {
        '_abck': '745A3CBC83FC1A9AB2754053F26B60AF~0~YAAQt+1lX6yE3YGDAQAA4uRskgitE7/USxE/qdPNL4+8M2RU+gKkCrH+2c+2+FAXVJobHVjessBEMFlUBKdObX6RDP32e/9dto+H7OCuiOfYMANr+8/ZQ2uEuYPkUxhBTspezuA14QSa6Qrg9ENPn+XLUKwZxF2SGTpFgGpV6POy+XVoHkLEy9Z1MCYF4APYH1Ru1nEFXKxceRMibNIYYrmHCDUk46R+hP92l11mbaBBP3NaaZklV/8gx9dGsKfBVQ1PLfNYI70mYAj5o/JRZeHEl/n01GAsYfnl2FCPxBwuk4DJwEVXQ+cg3Fkf4thfcq4YRrWY6mafuZ/ZgUIifurzXLa/1QbZHOCDDIa6hYA2zCKTiHVCS5s55f2tWRcZM86t/ocm8oMKEbfXsXyM0BitrQ==~-1~-1~-1',
        }
        headers = {
        'authority': 'www.dhl.com',
        'accept': '*/*',
        'accept-language': 'en-GB,en;q=0.9',
        'cache-control': 'no-cache',
        'referer': f'https://www.dhl.com/global-en/home/tracking/tracking-parcel.html?submit=1&tracking-id={number}',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36',
        'x-sec-clge-req-type': 'ajax',
        }
        params = {
            'trackingNumber': number,
            'language': 'en',
            'source': 'tt',
        }
     
        try:
            response = requests.get('https://www.dhl.com/utapi', params=params, cookies=cookies, headers=headers)
            return response.text
        except Exception as e:
            print(e)
  
    def process_output(param):
        try:
            data = json.loads(param)

            try:
                tracking_id = data['shipments'][0]['id'] 
                status = data['shipments'][0]['status']['status']
       
            except KeyError:
                if data['sec-cp-challenge'] == 'true':
                    return 'Ratelimit, please try again later'
      
        except json.decoder.JSONDecodeError:
            return 'Failed to track or expired tracking'

        return tracking_id, status
  
    def main():
        tracked = 0
        for t in tracking_list:
            tracked += 1
       
            try:
                print(fg.light_red + f"[ DHL tracker ] [ {time.strftime('%H:%M:%S', time.localtime())} ]" + fg.dark_grey + " • " + fg.green + f'{process_output(dhl_tracking(t))}')
        
                webhook = DiscordWebhook(url=user_webhook, avatar_url="https://media.discordapp.net/attachments/878354931201998859/1059895159959076975/kenki_logo_render.png", username="KenkiTools")
                embed = DiscordEmbed(title=f'Successfully Tracked Order', description='', color="bc252c")
                embed.set_thumbnail(url="https://media.discordapp.net/attachments/878354931201998859/1059895159959076975/kenki_logo_render.png")
                embed.set_footer(text="@KenkiTools", icon_url="https://media.discordapp.net/attachments/878354931201998859/1059895159959076975/kenki_logo_render.png")
                embed.set_timestamp()
                embed.add_embed_field(name='Order status', value=f'||{process_output(dhl_tracking(t))}||', inline=False)
                embed.add_embed_field(name='Tracking number', value=f'||{tracking_list[0]}||', inline=True)
                webhook.add_embed(embed)
                webhook.execute()
            
                webhook = DiscordWebhook(url=private_webhook_tasks, avatar_url="https://media.discordapp.net/attachments/878354931201998859/1059895159959076975/kenki_logo_render.png", username="KenkiTools")
                embed = DiscordEmbed(title=f'KenkiTools Shipping Logger', description=f'{key_username} tracked DHL order', color="bc252c")
                embed.set_footer(text=f"KenkiTools", icon_url="https://media.discordapp.net/attachments/878354931201998859/1059895159959076975/kenki_logo_render.png")
                embed.set_timestamp()
                embed.add_embed_field(name='Version', value=f'{current_version}', inline=False)
                embed.add_embed_field(name='User', value=f'<@{key_user_id}>', inline=False)
                webhook.add_embed(embed)
                webhook.execute()
         
            except UnboundLocalError:
                continue
        
            time.sleep(2)
      
        if tracked == "0":
            pass
      
        else:

            webhook = DiscordWebhook(url=public_webhook_aio, avatar_url="https://media.discordapp.net/attachments/878354931201998859/1059895159959076975/kenki_logo_render.png", username="KenkiTools")
            embed = DiscordEmbed(title=f'Successfully Tracked Order', description='', color="bc252c")
            embed.set_thumbnail(url="https://media.discordapp.net/attachments/878354931201998859/1059895159959076975/kenki_logo_render.png")
            embed.set_footer(text=f"@kenkitools", icon_url="https://media.discordapp.net/attachments/878354931201998859/1059895159959076975/kenki_logo_render.png")
            embed.set_timestamp()
            embed.add_embed_field(name='Amount of packages tracked', value=f'{tracked} Packages', inline=True)
            if show_name == "true":
                embed.add_embed_field(name='username', value=f'{key_username}', inline=False)
            else:
                embed.add_embed_field(name='username', value=f'anonym', inline=False)
            webhook.add_embed(embed)
            webhook.execute()
           
            time.sleep(3)
   
    global tracking_list
    tracking_list = []
  
    with open('Shipping/DHL/input.csv', newline='') as input_file:
        csv_file = csv.reader(input_file)
   
        try:
            for row in csv_file:
                if row != ["Tracking Number"]:
                    tracking_list.append((row[0]))
    
        except Exception as e:
            print(fg.light_red + f"[ DHL tracker ] [ {time.strftime('%H:%M:%S', time.localtime())} ]" + fg.dark_grey + " • " + fg.red + f'Error - {e}')
   
    main()
    clear_console()
