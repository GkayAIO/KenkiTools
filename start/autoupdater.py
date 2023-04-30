import urllib.request, sys

from data.storage import *

print(fg.light_red + f"[ Home ] [ {time.strftime('%H:%M:%S', time.localtime())} ]" + fg.dark_grey + " • " + fg.rs + "checking for updates...") 

url = urllib.request.urlopen('https://www.dropbox.com/s/tr7u290ibvaelli/version.html?dl=1')
data = url.read().decode("utf-8")

if data != current_version:

    try:
        os.remove("trash.tmp")
    except:
        pass

    print(fg.light_red + f"[ Home ] [ {time.strftime('%H:%M:%S', time.localtime())} ]" + fg.dark_grey + " • " + fg.light_blue + f"Found update, installing version {data}...") 
    new_version = requests.get("https://www.dropbox.com/s/c7137dcnac1wg37/KenkiTools.exe?dl=1")

    os.rename("KenkiTools.exe", "trash.tmp")
    open("KenkiTools.exe", "wb").write(new_version.content)
    print(fg.light_red + f"[ Home ] [ {time.strftime('%H:%M:%S', time.localtime())} ]" + fg.dark_grey + " • " + fg.green + "Successfully updated kenkitools, restarting...")
    
    version = {"version": f"{data}"}
    json.object = json.dumps(version, indent=1)
    with open("version.json", "w") as f:
        f.write(json.object)

    clear_console()
    os.system("KenkiTools.exe")
    sys.exit()
    
else:
    print(fg.light_red + f"[ Home ] [ {time.strftime('%H:%M:%S', time.localtime())} ]" + fg.dark_grey + " • " + fg.green + "You are on the newest version!")