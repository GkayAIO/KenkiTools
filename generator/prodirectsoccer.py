import threading, selenium, names, random, csv
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from discord_webhook import DiscordWebhook, DiscordEmbed

from data.storage import *

Birthday = ['//*[@id="gigya-dropdown-146207948822614900"]/option[2]', '//*[@id="gigya-dropdown-146207948822614900"]/option[3]', '//*[@id="gigya-dropdown-146207948822614900"]/option[4]', '//*[@id="gigya-dropdown-146207948822614900"]/option[5]', '//*[@id="gigya-dropdown-146207948822614900"]/option[6]', '//*[@id="gigya-dropdown-146207948822614900"]/option[7]', '//*[@id="gigya-dropdown-146207948822614900"]/option[8]', '//*[@id="gigya-dropdown-146207948822614900"]/option[9]', '//*[@id="gigya-dropdown-146207948822614900"]/option[10]', '//*[@id="gigya-dropdown-146207948822614900"]/option[11]', '//*[@id="gigya-dropdown-146207948822614900"]/option[12]', '//*[@id="gigya-dropdown-146207948822614900"]/option[13]', '//*[@id="gigya-dropdown-146207948822614900"]/option[14]', '//*[@id="gigya-dropdown-146207948822614900"]/option[15]', '//*[@id="gigya-dropdown-146207948822614900"]/option[16]', '//*[@id="gigya-dropdown-146207948822614900"]/option[17]', '//*[@id="gigya-dropdown-146207948822614900"]/option[18]', '//*[@id="gigya-dropdown-146207948822614900"]/option[19]', '//*[@id="gigya-dropdown-146207948822614900"]/option[20]', '//*[@id="gigya-dropdown-146207948822614900"]/option[21]', '//*[@id="gigya-dropdown-146207948822614900"]/option[22]', '//*[@id="gigya-dropdown-146207948822614900"]/option[23]', '//*[@id="gigya-dropdown-146207948822614900"]/option[24]', '//*[@id="gigya-dropdown-146207948822614900"]/option[25]', '//*[@id="gigya-dropdown-146207948822614900"]/option[26]', '//*[@id="gigya-dropdown-146207948822614900"]/option[27]', '//*[@id="gigya-dropdown-146207948822614900"]/option[28]']
Birthmonth = ['//*[@id="gigya-dropdown-89077813948458720"]/option[2]', '//*[@id="gigya-dropdown-89077813948458720"]/option[3]', '//*[@id="gigya-dropdown-89077813948458720"]/option[4]', '//*[@id="gigya-dropdown-89077813948458720"]/option[5]', '//*[@id="gigya-dropdown-89077813948458720"]/option[6]', '//*[@id="gigya-dropdown-89077813948458720"]/option[7]', '//*[@id="gigya-dropdown-89077813948458720"]/option[8]', '//*[@id="gigya-dropdown-89077813948458720"]/option[9]', '//*[@id="gigya-dropdown-89077813948458720"]/option[10]', '//*[@id="gigya-dropdown-89077813948458720"]/option[11]', '//*[@id="gigya-dropdown-89077813948458720"]/option[12]']
Birthyear = ['//*[@id="gigya-dropdown-59600094459750890"]/option[86]', '//*[@id="gigya-dropdown-59600094459750890"]/option[85]', '//*[@id="gigya-dropdown-59600094459750890"]/option[84]', '//*[@id="gigya-dropdown-59600094459750890"]/option[83]', '//*[@id="gigya-dropdown-59600094459750890"]/option[82]', '//*[@id="gigya-dropdown-59600094459750890"]/option[81]', '//*[@id="gigya-dropdown-59600094459750890"]/option[80]', '//*[@id="gigya-dropdown-59600094459750890"]/option[79]', '//*[@id="gigya-dropdown-59600094459750890"]/option[78]', '//*[@id="gigya-dropdown-59600094459750890"]/option[77]', '//*[@id="gigya-dropdown-59600094459750890"]/option[76]', '//*[@id="gigya-dropdown-59600094459750890"]/option[75]', '//*[@id="gigya-dropdown-59600094459750890"]/option[74]', '//*[@id="gigya-dropdown-59600094459750890"]/option[73]', '//*[@id="gigya-dropdown-59600094459750890"]/option[72]']
Gender = ['//*[@id="gigya-multiChoice-0-13379478539294850"]', '//*[@id="gigya-multiChoice-1-13379478539294850"]', '//*[@id="gigya-multiChoice-2-13379478539294850"]']
successfull = 1

print_logo()
max_threads = int(input(fg.light_red + f"[ Prodirectsoccer ] [ {time.strftime('%H:%M:%S', time.localtime())} ]" + fg.dark_grey + " • " + fg.rs + "Input the amount of threads you want to run: "))
sema = threading.Semaphore(value=max_threads)

def prodirect_generator(email, password,firstname, lastname, proxy, country_code):

    sema.acquire()
    global successfull
    global tasks
    print(fg.light_red + f"[ Prodirectsoccer ] [ {time.strftime('%H:%M:%S', time.localtime())} ] [ {successfull}/{tasks} ]" + fg.dark_grey + " • " + fg.rs + "Loading browser...")
    split_proxie = proxy.split(":")

    while True:
        final_proxie = split_proxie[2]+split_proxie[3]+"@"+split_proxie[0]+split_proxie[1]

        selenium.webdriver.DesiredCapabilities.CHROME['proxy'] = {
            'httpProxy': 'http://'+final_proxie,
            'ftpProxy': 'http://'+final_proxie,
            'sslProxy': 'http://'+final_proxie,
            'proxyType': 'MANUAL',
            }
        
        selenium.webdriver.DesiredCapabilities.CHROME['acceptSslCerts']=True

        options = selenium.webdriver.ChromeOptions()
        options.add_argument('headless')
        options.add_argument('window-size=1920x1080')
        options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36')
        options.add_argument("disable-gpu")
        options.add_argument('--ignore-certificate-errors')
        options.add_argument('--allow-running-insecure-content')
        options.add_experimental_option("excludeSwitches", ["enable-logging"])
        driver = selenium.webdriver.Chrome(options = options)

        if firstname == "RANDOM":
            firstname = f"{names.get_first_name()}"
        if lastname == "RANDOM":
            lastname = f"{names.get_last_name()}"
        if password == "RANDOM":
            password = f"{firstname}{lastname}123!"
        if email.startswith("RANDOM"):
            email = f"{firstname}{lastname}@"+email.split("@")[1]

        print(fg.light_red + f"[ Prodirectsoccer ] [ {time.strftime('%H:%M:%S', time.localtime())} ] [ {successfull}/{tasks} ]" + fg.dark_grey + " • " + fg.rs + "Loading page...")
        while True:

            if country_code == "de" or country_code == "DE":
                driver.get("https://www.prodirectsport.de/")
                
            if country_code == "fr" or country_code == "FR":
                driver.get("https://www.prodirectsport.fr/")

            if country_code == "es" or country_code == "ES":
                driver.get("https://www.prodirectsport.es/")

            if country_code == "it" or country_code == "IT":
                driver.get("https://www.prodirectsport.it/")

            if country_code == "us" or country_code == "US":
                driver.get("https://www.prodirectsport.us/")
                
            else:
                driver.get("https://www.prodirectsoccer.com/")

            try:
                while True:
                    if driver.current_url == "https://www.prodirectsport.com/soccer/":
                        driver.back()
                    element = WebDriverWait(driver, 5).until(
                        EC.presence_of_element_located((By.XPATH, '//*[@id="fancybox-container-1"]/div[2]/div[4]/div/div/button'))
                    )
                    try:
                        element.click()
                    except:
                        pass
                    if driver.current_url == "https://www.prodirectsport.com/soccer/":
                        driver.back()
                        continue
                    else:
                        break

            except:
                pass
            print(fg.light_red + f"[ Prodirectsoccer ] [ {time.strftime('%H:%M:%S', time.localtime())} ] [ {successfull}/{tasks} ]" + fg.dark_grey + " • " + fg.rs + "Getting signup page...")
           
            try:
                login = WebDriverWait(driver, 5).until(
                    EC.presence_of_element_located((By.XPATH, '/html/body/header/section[1]/div/div/div[2]/ul/li/a/span'))
                )
                login.click()
    
            except Exception as e:
                driver.get_screenshot_as_file("screenshot.png")
                print(e)
                print(fg.light_red + f"[ Prodirectsoccer ] [ {time.strftime('%H:%M:%S', time.localtime())} ] [ {successfull}/{tasks} ]" + fg.dark_grey + " • " + fg.red + "Error getting signup page, retrying...")
                continue
      
            try:
                element = WebDriverWait(driver, 1).until(
                    EC.presence_of_element_located((By.XPATH, '/html/body/header/section[1]/div/div/div[2]/ul/li/a'))
                )
                element.click()
  
            except:
                pass
    
            finally:
                time.sleep(random.randint(1,2))
                element = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, '//*[@id="gigya-login-form"]/div[1]/h2[2]/a'))
                )
                element.click()
                
                print(fg.light_red + f"[ Prodirectsoccer ] [ {time.strftime('%H:%M:%S', time.localtime())} ] [ {successfull}/{tasks} ]" + fg.dark_grey + " • " + fg.light_yellow + "Submitting Information...")
                element = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, '//*[@id="gigya-textbox-97893954494816370"]'))
                )
                for character in firstname:
                    element.send_keys(character)
                    time.sleep(round(random.uniform(0.1, 0.15), 10))

                el = driver.find_element(By.XPATH, '//*[@id="gigya-textbox-92372602731225460"]')
                for character in lastname:
                    el.send_keys(character)
                    time.sleep(round(random.uniform(0.1, 0.15), 10))

                el = driver.find_element(By.XPATH, '//*[@id="gigya-register-form"]/div[1]/div[7]/input')
                for character in email:
                    el.send_keys(character)
                    time.sleep(round(random.uniform(0.1, 0.15), 10))
                
                el = driver.find_element(By.XPATH, '//*[@id="gigya-password-116794160066065020"]')
                for character in password:
                    el.send_keys(character)
                    time.sleep(round(random.uniform(0.1, 0.15), 10))
            
                driver.find_element(By.XPATH, '//*[@id="gigya-register-form"]/div[1]/div[9]/input').click()
                print(fg.light_red + f"[ Prodirectsoccer ] [ {time.strftime('%H:%M:%S', time.localtime())} ] [ {successfull}/{tasks} ]" + fg.dark_grey + " • " + fg.light_blue + "Adding additional information...")
                element = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, '//*[@id="gigya-dropdown-146207948822614900"]'))
                )

                element.click()
                driver.find_element(By.XPATH, random.choice(Birthday)).click()
                driver.find_element(By.XPATH, '//*[@id="gigya-dropdown-89077813948458720"]').click()
                driver.find_element(By.XPATH, random.choice(Birthmonth)).click()
                driver.find_element(By.XPATH, '//*[@id="gigya-dropdown-59600094459750890"]').click()
                driver.find_element(By.XPATH, random.choice(Birthyear)).click()
                driver.find_element(By.XPATH, random.choice(Gender)).click()
                
                try:
                    element = WebDriverWait(driver, 5).until(
                        EC.presence_of_element_located((By.XPATH, '//*[@id="gigya-profile-form"]/div[2]/div[5]/input'))
                    )
                    element.click()
                except:
                    pass
                
                driver.quit()
                print(fg.light_red + f"[ Prodirectsoccer ] [ {time.strftime('%H:%M:%S', time.localtime())} ] [ {successfull}/{tasks} ]" + fg.dark_grey + " • " + fg.green + "Successfully generated account!")
                successfull += 1
             
                webhook = DiscordWebhook(url=user_webhook, avatar_url="https://media.discordapp.net/attachments/878354931201998859/1059895159959076975/kenki_logo_render.png", username="KenkiTools")
                embed = DiscordEmbed(title=f'Successfully generated prodirectsoccer account', description='', color='bc252c')
                embed.set_thumbnail(url="https://media.discordapp.net/attachments/878354931201998859/1059895159959076975/kenki_logo_render.png")
                embed.set_footer(text=f'@KenkiTools', icon_url=f"https://media.discordapp.net/attachments/878354931201998859/1059895159959076975/kenki_logo_render.png")
                embed.set_timestamp()
                embed.add_embed_field(name='Region', value=f':flag_{country_code.lower()}:', inline=False)
                embed.add_embed_field(name='Email', value=f'{email}', inline=True)
                embed.add_embed_field(name='Password', value=f'||{password}||', inline=True)
                embed.add_embed_field(name='Name', value=f'{firstname} {lastname}', inline=True)
                embed.add_embed_field(name='Proxy', value=f'||{proxy}||', inline=False)
                webhook.add_embed(embed)
                webhook.execute()
         
                webhook = DiscordWebhook(url=public_webhook_aio, avatar_url="https://media.discordapp.net/attachments/878354931201998859/1059895159959076975/kenki_logo_render.png", username="KenkiTools")
                embed = DiscordEmbed(title=f'Successfully Generated Account', description='', color='bc252c')
                embed.set_thumbnail(url="https://media.discordapp.net/attachments/878354931201998859/1059895159959076975/kenki_logo_render.png")
                embed.set_footer(text=f'KenkiTools', icon_url="https://media.discordapp.net/attachments/878354931201998859/1059895159959076975/kenki_logo_render.png")
                embed.set_timestamp()
                embed.add_embed_field(name='Site', value=f'Prodirectsoccer :flag_{country_code.lower()}:', inline=False)
                if show_name == "true":
                    embed.add_embed_field(name='username', value=f'{key_username}', inline=False)
                else:
                    embed.add_embed_field(name='username', value=f'anonym', inline=False)
                webhook.add_embed(embed)
                webhook.execute()

                sema.release()

            break
        break

print(fg.light_red + f"[ Prodirectsoccer ] [ {time.strftime('%H:%M:%S', time.localtime())} ]" + fg.dark_grey + " • " + fg.rs + "Loading tasks...")

global total_proxies
total_proxies = 0
global proxy
proxy = []

with open("proxy.txt", 'r+') as f:
    proxy_list = f.readlines()
    for line in proxy_list:
        total_proxies += 1
        proxy.append(line.strip())
    f.close()

global processlist
processlist = []
tasks = 0

with open('Generator/Sneaker/Prodirectsoccer/input.csv', newline='') as input_file:

    csv_file = csv.reader(input_file)

    try:
        for row in csv_file:
            if row != ["email", "password", "firstname", "lastname", "countrycode"]:

                tasks += 1
                thread = threading.Thread(target=prodirect_generator, args=(row[0],row[1],row[2],row[3], proxy[tasks], row[4], ))
                processlist.append(thread)
                thread.start()

    except Exception as e:

        print(fg.light_red + f"[ Prodirectsoccer ] [ {time.strftime('%H:%M:%S', time.localtime())} ]" + fg.dark_grey + " • " + fg.red + f"Error - {e}")

webhook = DiscordWebhook(url=private_webhook_tasks, avatar_url="https://media.discordapp.net/attachments/878354931201998859/1059895159959076975/kenki_logo_render.png", username="KenkiTools")
embed = DiscordEmbed(title=f'KenkiTools Prodirectsoccer Logger', description=f'{key_username} generating accounts', color="bc252c")
embed.set_footer(text=f"KenkiTools", icon_url="https://media.discordapp.net/attachments/878354931201998859/1059895159959076975/kenki_logo_render.png")
embed.set_timestamp()
embed.add_embed_field(name='Version', value=f'{current_version}', inline=False)
embed.add_embed_field(name='User', value=f'<@{key_user_id}>', inline=False)
embed.add_embed_field(name='Amount of accounts', value=f'{tasks}', inline=False)
webhook.add_embed(embed)
webhook.execute()