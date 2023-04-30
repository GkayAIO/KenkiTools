import csv, random, names

from data.storage import *

class b4b():

    def load_tasks(self):

        self.profiles = []
        self.tasks = 0

        with open("Generator/Sneaker/Basket4Ballers/input.csv", newline='') as f:
            csv_file = csv.reader(f)
            next(csv_file)

            try:
                for row in csv_file:

                    self.tasks += 1
                    self.profiles.append((row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8]))
                
                print(fg.light_red + f"[ Basket4Ballers ] [ {time.strftime('%H:%M:%S', time.localtime())} ]" + fg.dark_grey + " • " + fg.rs + f"Successfully loaded {self.tasks} tasks!")
            
            except:
                print(fg.light_red + f"[ Basket4Ballers ] [ {time.strftime('%H:%M:%S', time.localtime())} ]" + fg.dark_grey + " • " + fg.red + f"Error scraping profiles")
    
    def load_proxies(self):

        self.total_proxies = 0

        try:
            self.proxies = open('proxy.txt').read().splitlines()

            with open("proxy.txt") as file:
                for line in file:
                    self.total_proxies += 1

            print(fg.light_red + f"[ Basket4Ballers ] [ {time.strftime('%H:%M:%S', time.localtime())} ]" + fg.dark_grey + " • " + fg.rs + f"Successfully loaded {self.total_proxies} proxies!")
        
        except:
            print(fg.light_red + f"[ Basket4Ballers ] [ {time.strftime('%H:%M:%S', time.localtime())} ]" + fg.dark_grey + " • " + fg.red + f"Error loading profiles")

    def solve_captcha(self):

        print(fg.light_red + f"[ Basket4Ballers ] [ {time.strftime('%H:%M:%S', time.localtime())} ]" + fg.dark_grey + " • " + fg.rs + "Solving captcha...")
        try:

            solve_captcha_request = solver.recaptcha(
                sitekey="6LcpBD0UAAAAALwqETJkSSuQZYcavdDKu1sy_XPN",
                url="https://www.basket4ballers.com/en/authentification?back=my-account",
                version="v2",
                action="demo_action",
                score=0.3
            )

            captcha_code = str(solve_captcha_request["code"])
            print(fg.light_red + f"[ Basket4Ballers ] [ {time.strftime('%H:%M:%S', time.localtime())} ]" + fg.dark_grey + " • " + fg.light_blue + "Successfully solved captcha!")
            return captcha_code
        
        except Exception as e:
            print(e)
    
    def generate_account(self):

        print(fg.light_red + f"[ Basket4Ballers ] [ {time.strftime('%H:%M:%S', time.localtime())} ]" + fg.dark_grey + " • " + fg.rs + "Generating account...")
        
        headers = {
            'authority': 'www.basket4ballers.com',
            'method': 'POST',
            'path': '/en/authentification',
            'scheme': 'https',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'de-DE,de;q=0.9,en-US;q=0.8,en;q=0.7',
            'cache-control': 'no-cache',
            'content-type': 'application/x-www-form-urlencoded',
            'dnt': '1',
            'origin': 'https://www.basket4ballers.com',
            'pragma': 'no-cache',
            'referer': 'https://www.basket4ballers.com/en/authentification',
            'sec-ch-ua': '"Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'
        }

        payload = {
            'id_gender': str(random.randint(1,3)),
            'customer_lastname': self.lastname,
            'customer_firstname': self.firstname,
            'email': self.email,
            'passwd': self.password,
            'days': str(random.randint(1,28)),
            'months': str(random.randint(1,12)),
            'years': str(random.randint(1980, 2004)),
            'firstname': self.firstname,
            'lastname': self.lastname,
            'company': '',
            'vat_number': '',
            'address1': self.address,
            'address2': self.address2,
            'postcode': self.postcode,
            'city': self.city,
            'id_country': '1',
            'id_state': '',
            'other': '',
            'phone': self.phonenumber,
            'phone_mobile': self.phonenumber,
            'alias': 'My address',
            'dni': '',
            'new_abo[subscriptions][]': '3',
            'new_abo[subscriptions][]': '5',
            'new_abo[subscriptions][]': '6',
            'new_abo[subscriptions][]': '4',
            'new_abo[id_country]': '8',
            'new_abo[phone]': self.phonenumber,
            'referralprogram': '',
            'g-recaptcha-response': self.solve_captcha(),
            'email_create': '1',
            'is_new_customer': '1',
            'back': 'my-account',
            'submitAccount': ''
        }

        req = self.session.post("https://www.basket4ballers.com/en/authentification", headers=headers, data=payload, proxies=self.proxy)
        if req.status_code == 200:
            print(fg.light_red + f"[ Basket4Ballers ] [ {time.strftime('%H:%M:%S', time.localtime())} ]" + fg.dark_grey + " • " + fg.green + "Successfully generated account")

        else:
            print(fg.light_red + f"[ Basket4Ballers ] [ {time.strftime('%H:%M:%S', time.localtime())} ]" + fg.dark_grey + " • " + fg.red + f"Error generating account -> {req.status_code}")
    
    def __init__(self):

        self.profiles = None
        self.tasks = None
        self.total_proxies = None
        self.proxies = None
        self.successful_tasks = 0

        self.load_tasks()
        self.load_proxies()

        for row in self.profiles:
            
            self.session = requests.Session()
            self.proxy = {"http": f"http://{random.choice(self.proxies)}"}

            self.email = row[0]
            self.password = row[1]
            self.firstname = row[2]
            self.lastname = row[3]
            self.address = row[4]
            self.address2 = row[5]
            self.phonenumber = row[6]
            self.city = row[7]
            self.postcode = row[8]

            if self.firstname.lower() == "random":
                self.firstname = names.get_first_name()
            if self.lastname.lower() == "random":
                self.lastname = names.get_last_name()
            if self.password.lower() == "random":
                self.password = f"!{self.firstname}{self.lastname}{str(random.randint(100,999))}!"
            if "random" in self.email.lower():
                self.email = self.email.split("@")
                self.email = f"{self.firstname}{self.lastname}{str(random.randint(100,999))}@{self.email[1]}"
            
            self.generate_account()
