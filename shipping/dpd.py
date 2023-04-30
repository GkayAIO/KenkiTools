import csv
from discord_webhook import DiscordWebhook, DiscordEmbed

from data.storage import *

def dpdtracker():
    clear_console()
    print_logo()
    print(fg.light_red + f"[ DPD tracker ] [ {time.strftime('%H:%M:%S', time.localtime())} ]" + fg.dark_grey + " • " + fg.rs + 'Fetching information...')
    global tracking_list
    tracking_list = []
    tracked = 0
   
    with open('Shipping/Shipping Tracker/DPD.csv', newline='') as input_file:
        csv_file = csv.reader(input_file)
    
        try:
            for row in csv_file:
                if row != ["Tracking Number"]:
                    tracking_list.append((row[0]))
  
        except Exception as e:
            print(fg.light_red + f"[ DPD tracker ] [ {time.strftime('%H:%M:%S', time.localtime())} ]" + fg.dark_grey + " • " + fg.red + f'Error - {e}')
 
    print(fg.light_red + f"[ DPD tracker ] [ {time.strftime('%H:%M:%S', time.localtime())} ]" + fg.dark_grey + " • " + fg.green + 'Successfully fetched information')
 
    def fetch_url(number):
  
        headers = {
            'authority': 'apis.track.dpd.co.uk',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
            'accept-language': 'en-GB,en;q=0.7',
            'cache-control': 'no-cache',
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36',
        }
        params = {
            'postcode': '',
            'parcel': number
        }
        response = requests.get('https://apis.track.dpd.co.uk/v1/track', params=params, headers=headers)
        url = response.url
        return url.split('/')[-1]
    
    def dpd_tracking(number_hash):
        headers = {
            'accept': 'application/json',
            'accept-language': 'en-GB,en;q=0.7',
            'authority': 'apis.track.dpd.co.uk',
            'cache-control': 'no-cache',
            'content-type': 'application/json',
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36',
        }
        response = requests.get(f'https://apis.track.dpd.co.uk/v1/parcels/{number_hash}', headers=headers)
        response_json = json.loads(response.text)
        return response_json['data']['trackingStatusCurrent']
    
    for tracking in tracking_list:
        tracked += 1
        print(fg.light_red + f"[ DPD tracker ] [ {time.strftime('%H:%M:%S', time.localtime())} ]" + fg.dark_grey + " • " + fg.green + f'{dpd_tracking(fetch_url(tracking))}')
  
        webhook = DiscordWebhook(url=user_webhook, avatar_url="https://media.discordapp.net/attachments/878354931201998859/1059895159959076975/kenki_logo_render.png", username="KenkiTools")
        embed = DiscordEmbed(title=f'Successfully Tracked Order', description='', color="bc252c")
        embed.set_thumbnail(url="https://media.discordapp.net/attachments/878354931201998859/1059895159959076975/kenki_logo_render.png")
        embed.set_footer(text='@KenkiTools', icon_url="https://media.discordapp.net/attachments/878354931201998859/1059895159959076975/kenki_logo_render.png")
        embed.set_timestamp()
        embed.add_embed_field(name='Order status', value=f'||{dpd_tracking(fetch_url(tracking))}||', inline=False)
        embed.add_embed_field(name='Tracking number', value=f'||{tracking}||', inline=True)
        webhook.add_embed(embed)
        webhook.execute()
    
        webhook = DiscordWebhook(url=private_webhook_tasks, avatar_url="https://media.discordapp.net/attachments/878354931201998859/1059895159959076975/kenki_logo_render.png", username="KenkiTools")
        embed = DiscordEmbed(title=f'KenkiTools Shipping Logger', description=f'{key_username} tracked DPD order', color="bc252c")
        embed.set_footer(text=f"KenkiTools", icon_url="https://media.discordapp.net/attachments/878354931201998859/1059895159959076975/kenki_logo_render.png")
        embed.set_timestamp()
        embed.add_embed_field(name='Version', value=f'{current_version}', inline=False)
        embed.add_embed_field(name='User', value=f'<@{key_user_id}>', inline=False)
        webhook.add_embed(embed)
        webhook.execute()
   
        time.sleep(2)
   
    if tracked == "0":
        pass
   
    else:
     
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