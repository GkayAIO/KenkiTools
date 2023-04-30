import pypresence, os, datetime, random

os.system("title KenkiTools")

from data.colors import *
from start.check_files import *
from data.storage import *
from start.authentication import *
from start.autoupdater import *

try:
    RPC = pypresence.Presence("")
    RPC.connect()
    RPC.update(
        large_image = "kenki2",
        details = f"{key_username[:-5]} - v{current_version}",
        state = "Browsing...",
        start = start,
    )
except:
    pass

while True:
    try:

        clear_console()
        os.system(f"title {key_username[:-5]}'s KenkiTools[{current_version}] • main menu")

        print(fg.light_red + "    _  __             _     _    _____             _")
        print(fg.light_red + "   | |/ / ___  _ __  | | _ (_)  |_   _| __   ___  | | ___ ")
        print(fg.light_red + "   | ' / / _ \| '_ \ | |/ /| |    | | / _ \ / _ \ | |/ __|")
        print(fg.light_red + "   | . \   __/| | | ||   < | |    | || (_) | (_) || |\__ \\")
        print(fg.light_red + "   |_|\_\\\\___||_| |_||_|\_\|_|    |_| \___/ \___/ |_||___/\n\n")
        print(fg.light_red + "   Welcome " + fg.rs + f"{key_username}" + fg.light_red + " !")
        print(fg.light_red + "   You are on version " + fg.rs + f"{current_version}" + fg.light_red + "\n\n")

        print(fg.rs + f"   {fg.light_red}[1]{fg.rs}  Misc               {fg.light_red}[2]{fg.rs}  Generator          {fg.light_red}[3]{fg.rs}  J1gger")
        print(fg.rs + f"   {fg.light_red}[4]{fg.rs}  Wethenew           {fg.light_red}[5]{fg.rs}  Profile            {fg.light_red}[6]{fg.rs}  Shipping")
        print(fg.rs + f"   {fg.light_red}[7]{fg.rs}  Nike               {fg.light_red}[8]{fg.rs}  Hyper              {fg.light_red}[9]{fg.rs}  Revolut\n\n")
        print(fg.rs + f"   {fg.light_red}[10]{fg.rs} Settings           {fg.light_red}[11]{fg.rs} Statistics")
        print(fg.light_red + f"\n   ["+fg.dark_red+"X"+fg.light_red+f"] {fg.rs} Exit\n")
        
        Main_Module = input(fg.light_red + "   Select a Module: "+fg.rs)
        clear_console()

        if Main_Module == "1":

            os.system(f"title {key_username[:-5]}'s KenkiTools[{current_version}] • misc menu")
            
            try:
                user_webhook = config["Webhook"]
            except:
                print(fg.light_red + f'  [ menu ] [ {(datetime.time(datetime.now()))} ]' + fg.dark_grey + " • " + fg.light_blue + "Error getting webhook")
            
            print_logo()
            print(fg.rs + f"   {fg.light_red}[1]{fg.rs}  Names              {fg.light_red}[2]{fg.rs}  Catchall           {fg.light_red}[3]{fg.rs}  Password")
            print(fg.rs + f"   {fg.light_red}[4]{fg.rs}  Phonenumber        {fg.light_red}[5]{fg.rs}  Address            {fg.light_red}[6]{fg.rs}  Instagram")
            print(fg.rs + f"   {fg.light_red}[7]{fg.rs}  Spoofer            {fg.light_red}[8]{fg.rs}  Proxies")
            print(fg.light_red + f"\n   ["+fg.dark_red+"X"+fg.light_red+f"] {fg.rs} Exit")
            
            while True:
                try:
                    Mix_Module = input(fg.light_red + "\n   Select a Module: "+fg.rs)
                    break
                except:
                    pass
            clear_console()

            if Mix_Module == "x" or Mix_Module == "X":
                continue

            if Mix_Module == "1":

                try:
                    RPC.update(
                        large_image = "kenki2",
                        details = f"{key_username[:-5]} - v{current_version}",
                        state = f"Generating Credentials",
                        start = start,
                    )
                except:
                    pass

                from misc.credentials import nameGenerator
                nameGenerator()
                continue

            if Mix_Module == "2":

                try:
                    RPC.update(
                        large_image = "kenki2",
                        details = f"{key_username[:-5]} - v{current_version}",
                        state = f"Generating Credentials",
                        start = start,
                    )
                except:
                    pass

                from misc.credentials import catchallGenerator
                catchallGenerator()
                continue

            if Mix_Module == "3":

                try:
                    RPC.update(
                        large_image = "kenki2",
                        details = f"{key_username[:-5]} - v{current_version}",
                        state = f"Generating Credentials",
                        start = start,
                    )
                except:
                    pass

                from misc.credentials import passwordGenerator
                passwordGenerator()
                continue

            if Mix_Module == "4":

                try:
                    RPC.update(
                        large_image = "kenki2",
                        details = f"{key_username[:-5]} - v{current_version}",
                        state = f"Generating Credentials",
                        start = start,
                    )
                except:
                    pass

                from misc.credentials import phonenumberGenerator
                phonenumberGenerator()
                continue

            if Mix_Module == "8":

                try:
                    RPC.update(
                        large_image = "kenki2",
                        details = f"{key_username[:-5]} - v{current_version}",
                        state = f"Managing Proxies",
                        start = start,
                    )
                except:
                    pass

                print_logo()
                print(fg.rs + f"   {fg.light_red}[1]{fg.rs}  Proxy tester       {fg.light_red}[2]{fg.rs}  Proxy Shuffler")
                print(fg.light_red + f"\n   ["+fg.dark_red+"X"+fg.light_red+f"] {fg.rs} Exit")

                while True:
                    try:
                        Proxy_Module = input(fg.light_red + "\n   Select a Module: "+fg.rs)
                        break
                    except:
                        pass
                clear_console()

                if Proxy_Module == "x" or Proxy_Module == "X":
                    time.sleep(0.8)
                    continue

                if Proxy_Module == "1":
                    print(fg.light_red + f'\n  [ menu ] [ {(datetime.time(datetime.now()))} ]' + fg.dark_grey + " • " + fg.red + "Module currently locked")
                    time.sleep(5)
                    continue

                if Proxy_Module == "2":
                    from misc.proxies import shuffleProxies
                    shuffleProxies()
                    continue

                else:
                    print(fg.light_red + f'  [ menu ] [ {(datetime.time(datetime.now()))} ]' + fg.dark_grey + " • " + fg.red + "Wrong input")
                    time.sleep(4)
                    continue
            else:
                print(fg.light_red + f'  [ menu ] [ {(datetime.time(datetime.now()))} ]' + fg.dark_grey + " • " + fg.red + "Module does not exist")
                time.sleep(3)
                continue

        if Main_Module == "2":

            os.system(f"title {key_username[:-5]}'s KenkiTools[{current_version}] • generator menu")
            try:
                RPC.update(
                    large_image = "kenki2",
                    details = f"{key_username[:-5]} - v{current_version}",
                    state = f"Generating Accounts",
                    start = start,
                )
            except:
                pass

            print_logo()
            print(fg.rs + f"   {fg.light_red}[1]{fg.rs}  Sneaker            {fg.light_red}[2]{fg.rs}  Alternativ         {fg.light_red}[3]{fg.rs}  Other")
            print(fg.light_red + f"\n   ["+fg.dark_red+"X"+fg.light_red+f"] {fg.rs} Exit\n")
            
            while True:
                try:
                    Generator_Module = input(fg.light_red + "   Select a Module: "+fg.rs)
                    break
                except:
                    pass

            if Generator_Module == "x" or Generator_Module == "X":
                clear_console()
                continue

            if Generator_Module == "1":

                clear_console()
                print_logo()
                print(fg.rs + f"   {fg.light_red}[01]{fg.rs}  Basket4Ballers     {fg.light_red}[02]{fg.rs}  Snipes             {fg.light_red}[03]{fg.rs}  Solebox")
                print(fg.rs + f"   {fg.light_red}[04]{fg.rs}  Prodirectsoccer")
                print(fg.light_red + f"\n   ["+fg.dark_red+"X"+fg.light_red+f"] {fg.rs} Exit\n")

                while True:
                    try:
                        Sneaker_Module = input(fg.light_red + "   Select a Module: "+fg.rs)
                        break
                    except:
                        pass
                clear_console()

                if Sneaker_Module == "x" or Sneaker_Module == "X":
                    clear_console()
                    continue
                if Sneaker_Module == "1":
                    from generator.basket4ballers import b4b
                    b4b()
                    continue

                if Sneaker_Module == "2":
                    from generator.snipes import snps
                    snps()
                    continue

                if Sneaker_Module == "3":
                    from generator.solebox import sbx
                    sbx()
                    continue

                if Sneaker_Module == "4":
                    import generator.prodirectsoccer
                    continue

                else:
                    print(fg.light_red + f'  [ menu ] [ {(datetime.time(datetime.now()))} ]' + fg.dark_grey + " • " + fg.red + "Wrong input")
                    time.sleep(4)
                    continue

            if Generator_Module == "2":

                clear_console()
                print_logo()
                print(fg.light_red + f'  [ menu ] [ {(datetime.time(datetime.now()))} ]' + fg.dark_grey + " • " + fg.light_blue + "Module currently locked")
                time.sleep(4)
                clear_console()
                continue

            if Generator_Module == "3":

                clear_console()
                print_logo()
                print(fg.rs + f"   {fg.light_red}[01]{fg.rs}  Vinted Views       {fg.light_red}[02]{fg.rs}  Three sim")
                print(fg.light_red + f"\n   ["+fg.dark_red+"X"+fg.light_red+f"] {fg.rs} Exit")

                while True:
                    try:
                        Other_gen_Module = input(fg.light_red + "\n   Select a Module: "+fg.rs)
                        break
                    except:
                        pass

                if Other_gen_Module == "x" or Other_gen_Module == "X":
                    clear_console()
                    continue

                if Other_gen_Module == "1":
                    import generator.vinted
                    continue

                if Other_gen_Module == "2":
                    import generator.three
                    continue

                else:
                    print(fg.light_red + f'\n  [ menu ] [ {(datetime.time(datetime.now()))} ]' + fg.dark_grey + " • " + fg.red + "Wrong input!")
                    time.sleep(4)
                    continue

            else:
                print(fg.light_red + f'\n  [ menu ] [ {(datetime.time(datetime.now()))} ]' + fg.dark_grey + " • " + fg.red + "Wrong input!")
                time.sleep(4)
                continue

        if Main_Module == "3":

            os.system(f"title {key_username[:-5]}'s KenkiTools[{current_version}] • jigg menu")
            try:
                RPC.update(
                    large_image = "kenki2",
                    details = f"{key_username[:-5]} - v{current_version}",
                    state = f"Jigging Information",
                    start = start,
                )
            except:
                pass

            from misc.jigger import addressabcjigg, addresshardjigg, addresslightjigg
            user_webhook = config["Webhook"]
           
            clear_console()
            print_logo()
            print(fg.rs + f"   {fg.light_red}[01]{fg.rs}  ABC Jigg           {fg.light_red}[02]{fg.rs}  Light Jigg         {fg.light_red}[03]{fg.rs}  Hard Jigg")
            print(fg.light_red + f"\n   ["+fg.dark_red+"X"+fg.light_red+f"] {fg.rs} Exit")
          
            while True:
                try:
                    Address_Module = input(fg.light_red + "\n   Select a Module: "+fg.rs)
                    break
                except:
                    pass
         
            clear_console()
         
            if Address_Module == "x" or Address_Module == "X":
                continue
          
            if Address_Module == "1":
                addressabcjigg()
                continue
         
            if Address_Module == "2":
                addresslightjigg()
                continue
           
            if Address_Module == "3":
                addresshardjigg()
                continue
        
            else:
                print(fg.light_red + f'[ menu ] [ {(datetime.time(datetime.now()))} ]' + fg.dark_grey + " • " + fg.red + "Wrong input")
                time.sleep(4)
                continue
      
        if Main_Module == 4:

            os.system(f"title {key_username[:-5]}'s KenkiTools[{current_version}] • wethenew menu")
            try:
                RPC.update(
                    large_image = "kenki2",
                    details = f"{key_username[:-5]} - v{current_version}",
                    state = f"Sniping wethenew offers",
                    start = start,
                )
            except:
                pass
           
            clear_console()
            print_logo()
            continue
            
        if Main_Module == "5":

            os.system(f"title {key_username[:-5]}'s KenkiTools[{current_version}] • profile menu")
            try:
                RPC.update(
                    large_image = "kenki2",
                    details = f"{key_username[:-5]} - v{current_version}",
                    state = f"Managing Profiles",
                    start = start,
                )
            except:
                pass
          
            from misc.profileconverter import profileconverter
            clear_console()
            print_logo()
           
            print(fg.rs + f"   {fg.light_red}[01]{fg.rs}  FlareAIO           {fg.light_red}[02]{fg.rs}  Fuze               {fg.light_red}[03]{fg.rs}  Infinit")
            print(fg.rs + f"   {fg.light_red}[04]{fg.rs}  DemonRaffle        {fg.light_red}[05]{fg.rs}  StormAIO           {fg.light_red}[06]{fg.rs}  Adonis")
            print(fg.rs + f"   {fg.light_red}[07]{fg.rs}  Ganesh             {fg.light_red}[08]{fg.rs}  FlexAIO            {fg.light_red}[09]{fg.rs}  Earthside")
            print(fg.rs + f"   {fg.light_red}[10]{fg.rs}  Kallisto           {fg.light_red}[11]{fg.rs}  GammaAIO           {fg.light_red}[12]{fg.rs}  NeoRaffles")
            print(fg.rs + f"   {fg.light_red}[13]{fg.rs}  ThunderIO          {fg.light_red}[14]{fg.rs}  Mirage             {fg.light_red}[15]{fg.rs}  Haze")
            print(fg.rs + f"   {fg.light_red}[16]{fg.rs}  ClipAIO            {fg.light_red}[17]{fg.rs}  Burst              {fg.light_red}[18]{fg.rs}  BananaAIO")
            print(fg.rs + f"   {fg.light_red}[19]{fg.rs}  Calix              {fg.light_red}[20]{fg.rs}  Nova               {fg.light_red}[21]{fg.rs}  Ormyx")
            print(fg.rs + f"   {fg.light_red}[22]{fg.rs}  Loscobot           {fg.light_red}[23]{fg.rs}  PanAIO")
            print(fg.light_red + f"\n   ["+fg.dark_red+"X"+fg.light_red+f"] {fg.rs} Exit")
           
            while True:
                try:
                    Profile_Module = input(fg.light_red + "\n   Select a Module: "+fg.rs)
                    break
                except:
                    pass
          
            if Profile_Module == "x" or Profile_Module == "X":
                clear_console()
                continue
          
            clear_console()
            print_logo()
            global converter
            converter = []
         
            with open('Profile/Profile.csv', newline='') as input_file:
                csv_file = csv.reader(input_file)
                try:
                    for row in csv_file:
                  
                        if row != ["profile name","email","firstname","lastname","address","address 2","housenumber","city","state","zip code","countrycode","prefix","phone","cc","month/year","cvv","cardtype","name on card"]:
                            converter.append(row)
               
                except Exception as e:
                    print(fg.light_red + f"[ Profile ] [ {time.strftime('%H:%M:%S', time.localtime())} ]" + fg.dark_grey + " • " + fg.red + "Error fetching information!")
         
            if Profile_Module == "1":
                for x in converter: 
             
                    y = x[14]
                    z = y.split("/")
                    rows = [x[0], x[1], x[2], x[3], x[6], x[4], x[5], x[9], x[7], x[8], x[10], x[11]+x[12], "TRUE", x[16], x[13], z[0], z[1], x[15], "RANDOM"]
                    header = ["PROFILE NAME", "EMAIL", "SHIPPING FIRST NAME", "SHIPPING LAST NAME", "SHIPPING HOUSE NUMBER", "SHIPPING ADDRESS LINE 1", "SHIPPING ADDRESS LINE 2", "SHIPPING POSTAL CODE", "SHIPPING CITY", "SHIPPING STATE", "SHIPPING COUNTRY (XX)", "SHIPPING PHONE NUMBER", "IS BILLING SAME", "CARD TYPE", "CARD NUMBER", "CARD EXPIRY MONTH (MM)", "CARD EXPIRY YEAR (YYYY)", "CARD CVV", "BIRTHDAY (DD/MM/YYYY)", "PAYPAL EMAIL", "DISCORD WEBHOOK", "SOCIAL NUMBER", "BILLING FIRST NAME", "BILLING LAST NAME", "BILLING HOUSE NUMBER", "BILLING ADDRESS LINE 1", "BILLING ADDRESS LINE 2", "BILLING POSTAL CODE", "BILLING CITY", "BILLING STATE", "BILLING COUNTRY (XX)", "BILLING PHONE NUMBER", "ADDRESS ID", "VAT ID"]
                    profileconverter("FlareAIO", rows, header)
                continue
         
            if Profile_Module == "2":
                for x in converter: 
            
                    y = x[14]
                    z = y.split("/")
                    rows = [x[0], x[1], x[2], x[3], x[6], x[4], x[5], x[9], x[7], x[8], x[10], x[11]+x[12], "TRUE", x[16], x[13], z[0], z[1], x[15], "RANDOM"]
                    header = ["PROFILE NAME", "EMAIL", "SHIPPING FIRST NAME", "SHIPPING LAST NAME", "SHIPPING HOUSE NUMBER", "SHIPPING ADDRESS LINE 1", "SHIPPING ADDRESS LINE 2", "SHIPPING POSTAL CODE", "SHIPPING CITY", "SHIPPING STATE", "SHIPPING COUNTRY (XX)", "SHIPPING PHONE NUMBER", "IS BILLING SAME", "CARD TYPE", "CARD NUMBER", "CARD EXPIRY MONTH (MM)", "CARD EXPIRY YEAR (YYYY)", "CARD CVV", "BIRTHDAY (DD/MM/YYYY)", "PAYPAL EMAIL", "DISCORD WEBHOOK", "SOCIAL NUMBER", "BILLING FIRST NAME", "BILLING LAST NAME", "BILLING HOUSE NUMBER", "BILLING ADDRESS LINE 1", "BILLING ADDRESS LINE 2", "BILLING POSTAL CODE", "BILLING CITY", "BILLING STATE", "BILLING COUNTRY (XX)", "BILLING PHONE NUMBER", "ADDRESS ID", "VAT ID"]
                    profileconverter("Fuze", rows, header)
                continue
           
            if Profile_Module == "3":
                for x in converter: 
       
                    y = x[14]
                    z = y.split("/")
                    rows = [x[2], x[3], x[1], "", x[11], x[12], x[4], x[6], x[5], x[9], x[7], x[8], x[10], x[13], x[15], z[0], z[1], x[17]]
                    header = ["first_name", "last_name", "email", "password", "prefix", "phone", "street", "house_number", "door", "zip", "city", "province", "country_code", "cc_number", "cc_cvc", "cc_month", "cc_year", "cc_name", "paypal_email", "paypal_password"]
                    profileconverter("Infinit", rows, header)
                continue
          
            if Profile_Module == "4":
                for x in converter: 
       
                    y = x[14]
                    z = y.split("/")
                    rows = [x[2], x[3], x[1], "", x[4], x[6], x[5], x[9], x[7], x[8], x[10], x[11], x[12]]
                    header = ["FIRST NAME", "LAST NAME", "EMAIL", "PASSWORD", "STREET", "STREET NUMBER", "ADDRESS LINE 2", "ZIP CODE", "CITY", "STATE", "COUNTRY CODE", "PREFIX", "PHONE NUMBER", "INSTAGRAM"]
                    profileconverter("DemonRaffles", rows, header)
                continue
        
            if Profile_Module == "5":
                for x in converter: 
           
                    y = x[14]
                    z = y.split("/")
                    rows = [x[0], x[2], x[3], x[1], x[4], x[6], x[5], x[7], x[8], x[9], x[10], x[11], x[12], x[13], z[0], z[1], x[15]]
                    header = ["PROFILE NAME", "FIRST NAME", "LAST NAME", "EMAIL", "STREET", "HOUSE NUMBER", "ADDRESS 2", "CITY", "STATE", "POSTCODE", "COUNTRY", "PHONE PREFIX", "PHONE NUMBER", "CARD NUMBER", "CARD MONTH", "CARD YEAR", "CARD CVC", "WEBHOOK"]
                    profileconverter("StormAIO", rows, header)
                continue
       
            if Profile_Module == "6":
                for x in converter: 
         
                    y = x[14]
                    z = y.split("/")
                    rows = ["", "", "", "", "", x[2], x[3], x[4], x[5], x[6], x[9], x[7], x[11]+x[12], x[10], x[1], "", x[16], x[13], z[0], z[1], x[15]]
                    header = ["SITE", "URL", "DUMMY_URL", "MODE", "SIZE", "FIRSTNAME", "LASTNAME", "ADDRESS_LINE_1", "ADDRESS_LINE_2", "HOUSENUMBER", "POSTCODE", "CITY", "PHONENUMBER", "COUNTRY_CODE", "EMAIL", "PASSWORD", "CARD_TYPE", "CREDIT_CARD", "EXPIRY_MONTH", "EXPIRY_YEAR", "CVV", "QUANTITY", "BIC", "ISSUERID", "STATE", "REGION_ID", "DISCOUNT_CODE"]
                    profileconverter("Adonis", rows, header)
                continue
         
            if Profile_Module == "7":
                for x in converter: 
      
                    y = x[14]
                    z = y.split("/")
                    rows = ["", "", "", "", "", x[2], x[3], x[1], x[11]+x[12], x[4]+" "+x[6], x[5], x[7], x[8], x[9], x[10], x[13], z[0], z[1], x[15]]
                    header = ["STORE", "MODE", "PRODUCT", "SIZE", "TIMER", "FIRST NAME", "LAST NAME", "EMAIL", "PHONE NUMBER", "ADDRESS LINE 1", "ADDRESS LINE 2", "CITY", "STATE", "POSTCODE / ZIP", "COUNTRY", "CARD NUMBER", "EXPIRE MONTH", "EXPIRE YEAR", "CARD CVC"]
                    profileconverter("Ganesh", rows, header)
                continue
   
            if Profile_Module == "8":
                for x in converter: 
       
                    y = x[14]
                    z = y.split("/")
                    rows = [x[0], "", "", "", x[2], x[3], x[1], x[11]+x[12], x[4]+" "+x[6], x[5], x[7], x[8], x[9], x[10], x[13], z[0], z[1], x[15]]
                    header = ["IDENTIFIER","MODE","SIZE","PROXY (can leave empty)","FIRST NAME","LAST NAME","EMAIL / ACCOUNT","PHONE NUMBER","ADDRESS LINE 1","ADDRESS LINE 2","CITY","STATE","POSTCODE / ZIPCODE","COUNTRY (ISO2)","CARD NUMBER","EXPIRY MONTH (XX)","EXPIRY YEAR (XXXX)","CVV","DISCOUNT"]
                    profileconverter("FlexAIO", rows, header)
                continue
        
            if Profile_Module == "9":
                for x in converter: 
        
                    y = x[14]
                    z = y.split("/")
                    rows = [x[0], x[1], "", x[2], x[3], x[4], x[5], x[6], x[9], x[7], x[8], x[10], x[11]+x[12], x[17], x[13], z[0], z[1], x[15]]
                    header = ["PROFILE NAME","EMAIL","PASSWORD","FIRST NAME","LAST NAME","ADDRESS 1","ADDRESS 2","HOUSE NUMBER","POSTCODE","CITY","STATE","COUNTRY","PHONE","CARDHOLDER NAME","CARD NUMBER","EXPIRY MONTH","EXPIRY YEAR","CVC","WEBHOOK"]
                    profileconverter("Earthside", rows, header)
                continue
           
            if Profile_Module == "10":
                for x in converter: 
         
                    y = x[14]
                    z = y.split("/")
                    rows = [x[0], x[1], "", x[11]+x[12], x[2], x[3], x[4]+" "+x[6], "", x[5], x[9], x[7], x[8], x[10], x[17], x[13], z[0], z[1], x[15]]
                    header = ["ProfileName", "Email", "Account", "Telephone", "FirstName", "LastName", "Address1", "Apt", "Address2", "Zip", "City", "State", "Country", "Card.Holder", "Card.Number", "Card.ExpiryMonth", "Card.ExpiryYear", "Card.Cvv", "Webhook"]
                    profileconverter("Kallisto", rows, header)
                continue
          
            if Profile_Module == "11":
                pass
          
            if Profile_Module == "12":
                for x in converter: 
            
                    y = x[14]
                    z = y.split("/")
                    rows = [x[1], "", x[2], x[3], x[4]+" "+x[6], x[7], x[9], x[8], x[10], x[13], z[0], z[1], x[15]]
                    header = ["EMAIL", "PASSWORD", "FIRST NAME", "LAST NAME", "ADDRESS LINE 1", "CITY", "ZIPCODE", "STATE/PROVINCE", "COUNTRY", "CARD NUMBER", "EXPIRE MONTH", "EXPIRE YEAR", "CARD CVC"]
                    profileconverter("NeoRaffle", rows, header)
                continue
           
            if Profile_Module == "13":
                for x in converter: 
          
                    y = x[14]
                    z = y.split("/")
                    rows = [x[0], x[2], x[3], x[6], x[4], x[5], x[9], x[7], x[8], x[10], "TRUE", "", "", "", "", "", "", "", x[11]+x[12], x[16], x[13], z[0], z[1], x[15]]
                    header = ["PROFILENAME", "FIRST NAME", "LAST NAME", "SHIPPING_ADDRESS_NUMBER", "SHIPPING_ADDRESS", "SHIPPING_ADDRESS2", "SHIPPING_POSTCODE", "SHIPPING_CITY", "SHIPPING_STATE", "SHIPPING_COUNTRY", "SAME_SHIPPING_AS_BILLING", "BILLING_ADDRESS_NUMBER", "BILLING_ADDRESS", "BILLING_ADDRESS2", "BILLING_POSTCODE", "BILLING_CITY", "BILLING_STATE", "BILLING_COUNTRY", "PHONE", "CC TYPE", "CC NUMBER", "EXPIRY_MONTH", "EXPIRY_YEAR", "CVC"]
                    profileconverter("ThunderIO", rows, header)
                continue
          
            if Profile_Module == "14":
                for x in converter: 
        
                    y = x[14]
                    z = y.split("/")
                    rows = [x[1], "", "", "", x[4]+" "+x[6], x[5], x[2], x[3], x[7], x[11]+x[12], x[9], x[8], x[10], x[13], z[1], z[0], x[15]]
                    header = ["EMAIL", "PRODUCT", "SIZE", "PASSWORD", "ADDRESS1", "ADDRESS2", "FIRSTNAME", "LASTNAME", "CITY", "PHONE", "POSTCODE","COUNTY", "COUNTRY", "CARDNUM", "CARDYEAR", "CARDMONTH", "CARDCVC", "LOOPS"]
                    profileconverter("Mirage", rows, header)
                continue
          
            if Profile_Module == "15":
                for x in converter: 
           
                    y = x[14]
                    z = y.split("/")
                    rows = [x[0], x[2], x[3], x[1], x[4], x[6], x[5], x[9], x[7], x[8], x[10], x[11]+x[12], "", x[16], x[13], z[0], z[1], x[15]]
                    header = ["PROFILENAME", "FIRSTNAME", "LASTNAME", "EMAIL", "STREET", "HOUSENUMBER", "ADDRESS2", "ZIPCODE", "CITY", "STATE", "COUNTRY", "PHONE", "POST_NUMBER", "CARDTYPE", "CC_NUMBER", "CC_EXPMONTH", "CC_EXPYEAR", "CC_CVV"]
                    profileconverter("Haze", rows, header)
                continue
          
            if Profile_Module == "16":
                pass
         
            if Profile_Module == "17":
                pass
         
            if Profile_Module == "18":
                for x in converter: 
          
                    y = x[14]
                    z = y.split("/")
                    rows = [x[0], x[2], x[3], x[7], x[4]+" "+x[6], x[9], x[5], "", "", "", "", "", "", "", "", x[11]+x[12]]
                    header = ["ProfileName","ShippingFirstname","ShippingLastname","ShippingCity","ShippingStreet","ShippingZip","ShippingAdditional","SameBilling","BillingFirstname","BillingLastname","BillingCity","BillingStreet","BillingZip","BillingAdditional","BillingCountryCode","PhoneNumber","Webhook"]
                    profileconverter("Banana", rows, header)
                continue
           
            if Profile_Module == "19":
                pass
        
            if Profile_Module == "20":
                for x in converter: 
          
                    y = x[14]
                    z = y.split("/")
                    rows = [x[0], x[2], x[3], x[1], x[4]+" "+x[6], x[7], x[9], x[11]+x[12], x[10], x[13], z[0], z[1], x[15]]
                    header = ["profilename","fname","lname","Email","BillingAddress1","BillingCity","BillingZIP","BillingPhone","countryID","CreditCardNumber","cardExpiryMonth","cardExpiryYear","cvdNumber"]
                    profileconverter("Nova", rows, header)
                continue
        
            if Profile_Module == "21":
                for x in converter: 
        
                    y = x[14]
                    z = y.split("/")
                    rows = [x[1], "", "", "", "", x[10], "", "", "", "", "", "", "", "", "", x[13], z[0], z[1], x[15], x[17]]
                    header = ["email","password","specialMode","usePreload","start","country","PID_item","PID_size","sizeEU","delay","proxy","mode","modeDelay","useHarvester","resolveDDCaptcha","ccNumber","expiryMonth","expiryYear","cvc","ccOwner"]
                    profileconverter("Ormyx", rows, header)
                continue
         
            if Profile_Module == "22":
                for x in converter: 
         
                    y = x[14]
                    z = y.split("/")
                    rows = [x[0], x[2], x[3], x[11]+x[12], x[4], x[5], "", x[6], x[7], x[8], x[9], x[10]]
                    header = ["Profile Name","First Name","Last Name","Mobile Number","Address","Address 2","Address 3","House Number","City","State","ZIP","Country","Billing First Name","Billing Last Name","Billing Mobile Number","Billing Address","Billing Address 2","Billing Address 3","Billing House Number","Billing City","Billing State","Billing ZIP","Billing Country","COMPANYNAME---VATNUMBER"]
                    profileconverter("Losco", rows, header)
                continue
         
            if Profile_Module == "23":
                for x in converter: 
         
                    y = x[14]
                    z = y.split("/")
                    rows = [x[2]+" "+x[3], x[4]+" "+x[6], x[5], x[7], x[9], x[1], x[10], x[8], x[16], x[17], x[13], z[0], z[1], x[15], x[11]+x[12], x[0], ""]
                    header = ["name", "address", "address2", "city", "postcode", "email", "country", "region", "cards", "holder", "numbercard", "month", "year", "cvv", "phone", "profileName", "webhook"]
                    profileconverter("PanAIO", rows, header)
                continue
          
            else:
                print(fg.light_red + f'[ menu ] [ {(datetime.time(datetime.now()))} ]' + fg.dark_grey + " • " + fg.red + "Wrong input")
                time.sleep(4)
                continue
            
        if Main_Module == "6":

            os.system(f"title {key_username[:-5]}'s KenkiTools[{current_version}] • shipping menu")
            try:
                RPC.update(
                    large_image = "kenki2",
                    details = f"{key_username[:-5]} - v{current_version}",
                    state = f"Tracking Orders",
                    start = start,
                )
            except:
                pass
         
            clear_console()
            print_logo()
            print(fg.rs + f"   {fg.light_red}[1]{fg.rs}  Mesh Tracker        {fg.light_red}[2]{fg.rs}  DHL Tracker         {fg.light_red}[3]{fg.rs}  DPD Tracker")
            print(fg.rs + f"   {fg.light_red}[4]{fg.rs}  Nike Tracker")
            print(fg.light_red + f"\n   ["+fg.dark_red+"X"+fg.light_red+f"] {fg.rs} Exit")
       
            while True:
                try:
                    Other_Module = input(fg.light_red + "\n   Select a Module: "+fg.rs)
                    break
                except:
                    pass
        
            if Other_Module == "x" or Other_Module == "X":
                time.sleep(0.8)
                clear_console()
                continue
          
            if Other_Module == "1":
                from shipping.mesh import meshtracker
                meshtracker()
                continue
         
            if Other_Module == "2":
                from shipping.dhl import dhltracker
                dhltracker()
                continue
          
            if Other_Module == "3":
                from shipping.dpd import dpdtracker
                dpdtracker()
                continue
         
            if Other_Module == "4":
                from shipping.nike import nikeordertracker
                nikeordertracker()
                continue
          
            else:
                print(fg.red + "Wrong input")
                time.sleep(4)
                continue

        if Main_Module == "7":

            clear_console()
            os.system(f"title {key_username[:-5]}'s KenkiTools[{current_version}] • Nike menu")
        
            try:
                RPC.update(
                    large_image = "kenki2",
                    details = f"{key_username[:-5]} - v{current_version}",
                    state = "Farming nike activity",
                    start = start,
                )
            except:
                pass
          
            clear_console()
            print_logo()
            print(fg.rs + f"   {fg.light_red}[01]{fg.rs}  Account Farmer     {fg.light_red}[02]{fg.rs}  Account checker     {fg.light_red}[03]{fg.rs}  Email changer")
            print(fg.rs + f"   {fg.light_red}[04]{fg.rs}  Password changer   {fg.light_red}[05]{fg.rs}  Region changer")
            print(fg.light_red + f"\n   ["+fg.dark_red+"X"+fg.light_red+f"] {fg.rs} Exit")
        
            while True:
                try:
                    Nike_Module = input(fg.light_red + "\n   Select a Module: "+fg.rs)
                    break
                except:
                    pass
         
            clear_console()
            
            if Nike_Module == "x" or Nike_Module == "X":
                time.sleep(0.8)
                clear_console()
                continue
         
            if Nike_Module == "1":
                import nike.farmer
                input("")
         
            if Nike_Module == "2":
                import nike.checker
                input("")
         
            if Nike_Module == "3":
                import nike.email
                input("")
         
            if Nike_Module == "4":
                import nike.password
                input("")
        
            if Nike_Module == "5":
                import nike.region
                input("")
          
            else:
                print(fg.red+"Wrong input")
                time.sleep(2)
                continue
        
        if Main_Module == "8":

            os.system(f"title {key_username[:-5]}'s KenkiTools[{current_version}] • hyper menu")
            number = random.randint(0, 5)
         
            try:
         
                if number == 1:
                    RPC.close()
                    client_id = "1059131616473120848"
                    RPC = pypresence.Presence(client_id)
                    RPC.connect()
                    RPC.update(
                        large_image = "fortnite",
                        large_text= f"Stufe {random.randint(1, 100)}",
                        details = f"Battle Royale - In Lobby",
                        state = f"Ist in Einheit (1 of 4)",
                        start = start,
                    )
          
                if number == 2:
                    RPC.close()
                    client_id = "1059131365787959380"
                    RPC = pypresence.Presence(client_id)
                    RPC.connect()
                    RPC.update(
                        large_image = "rust",
                        start = start,
                    )
           
                if number == 3:
                    RPC.close()
                    client_id = "1059132155411832842"
                    RPC = pypresence.Presence(client_id)
                    RPC.connect()
                    RPC.update(
                        large_image = "tarkov",
                        start = start,
                    )
          
                if number == 4:
                    RPC.close()
                    client_id = "1059133322766332016"
                    RPC = pypresence.Presence(client_id)
                    RPC.connect()
                    RPC.update(
                        large_image = "rocket",
                        start = start,
                    )
           
            except:
                pass
        
            import hyper.load
      
        if Main_Module == "9":
            os.system(f"title {key_username[:-5]}'s KenkiTools[{current_version}] • Revolut menu")
         
            try:
                RPC.update(
                    large_image = "kenki2",
                    details = f"{key_username[:-5]} - v{current_version}",
                    state = f"Solving 3ds...",
                    start = start,
                )
            except:
                pass
          
            print_logo()
            print(fg.rs + f"   {fg.light_red}[1]{fg.rs}  Revolut            {fg.light_red}[2]{fg.rs}  Revolut business")
            print(fg.light_red + f"\n   ["+fg.dark_red+"X"+fg.light_red+f"] {fg.rs} Exit")
            revolut_module = input(fg.light_red + "\n   Select a Module: "+fg.rs)
            clear_console()
          
            if revolut_module == "x" or revolut_module == "X":
                continue
          
            if revolut_module == "1":
                print_logo()
                print(fg.rs + f"   {fg.light_red}[1]{fg.rs}  Solve 3ds          {fg.light_red}[2]{fg.rs}  Generate Session")
                print(fg.light_red + f"\n   ["+fg.dark_red+"X"+fg.light_red+f"] {fg.rs} Exit\n")
                revolut_module = input(fg.light_red + "   Select a Module: "+fg.rs)
                clear_console()
              
                if revolut_module == "x" or revolut_module == "X":
                    continue
                
                if revolut_module == "1":
                    from revolut.personal_start import solvethreeds
                    print_logo()
                    solvethreeds()
               
                if revolut_module == "2":
                    from revolut.personal_start import createsession
                    print_logo()
                    createsession()
         
            if revolut_module == "2":
                print_logo()
                print(fg.rs + f"   {fg.light_red}[1]{fg.rs}  Solve 3ds          {fg.light_red}[2]{fg.rs}  Generate Session")
                print(fg.light_red + f"\n   ["+fg.dark_red+"X"+fg.light_red+f"] {fg.rs} Exit\n")
                revolut_module = input(fg.light_red + "   Select a Module: "+fg.rs)
                clear_console()
             
                if revolut_module == "x" or revolut_module == "X":
                    continue
               
                if revolut_module == "1":
                    from revolut.business_start import solvethreeds
                    print_logo()
                    solvethreeds()
               
                if revolut_module == "2":
                    from revolut.business_start import createsession
                    print_logo()
                    createsession()

        
        if Main_Module == "10":
          
            os.system(f"title {key_username[:-5]}'s KenkiTools[{current_version}] • Settings")
            try:
                RPC.update(
                    large_image = "kenki2",
                    details = f"{key_username[:-5]} - v{current_version}",
                    state = f"Editing Settings",
                    start = start,
                )
            except:
                pass
           
            while True:
                clear_console()
                print_logo()
                print(fg.light_red + f'  [ Settings ]' + fg.dark_grey + " • " + fg.rs + f"1 - Add webhook")
                print(fg.light_red + f'  [ Settings ]' + fg.dark_grey + " • " + fg.rs + f"2 - show username in webhook")
                print(fg.light_red + f'  [ Settings ]' + fg.dark_grey + " • " + fg.rs + f"3 - Set imap details\n")
                print(fg.light_red + f'  [ Settings ]' + fg.dark_grey + " • " + fg.rs + f"4 - Open settings")
                print(fg.light_red + f'  [ Settings ]' + fg.dark_grey + " • " + fg.rs + f"5 - Send test webhook")
                print(fg.light_red + f'\n\n  [ Settings ]' + fg.dark_grey + " • " + fg.rs + f"X - Exit\n")
                settings_option = input(fg.light_red + "  Select your option: : "+fg.rs)
              
                if settings_option == "1":
                    new_webhook = input(fg.light_red + "  Input your Webhook: "+fg.rs)
                   
                    with open('config.json', 'r+') as f:
                        data = json.load(f)
                        data['Webhook'] = new_webhook
                        f.seek(0)
                        json.dump(data, f, indent=4)
                        f.truncate()
              
                if settings_option == "2":
                 
                    while True:
                        show_username = input(fg.light_red + "  Show username (y/n): "+fg.rs)
                   
                        if show_username == "y" or show_username == "Y" or show_username == "n" or show_username == "N":
                            break
                       
                        else:
                            continue
                
                    if show_username == "y" or show_username == "Y":
                        show_username = "true"
                  
                    if show_username == "n" or show_username == "N":
                        show_username = "false"
                  
                    with open('config.json', 'r+') as f:
                        data = json.load(f)
                        data['show-username'] = show_username
                        f.seek(0)
                        json.dump(data, f, indent=4)
                        f.truncate()
              
                if settings_option == "3":
                    email = input(fg.light_red + "  Input your email: "+fg.rs)
                    password = input(fg.light_red + "  Input your password: "+fg.rs)
                
                    with open('config.json', 'r+') as f:
                        data = json.load(f)
                        data['Raffle']['Email'] = email
                        data['Raffle']['Password'] = password
                        f.seek(0)
                        json.dump(data, f, indent=4)
                        f.truncate()
              
                if settings_option == "4":
                    os.system("config.json")
                    continue
               
                if settings_option == "5":
                  
                    if user_webhook != "":
                     
                        webhook = DiscordWebhook(url=user_webhook, avatar_url="https://media.discordapp.net/attachments/878354931201998859/1059895159959076975/kenki_logo_render.png", username="KenkiTools")
                        embed = DiscordEmbed(title=f'Test Webhook', description='Your webhook is working perfectly!', color='bc252c', url="https://twitter.com/KenkiTools")
                        embed.set_thumbnail(url="https://media.discordapp.net/attachments/878354931201998859/1059895159959076975/kenki_logo_render.png")
                        embed.set_footer(text=f'@KenkiTools', icon_url=f"https://media.discordapp.net/attachments/878354931201998859/1059895159959076975/kenki_logo_render.png")
                        site = ["Gmail","Nike","Outlook","icloud","Hyper","Whop","Revolut"]
                        embed.add_embed_field(name='Site', value=f'{random.choice(site)}', inline=False)
                        embed.add_embed_field(name='Product', value=f'[KenkiTools](https://kenkitools.com)', inline=False)
                        embed.add_embed_field(name='Email', value='||test@kenkitools.com||', inline=True)
                        embed.add_embed_field(name='Password', value='||KenkiTools123!||', inline=True)
                        embed.add_embed_field(name='Profile', value='||Gkay||', inline=True)
                        embed.add_embed_field(name='Information', value=f'This is a test webhook for {key_username}', inline=False)
                        embed.add_embed_field(name='Information', value='have fun exploring the world with kenkitools!', inline=False)
                        embed.set_timestamp()
                        webhook.add_embed(embed)
                        webhook.execute()
             
                if settings_option == "X" or settings_option == "x":
                    break
              
                else:
                    pass
        
        if Main_Module == "11":
            clear_console()
            accounts_generated = open("Data/accounts", 'r').read()
            accounts_farmed = open("Data/accounts_farmed", 'r').read()
            mails_generated = open("Data/mails", 'r').read()
            solved_3ds = open("Data/revolut", 'r').read()
            hyper_checkout = -1
           
            with open('Data/hyper.csv', newline='') as input_file:
                csv_file = csv.reader(input_file)
                next(csv_file)
               
                for row in csv_file:
                    hyper_checkout += 1
          
            print_logo()
            print(fg.light_red + f'  [ analytics ]' + fg.dark_grey + " • " + fg.rs + f"Accounts created   :  {str(accounts_generated)}")
            print(fg.light_red + f'  [ analytics ]' + fg.dark_grey + " • " + fg.rs + f"Mails generated    :  {str(mails_generated)}")
            print(fg.light_red + f'  [ analytics ]' + fg.dark_grey + " • " + fg.rs + f"Hyper checkouts    :  {str(hyper_checkout)}")
            print(fg.light_red + f'  [ analytics ]' + fg.dark_grey + " • " + fg.rs + f"Accounts farmed    :  {str(accounts_farmed)}")
            print(fg.light_red + f'  [ analytics ]' + fg.dark_grey + " • " + fg.rs + f"Solved 3ds         :  {str(solved_3ds)}")
            print(fg.light_red + f'\n\n  [ analytics ]' + fg.dark_grey + " • " + fg.rs + f"X - Exit\n")
           
            while True:
                analytics_option = input(fg.light_red + "  Select your option: : "+fg.rs)
              
                if analytics_option == "x" or analytics_option == "X":
                    break
              
                else:
                    continue
            
        elif Main_Module == "x" or Main_Module == "X":
            os.system(f"title {key_username[:-5]}'s KenkiTools[{current_version}] • goodbye")
            clear_console()
            print_logo()
            print(fg.light_red + "Goodbye...")
            time.sleep(2)
            break
    
    except Exception as e:
        error_id = uuid.uuid4().hex[:8]
        exc_type, exc_obj, exc_tb = sys.exc_info()
        filename = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
       
        print(fg.light_red + f'[ Home ] [ {(datetime.datetime.time(datetime.now()))} ]' + fg.dark_grey + " • " + fg.red + f"{e} - #{error_id}")
       
        webhook = DiscordWebhook(url=private_webhook_error, avatar_url="https://media.discordapp.net/attachments/878354931201998859/1059895159959076975/kenki_logo_render.png", username="KenkiTools")
        embed = DiscordEmbed(title=f'KenkiTools Error Logger', description=f'{key_username} had an error in KenkiTools', color="bc252c")
        embed.set_footer(text=f"KenkiTools", icon_url="https://media.discordapp.net/attachments/878354931201998859/1059895159959076975/kenki_logo_render.png")
        embed.set_timestamp()
        embed.add_embed_field(name='Version', value=f'{current_version}', inline=False)
        embed.add_embed_field(name='User', value=f'<@{key_user_id}>', inline=False)
        embed.add_embed_field(name='File', value=f'{filename}', inline=False)
        embed.add_embed_field(name='Line', value=f'{exc_tb.tb_lineno}', inline=False)
        embed.add_embed_field(name='Error type', value=f'{exc_type}', inline=False)
        embed.add_embed_field(name='Error', value=f'{e}', inline=False)
        embed.add_embed_field(name='Error ID', value=f'{error_id}', inline=False)
        webhook.add_embed(embed)
        webhook.execute()
      
        time.sleep(3)
        clear_console()