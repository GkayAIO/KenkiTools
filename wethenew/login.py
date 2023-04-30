import tls_client, fake_useragent

from data.storage import *

ua = fake_useragent.UserAgent()

def wethenew_login(session):
    agent = ua.random
    print(fg.light_red + f"[ Wethenew ] [ {time.strftime('%H:%M:%S', time.localtime())} ]" + fg.dark_grey + " • " + fg.rs + "Checking token...")
    
    while True:
        
        with open("data/wethenew", "r") as f:
            wethenew_token = f.read()
            f.close()
   
        if wethenew_token == "":
            email = input(fg.light_red + f"[ Wethenew ] [ {time.strftime('%H:%M:%S', time.localtime())} ]" + fg.dark_grey + " • " + fg.rs + "Input your email: ")
            password = input(fg.light_red + f"[ Wethenew ] [ {time.strftime('%H:%M:%S', time.localtime())} ]" + fg.dark_grey + " • " + fg.rs + "Input your password: ")
            print(fg.light_red + f"[ Wethenew ] [ {time.strftime('%H:%M:%S', time.localtime())} ]" + fg.dark_grey + " • " + fg.rs + "No token found, solving captcha...")
      
            try:
                result = solver.recaptcha(
                    sitekey='6LeJBSAdAAAAACyoWxmCY7q5G-_6GnKBdpF4raee',
                    url='https://sell.wethenew.com/login',
                    version='v2',
                    action='demo_action',
                    score=0.3
                )
                print(fg.light_red + f"[ Wethenew ] [ {time.strftime('%H:%M:%S', time.localtime())} ]" + fg.dark_grey + " • " + fg.rs + "Successfully solved captcha, logging in...")
            except:
                print(fg.light_red + f"[ Wethenew ] [ {time.strftime('%H:%M:%S', time.localtime())} ]" + fg.dark_grey + " • " + fg.red + "Error solving captcha")
       
            r = session.get("https://sell.wethenew.com/api/auth/csrf")
            json_data = json.loads(r.text)
            csrf_token = json_data["csrfToken"]
            payload = {
                "redirect": "false",
                "email": email,
                "password": password,
                "recaptchaToken": str(result["code"]),
                "pushToken": "undefined",
                "os": "undefined",
                "osVersion": "undefined",
                "csrfToken": csrf_token,
                "callbackUrl": "https://sell.wethenew.com/login",
                "json": "true"
            }
            header = {
                "content-type": "application/json",
                "user-agent": agent
            }
            r_login1 = session.post('https://sell.wethenew.com/api/auth/callback/credentials?', headers=header, json=payload)
          
            header = {
                "user-agent": agent
            }
            r_login2 = session.get("https://sell.wethenew.com/api/auth/session", headers=header).json()
          
            try:
                wethenew_token = r_login2["user"]["accessToken"]
         
            except:
                print(fg.light_red + f"[ Wethenew ] [ {time.strftime('%H:%M:%S', time.localtime())} ]" + fg.dark_grey + " • " + fg.red + "Error getting token")
                continue
        
            if wethenew_token == "":
                print(fg.light_red + f"[ Wethenew ] [ {time.strftime('%H:%M:%S', time.localtime())} ]" + fg.dark_grey + " • " + fg.red + "Error getting token")
        
            if wethenew_token != "":
                with open("data/wethenew", "r+") as f:
                    f.write(wethenew_token)
                    f.close()
                print(fg.light_red + f"[ Wethenew ] [ {time.strftime('%H:%M:%S', time.localtime())} ]" + fg.dark_grey + " • " + fg.green + "Successfully got token")
                break
   
        else:
            print(fg.light_red + f"[ Wethenew ] [ {time.strftime('%H:%M:%S', time.localtime())} ]" + fg.dark_grey + " • " + fg.rs + "Found saved wethenew token, checking if token is valid...")
            header = {
                "authorization": f"Bearer {wethenew_token}",
                "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36", 
                "x-xss-protection": "0"
            }
            payload = {
                "skip": "0",
                "take": "10"
            }
            check_login_request = session.get("https://api-sell.wethenew.com/offers", headers=header, params=payload)
         
            if check_login_request.status_code == 200:
                print(fg.light_red + f"[ Wethenew ] [ {time.strftime('%H:%M:%S', time.localtime())} ]" + fg.dark_grey + " • " + fg.green + "Token is valid")
                break
         
            elif check_login_request.status_code == 429:
                print(check_login_request.text)
                print(fg.light_red + f"[ Wethenew ] [ {time.strftime('%H:%M:%S', time.localtime())} ]" + fg.dark_grey + " • " + fg.red + "Rate limited, retrying after 60 seconds")
                time.sleep(60)
         
            else:
                print(fg.light_red + f"[ Wethenew ] [ {time.strftime('%H:%M:%S', time.localtime())} ]" + fg.dark_grey + " • " + fg.red + "Invalid token, refreshing the token...")
            
                with open("data/wethenew", "r+") as f:
                    f.truncate(0)
                    f.close()
            

wethenew_login(tls_client.Session(client_identifier="chrome_108"))
