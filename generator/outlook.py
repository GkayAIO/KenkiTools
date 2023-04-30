import re, json, time, random, names, threading, requests, datetime, tls_client
from discord_webhook import DiscordWebhook, DiscordEmbed
from execjs import compile

from data.storage import *

thr_am = 1

class Funcaptcha:

    def getKey(proxy) -> str:
        key = ""
        print(fg.light_red + f"[ Outlook ] [ {time.strftime('%H:%M:%S', time.localtime())} ]" + fg.dark_grey + " • " + fg.rs + "Solving captcha...")
        proxy_selected = random.choice(proxy)
        payload = json.dumps({
        "clientKey": Funcaptcha.key,
        "task": {
            "type"            : "FunCaptchaTask",
            "websitePublicKey": "B7D8911C-5CC8-A9A3-35B0-554ACEE604DA",
            "websiteURL"      : "https://signup.live.com/API/CreateAccount?lcid=1033&wa=wsignin1.0&rpsnv=13&ct=1667394016&rver=7.0.6737.0&wp=MBI_SSL&wreply=https%3a%2f%2foutlook.live.com%2fowa%2f%3fnlp%3d1%26signup%3d1%26RpsCsrfState%3d7f6d4048-5351-f65f-8b93-409ba7e7e4e4&id=292841&CBCXT=out&lw=1&fl=dob%2cflname%2cwld&cobrandid=90015&lic=1&uaid=93bc3e1fb03c42568561df0711c6d450",
            "funcaptchaApiJSSubdomain": "https://client-api.arkoselabs.com",
            "proxy": proxy_selected
        }
        }
        )
        req = requests.post("https://api.capsolver.com/createTask", data = payload)
        status = ""
        while status == "" or status == "processing":
            time.sleep(0.3)
            task = requests.post("https://api.capsolver.com/getTaskResult", json = {
                "clientKey" : Funcaptcha.key,
                "taskId"    : req.json()["taskId"]
            })
            status = task.json()["status"]
            if task.json()["status"] == "ready":
                return task.json()["solution"]["token"]
            
class Crypto:
    script = compile(open("enc.js").read())

    def encrypt(password: str, randomNum: str, Key: str) -> str:

        return Crypto.script.call(
            "encrypt", password, randomNum, Key)


class generateOutlook():

    def __init__(self, proxy) -> None:
        print(fg.light_red + f"[ Outlook ] [ {time.strftime('%H:%M:%S', time.localtime())} ]" + fg.dark_grey + " • " + fg.rs + "Loading task...")
        self.client = tls_client.Session(client_identifier='chrome_108')
        proxy_split = proxy.split(":")
        proxy = f"{proxy_split[2]}:{proxy_split[3]}@{proxy_split[0]}:{proxy_split[1]}"
        self.client.proxies = {'http' : f'http://{proxy}','https': f'http://{proxy}'} if proxy else None

        self.Key = None
        self.randomNum = None
        self.SKI = None
        self.uaid = None
        self.tcxt = None
        self.apiCanary = None
        self.encAttemptToken = ""
        self.dfpRequestId = ""

        global captcha_solved_status
        captcha_solved_status = False
        
        self.siteKey = "B7D8911C-5CC8-A9A3-35B0-554ACEE604DA"
        self.userAgent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36"

        self.__start__ = self.init_client()
        self.account_info = self.account_info()

        self.cipher = Crypto.encrypt(self.account_info['password'], self.randomNum, self.Key)
    
    def account_info(self) -> dict:
        string_upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        string_lower = "abcdefghijklmnopqrstuvwxyz"
        string_other = "!?"
        first_name = names.get_first_name()
        last_name = names.get_last_name()
        email = f"{first_name}{last_name}{str(random.randint(100,999))}@outlook.com".lower()
        password = f"!{random.choice(string_upper)}{random.choice(string_lower)}{random.choice(string_other)}{random.choice(string_lower)}{random.choice(string_lower)}{random.choice(string_lower)}{random.choice(string_lower)}{random.choice(string_other)}{random.choice(string_lower)}{random.choice(string_lower)}{random.choice(string_lower)}{random.choice(string_other)}{random.choice(string_upper)}!"

        return {
            "password": password,
            "CheckAvailStateMap": [
                f"{email}:undefined"
            ],
            "MemberName": email,
            "FirstName": first_name,
            "LastName": last_name,
            "BirthDate": f"{random.randint(1, 27)}:0{random.randint(1, 9)}:{random.randint(1969, 2000)}"
        }

    def payload_b(self, captcha_s: bool) -> dict:
        payload = {
            **self.account_info,
            "RequestTimeStamp"          : str(datetime.now()).replace(" ", "T")[:-3] + "Z",
            "EvictionWarningShown"      : [],
            "UpgradeFlowToken"          : {},
            "MemberNameChangeCount"     : 1,
            "MemberNameAvailableCount"  : 1,
            "MemberNameUnavailableCount": 0,
            "CipherValue"               : self.cipher,
            "SKI"                       : self.SKI,
            "Country"                   : "CA",
            "AltEmail"                  : None,
            "IsOptOutEmailDefault"      : True,
            "IsOptOutEmailShown"        : True,
            "IsOptOutEmail"             : True,
            "LW"                        : True,
            "SiteId"                    : 68692,
            "IsRDM"                     : 0,
            "WReply"                    : None,
            "ReturnUrl"                 : None,
            "SignupReturnUrl"           : None,
            "uiflvr"                    : 1001,
            "uaid"                      : self.uaid,
            "SuggestedAccountType"      : "OUTLOOK",
            "SuggestionType"            : "Locked",
            "encAttemptToken"           : self.encAttemptToken,
            "dfpRequestId"              : self.dfpRequestId,
            "scid"                      : 100118,
            "hpgid"                     : 201040,
        }

        if captcha_s:
            global captcha_solved_status
            if captcha_solved_status == True:
                return payload
            cap_token = Funcaptcha.getKey(proxies)
            print(fg.light_red + f"[ Outlook ] [ {time.strftime('%H:%M:%S', time.localtime())} ]" + fg.dark_grey + " • " + fg.light_blue + "Successfully solved captcha")

            payload.update({
                "HType" : "enforcement",
                "HSol"  : cap_token,
                "HPId"  : self.siteKey,
            })
            captcha_solved_status = True
        
        return payload

    def init_cl(self):
        headers = {
            "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
            "accept-encoding": "gzip, deflate, br",
            "connection": "keep-alive",
            "user-agent": self.userAgent
        }
        print(fg.light_red + f"[ Outlook ] [ {time.strftime('%H:%M:%S', time.localtime())} ]" + fg.dark_grey + " • " + fg.rs + "Getting page...")
        req = self.client.get('https://signup.live.com/signup?lic=1', headers=headers).text

        self.Key , self.randomNum, self.SKI = re.findall(r'Key="(.*?)"; var randomNum="(.*?)"; var SKI="(.*?)"', req)[0]
        json_data = json.loads(re.findall(r't0=([\s\S]*)w\["\$Config"]=', req)[0].replace(';', ''))

        self.uaid = json_data['clientTelemetry']['uaid']
        self.tcxt = json_data['clientTelemetry']['tcxt']
        self.apiCanary = json_data['apiCanary']
    
    def register_acc(self, captcha_solved: bool = False) -> (dict and str):
        print(fg.light_red + f"[ Outlook ] [ {time.strftime('%H:%M:%S', time.localtime())} ]" + fg.dark_grey + " • " + fg.light_yellow + "Generating account...")

        try:
            try:
                response = self.client.post('https://signup.live.com/API/CreateAccount?lic=1', json=self.base_payload(captcha_solved), headers=self.base_headers())

            except Exception as e:
                print(fg.light_red + f"[ Outlook ] [ {time.strftime('%H:%M:%S', time.localtime())} ]" + fg.dark_grey + " • " + fg.red + f"Error generating account -> {e}")
                self.register_account(True)
            
            error = response.json().get("error")
            if error:
                code = error.get("code")
                if '1041' in code:
                    print(fg.light_red + f"[ Outlook ] [ {time.strftime('%H:%M:%S', time.localtime())} ]" + fg.dark_grey + " • " + fg.red + "Error generating account, retrying...")
                    error_data = json.loads(error.get("data"))

                    self.encAttemptToken = error_data['encAttemptToken']
                    self.dfpRequestId = error_data['dfpRequestId']

                    return self.register_account(True)
                
                else:
                    return None, error
            else:
                print(fg.light_red + f"[ Outlook ] [ {time.strftime('%H:%M:%S', time.localtime())} ]" + fg.dark_grey + " • " + fg.green + "Successfully generated account!")
                return self.account_info, 'Success'
                
        except Exception as e:
            return None, str(e)
    
def loop(proxies: list):
    while True:
        outl = generateOutlook(random.choice(proxies))
        account, status = outl.register_acc()

        if status == 'Success':
            webhook = DiscordWebhook(url=public_webhook_aio, avatar_url="https://media.discordapp.net/attachments/878354931201998859/1059895159959076975/kenki_logo_render.png", username="KenkiTools")
            embed = DiscordEmbed(title=f'Successfully generated Outlook', description='', color='bc252c')
            embed.set_thumbnail(url="https://upload.wikimedia.org/wikipedia/commons/thumb/d/df/Microsoft_Office_Outlook_%282018%E2%80%93present%29.svg/1101px-Microsoft_Office_Outlook_%282018%E2%80%93present%29.svg.png")
            embed.set_footer(text=f"KenkiTools", icon_url="https://media.discordapp.net/attachments/878354931201998859/1059895159959076975/kenki_logo_render.png")
            embed.set_timestamp()
            if show_name == "true":
                embed.add_embed_field(name='username', value=f'{key_username}', inline=False)
            else:
                embed.add_embed_field(name='username', value=f'anonym', inline=False)
            webhook.add_embed(embed)
            webhook.execute()
            print(f"{account['MemberName']}")
            print(f"{account['password']}")
            input("")
        else:
            print("error")
            print(status)
            input("")

proxies = open('proxy.txt').read().splitlines()

for i in range(thr_am):
    th = threading.Thread(target = loop, args= (proxies,))
    th.start()