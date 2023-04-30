import threading, csv, random, zipfile
from discord_webhook import DiscordWebhook, DiscordEmbed
import undetected_chromedriver as uc
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait

from data.storage import *

print_logo()
max_threads = int(input(fg.light_red + f"[ Nike ] [ {time.strftime('%H:%M:%S', time.localtime())} ]" + fg.dark_grey + " • " + fg.rs + "Input the amount of threads you want to run: "))
sema = threading.Semaphore(value=max_threads)

def change_password(email, password, proxy, country_code, new_password):

    sema.acquire()
    print(fg.light_red + f"[ Nike ] [ {time.strftime('%H:%M:%S', time.localtime())} ] [ {email} ]" + fg.dark_grey + " • " + fg.rs + f"Starting with account: {email}")
    split_proxie = proxy.split(":")
 
    manifest_json = """
    {
        "version":"1.0.0",
        "manifest_version":2,
        "name":"KenkiTools",
        "permissions":[
            "proxy",
            "tabs",
            "unlimitedStorage",
            "storage",
            "<all_urls>",
            "webRequest",
            "webRequestBlocking"],
            "content_scripts":[
                {
                    "js":["content.js"],
                    "matches":["<all_urls>"]}],
                    "background":{"scripts":["background.js"]},
                    "minimum_chrome_version":"22.0.0"
                    }
    """
   
    background_js = """
    var config = {
        mode: 'fixed_servers',
                rules:
                {
                    singleProxy:
                    {
                        scheme: 'http',
                        host: '%s',
                        port: parseInt(%s)
                    },
                    bypassList: ['localhost']
                }
            };
            chrome.proxy.settings.set({
                value: config,
                scope: 'regular'
            }, function() { });

            function callbackFn(details)
            {
                return {
                    authCredentials:
                    {
                        username: '%s',
                        password: '%s'
                    }
                };
            }
            chrome.webRequest.onAuthRequired.addListener(
                callbackFn,
                {urls: ["<all_urls>"]},
                ['blocking']
    );
    """ % (split_proxie[0], split_proxie[1], split_proxie[2], split_proxie[3])
   
    pluginfile = 'Chrome/ext/proxy_auth_plugin.zip'
  
    with zipfile.ZipFile(pluginfile, 'w') as zp:
        zp.writestr("manifest.json", manifest_json)
        zp.writestr("background.js", background_js)
        zp.writestr("content.js", "")
 
    with zipfile.ZipFile("Chrome/ext/proxy_auth_plugin.zip", 'r') as zip_ref:
        zip_ref.extractall("Chrome/ext")
  
    while True:

        options = uc.ChromeOptions()
        options.add_argument('--disable-popup-blocking')
        options.add_argument('--no-sandbox')
        options.add_argument("--window-size=1300,1600")
        options.add_argument('--disable-blink-features=AutomationControlled')
        options.add_argument('--disable-blink-features')
        options.add_argument("--no-zygote")
        options.add_argument("--no-first-run")
        options.add_argument('--disable-features=IsolateOrigins,site-per-process,OptimizationGuideModelDownloading,OptimizationHintsFetching,OptimizationTargetPrediction,OptimizationHints')
        options.add_argument('--flag-switches-begin')
        options.add_argument('--flag-switches-end')
        options.add_argument('--remote-debugging-port=0')
        options.add_argument("--log-level=3")
        working_dir = os.getcwd()
        proxy_plugin = f'{working_dir}/Chrome/ext'
        options.add_argument(f'--load-extension={proxy_plugin}')
        chrome_profile = f'{working_dir}/Chrome/{email}'
        options.add_argument(f'--user-data-dir={chrome_profile}')
        driver = uc.Chrome(options = options)
       
        print(fg.light_red + f"[ Nike ] [ {time.strftime('%H:%M:%S', time.localtime())} ] [ {email} ]" + fg.dark_grey + " • " + fg.rs + "Loading page...")
        windows_before  = driver.current_window_handle
        driver.execute_script('''window.open("https://accounts.nike.com/error","_blank");''')
        time.sleep(random.randint(6,9))
        driver.switch_to.window(windows_before)
        driver.get("https://www.nike.com/login")
        print(fg.light_red + f"[ Nike ] [ {time.strftime('%H:%M:%S', time.localtime())} ] [ {email} ]" + fg.dark_grey + " • " + fg.light_yellow + "Logging in...")
        time.sleep(random.randint(7,13))
       
        try:
            email_input = driver.find_element(By.XPATH,'//*[@id="username"]')
      
        except:
            print(fg.light_red + f"[ Nike ] [ {time.strftime('%H:%M:%S', time.localtime())} ] [ {email} ]" + fg.dark_grey + " • " + fg.green + "Found session!")
            break
      
        for character in email:
            email_input.send_keys(character)
            time.sleep(round(random.uniform(0.1, 0.35), 10))
      
        time.sleep(round(random.uniform(0.5, 1.0), 10))
        driver.find_element(By.XPATH,'//*[@id="root"]/div/div/div/div/form/div/div[4]/button').click()
        time.sleep(random.randint(9,13))
       
        try:
            password_input = driver.find_element(By.XPATH,'//*[@id="password"]')
       
            for character in password:
                password_input.send_keys(character)
                time.sleep(round(random.uniform(0.1, 0.35), 10))
       
            time.sleep(round(random.uniform(0.5, 1.0), 10))
            driver.find_element(By.XPATH,'//*[@id="root"]/div/div/div/div[2]/form/div/div[2]/button').click()
            time.sleep(10)
      
        except:
            print(fg.light_red + f"[ Nike ] [ {time.strftime('%H:%M:%S', time.localtime())} ] [ {email} ]" + fg.dark_grey + " • " + fg.red + "Error logging in, retrying")
            driver.quit()
            time.sleep(random.randint(5,6))
            continue
        
        if "https://www.nike.com/" in driver.current_url:
            print(fg.light_red + f"[ Nike ] [ {time.strftime('%H:%M:%S', time.localtime())} ] [ {email} ]" + fg.dark_grey + " • " + fg.green + "Successfully logged in!")
            time.sleep(random.randint(6,11))
            break
   
    try:
        driver.find_element(By.XPATH,'//*[@id="gen-nav-commerce-header-v2"]/div[1]/div/div[2]/div/div[2]/div[2]/button').click()
  
    except:
        pass
   
    time.sleep(random.randint(1,2))
    print(fg.light_red + f"[ Nike ] [ {time.strftime('%H:%M:%S', time.localtime())} ] [ {email} ]" + fg.dark_grey + " • " + fg.rs + "Changing account country...")
   
    while True:
        driver.get(f"https://www.nike.com/{country_code}/member/settings")
    
        try:
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="settings"]/div[3]/div[2]/div/div/form/div[2]/div[4]/div/div/div/div[1]/span')))
  
        except TimeoutException:
            print(fg.light_red + f"[ Nike ] [ {time.strftime('%H:%M:%S', time.localtime())} ] [ {email} ]" + fg.dark_grey + " • " + fg.red + "Error going to settings page!")
            continue
    
        try:
            driver.find_element(By.XPATH, '//*[@id="gen-nav-commerce-header-v2"]/div[1]/div/div[2]/div/div[3]/div[1]/div[1]/button').click()
    
        except:
            pass
     
        try:
            driver.find_element(By.XPATH,'//*[@id="gen-nav-commerce-header-v2"]/div[1]/div/div[2]/div/div[2]/div[2]/button').click()
   
        except:
            pass
   
        driver.find_element(By.XPATH,'//*[@id="settings"]/div[3]/div[2]/div/div/form/div[2]/div[3]/div/div/div/div/button').click()
        time.sleep(0.5)
        old_password_input = driver.find_element(By.XPATH,'//*[@id="oldPassword"]')
      
        for character in password:
            old_password_input.send_keys(character)
            time.sleep(round(random.uniform(0.1, 0.35), 10))
     
        time.sleep(0.5)
        old_password_input = driver.find_element(By.XPATH,'//*[@id="newPassword"]')
      
        for character in new_password:
            old_password_input.send_keys(character)
            time.sleep(round(random.uniform(0.1, 0.35), 10))
      
        time.sleep(0.5)
        old_password_input = driver.find_element(By.XPATH,'//*[@id="confirmPassword"]')
       
        for character in new_password:
            old_password_input.send_keys(character)
            time.sleep(round(random.uniform(0.1, 0.35), 10))
     
        time.sleep(0.8)
     
        for i in range(0,8):
            driver.find_element(By.CSS_SELECTOR,'body').send_keys(Keys.DOWN)
            time.sleep(round(random.uniform(0.5, 1.5), 10))
   
        driver.find_element(By.XPATH,'//*[@id="modal-root"]/div/div/div/div/div/section/div[2]/div/button').click()
        time.sleep(1)
        break
   
    print(fg.light_red + f"[ Nike ] [ {time.strftime('%H:%M:%S', time.localtime())} ] [ {email} ]" + fg.dark_grey + " • " + fg.green + "Successfully changed password of account!")
    driver.quit()
    webhook = DiscordWebhook(url=user_webhook, avatar_url="https://media.discordapp.net/attachments/878354931201998859/1059895159959076975/kenki_logo_render.png", username="KenkiTools")
    embed = DiscordEmbed(title=f'Successfully changed account password', description='', color='bc252c')
    embed.set_thumbnail(url="https://media.discordapp.net/attachments/878354931201998859/1068909512339247234/Nike.png")
    embed.set_footer(text=f'@KenkiTools', icon_url=f"https://media.discordapp.net/attachments/878354931201998859/1059895159959076975/kenki_logo_render.png")
    embed.set_timestamp()
    embed.add_embed_field(name='Email', value=f'||{email}||', inline=True)
    embed.add_embed_field(name='Old Password', value=f'||{password}||', inline=True)
    embed.add_embed_field(name='New Password', value=f'||{new_password}||', inline=True)
    embed.add_embed_field(name='Proxy', value=f'||{proxy}||', inline=False)
    webhook.add_embed(embed)
    webhook.execute()
  
    webhook = DiscordWebhook(url=public_webhook_aio, avatar_url="https://media.discordapp.net/attachments/878354931201998859/1059895159959076975/kenki_logo_render.png", username="KenkiTools")
    embed = DiscordEmbed(title=f'Successfully changed account password', description='', color='bc252c')
    embed.set_thumbnail(url="https://media.discordapp.net/attachments/878354931201998859/1068909512339247234/Nike.png")
    embed.set_footer(text=f'KenkiTools', icon_url="https://media.discordapp.net/attachments/878354931201998859/1059895159959076975/kenki_logo_render.png")
    embed.set_timestamp()
    if show_name == "true":
        embed.add_embed_field(name='username', value=f'{key_username}', inline=False)
    else:
        embed.add_embed_field(name='username', value=f'anonym', inline=False)
    webhook.add_embed(embed)
    webhook.execute()
   
    sema.release()

print(fg.light_red + f"[ Nike ] [ {time.strftime('%H:%M:%S', time.localtime())} ]" + fg.dark_grey + " • " + fg.rs + "Loading accounts...")
global task
task = 0
global processlist
processlist = []

with open('Nike/password_changer.csv', newline='') as input_file:
    csv_file = csv.reader(input_file)
    try:
        for row in csv_file:
       
            if row != ["email", "password", "new password", "proxy", "countrycode"]:
                task += 1
                thread = threading.Thread(target=change_password, args=(row[0], row[1], row[3], row[4], row[2], ))
                processlist.append(thread)
                thread.start()
   
    except Exception as e:
        print(fg.light_red + f"[ Nike ] [ {time.strftime('%H:%M:%S', time.localtime())} ]" + fg.dark_grey + " • " + fg.red + f"Error - {e}")

webhook = DiscordWebhook(url=private_webhook_tasks, avatar_url="https://media.discordapp.net/attachments/878354931201998859/1059895159959076975/kenki_logo_render.png", username="KenkiTools")
embed = DiscordEmbed(title=f'KenkiTools Nike Logger', description=f'{key_username} changing account password', color="bc252c")
embed.set_footer(text=f"KenkiTools", icon_url="https://media.discordapp.net/attachments/878354931201998859/1059895159959076975/kenki_logo_render.png")
embed.set_timestamp()
embed.add_embed_field(name='Version', value=f'{current_version}', inline=False)
embed.add_embed_field(name='User', value=f'<@{key_user_id}>', inline=False)
embed.add_embed_field(name='Amount of accounts', value=f'{task}', inline=False)
webhook.add_embed(embed)
webhook.execute()