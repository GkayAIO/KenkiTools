import random, csv, names
from discord_webhook import DiscordWebhook, DiscordEmbed

from data.storage import *

class sbx():

    def load_csv(self):

        self.profiles = []
        self.tasks = 0

        with open("Generator/Sneaker/Solebox/input.csv", newline='') as f:
            csv_file = csv.reader(f)
            next(csv_file)

            try:
                for row in csv_file:
                    self.tasks += 1
                    self.profiles.append((row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8]))
                print(fg.light_red + f"[ Solebox ] [ {time.strftime('%H:%M:%S', time.localtime())} ]" + fg.dark_grey + " • " + fg.rs + f"Successfully loaded {self.tasks} tasks!")
            
            except:
                print(fg.light_red + f"[ Solebox ] [ {time.strftime('%H:%M:%S', time.localtime())} ]" + fg.dark_grey + " • " + fg.red + f"Error scraping profiles")
  
    def load_proxies(self):

        self.total_proxies = 0
        try:
            self.proxies = open('proxy.txt').read().splitlines()
           
            with open("proxy.txt") as file:
                for line in file:
                    self.total_proxies += 1
            print(fg.light_red + f"[ Solebox ] [ {time.strftime('%H:%M:%S', time.localtime())} ]" + fg.dark_grey + " • " + fg.rs + f"Successfully loaded {self.total_proxies} proxies!")
     
        except:
            print(fg.light_red + f"[ Solebox ] [ {time.strftime('%H:%M:%S', time.localtime())} ]" + fg.dark_grey + " • " + fg.red + f"Error loading profiles")
    
    def generate_account(self):

        print(fg.light_red + f"[ Solebox ] [ {time.strftime('%H:%M:%S', time.localtime())} ] [ {self.successful_tasks}/{self.tasks} ]" + fg.dark_grey + " • " + fg.rs + "Loading page...")
      
        payload = {
            "rurl": "1"
        }
     
        headers = {
            "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"
        }
  
        req = self.session.get(f"https://www.solebox.com/{self.country_prefix}/registration", headers=headers, params=payload, proxies=self.proxy)
      
        try:
            csrf_token = re.findall('name="csrf_token" value="(.*?)"', str(req.text))[0]
            register_token1 = re.findall('<span data-id="(.*?)" data-value', str(req.text))[0]
            register_token2 =re.findall('" data-value="(.*?)"></span>', str(req.text))[0]
    
        except:
            print(fg.light_red + f"[ Solebox ] [ {time.strftime('%H:%M:%S', time.localtime())} ] [ {self.successful_tasks}/{self.tasks} ]" + fg.dark_grey + " • " + fg.red + "Error fetching token -> check proxies!")
            return -1
 
        print(fg.light_red + f"[ Solebox ] [ {time.strftime('%H:%M:%S', time.localtime())} ] [ {self.successful_tasks}/{self.tasks} ]" + fg.light_yellow + " • " + fg.rs + "Submitting information...")
    
        payload = {
            register_token1: register_token2,
            "dwfrm_profile_register_title": random.choice(["Herr", "Frau"]),
            "dwfrm_profile_register_firstName": self.firstname,
            "dwfrm_profile_register_lastName": self.lastname,
            "dwfrm_profile_register_email": self.email,
            "dwfrm_profile_register_emailConfirm": self.email,
            "dwfrm_profile_register_password": self.password,
            "dwfrm_profile_register_passwordConfirm": self.password,
            "dwfrm_profile_register_phone":  "",
            "dwfrm_profile_register_birthday": "",
            "dwfrm_profile_register_acceptPolicy": "true",
            "csrf_token": csrf_token
        }
        req = self.session.post(f"https://www.solebox.com/on/demandware.store/Sites-solebox-Site/{self.country_prefix}/Account-SubmitRegistration?rurl=1&format=ajax", data=payload, headers=headers, proxies=self.proxy)
    
        if req.status_code == 200:
            print(fg.light_red + f"[ Solebox ] [ {time.strftime('%H:%M:%S', time.localtime())} ] [ {self.successful_tasks}/{self.tasks} ]" + fg.dark_grey + " • " + fg.green + "Successfully generated account!")
            data = [f'{self.email}', f'{self.password}', f'{self.firstname}', f'{self.lastname}']
          
            with open(f'Generator/Sneaker/Solebox/Output/accounts.csv', 'a+', encoding='UTF8', newline='') as f:
                writer = csv.writer(f)
                writer.writerow(data)
        
            with open ("Data/accounts", "r+") as f:
                data = f.read()
                accounts_generated = int(data.replace('\x00',''))
                accounts_generated += 1
                f.truncate(0)
                f.write(str(accounts_generated))
          
            webhook = DiscordWebhook(url=user_webhook, avatar_url="https://media.discordapp.net/attachments/878354931201998859/1059895159959076975/kenki_logo_render.png", username="KenkiTools")
            embed = DiscordEmbed(title=f'Successfully Generated Account', description='', color='bc252c')
            embed.set_thumbnail(url="https://media.discordapp.net/attachments/878354931201998859/1068966966125138051/Solebox.png")
            embed.set_footer(text=f'@KenkiTools', icon_url=f"https://media.discordapp.net/attachments/878354931201998859/1059895159959076975/kenki_logo_render.png")
            embed.set_timestamp()
            embed.add_embed_field(name='Site', value='Solebox', inline=False)
            embed.add_embed_field(name='Name', value=f'{self.firstname} {self.lastname}', inline=False)
            embed.add_embed_field(name='Email', value=f'||{self.email}||', inline=True)
            embed.add_embed_field(name='Password', value=f'||{self.password}||', inline=True)
            embed.add_embed_field(name='Proxy', value=f'||{self.proxy}||', inline=False)
            webhook.add_embed(embed)
            webhook.execute()
       
            webhook = DiscordWebhook(url=private_webhook_tasks, avatar_url="https://media.discordapp.net/attachments/878354931201998859/1059895159959076975/kenki_logo_render.png", username="KenkiTools")
            embed = DiscordEmbed(title=f'Successfully Generated Solebox Account', description='', color='bc252c')
            embed.set_thumbnail(url="https://media.discordapp.net/attachments/878354931201998859/1068966966125138051/Solebox.png")
            embed.set_footer(text=f'KenkiTools', icon_url="https://media.discordapp.net/attachments/878354931201998859/1059895159959076975/kenki_logo_render.png")
            embed.set_timestamp()
            if show_name == "true":
                embed.add_embed_field(name='username', value=f'{key_username}', inline=False)
            else:
                embed.add_embed_field(name='username', value=f'anonym', inline=False)
            webhook.add_embed(embed)
            webhook.execute()

            return True
        
        else:
            print(fg.light_red + f"[ Solebox ] [ {time.strftime('%H:%M:%S', time.localtime())} ] [ {self.successful_tasks}/{self.tasks} ]" + fg.dark_grey + " • " + fg.red + f"Error generating account! -> {req.status_code}")
            print(req.text)
            return False
    
    def add_address(self):
        
        print(fg.light_red + f"[ Solebox ] [ {time.strftime('%H:%M:%S', time.localtime())} ] [ {self.successful_tasks}/{self.tasks} ]" + fg.dark_grey + " • " + fg.light_yellow + f"Adding paypal as payment method...")
        headers = {
            "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"
        }
        req = self.session.get(f"https://www.solebox.com/on/demandware.store/Sites-solebox-Site/{self.country_prefix}/Account-ShowPaymentMethods", headers=headers, proxies=self.proxy)
       
        try:
            csrf_token = re.findall('"csrf_token" value="(.*?)"', str(req.text))[0]
    
        except:
            print(fg.light_red + f"[ Solebox ] [ {time.strftime('%H:%M:%S', time.localtime())} ] [ {self.successful_tasks}/{self.tasks} ]" + fg.dark_grey + " • " + fg.red + f"Error getting csrf token -> {req.status_code}")
            return False
  
        params = {
            "format": "ajax"
        }
        payload = {
            "dwfrm_accountPaymentMethods_paymentMethod": "Paypal",
            "csrf_token": csrf_token
        }
        req = self.session.post(f"https://www.solebox.com/on/demandware.store/Sites-solebox-Site/{self.country_prefix}/Account-SubmitPaymenMethod?format=ajax", headers=headers, data=payload, params=params, proxies=self.proxy)
     
        if req.status_code == 200:
            print(fg.light_red + f"[ Solebox ] [ {time.strftime('%H:%M:%S', time.localtime())} ] [ {self.successful_tasks}/{self.tasks} ]" + fg.dark_grey + " • " + fg.green + "Successfully added paypal as standart payment method!")
            print(fg.light_red + f"[ Solebox ] [ {time.strftime('%H:%M:%S', time.localtime())} ] [ {self.successful_tasks}/{self.tasks} ]" + fg.dark_grey + " • " + fg.rs + "Adding address...")
            req = self.session.get(f"https://www.solebox.com/on/demandware.store/Sites-solebox-Site/{self.country_prefix}/Address-AddAddress?format=ajax", headers=headers, params=params, proxies=self.proxy)
     
            if req.status_code == 200:
                try:
                    csrf_token = re.findall('data-csrf-token="(.*?)"', str(req.text))[0]
        
                except:
                    print(fg.light_red + f"[ Solebox ] [ {time.strftime('%H:%M:%S', time.localtime())} ] [ {self.successful_tasks}/{self.tasks} ]" + fg.dark_grey + " • " + fg.red + f"Error getting csrf token -> {req.status_code}")
                    return -1
            
                headers = {
                    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36",
                    "x-requested-with": "XMLHttpRequest",
                    "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
                    "accept": "application/json, text/javascript, */*; q=0.01"
                }
                payload = {
                    "street": self.address,
                    "houseNo": self.housenumber,
                    "postalCode": self.zip_code,
                    "city": self.city,
                    "country": "DE",
                    "csrf_token": csrf_token
                }
                req = self.session.post(f"https://www.solebox.com/on/demandware.store/Sites-solebox-Site/{self.country_prefix}/CheckoutAddressServices-Validate?format=ajax", headers=headers, params=params, data=payload, proxies=self.proxy)
          
                try:
                    valid = re.findall('"valid": (.*?),', str(req.text))[0]
           
                except:
                    return -1
            
                if valid == "true":
                    params = {
                        "methodid": "home-delivery",
                        "format": "ajax"
                    }
                    payload = {
                        "dwfrm_address_title": random.choice(["Herr", "Frau"]),
                        "dwfrm_address_firstName": self.firstname,
                        "dwfrm_address_lastName": self.lastname,
                        "dwfrm_address_postalCode": self.zip_code,
                        "dwfrm_address_city": self.city,
                        "dwfrm_address_street": self.address,
                        "dwfrm_address_suite": self.housenumber,
                        "dwfrm_address_address1": "",
                        "dwfrm_address_address2": "",
                        "dwfrm_address_phone": "",
                        "dwfrm_address_countryCode": "DE",
                        "dwfrm_address_carrier": "dhl",
                        "csrf_token": csrf_token
                    }
                    req = self.session.post(f"https://www.solebox.com/on/demandware.store/Sites-solebox-Site/{self.country_prefix}/Address-SaveAddress", headers=headers, data=payload, params=params, proxies=self.proxy)
                
                    if '"success": true' in str(req.text):
                        print(fg.light_red + f"[ Solebox ] [ {time.strftime('%H:%M:%S', time.localtime())} ] [ {self.successful_tasks}/{self.tasks} ]" + fg.dark_grey + " • " + fg.green + "Successfully set address!")
                        return True
                
                    else:
                        print(fg.light_red + f"[ Solebox ] [ {time.strftime('%H:%M:%S', time.localtime())} ] [ {self.successful_tasks}/{self.tasks} ]" + fg.dark_grey + " • " + fg.red + f"Error setting address -> {req.status_code}")
                        return False
         
                else:
                    print(fg.light_red + f"[ Solebox ] [ {time.strftime('%H:%M:%S', time.localtime())} ] [ {self.successful_tasks}/{self.tasks} ]" + fg.dark_grey + " • " + fg.red + f"Error setting address -> {valid}")
                    return False
       
            else:
                print(fg.light_red + f"[ Solebox ] [ {time.strftime('%H:%M:%S', time.localtime())} ] [ {self.successful_tasks}/{self.tasks} ]" + fg.dark_grey + " • " + fg.red + f"Error setting address -> {req.status_code}")
                return False
                        
    def __init__(self):

        self.profiles = None
        self.tasks = None
        self.total_proxies = None
        self.proxies = None
        self.successful_tasks = 0
        self.load_csv()
        self.load_proxies()

        while True:
            add_address_input = input(fg.light_red + f"[ Solebox ] [ {time.strftime('%H:%M:%S', time.localtime())} ]" + fg.dark_grey + " • " + fg.rs + "Do you want to add a address (y/n): ")
         
            if add_address_input.lower() == "y":
                add_address_input = True
                break
        
            if add_address_input.lower() == "n":
                add_address_input = False
                break
         
            else:
                continue
    
        for row in self.profiles:
            
            self.session = requests.Session()
            self.proxy = {"http": f"http://{random.choice(self.proxies)}"}
            self.email = row[0]
            self.password = row[1]
            self.firstname = row[2]
            self.lastname = row[3]
            self.country = row[8]

            if self.firstname.lower() == "random":
                self.firstname = names.get_first_name()
         
            if self.lastname.lower() == "random":
                self.lastname = names.get_last_name()
         
            if self.password.lower() == "random":
                self.password = f"!{self.firstname}{self.lastname}{str(random.randint(100,999))}!"
         
            if "random" in self.email.lower():
                self.email = self.email.split("@")
                self.email = f"{self.firstname}{self.lastname}{str(random.randint(100,999))}@{self.email[1]}"
        
            self.country_prefix = f"{self.country.lower()}_{self.country.upper()}"
         
            if self.generate_account():
            
                if add_address_input == True:
                    self.address = row[4]
                    self.housenumber = row[5]
                    self.zip_code = row[6]
                    self.city = row[7]

                    if self.add_address():
                        self.successful_tasks += 1
                        
                else:
                    self.successful_tasks += 1