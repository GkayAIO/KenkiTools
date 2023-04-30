import urllib.request, sys, csv, pyperclip
from discord_webhook import DiscordWebhook, DiscordEmbed

from data.storage import *

def hyper(token, email, firstname, lastname, address1, address2, zip, city, state, countrycode, cc, cvc, exp, channel_id, dash, paid, task):
   
    s = requests.Session()
    exp_month = exp.split("/")[0]
    exp_year = exp.split("/")[1]
    print(fg.light_red + f"[ Hyper ] [ {time.strftime('%H:%M:%S', time.localtime())} ] [ {task} ]" + fg.dark_grey + " • " + fg.rs + 'Loading tasks...')
    r = s.get(dash)
    checkout_product = re.findall('<title>(.*?)</title', r.text)[0]
    hyper_account_id = re.findall('"id":"(.*)"},"links":', r.text)[0]
    collect_address = re.findall('"collect_billing_address":(.*?),', r.text)[0]
   
    if collect_address == "false":
        collect_address = False
  
    else:
        collect_address = True
   
    if paid == True:
   
        try:
            stripe_account = re.findall('"stripe_account":"(.*?)"', r.text)[0]
   
        except:
            print(fg.light_red + f"[ Hyper ] [ {time.strftime('%H:%M:%S', time.localtime())} ] [ {task} ]" + fg.dark_grey + " • " + fg.red + 'Error fetching stripe token')
  
    header = {"authorization":token,"content-type":"application/json"}
    payload = {"permissions":"0","authorize": "true"}
    r = s.post("https://discord.com/api/v9/oauth2/authorize?client_id=648234176805470248&response_type=code&redirect_uri=https%3A%2F%2Fapi.hyper.co%2Fauth%2Flogin%2Fdiscord%2Fcallback&scope=identify%20email%20guilds%20guilds.join%20guilds.members.read&state=%7B%22account%22%3A%22Az0SO5153wxFsnQ7VdqAV%22%7D",headers=header,json=payload)
   
    if r.text == '{"message": "401: Unauthorized", "code": 0}':
        print(fg.light_red + f"[ Hyper ] [ {time.strftime('%H:%M:%S', time.localtime())} ] [ {task} ]" + fg.dark_grey + " • " + fg.red + 'Invalid discord token')
   
    find_code = re.findall("code=(.*?)&state", r.text)
    r = s.get(f"https://api.hyper.co/auth/login/discord/callback?code={find_code[0]}&state=%7B%22account%22%3A%22{hyper_account_id}%22%7D")
    hypertoken = s.cookies["authorization"]
    header = {"cookie":"authorization="+hypertoken,"hyper-account":hyper_account_id}
    r = s.get(f"{dash}ajax/auth/user", headers=header)
    json_data = json.loads(r.text)
    owner = json_data["id"]
   
    if paid == True:
    
        try:
            header = {"content-type": "application/x-www-form-urlencoded"}
            payload = {
                "type": "card",
                "billing_details[name]": firstname + " " + lastname,
                "billing_details[email]": email,
                "card[number]": cc,
                "card[cvc]": cvc,
                "card[exp_month]": exp_month,
                "card[exp_year]": exp_year, 
                "key": "pk_live_51GXa1YLZrAkO7Fk2tcUO7vabkO7sgDamOww2OPYQVFhPZOllT75f7owzIOlP75MMdDXHKoy6wPt40HsuQDObpkHv004T74fAzs", #
                "_stripe_account": stripe_account
            }
            stripe = requests.post("https://api.stripe.com/v1/payment_methods", headers=header, data=payload)
            stripe_json = json.loads(stripe.text)
            stripe_id = stripe_json["id"]
    
        except:
            print(fg.light_red + f"[ Hyper ] [ {time.strftime('%H:%M:%S', time.localtime())} ] [ {task} ]" + fg.dark_grey + " • " + fg.red + 'Error fetching stripe token')
   
    while True:
        limit = 1
        headers = {
            "authorization": token
        }
        last_message_id = None
        query_parameters = f'limit={limit}'
      
        if last_message_id is not None:
            query_parameters += f'&before={last_message_id}'
       
        r = requests.get(f'https://discord.com/api/v9/channels/{channel_id}/messages?{query_parameters}', headers=headers)
        jsonn = json.loads(r.text)
      
        for value in jsonn:
    
                try:
                    old_content = f"{value['content']}"
   
                except:
                    print(fg.light_red + f"[ Hyper ] [ {time.strftime('%H:%M:%S', time.localtime())} ] [ {task} ]" + fg.dark_grey + " • " + fg.red + "Wrong token")
                    time.sleep(5)
                    sys.exit()
     
        print(fg.light_red + f"[ Hyper ] [ {time.strftime('%H:%M:%S', time.localtime())} ] [ {task} ]" + fg.dark_grey + " • " + fg.rs + "Successfully loaded task, waiting for link...")
      
        while True:
            limit = 1
            headers = {
                "authorization": token
            }
            last_message_id = None
            query_parameters = f'limit={limit}'
         
            if last_message_id is not None:
                query_parameters += f'&before={last_message_id}'
           
            r = requests.get(f'https://discord.com/api/v9/channels/{channel_id}/messages?{query_parameters}', headers=headers)
            jsonn = json.loads(r.text)
            clipboard_content = pyperclip.paste()
           
            if clipboard_content != old_content:
         
                if dash+"purchase?link=" in clipboard_content or "https://hpr.co/" in clipboard_content or dash+"password" in clipboard_content:
                    break
          
            for value in jsonn:
               
                try:
                    content = f"{value['content']}"
               
                except:
                    print(fg.light_red + f"[ Hyper ] [ {time.strftime('%H:%M:%S', time.localtime())} ] [ {task} ]" + fg.dark_grey + " • " + fg.red + f"Token has no access to the provided channel id")
                    input("")
                    sys.exit()
               
                try:
                  
                    if content == old_content:
                        continue
                    
                    else:
                        break
                
                except:
                    break
            
            if content == old_content:
                continue
          
            else:
                break
            
        if dash+"purchase?link=" in content or "https://hpr.co/" in content or dash+"password" in content or dash+"purchase?link=" in clipboard_content or "https://hpr.co/" in clipboard_content or dash+"password" in clipboard_content or "https://tinyurl.com/" in content:
            mode = "discord"
          
            try:
                checkout_link = re.search("(?P<url>https?://[^\s]+)", content).group("url")
         
            except:
                print(fg.light_red + f"[ Hyper ] [ {time.strftime('%H:%M:%S', time.localtime())} ] [ {task} ]" + fg.dark_grey + " • " + fg.light_blue + "Link found in clipboard")
                content = clipboard_content
                checkout_link = re.search("(?P<url>https?://[^\s]+)", content).group("url")
                mode = "clipboard"
          
            print(fg.light_red + f"[ Hyper ] [ {time.strftime('%H:%M:%S', time.localtime())} ] [ {task} ]" + fg.dark_grey + " • " + fg.light_blue + f"Checkoutlink: {checkout_link}")
            start_time = time.time()
         
            if "https://tinyurl.com/" in content:
                f = urllib.request.urlopen(content)
                content = f.geturl()
                print(fg.light_red + f"[ Hyper ] [ {time.strftime('%H:%M:%S', time.localtime())} ] [ {task} ]" + fg.dark_grey + " • " + fg.light_blue + f"Checkoutlink: {content}")
          
            if dash+"password" in content:
                checkout_url_password = input(fg.light_red + f"[ Hyper ] [ {time.strftime('%H:%M:%S', time.localtime())} ] [ {task} ]" + fg.dark_grey + " • " + fg.light_grey + f"Manual checkoutlink detected! input the password: ")
                headers = {
                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36"
                }

                r = s.get(f'{dash}/api/release?password={checkout_url_password}', headers=headers)
             
                if r.status_code == 200:
                    r_text = r.text
                    r_text2 = json.loads(r_text)
                    checkout_url_link = r_text2["id"]
                    password = True
              
                else:
                    print(fg.light_red + f"[ Hyper ] [ {time.strftime('%H:%M:%S', time.localtime())} ] [ {task} ]" + fg.dark_grey + " • " + fg.red + "Invalid password")
         
            elif dash in content:
                split_checkout_link = checkout_link.split('?link=')[1]
                split2_checkout_link = split_checkout_link.split('&')
            
                try:
                    checkout_url_link = split2_checkout_link[0]
                    checkout_url_password = split2_checkout_link[1].split('=')[1]
                    password = True
              
                except:
                    password = False
               
                if checkout_link[len(checkout_link)-3:] == "rd=":
                    checkout_url_password = input(fg.light_red + f"[ Hyper ] [ {time.strftime('%H:%M:%S', time.localtime())} ] [ {task} ]" + fg.dark_grey + " • " + fg.light_grey + "Manual checkoutlink detected! input the password: password=")
                    password = True
                    checkout_url_link = split2_checkout_link[0]
              
                if checkout_link[len(checkout_link)-3:] == "nk=":
                    checkout_url_link = input(fg.light_red + f"[ Hyper ] [ {time.strftime('%H:%M:%S', time.localtime())} ] [ {task} ]" + fg.dark_grey + " • " + fg.light_grey + "Manual checkoutlink detected! input the password: link=")
                    password = False
             
                else:
                    pass
          
            elif "https://hpr.co/" in content:
                split_checkout_link = checkout_link.split('/')[3]
                split2_checkout_link = split_checkout_link.split('?password=')
                checkout_url_link = split2_checkout_link[0]
              
                try:
                    checkout_url_password = split2_checkout_link[1]
                    password = True
                
                    if checkout_url_password == "":
                 
                        if checkout_link[len(checkout_link)-1] == "=":
                            checkout_url_password = input(fg.light_red + f"[ Hyper ] [ {time.strftime('%H:%M:%S', time.localtime())} ] [ {task} ]" + fg.dark_grey + " • " + fg.light_grey + "Manual checkoutlink detected! input the password: ")
                
                        else:
                            pass
               
                except:
                    password = False
            
            header = {
                "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36",
                "content-type": "application/json",
                "hyper-account": hyper_account_id,
            }
                
            if paid == False:
              
                if collect_address == True:
                   
                    if password == True:
                        payload = { 
                            "release": checkout_url_link,
                            "password": checkout_url_password,
                            "billing_details": {
                                "name": firstname + " " + lastname,
                                "email": email,
                                "address": {
                                    "postal_code": zip,
                                    "city": city,
                                    "country": countrycode,
                                    "line1": address1,
                                    "line2": address2,
                                    "state": state
                                },
                                "business_tax": {
                                    "business_tax_id": "",
                                    "business_tax_id_type": ""
                                }
                            },
                            "user": owner,
                            "payment_method": None,
                            "integrations": {}
                        }
                   
                    if password == False:
                        payload = {
                            "release": checkout_url_link,
                            "password": None,
                            "billing_details": {
                                "name": firstname + " " + lastname,
                                "email": email,
                                "address": {
                                    "postcal_code": zip,
                                    "city": city,
                                    "country": countrycode,
                                    "line1": address1,
                                    "line2": address2,
                                    "state": state
                                },
                                "business_tax": {
                                    "business_tax_id": "",
                                    "business_tax_id_type": ""
                                }
                            },
                            "user": owner,
                            "payment_method": None,
                            "integrations": {}
                        }
              
                if collect_address == False:
                   
                    if password == True:
                        payload = {
                            "release":checkout_url_link,
                            "password":checkout_url_password,
                            "billing_details": {
                                "name":firstname + " " + lastname,
                                "email":email,
                                "address":None,
                                "business_tax":{
                                    "business_tax_id":"",
                                    "business_tax_id_type":""
                                    }
                                },
                            "user":owner,
                            "payment_method":None,
                            "integrations":{}
                            }
                 
                    if password == False:
                        payload = {
                            "release":checkout_url_link,
                            "password":None,
                            "billing_details": {
                                "name":firstname + " " + lastname,
                                "email":email,
                                "address":None,
                                "business_tax":{
                                    "business_tax_id":"",
                                    "business_tax_id_type":""
                                    }
                                },
                            "user":owner,
                            "payment_method":None,
                            "integrations":{}
                            }
         
            if paid == True:
             
                if password == True:
                    payload = {
                        "release": checkout_url_link,
                        "password": checkout_url_password,
                        "billing_details": {
                            "name": firstname + " " + lastname,
                            "email": email,
                            "address": {
                                "postal_code": zip,
                                "city": city,
                                "country": countrycode,
                                "line1": address1,
                                "line2": address2,
                                "state": state,
                            },
                            "business_tax": {
                                "business_tax_id": "",
                                "business_tax_id_type": ""
                            }
                        },
                        "user": owner,
                        "payment_method": stripe_id,
                        "integrations": {}
                    }
              
                if password == False:
                    payload = {
                        "release": checkout_url_link,
                        "password": None,
                        "billing_details": {
                            "name": firstname + " " + lastname,
                            "email": email,
                            "address": {
                                "postal_code": zip,
                                "city": city,
                                "country": countrycode,
                                "line1": address1,
                                "line2": address2,
                                "state": state,
                            },
                            "business_tax": {
                                "business_tax_id": "",
                                "business_tax_id_type": ""
                            }
                        },
                        "user": owner,
                        "payment_method": stripe_id,
                        "integrations": {}
                    }
          
            print(fg.light_red + f"[ Hyper ] [ {time.strftime('%H:%M:%S', time.localtime())} ] [ {task} ]" + fg.dark_grey + " • " + fg.rs + "Submitting Information...")
            submitting = s.post(f"{dash}ajax/checkouts", headers=header, json=payload)
          
            if submitting.status_code == 200:
                    submitting_text = submitting.text
                    submitting_text2 = json.loads(submitting_text)
                    submitting_id = submitting_text2["id"]
                    print(fg.light_red + f"[ Hyper ] [ {time.strftime('%H:%M:%S', time.localtime())} ] [ {task} ]" + fg.dark_grey + " • " + fg.light_yellow + "Processing...")
                    header = {
                        "Cookie": "authorization="+hypertoken,
                        "hyper-account": hyper_account_id,
                        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"
                    }
                    checkout = s.get(f"{dash}/ajax/checkouts/{submitting_id}", headers=header)
                    end_time = time.time()
                  
                    while True:
                        header = {
                            "Cookie": "authorization="+hypertoken,
                            "hyper-account": hyper_account_id,
                            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"
                        }
                        checkout = s.get(f"{dash}/ajax/checkouts/{submitting_id}", headers=header)
                      
                        if checkout.status_code == 200:
                            checkout_text = checkout.text
                            checkout_text2 = json.loads(checkout_text)
                            checkout_status = checkout_text2["status"]
                         
                            if checkout_status == "processing":
                                pass
                           
                            if checkout_status == "failed":
                                print(fg.light_red + f"[ Hyper ] [ {time.strftime('%H:%M:%S', time.localtime())} ] [ {task} ]" + fg.dark_grey + " • " + fg.light_red + "Checkout failed -> OOS!")
                                num = 0
                                limit = 1
                                headers = {
                                    "authorization": token
                                }
                                last_message_id = None
                                query_parameters = f'limit={limit}'
                              
                                if last_message_id is not None:
                                    query_parameters += f'&before={last_message_id}'
                               
                                r = requests.get(f'https://discord.com/api/v9/channels/{channel_id}/messages?{query_parameters}', headers=headers)
                                jsonn = json.loads(r.text)
                                
                                for value in jsonn:
                                    
                                        try:
                                            old_content = f"{value['content']}"
                                      
                                        except:
                                            print("Invalid token or no access to the provided channel ID")
                              
                                time.sleep(3)
                                break
                          
                            if checkout_status == "succeeded":
                                print(fg.light_red + f"[ Hyper ] [ {time.strftime('%H:%M:%S', time.localtime())} ] [ {task} ]" + fg.dark_grey + " • " + fg.green + "Checkout Successful, congrats you cooked!")
                                checkout_key = checkout_text2["license"]["key"]
                                checkout_user = checkout_text2["license"]["user"]["discord"]["username"] + "#" + checkout_text2["license"]["user"]["discord"]["discriminator"]
                               
                                if paid == True:
                                    checkout_price = "unknown"
                              
                                if paid == False:
                                    checkout_price = "FREE"
                              
                                data = [f'{checkout_product}', f'{checkout_user}', f'{checkout_key}']
                               
                                with open(f'Data/hyper.csv', 'r+', encoding='UTF8', newline='') as f:
                                    writer = csv.writer(f)
                                    writer.writerow(data)
                              
                                webhook = DiscordWebhook(url=user_webhook, avatar_url="https://media.discordapp.net/attachments/878354931201998859/1059895159959076975/kenki_logo_render.png", username="KenkiTools")
                                embed = DiscordEmbed(title=f'Successfully Smoked Stock', description=f'', color='bc252c', url="https://twitter.com/KenkiTools")
                                embed.set_thumbnail(url="https://media.discordapp.net/attachments/878354931201998859/1059895159959076975/kenki_logo_render.png")
                                embed.set_footer(text=f'@KenkiTools', icon_url=f"https://media.discordapp.net/attachments/878354931201998859/1059895159959076975/kenki_logo_render.png")
                                embed.set_timestamp()
                                try:
                                    embed.add_embed_field(name='Product', value=f'{checkout_product}', inline=False)
                                except:
                                    pass
                                embed.add_embed_field(name='Dashboard', value=f'[Dashboard link]({dash})', inline=True)
                                embed.add_embed_field(name='Checkout Speed', value=f'{end_time-start_time}s', inline=True)
                                embed.add_embed_field(name='Mode', value=f'{mode}', inline=True)
                                embed.add_embed_field(name='Key', value=f'||{checkout_key}||', inline=True)
                                embed.add_embed_field(name='Price', value=f'||{checkout_price}||', inline=True)
                                embed.add_embed_field(name='Profile', value=f'||{checkout_user}||', inline=True)
                                webhook.add_embed(embed)
                                webhook.execute()
                              
                                webhook = DiscordWebhook(url=public_webhook_hyper, avatar_url="https://media.discordapp.net/attachments/878354931201998859/1059895159959076975/kenki_logo_render.png", username="KenkiTools")
                                embed = DiscordEmbed(title=f'Someone Smoked the Stock', description='', color='bc252c')
                                embed.set_thumbnail(url="https://media.discordapp.net/attachments/878354931201998859/1059895159959076975/kenki_logo_render.png")
                                embed.set_footer(text=f'KenkiTools', icon_url="https://media.discordapp.net/attachments/878354931201998859/1059895159959076975/kenki_logo_render.png")
                                embed.set_timestamp()
                                try:
                                    embed.add_embed_field(name='Product', value=f'{checkout_product}', inline=False)
                                except:
                                    pass
                                embed.add_embed_field(name='Dashboard', value=f'[Dashboard link]({dash})', inline=False)
                                embed.add_embed_field(name='Mode', value=f'{mode}', inline=False)
                                webhook.add_embed(embed)
                                webhook.execute()
                               
                                webhook = DiscordWebhook(url=private_webhook_hyper, avatar_url="https://media.discordapp.net/attachments/878354931201998859/1059895159959076975/kenki_logo_render.png", username="KenkiTools")
                                embed = DiscordEmbed(title=f'KenkiTools Hyper Logger', description=f'{key_username} Smoked Stock', color='bc252c')
                                embed.set_footer(text=f'Kenkitools', icon_url="https://media.discordapp.net/attachments/878354931201998859/1059895159959076975/kenki_logo_render.png")
                                embed.set_timestamp()
                                embed.add_embed_field(name='Version', value=f'{current_version}', inline=False)
                                embed.add_embed_field(name='User', value=f'<@{key_user_id}>', inline=False)
                                embed.add_embed_field(name='Profile', value=f'{checkout_user}', inline=True)
                                embed.add_embed_field(name='Dashboard', value=f'{dash}', inline=False)
                                embed.add_embed_field(name='Channel id', value=f'{channel_id}', inline=False)
                                webhook.add_embed(embed)
                                webhook.execute()
                               
                                input("")
                                sys.exit()
                          
                            if checkout_status == "requires_action":
                                print(fg.light_red + f"[ Hyper ] [ {time.strftime('%H:%M:%S', time.localtime())} ] [ {task} ]" + fg.dark_grey + " • " + fg.red + "3ds required")
                                payment_intent_client_secret = checkout_text2["payment_intent_client_secret"]
                                payment_intent_client_secret1 = payment_intent_client_secret.partition("_secret_")[0]
                                header = {
                                    "authority": "api.stripe.com",
                                    "method": "POST",
                                    "path": f"/v1/payment_intents/{payment_intent_client_secret1}/confirm",
                                    "scheme": "https",
                                    "accept": "application/json",
                                    "accept-encoding": "gzip, deflate, br",
                                    "accept-language": "en-GB,en-US;q=0.9,en;q=0.8",
                                    "content-type": "application/x-www-form-urlencoded",
                                    "dnt": "1",
                                    "origin": "https://js.stripe.com",
                                    "referer": "https://js.stripe.com/",
                                    "sec-ch-ua": '"Not?A_Brand";v="8", "Chromium";v="108", "Google Chrome";v="108"',
                                    "sec-ch-ua-mobile": "?0",
                                    "sec-fetch-dest": "empty",
                                    "sec-fetch-mode": "cors",
                                    "sec-fetch-site": "same-site",
                                    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36",
                                }
                                payload = {
                                    "expected_payment_method_type": "card",
                                    "use_stripe_sdk": "true",
                                    "key": "pk_live_51GXa1YLZrAkO7Fk2tcUO7vabkO7sgDamOww2OPYQVFhPZOllT75f7owzIOlP75MMdDXHKoy6wPt40HsuQDObpkHv004T74fAzs",
                                    "_stripe_account": stripe_account,
                                    "client_secret": payment_intent_client_secret
                                }
                                r = s.post(f'https://api.stripe.com/v1/payment_intents/{payment_intent_client_secret1}/confirm', headers=header, data=payload)
                               
                                if r.status_code == 200:
                                    r_text = r.text
                                    r_text2 = json.loads(r_text)
                                    id = r_text2["next_action"]["use_stripe_sdk"]["server_transaction_id"]
                                    asource = r_text2["next_action"]["use_stripe_sdk"]["three_d_secure_2_source"]

                                    theheader = {
                                        "Host": "api.stripe.com",
                                        "accept": "application/json",
                                        "content-type": "application/x-www-form-urlencoded",
                                        "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36",
                                        'Authorization': 'Bearer pk_live_51GXa1YLZrAkO7Fk2tcUO7vabkO7sgDamOww2OPYQVFhPZOllT75f7owzIOlP75MMdDXHKoy6wPt40HsuQDObpkHv004T74fAzs',
                                    }
                                    thedata = {
                                        "source": asource,
                                        "browser": {"fingerprintAttempted":False,"fingerprintData":None,"challengeWindowSize":None,"threeDSCompInd":"Y","browserJavaEnabled":False,"browserJavascriptEnabled":True,"browserLanguage":"en-GB","browserColorDepth":"24","browserScreenHeight":"1080","browserScreenWidth":"1920","browserTZ":"-60","browserUserAgent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"},
                                        "one_click_authn_device_support[hosted]": False,
                                        "one_click_authn_device_support[same_origin_frame]": False,
                                        "one_click_authn_device_support[spc_eligible]": True,
                                        "one_click_authn_device_support[webauthn_eligible]": True,
                                        "one_click_authn_device_support[publickey_credentials_get_allowed]": True,
                                        "key":"pk_live_51GXa1YLZrAkO7Fk2tcUO7vabkO7sgDamOww2OPYQVFhPZOllT75f7owzIOlP75MMdDXHKoy6wPt40HsuQDObpkHv004T74fAzs",
                                        "_stripe_account": stripe_account
                                    }
                                    authenticate = s.post(f"https://api.stripe.com/v1/3ds2/authenticate?source={asource}&browser=%7B%22fingerprintAttempted%22%3Afalse%2C%22fingerprintData%22%3Anull%2C%22challengeWindowSize%22%3Anull%2C%22threeDSCompInd%22%3A%22Y%22%2C%22browserJavaEnabled%22%3Afalse%2C%22browserJavascriptEnabled%22%3Atrue%2C%22browserLanguage%22%3A%22en-GB%22%2C%22browserColorDepth%22%3A%2224%22%2C%22browserScreenHeight%22%3A%221080%22%2C%22browserScreenWidth%22%3A%221920%22%2C%22browserTZ%22%3A%22-60%22%2C%22browserUserAgent%22%3A%22Mozilla%2F5.0+(Macintosh%3B+Intel+Mac+OS+X+10_15_7)+AppleWebKit%2F537.36+(KHTML%2C+like+Gecko)+Chrome%2F108.0.0.0+Safari%2F537.36%22%7D&one_click_authn_device_support[hosted]=false&one_click_authn_device_support[same_origin_frame]=false&one_click_authn_device_support[spc_eligible]=true&one_click_authn_device_support[webauthn_eligible]=true&one_click_authn_device_support[publickey_credentials_get_allowed]=true&key=pk_live_51GXa1YLZrAkO7Fk2tcUO7vabkO7sgDamOww2OPYQVFhPZOllT75f7owzIOlP75MMdDXHKoy6wPt40HsuQDObpkHv004T74fAzs&_stripe_account={stripe_account}", headers=theheader, json=thedata)
                                
                                    if authenticate.status_code == 200:
                                        authenticate_text = authenticate.text
                                        authenticate_text2 = json.loads(authenticate_text)
                                        acctransid = authenticate_text2["ares"]["acsTransID"]
                                        payload = {"name":"WINDOW_ACTIVE"}
                                        header = {
                                            "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36",
                                            "accept": "application/json, text/plain, */*"
                                        }
                                        r = s.post(f'https://acs.revolut.com/activity/browser/{acctransid}', headers=header, json=payload)
                                        s.get(f'https://acs.revolut.com/activity/browser/{acctransid}', headers=header)
                                        payload = {"reason":"AUTHENTICATED"}
                                        r = s.post(f'https://acs.revolut.com/activity/browser/{acctransid}/submit', headers=header, json=payload)
                                        payload = {
                                            "source": asource,
                                            "final_cres": {
                                                "threeDSServerTransID": id,
                                                "transStatus": "Y",
                                                "acsTransID": acctransid,
                                                "messageType": "CRes",
                                                "messageVersion": "2.1.0"
                                                },
                                            "key": "pk_live_51GXa1YLZrAkO7Fk2tcUO7vabkO7sgDamOww2OPYQVFhPZOllT75f7owzIOlP75MMdDXHKoy6wPt40HsuQDObpkHv004T74fAzs",
                                            "_stripe_account": stripe_account
                                        }
                                        repeat = 0
                                      
                                        while True:
                                            repeat += 1
                                            r = s.post(f'https://api.stripe.com/v1/3ds2/challenge_complete', headers=theheader, data=payload)
                                            r_text = r.text
                                            r_text2 = json.loads(r_text)
                                            status = r_text2["state"]
                                         
                                            if status == "succeeded":
                                                break
                                          
                                            if repeat == 15:
                                                break
                                         
                                            else:
                                                continue
                                      
                                        payload = {
                                            "key": "pk_live_51GXa1YLZrAkO7Fk2tcUO7vabkO7sgDamOww2OPYQVFhPZOllT75f7owzIOlP75MMdDXHKoy6wPt40HsuQDObpkHv004T74fAzs",  
                                            "_stripe_account": stripe_account,
                                            "is_stripe_sdk": False,
                                            "client_secret": payment_intent_client_secret
                                        }
                                        header = {}
                                        r = s.get(f'https://api.stripe.com/v1/payment_intents/{payment_intent_client_secret1}?key=pk_live_51GXa1YLZrAkO7Fk2tcUO7vabkO7sgDamOww2OPYQVFhPZOllT75f7owzIOlP75MMdDXHKoy6wPt40HsuQDObpkHv004T74fAzs&_stripe_account={stripe_account}&is_stripe_sdk=false&client_secret={payment_intent_client_secret}', data=payload, headers=header)
                                      
                                        while True:
                                            header = {
                                                "Cookie": "authorization="+hypertoken,
                                                "hyper-account": hyper_account_id,
                                                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"
                                            }
                                            checkout = s.get(f"{dash}/ajax/checkouts/{submitting_id}", headers=header)
                                       
                                            if checkout.status_code == 200:
                                                checkout_text = checkout.text
                                                checkout_text2 = json.loads(checkout_text)
                                                checkout_status = checkout_text2["status"]
                                            
                                                if checkout_status == "processing":
                                                    pass
                                             
                                                if checkout_status == "failed":
                                                    num = 0
                                                    limit = 1
                                                    headers = {
                                                        "authorization": token
                                                    }
                                                    last_message_id = None
                                                    query_parameters = f'limit={limit}'
                                                   
                                                    if last_message_id is not None:
                                                        query_parameters += f'&before={last_message_id}'
                                                   
                                                    r = requests.get(f'https://discord.com/api/v9/channels/{channel_id}/messages?{query_parameters}', headers=headers)
                                                    jsonn = json.loads(r.text)
                                                   
                                                    for value in jsonn:
                                                          
                                                            try:
                                                                old_content = f"{value['content']}"
                                                          
                                                            except:
                                                                print("Invalid token or no access to the provided channel ID")
                                                   
                                                    time.sleep(3)
                                                    break
                                               
                                                if checkout_status == "succeeded":
                                                    print(fg.light_red + f"[ Hyper ] [ {time.strftime('%H:%M:%S', time.localtime())} ]" + fg.dark_grey + " • " + fg.green + "Checkout Successful, congrats you cooked!")
                                                    checkout_key = checkout_text2["license"]["key"]
                                                 
                                                    if paid == True:
                                                        checkout_price = "unknown"
                                                  
                                                    if paid == False:
                                                        checkout_price = "FREE"
                                                  
                                                    checkout_user = checkout_text2["license"]["user"]["discord"]["username"] + "#" + checkout_text2["license"]["user"]["discord"]["discriminator"]
                                                    webhook = DiscordWebhook(url=user_webhook, avatar_url="https://media.discordapp.net/attachments/878354931201998859/1059895159959076975/kenki_logo_render.png", username="KenkiTools")
                                                    embed = DiscordEmbed(title=f'Successfully Smoked Stock', description=f'', color='bc252c', url="https://twitter.com/KenkiTools")
                                                    embed.set_thumbnail(url="https://media.discordapp.net/attachments/878354931201998859/1059895159959076975/kenki_logo_render.png")
                                                    embed.set_footer(text=f'@KenkiTools', icon_url=f"https://media.discordapp.net/attachments/878354931201998859/1059895159959076975/kenki_logo_render.png")
                                                    embed.set_timestamp()
                                                    try:
                                                        embed.add_embed_field(name='Product', value=f'{checkout_product}', inline=False)
                                                    except:
                                                        pass
                                                    embed.add_embed_field(name='Dashboard', value=f'[Dashboard link]({dash})', inline=True)
                                                    embed.add_embed_field(name='Checkout Speed', value=f'{end_time-start_time}s', inline=True)
                                                    embed.add_embed_field(name='Mode', value=f'Bypass - {mode}', inline=True)
                                                    embed.add_embed_field(name='Key', value=f'||{checkout_key}||', inline=True)
                                                    embed.add_embed_field(name='Price', value=f'||{checkout_price}||', inline=True)
                                                    embed.add_embed_field(name='Profile', value=f'||{checkout_user}||', inline=True)
                                                    webhook.add_embed(embed)
                                                    webhook.execute()
                                                   
                                                    webhook = DiscordWebhook(url=public_webhook_hyper, avatar_url="https://media.discordapp.net/attachments/878354931201998859/1059895159959076975/kenki_logo_render.png", username="KenkiTools")
                                                    embed = DiscordEmbed(title=f'Someone Smoked the Stock', description='', color='bc252c')
                                                    embed.set_thumbnail(url="https://media.discordapp.net/attachments/878354931201998859/1059895159959076975/kenki_logo_render.png")
                                                    embed.set_footer(text=f'KenkiTools', icon_url="https://media.discordapp.net/attachments/878354931201998859/1059895159959076975/kenki_logo_render.png")
                                                    embed.set_timestamp()
                                                    try:
                                                        embed.add_embed_field(name='Product', value=f'{checkout_product}', inline=False)
                                                    except:
                                                        pass
                                                    embed.add_embed_field(name='Dashboard', value=f'[Dashboard link]({dash})', inline=False)
                                                    embed.add_embed_field(name='Mode', value=f'Bypass - {mode}', inline=False)
                                                    webhook.add_embed(embed)
                                                    webhook.execute()
                                                   
                                                    webhook = DiscordWebhook(url=private_webhook_hyper, avatar_url="https://media.discordapp.net/attachments/878354931201998859/1059895159959076975/kenki_logo_render.png", username="KenkiTools")
                                                    embed = DiscordEmbed(title=f'KenkiTools Hyper Logger', description=f'{key_username} Smoked Stock', color='bc252c')
                                                    embed.set_footer(text=f'Kenkitools', icon_url="https://media.discordapp.net/attachments/878354931201998859/1059895159959076975/kenki_logo_render.png")
                                                    embed.set_timestamp()
                                                    embed.add_embed_field(name='Version', value=f'{current_version}', inline=False)
                                                    embed.add_embed_field(name='User', value=f'<@{key_user_id}>', inline=False)
                                                    embed.add_embed_field(name='Profile', value=f'{checkout_user}', inline=True)
                                                    embed.add_embed_field(name='Dashboard', value=f'{dash}', inline=False)
                                                    embed.add_embed_field(name='Channel id', value=f'{channel_id}', inline=False)
                                                    webhook.add_embed(embed)
                                                    webhook.execute()
                                                
                                                    input("")
                                                    sys.exit()
                                           
                                                if checkout_status == "requires_action":
                                                    pass
           
            else:
                print(fg.light_red + f"[ Hyper ] [ {time.strftime('%H:%M:%S', time.localtime())} ] [ {task} ]" + fg.dark_grey + " • " + fg.light_red + f"Checkout failed -> OOS / wrong checkoutlink! - {submitting.status_code}")
                                
            num = 0
            limit = 1
            headers = {
                "authorization": token
            }
            last_message_id = None
            query_parameters = f'limit={limit}'
           
            if last_message_id is not None:
                query_parameters += f'&before={last_message_id}'
          
            r = requests.get(f'https://discord.com/api/v9/channels/{channel_id}/messages?{query_parameters}', headers=headers)
            jsonn = json.loads(r.text)
           
            for value in jsonn:
                   
                    try:
                        old_content = f"{value['content']}"
                  
                    except:
                        print(fg.light_red + f"[ Hyper ] [ {time.strftime('%H:%M:%S', time.localtime())} ] [ {task} ]" + fg.dark_grey + " • " + fg.red + f"Token has no access to the provided channel id")
                        input("")
                        sys.exit()