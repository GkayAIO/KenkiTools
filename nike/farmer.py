import random, zipfile, threading, csv
from discord_webhook import DiscordWebhook, DiscordEmbed
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
import undetected_chromedriver as uc    

from data.storage import *

moves = [Keys.DOWN, Keys.DOWN, Keys.DOWN, Keys.DOWN, Keys.UP]

print_logo()

while True:
    max_threads = int(input(fg.light_red + f"[ Nike ] [ {time.strftime('%H:%M:%S', time.localtime())} ]" + fg.dark_grey + " • " + fg.rs + "Input the amount of threads you want to run: "))
 
    if max_threads >= 6:
        print(fg.light_red + f"[ Nike ] [ {time.strftime('%H:%M:%S', time.localtime())} ]" + fg.dark_grey + " • " + fg.red + "Please only run max 5 threads!")
        continue

    else:
        break

sema = threading.Semaphore(value=max_threads)

def clearcart(email, country_code, driver):
  
    while True:
        print(fg.light_red + f"[ Nike ] [ {time.strftime('%H:%M:%S', time.localtime())} ]" + fg.dark_grey + " • " + fg.rs + "Starting cart function")
        driver.get(f"https://www.nike.com/{country_code}/cart")
     
        try:
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="maincontent"]/div[2]/div[1]/div[1]/h4')))
    
        except TimeoutException:
            print(fg.light_red + f"[ Nike ] [ {time.strftime('%H:%M:%S', time.localtime())} ]" + fg.dark_grey + " • " + fg.red + "Error going to cart page!")
            break
      
        time.sleep(random.randint(2,3))
        print(fg.light_red + f"[ Nike ] [ {time.strftime('%H:%M:%S', time.localtime())} ]" + fg.dark_grey + " • " + fg.rs + "Clearing cart...")
        items_in_cart = 0
    
        while True:
        
            try:
                driver.find_element(By.XPATH,'//*[@id="maincontent"]/div[2]/div[1]/div[1]/div[2]/div/div/div/div[2]/ul/li[3]/button').click()
                items_in_cart += 1
        
            except:
                break
      
        if items_in_cart == 0:
            print(fg.light_red + f"[ Nike ] [ {time.strftime('%H:%M:%S', time.localtime())} ]" + fg.dark_grey + " • " + fg.rs + "No items in cart")
            print(fg.light_red + f"[ Nike ] [ {time.strftime('%H:%M:%S', time.localtime())} ]" + fg.dark_grey + " • " + fg.green + "Successfully finished cart function!")
            break
        
        else:
            print(fg.light_red + f"[ Nike ] [ {time.strftime('%H:%M:%S', time.localtime())} ]" + fg.dark_grey + " • " + fg.rs + f"Successfully removed {items_in_cart} items")
            print(fg.light_red + f"[ Nike ] [ {time.strftime('%H:%M:%S', time.localtime())} ]" + fg.dark_grey + " • " + fg.green + "Successfully finished cart function!")
            break


def snkrs(email, country_code, driver):
   
    while True:
        print(fg.light_red + f"[ Nike ] [ {time.strftime('%H:%M:%S', time.localtime())} ]" + fg.dark_grey + " • " + fg.rs + "Starting snkrs function")
        driver.get(f"https://www.nike.com/{country_code}/launch")
      
        try:
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div/div[1]/div[1]/div/div[1]/div[2]/div/section[1]/figure[1]/div/div/a/img')))
      
        except TimeoutException:
            print(fg.light_red + f"[ Nike ] [ {time.strftime('%H:%M:%S', time.localtime())} ]" + fg.dark_grey + " • " + fg.red + "Error going to news page!")
            break
     
        print(fg.light_red + f"[ Nike ] [ {time.strftime('%H:%M:%S', time.localtime())} ]" + fg.dark_grey + " • " + fg.rs + "Watching livestream...")
        driver.find_element(By.XPATH,'//*[@id="root"]/div/div[1]/div[1]/div/div[1]/div[2]/div/section[1]/figure[1]/div/div/a').click()
        time.sleep(random.randint(90, 110))
        print(fg.light_red + f"[ Nike ] [ {time.strftime('%H:%M:%S', time.localtime())} ]" + fg.dark_grey + " • " + fg.rs + "Leaving livestream")
      
        try:
            driver.find_element(By.XPATH,'//*[@id="root"]/div/a').click()
      
        except:
            driver.back()
     
        time.sleep(random.randint(6,9))
        driver.find_element(By.XPATH,'//*[@id="root"]/div/div[1]/div[1]/div/div[1]/div[1]/header/div/div/div[2]/div/nav/ul/li[3]/a').click()
        print(fg.light_red + f"[ Nike ] [ {time.strftime('%H:%M:%S', time.localtime())} ]" + fg.dark_grey + " • " + fg.rs + "Going to random snkrs product pages")
     
        for i in range(0,random.randint(4,6)):
            time.sleep(random.randint(7,9))
     
            while True:
    
                try:
                    random_6 = random.randint(1,6)
                    driver.find_element(By.XPATH,f'//*[@id="root"]/div/div[1]/div[1]/div/div[1]/div[2]/div/section[1]/figure[{random_6}]/div/div/a').click()
                    print(fg.light_red + f"[ Nike ] [ {time.strftime('%H:%M:%S', time.localtime())} ] [ {email} ]" + fg.dark_grey + " • " + fg.rs + f"Looking at product {random_6}")
                    break
       
                except:
                    pass
         
            time.sleep(random.randint(4,6))
       
            for i in range(0,random.randint(9,14)):
                driver.find_element(By.CSS_SELECTOR,'body').send_keys(random.choice(moves))
                time.sleep(round(random.uniform(0.3, 0.5), 10))
        
            time.sleep(random.randint(4,7))
            driver.back()
      
        break
   
    print(fg.light_red + f"[ Nike ] [ {time.strftime('%H:%M:%S', time.localtime())} ] [ {email} ]" + fg.dark_grey + " • " + fg.green + "Successfully finished snkrs function")

def newsroom(email, country_code, driver):
   
    while True:
        print(fg.light_red + f"[ Nike ] [ {time.strftime('%H:%M:%S', time.localtime())} ] [ {email} ]" + fg.dark_grey + " • " + fg.rs + "Starting newsroom function")
        driver.get("https://about.nike.com/en/newsroom/releases")
    
        try:
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="main"]/section/div[2]/div[1]/ul/li[1]/div')))
   
        except TimeoutException:
            print(fg.light_red + f"[ Nike ] [ {time.strftime('%H:%M:%S', time.localtime())} ] [ {email} ]" + fg.dark_grey + " • " + fg.red + "Error going to newsroom page!")
            break
     
        for i in range(0,random.randint(15,30)):
            driver.find_element(By.CSS_SELECTOR,'body').send_keys(random.choice(moves))
            time.sleep(round(random.uniform(0.3, 0.5), 10))
      
        for i in range(0,random.randint(3,6)):
       
            while True:
         
                try:
                    random_12 = random.randint(1,12)
                    driver.find_element(By.XPATH,f'//*[@id="main"]/section/div[2]/div[1]/ul/li[{random_12}]/div/a').click()
                    print(fg.light_red + f"[ Nike ] [ {time.strftime('%H:%M:%S', time.localtime())} ] [ {email} ]" + fg.dark_grey + " • " + fg.rs + f"Reading release news article {random_12}")
                    break
          
                except:
                    pass
         
            time.sleep(random.randint(4,6))
          
            for i in range(0,random.randint(35,50)):
                driver.find_element(By.CSS_SELECTOR,'body').send_keys(Keys.DOWN)
                time.sleep(round(random.uniform(0.5, 1.5), 10))
          
            time.sleep(random.randint(4,7))
            driver.back()
       
        print(fg.light_red + f"[ Nike ] [ {time.strftime('%H:%M:%S', time.localtime())} ] [ {email} ]" + fg.dark_grey + " • " + fg.green + "Successfully finished newsroom function")
        break

def profile(email, country_code, driver):
    
    while True:
        print(fg.light_red + f"[ Nike ] [ {time.strftime('%H:%M:%S', time.localtime())} ] [ {email} ]" + fg.dark_grey + " • " + fg.rs + "Starting profile function")
        driver.get(f"https://www.nike.com/{country_code}/member/settings")
      
        try:
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="mex-profile-content"]/div/div/div[1]/header/div/div/div/div/div/div[1]/div/a')))
      
        except TimeoutException:
            print(fg.light_red + f"[ Nike ] [ {time.strftime('%H:%M:%S', time.localtime())} ] [ {email} ]" + fg.dark_grey + " • " + fg.red + "Error going to profile page!")
            break
     
        for i in range(0,random.randint(6,9)):
            driver.find_element(By.CSS_SELECTOR,'body').send_keys(random.choice(moves))
            time.sleep(round(random.uniform(0.3, 0.4), 10))
     
        driver.find_element(By.XPATH,'//*[@id="settings"]/div[3]/div[1]/div[7]/div/div[2]/div').click()
        time.sleep(random.randint(4,7))
        driver.find_element(By.XPATH,'//*[@id="settings"]/div[3]/div[1]/div[5]').click()
        break
   
    print(fg.light_red + f"[ Nike ] [ {time.strftime('%H:%M:%S', time.localtime())} ] [ {email} ]" + fg.dark_grey + " • " + fg.green + "Successfully finished profile function")

def farm(email, password, proxy, country_code):
    sema.acquire()
    start_time = time.time()
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
        options.add_argument("--window-size=1300,800")
        options.add_argument('--disable-blink-features=AutomationControlled')
        options.add_argument('--disable-blink-features')
        options.add_argument("--no-zygote")
        options.add_argument("--no-first-run")
        options.add_argument('--disable-features=IsolateOrigins,site-per-process,OptimizationGuideModelDownloading,OptimizationHintsFetching,OptimizationTargetPrediction,OptimizationHints')
        options.add_argument('--flag-switches-begin')
        options.add_argument('--flag-switches-end')
        options.add_argument('--remote-debugging-port=0')
        options.add_argument("--log-level=3")
        options.add_argument('--disable-browser-side-navigation')
        working_dir = os.getcwd()
        proxy_plugin = f'{working_dir}/Chrome/ext'
        options.add_argument(f'--load-extension={proxy_plugin}')
        chrome_profile = f'{working_dir}/Chrome/{email}'
        options.add_argument(f'--user-data-dir={chrome_profile}')
        driver = uc.Chrome(options = options)
        driver.command_executor.set_timeout(15)
      
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
       
        if f"https://www.nike.com/" in driver.current_url:
          
            try: 
                driver.find_element(By.XPATH,'//*[@id="gen-nav-commerce-header-v2"]/div[3]/header/div/div[1]/div[1]/a/svg')
                print(fg.light_red + f"[ Nike ] [ {time.strftime('%H:%M:%S', time.localtime())} ] [ {email} ]" + fg.dark_grey + " • " + fg.green + "Successfully logged in!")
                time.sleep(random.randint(6,11))
                break
         
            except:
                print(fg.light_red + f"[ Nike ] [ {time.strftime('%H:%M:%S', time.localtime())} ] [ {email} ]" + fg.dark_grey + " • " + fg.red + "Error logging in, retrying")
                driver.quit()
                time.sleep(random.randint(5,6))
                continue
    
    try:
        driver.find_element(By.XPATH,'//*[@id="gen-nav-commerce-header-v2"]/div[1]/div/div[2]/div/div[2]/div[2]/button').click()
    
    except:
        pass
    
    time.sleep(random.randint(5,6))
    clearcart(email, country_code, driver)
    time.sleep(random.randint(5,6))
    random_actions = [snkrs, newsroom, snkrs, newsroom]
    random.shuffle(random_actions)
    
    try:
 
        for func in random_actions:
            func(email, country_code, driver)
            time.sleep(random.randint(5,6))
   
    except:
        pass
 
    while True:
        print(fg.light_red + f"[ Nike ] [ {time.strftime('%H:%M:%S', time.localtime())} ] [ {email} ]" + fg.dark_grey + " • " + fg.rs + "Starting profile function")
        driver.get(f"https://www.nike.com/{country_code}/member/settings")
    
        try:
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="mex-profile-content"]/div/div/div[1]/header/div/div/div/div/div/div[1]/div/a')))
 
        except TimeoutException:
            print(fg.light_red + f"[ Nike ] [ {time.strftime('%H:%M:%S', time.localtime())} ] [ {email} ]" + fg.dark_grey + " • " + fg.red + "Error going to profile page!")
            break
 
        for i in range(0,random.randint(6,9)):
            driver.find_element(By.CSS_SELECTOR,'body').send_keys(random.choice(moves))
            time.sleep(round(random.uniform(0.3, 0.4), 10))
    
        driver.find_element(By.XPATH,'//*[@id="settings"]/div[3]/div[1]/div[7]/div/div[2]/div').click()
        time.sleep(random.randint(4,7))
        driver.find_element(By.XPATH,'//*[@id="settings"]/div[3]/div[1]/div[5]').click()
        break
   
    print(fg.light_red + f"[ Nike ] [ {time.strftime('%H:%M:%S', time.localtime())} ] [ {email} ]" + fg.dark_grey + " • " + fg.green + "Successfully finished profile function")
    time.sleep(random.randint(5,6))
    print(fg.light_red + f"[ Nike ] [ {time.strftime('%H:%M:%S', time.localtime())} ] [ {email} ]" + fg.dark_grey + " • " + fg.green + f"Successfully farmed account {email}\n")
    driver.quit()
    end_time = time.time()-start_time
    total_time = time.strftime("%M:%S", time.gmtime(end_time))
   
    with open ("Data/accounts_farmed", "r+") as f:
        data = f.read()
        accounts_generated = int(data.replace('\x00',''))
        accounts_generated += 1
        f.truncate(0)
        f.write(str(accounts_generated))
    
    webhook = DiscordWebhook(url=user_webhook, avatar_url="https://media.discordapp.net/attachments/878354931201998859/1059895159959076975/kenki_logo_render.png", username="KenkiTools")
    embed = DiscordEmbed(title=f'Successfully farmed nike account', description='', color='bc252c')
    embed.set_thumbnail(url="https://media.discordapp.net/attachments/878354931201998859/1068909512339247234/Nike.png")
    embed.set_footer(text=f'@KenkiTools', icon_url=f"https://media.discordapp.net/attachments/878354931201998859/1059895159959076975/kenki_logo_render.png")
    embed.set_timestamp()
    embed.add_embed_field(name='Time', value=f'{total_time} minutes', inline=False)
    embed.add_embed_field(name='Email', value=f'||{email}||', inline=True)
    embed.add_embed_field(name='Password', value=f'||{password}||', inline=True)
    embed.add_embed_field(name='Proxy', value=f'||{proxy}||', inline=False)
    webhook.add_embed(embed)
    webhook.execute()
    
    webhook = DiscordWebhook(url=public_webhook_aio, avatar_url="https://media.discordapp.net/attachments/878354931201998859/1059895159959076975/kenki_logo_render.png", username="KenkiTools")
    embed = DiscordEmbed(title=f'Successfully farmed nike account', description='', color='bc252c')
    embed.set_thumbnail(url="https://media.discordapp.net/attachments/878354931201998859/1068909512339247234/Nike.png")
    embed.set_footer(text=f'KenkiTools', icon_url="https://media.discordapp.net/attachments/878354931201998859/1059895159959076975/kenki_logo_render.png")
    embed.set_timestamp()
    embed.add_embed_field(name='Time', value=f'{total_time} minutes', inline=False)
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

with open('Nike/activity_farmer.csv', newline='') as input_file:
    csv_file = csv.reader(input_file)
    try:
        for row in csv_file:
    
            if row != ["email", "password", "proxy", "countrycode"]:
                task += 1
                thread = threading.Thread(target=farm, args=(row[0], row[1], row[2], row[3], ))
                processlist.append(thread)
                thread.start()
  
    except Exception as e:
        print(fg.light_red + f"[ Nike ] [ {time.strftime('%H:%M:%S', time.localtime())} ]" + fg.dark_grey + " • " + fg.red + f"Error - {e}")

webhook = DiscordWebhook(url=private_webhook_tasks, avatar_url="https://media.discordapp.net/attachments/878354931201998859/1059895159959076975/kenki_logo_render.png", username="KenkiTools")
embed = DiscordEmbed(title=f'KenkiTools Nike Logger', description=f'{key_username} Farming accounts', color="bc252c")
embed.set_footer(text=f"KenkiTools", icon_url="https://media.discordapp.net/attachments/878354931201998859/1059895159959076975/kenki_logo_render.png")
embed.set_timestamp()
embed.add_embed_field(name='Version', value=f'{current_version}', inline=False)
embed.add_embed_field(name='User', value=f'<@{key_user_id}>', inline=False)
embed.add_embed_field(name='Amount of accounts', value=f'{task}', inline=False)
webhook.add_embed(embed)
webhook.execute()