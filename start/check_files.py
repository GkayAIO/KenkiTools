import csv

from data.storage import *

print(fg.light_red + "    _  __             _     _    _____             _")
print(fg.light_red + "   | |/ / ___  _ __  | | _ (_)  |_   _| __   ___  | | ___ ")
print(fg.light_red + "   | ' / / _ \| '_ \ | |/ /| |    | | / _ \ / _ \ | |/ __|")
print(fg.light_red + "   | . \   __/| | | ||   < | |    | || (_) | (_) || |\__ \\")
print(fg.light_red + "   |_|\_\\\\___||_| |_||_|\_\|_|    |_| \___/ \___/ |_||___/\n\n")
print(fg.light_red + f"[ Home ] [ {time.strftime('%H:%M:%S', time.localtime())} ]" + fg.dark_grey + " • " + fg.rs + "Updating files...")

if os.path.exists("config.json") == False:
    config = {
        "License_Key": "KENKI-0000-0000-0000-0000",
        "Webhook": "",
        "show-username": "",
        "Misc": {
            "Catchall": ""
        },
        "Generator": {
            "2Captcha": "",
            "Sms-Activate": ""
        },
        "Raffle": {
            "Geocode_Key": "",
            "Email": "",
            "Password": ""
        },
        "revolut": {
        "business": {
            "monitor-delay": "",
            "solve-delay": ""
        },
        "Personal": {
            "monitor-delay": "",
            "solve-delay": ""
        }
    }
    }
    with open('config.json', 'w') as f:
        json.dump(config, f, indent=4, default=tuple)
        f.close()

if os.path.exists("version.json") == False:
    version = {
        "version": ""
    }
    with open('version.json', 'w') as f:
        json.dump(version, f, indent=4, default=tuple)
        f.close()

if os.path.exists('proxy.txt') == False:
    with open('proxy.txt', 'w') as f:
        f.close()

if os.path.exists('Generator') == False:
    os.makedirs('Generator')

if os.path.exists('Generator/Sneaker') == False:
    os.makedirs('Generator/Sneaker')

if os.path.exists('Generator/Alternative') == False:
    os.makedirs('Generator/Alternative')

if os.path.exists('Generator/Other') == False:
    os.makedirs('Generator/Other')

if os.path.exists('Generator/Sneaker/Asphaltgold') == False:
    os.makedirs('Generator/Sneaker/Asphaltgold')

if os.path.exists('Generator/Sneaker/Asphaltgold/Output') == False:
    os.makedirs('Generator/Sneaker/Asphaltgold/Output')

if os.path.exists('Generator/Sneaker/Asphaltgold/input.csv') == False:
    header = ["email", "password", "firstname", "lastname"]
    with open('Generator/Sneaker/asphaltgold/input.csv', 'w') as f:
        csv.writer(f).writerow(header)
        f.close()

if os.path.exists('Generator/Sneaker/Prodirectsoccer') == False:
    os.makedirs('Generator/Sneaker/Prodirectsoccer')

if os.path.exists('Generator/Sneaker/Prodirectsoccer/Output') == False:
    os.makedirs('Generator/Sneaker/Prodirectsoccer/Output')

if os.path.exists('Generator/Sneaker/Prodirectsoccer/input.csv') == False:
    header = ["email", "password", "firstname", "lastname", "countrycode"]
    with open('Generator/Sneaker/Prodirectsoccer/input.csv', 'w') as f:
        csv.writer(f).writerow(header)
        f.close()

if os.path.exists('Generator/Sneaker/SlamJam') == False:
    os.makedirs('Generator/Sneaker/SlamJam')

if os.path.exists('Generator/Sneaker/SlamJam/Output') == False:
    os.makedirs('Generator/Sneaker/SlamJam/Output')

if os.path.exists('Generator/Sneaker/SlamJam/input.csv') == False:
    header = ["email", "password", "firstname", "lastname"]
    with open('Generator/Sneaker/SlamJam/input.csv', 'w') as f:
        csv.writer(f).writerow(header)
        f.close()

if os.path.exists('Generator/Sneaker/Patta') == False:
    os.makedirs('Generator/Sneaker/Patta')

if os.path.exists('Generator/Sneaker/Patta/Output') == False:
    os.makedirs('Generator/Sneaker/Patta/Output')

if os.path.exists('Generator/Sneaker/Patta/input.csv') == False:
    header = ["email", "password", "firstname", "lastname"]
    with open('Generator/Sneaker/Patta/input.csv', 'w') as f:
        csv.writer(f).writerow(header)
        f.close()

if os.path.exists('Generator/Sneaker/GoodHood') == False:
    os.makedirs('Generator/Sneaker/GoodHood')

if os.path.exists('Generator/Sneaker/GoodHood/Output') == False:
    os.makedirs('Generator/Sneaker/GoodHood/Output')

if os.path.exists('Generator/Sneaker/GoodHood/input.csv') == False:
    header = ["email", "password", "firstname", "lastname"]
    with open('Generator/Sneaker/GoodHood/input.csv', 'w') as f:
        csv.writer(f).writerow(header)
        f.close()

if os.path.exists('Generator/Sneaker/Basket4Ballers') == False:
    os.makedirs('Generator/Sneaker/Basket4Ballers')

if os.path.exists('Generator/Sneaker/Basket4Ballers/Output') == False:
    os.makedirs('Generator/Sneaker/Basket4Ballers/Output')

if os.path.exists('Generator/Sneaker/Basket4Ballers/input.csv') == False:
    header = ["email", "password", "firstname", "lastname", "address1", "address2", "phonenumber", "city", "zipcode"]
    with open('Generator/Sneaker/Basket4Ballers/input.csv', 'w') as f:
        csv.writer(f).writerow(header)
        f.close()

if os.path.exists('Generator/Sneaker/Prodirectsoccer') == False:
    os.makedirs('Generator/Sneaker/Prodirectsoccer')

if os.path.exists('Generator/Sneaker/Prodirectsoccer/Output') == False:
    os.makedirs('Generator/Sneaker/Prodirectsoccer/Output')

if os.path.exists('Generator/Sneaker/Prodirectsoccer/input.csv') == False:
    header = ["countrycode", "email", "password", "firstname", "lastname"]
    with open('Generator/Sneaker/Prodirectsoccer/input.csv', 'w') as f:
        csv.writer(f).writerow(header)
        f.close()

if os.path.exists('Generator/Sneaker/KithEU') == False:
    os.makedirs('Generator/Sneaker/KithEU')

if os.path.exists('Generator/Sneaker/KithEU/Output') == False:
    os.makedirs('Generator/Sneaker/KithEU/Output')

if os.path.exists('Generator/Sneaker/KithEU/input.csv') == False:
    header = ["email", "password", "firstname", "lastname"]
    with open('Generator/Sneaker/KithEU/input.csv', 'w') as f:
        csv.writer(f).writerow(header)
        f.close()

if os.path.exists('Generator/Sneaker/Naked') == False:
    os.makedirs('Generator/Sneaker/Naked')

if os.path.exists('Generator/Sneaker/Naked/Output') == False:
    os.makedirs('Generator/Sneaker/Naked/Output')

if os.path.exists('Generator/Sneaker/Naked/input.csv') == False:
    header = ["email", "password", "firstname"]
    with open('Generator/Sneaker/Naked/input.csv', 'w') as f:
        csv.writer(f).writerow(header)
        f.close()

if os.path.exists('Generator/Sneaker/Snipes') == False:
    os.makedirs('Generator/Sneaker/Snipes')

if os.path.exists('Generator/Sneaker/Snipes/Output') == False:
    os.makedirs('Generator/Sneaker/Snipes/Output')

if os.path.exists('Generator/Sneaker/Snipes/input.csv') == False:
    header = ["email", "password", "firstname", "lastname", "address", "housenumber", "zip", "city", "country code"]
    with open('Generator/Sneaker/Snipes/input.csv', 'w') as f:
        csv.writer(f).writerow(header)
        f.close()

if os.path.exists('Generator/Sneaker/Solebox') == False:
    os.makedirs('Generator/Sneaker/Solebox')

if os.path.exists('Generator/Sneaker/Solebox/Output') == False:
    os.makedirs('Generator/Sneaker/Solebox/Output')

if os.path.exists('Generator/Sneaker/Solebox/input.csv') == False:
    header = ["email", "password", "firstname", "lastname", "address", "housenumber", "zip", "city"]
    with open('Generator/Sneaker/Solebox/input.csv', 'w') as f:
        csv.writer(f).writerow(header)
        f.close()

if os.path.exists('Generator/Sneaker/Sivasdescalzo') == False:
    os.makedirs('Generator/Sneaker/Sivasdescalzo')

if os.path.exists('Generator/Sneaker/Sivasdescalzo/Output') == False:
    os.makedirs('Generator/Sneaker/Sivasdescalzo/Output')

if os.path.exists('Generator/Sneaker/Sivasdescalzo/input.csv') == False:
    header = ["email", "password", "firstname", "lastname"]
    with open('Generator/Sneaker/Sivasdescalzo/input.csv', 'w') as f:
        csv.writer(f).writerow(header)
        f.close()

if os.path.exists('Generator/Other/Three') == False:
    os.makedirs('Generator/Other/Three')

if os.path.exists('Generator/Other/Three/Output') == False:
    os.makedirs('Generator/Other/Three/Output')

if os.path.exists('Generator/Other/Three/input.csv') == False:
    header = ["email", "firstname", "lastname", "postcode", "address", "address2", "city"]
    with open('Generator/Other/Three/input.csv', 'w') as f:
        csv.writer(f).writerow(header)
        f.close()

if os.path.exists('Misc') == False:
    os.makedirs('Misc')

if os.path.exists('Misc/Credentials') == False:
    os.makedirs('Misc/Credentials')

if os.path.exists('Misc/Credentials/Address') == False:
    os.makedirs('Misc/Credentials/Address')

if os.path.exists('Misc/Credentials/Names') == False:
    os.makedirs('Misc/Credentials/Names')

if os.path.exists('Misc/Credentials/Other') == False:
    os.makedirs('Misc/Credentials/Other')

if os.path.exists('Misc/Proxies') == False:
    os.makedirs('Misc/Proxies')

if os.path.exists('Misc/Proxies/Output') == False:
    os.makedirs('Misc/Proxies/Output')

if os.path.exists('Misc/Proxies/Input.txt') == False:
    with open('Misc/Proxies/Input.txt', 'w') as f:
        f.close()

if os.path.exists('Jigger') == False:
    os.makedirs('Jigger')

if os.path.exists('Jigger/Name') == False:
    os.makedirs('Jigger/Name')

if os.path.exists('Jigger/Address') == False:
    os.makedirs('Jigger/Address')

if os.path.exists('Shipping') == False:
    os.makedirs('Shipping')

if os.path.exists('Shipping/Mesh') == False:
    os.makedirs('Shipping/Mesh')

if os.path.exists('Shipping/Mesh/input.csv') == False:
    header = ["store", "country code", "zip code", "ordernumber"]
    with open('Shipping/Mesh/input.csv', 'w') as f:
        csv.writer(f).writerow(header)
        f.close()

if os.path.exists('Shipping/DPD') == False:
    os.makedirs('Shipping/DPD')

if os.path.exists('Shipping/DPD/input.csv') == False:
    header = ["tracking number"]
    with open('Shipping/DPD/input.csv', 'w') as f:
        csv.writer(f).writerow(header)
        f.close()

if os.path.exists('Shipping/DHL') == False:
    os.makedirs('Shipping/DHL')

if os.path.exists('Shipping/DHL/input.csv') == False:
    header = ["tracking number"]
    with open('Shipping/DHL/input.csv', 'w') as f:
        csv.writer(f).writerow(header)
        f.close()
    
if os.path.exists('Shipping/Nike') == False:
    os.makedirs('Shipping/Nike')

if os.path.exists('Shipping/Nike/Output') == False:
    os.makedirs('Shipping/Nike/Output')

if os.path.exists('Shipping/Nike/input.csv') == False:
    header = ["order number", "email", "webhook"]
    with open('Shipping/Nike/input.csv', 'w') as f:
        csv.writer(f).writerow(header)
        f.close()

if os.path.exists('Profile') == False:
    os.makedirs('Profile')

if os.path.exists('Profile/Output') == False:
    os.makedirs('Profile/Output')

if os.path.exists('Profile/profile.csv') == False:
    header = ["profile name", "email", "firstname", "lastname", "address", "address 2", "housenumber", "city", "state", "zip code", "countrycode", "prefix", "phone", "cc", "month/year", "cvv", "cardtype", "name on card"]
    with open('Profile/profile.csv', 'w') as f:
        csv.writer(f).writerow(header)
        f.close()

if os.path.exists('chromedriver.exe') == False:
    NewVersion = requests.get("https://www.dropbox.com/s/n8et233bzwifihq/chromedriver.exe?dl=1")
    open("chromedriver.exe", "wb").write(NewVersion.content)

if os.path.exists('Hyper') == False:
    os.makedirs('Hyper')

if os.path.exists('Hyper/Profiles') == False:
    os.makedirs('Hyper/Profiles')

if os.path.exists('Hyper/Profiles/profile.csv') == False:
    header = ["discord token", "email", "firstname", "lastname", "address", "address2", "zip code", "city", "state", "countrycode", "cc", "cvc", "exp"]
    with open('Hyper/Profiles/profile.csv', 'w') as f:
        csv.writer(f).writerow(header)
        f.close()

if os.path.exists('Nike') == False:
    os.makedirs('Nike')

if os.path.exists('Nike/activity_farmer.csv') == False:
    header = ["email", "password", "proxy", "countrycode"]
    with open('Nike/activity_farmer.csv', 'w') as f:
        csv.writer(f).writerow(header)
        f.close()

if os.path.exists('Nike/account_checker.csv') == False:
    header = ["email", "password", "proxy", "countrycode"]
    with open('Nike/account_checker.csv', 'w') as f:
        csv.writer(f).writerow(header)
        f.close()

if os.path.exists('Nike/password_changer.csv') == False:
    header = ["email", "password", "new password", "proxy", "countrycode"]
    with open('Nike/password_changer.csv', 'w') as f:
        csv.writer(f).writerow(header)
        f.close()

if os.path.exists('Nike/email_changer.csv') == False:
    header = ["email", "new email", "password", "proxy", "countrycode"]
    with open('Nike/email_changer.csv', 'w') as f:
        csv.writer(f).writerow(header)
        f.close()

if os.path.exists('Nike/region_changer.csv') == False:
    header = ["email", "password", "proxy", "countrycode", "new region"]
    with open('Nike/region_changer.csv', 'w') as f:
        csv.writer(f).writerow(header)
        f.close()

if os.path.exists('Data') == False:
    os.makedirs('Data')

if os.path.exists('Data/accounts') == False:
    with open('Data/accounts', 'w') as f:
        f.write("0")
        f.close()

if os.path.exists('Data/revolut') == False:
    with open('Data/revolut', 'w') as f:
        f.write("0")
        f.close()

if os.path.exists('Data/accounts_farmed') == False:
    with open('Data/accounts_farmed', 'w') as f:
        f.write("0")
        f.close()

if os.path.exists('Data/mails') == False:
    with open('Data/mails', 'w') as f:
        f.write("0")
        f.close()

if os.path.exists('Data/wethenew') == False:
    with open('Data/wethenew', 'w') as f:
        f.close()

if os.path.exists('Data/hyper.csv') == False:
    header = ["product","email","key"]
    with open('Data/hyper.csv', 'w') as f:
        csv.writer(f).writerow(header)
        f.close()

if os.path.exists('Chrome') == False:
    os.makedirs('Chrome')

if os.path.exists('Chrome/ext') == False:
    os.makedirs('Chrome/ext')

if os.path.exists('revolut') == False:
    os.makedirs('revolut')

if os.path.exists('revolut/business') == False:
    os.makedirs('revolut/business')

if os.path.exists('revolut/business/selfies') == False:
    os.makedirs('revolut/business/selfies')

if os.path.exists('revolut/business/revolut_accounts.csv') == False:
    header = ["email","passcode","selfie image","nickname"]
    with open('revolut/business/revolut_accounts.csv', 'w') as f:
        csv.writer(f).writerow(header)
        f.close()

if os.path.exists('revolut/business/revolut_sessions.csv') == False:
    header = ["access token","refresh token","device id","employee id","user id","email","profile","timer","merchant"]
    with open('revolut/business/revolut_sessions.csv', 'w') as f:
        csv.writer(f).writerow(header)
        f.close()

if os.path.exists('revolut/personal') == False:
    os.makedirs('revolut/personal')

if os.path.exists('revolut/personal/selfies') == False:
    os.makedirs('revolut/personal/selfies')

if os.path.exists('revolut/Personal/revolut_accounts.csv') == False:
    header = ["email", "passcode", "selfie image", "phonenumber", "nickname"]
    with open('revolut/Personal/revolut_accounts.csv', 'w') as f:
        csv.writer(f).writerow(header)
        f.close()

if os.path.exists('revolut/Personal/revolut_sessions.csv') == False:
    header = ["access token","refresh token","device id","employee id","user id","email","profile","timer","merchant"]
    with open('revolut/Personal/revolut_sessions.csv', 'w') as f:
        csv.writer(f).writerow(header)
        f.close()

print(fg.light_red + f"[ Home ] [ {time.strftime('%H:%M:%S', time.localtime())} ]" + fg.dark_grey + " • " + fg.green + "successfully updated all files\n")