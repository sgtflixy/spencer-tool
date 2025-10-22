import tkinter as tk
import random
import time
import os
import shutil
from os import system
import requests
from urllib.parse import quote, urlparse, urlunparse
import urllib
import subprocess

links = """
            [ 01 ] -> https://games.sarge.wtf (requires bypass)
            [ 02 ] -> https://www.fedswtf.xyz/games/ (may require bypass soon)
            [ 03 ] -> https://spencertool.sgtflixy.xyz (main download site)
            [ 04 ] -> https://spencertool.sgtflixy.xyz/tutorialext.mp4 (HOW TO GET EXTENSION IDS)
            [ 05 ] -> https://spencertool.sgtflixy.xyz/spencertool.py (FOR UPDATING THE TOOL)
            
            [ II ] -> Shift click to open links!
"""

banner = """
     _______  _____  _______ __   _ _______ _______  ______      ______  __   __  _____  _______ _______ _______
     |______ |_____] |______ | \  | |       |______ |_____/      |_____]   \_/   |_____] |_____| |______ |______
     ______| |       |______ |  \_| |_____  |______ |    \_      |_____]    |    |       |     | ______| ______|

     - by T.G (sgtflixy), S.H (TERRATOME)
     
     --- [ We would request that you dont abuse this ;). BUUUT we know you will. ] ---
    

    """

def Startup():
    system("title " + "Starting ...")
    os.system('cls')
    intro = """
     _______  _____  _______ __   _ _______ _______  ______      ______  __   __  _____  _______ _______ _______
     |______ |_____] |______ | \  | |       |______ |_____/      |_____]   \_/   |_____] |_____| |______ |______
     ______| |       |______ |  \_| |_____  |______ |    \_      |_____]    |    |       |     | ______| ______|
                                                                                                      
"""
    print(intro)
    time.sleep(1)
    print("    - by T.G (sgtflixy), S.H (TERRATOME)")
    time.sleep(2)
    print("    A Mr Kerry tribute")
    time.sleep(0.5)
    Menu()

def Menu():
    system("title " + "SpencerTool - Menu")
    while True:
        os.system('cls')
        print(banner)
        print("""
            [ 001 ] -> Links
            [ 002 ] -> Close MSEdge
            [ 003 ] -> Kill smartscreen
            [ 004 ] -> Show tasks
            [ 005 ] -> Stop WebBlock
            [ 006 ] -> Delete an extension, 
                [ ARG ] -> <id>
                
            [ 007 ] -> File Spammer
                [ ARG ] -> <name>
            [ 008 ] -> Proxies
                [ ARG ] -> ip:password (OPTIONAL)
            [ 009 ] -> Quit process
                [ ARG ] -> process name
            [  A  ] -> Start Process
                [ ARG ] -> process name
            [  B  ] -> Terminal
                [ INF ] -> This is a remake of the terminal, not a real one.
                [ INF ] -> Therefore it only runs in the current dir.
            [  C  ] -> AI
                [ ARG ] -> Prompt
             
    """)
        menuChoice = input("            [ ?? ] -> ")

    # whole lotta if statements (we are NOT being derek with this one)
        # links
        if "1" in menuChoice:
            system("title " + "SpencerTool - Links")
            os.system('cls')
            print(banner)
            print(links)
            input("            [ !! ] -> Press enter to continue . . .")

        # edge closer
        elif "2" in menuChoice:
            system("title " + "SpencerTool - Edge Closer")
            os.system('cls')
            print(banner)
            output = os.system("taskkill -f /im msedge.exe")
            print("            [ !! ] -> Done! output is above!")
            print("")
            input("            [ !! ] -> Press enter to continue . . .")

        # smartscreen closer
        elif "3" in menuChoice:
            system("title " + "SpencerTool - Smartscreen remover")
            os.system('cls')
            print(banner)
            os.system("taskkill -f /im smartscreen.exe")
            print("            [ !! ] -> Done! output is above!")
            print("")
            input("            [ !! ] -> Press enter to continue . . .")

        elif "4" in menuChoice:
            system("title " + "SpencerTool - Tasklist")
            os.system('cls')
            print(banner)
            os.system("tasklist")
            print("            [ !! ] -> Done! output is above!")
            print("")
            input("            [ !! ] -> Press enter to continue . . .")
        elif "5" in menuChoice:
            system("title " + "SpencerTool - WebBlock remover")
            os.system('cls')
            print(banner)
            user = os.getlogin()
            filepath = fr"C:\Users\{user}\AppData\Local\Microsoft\Edge\User Data\Default\Extensions\dlcaglefdlidioooijnigjhfcndlncfp"
            while True:
                if os.path.exists(filepath):
                    shutil.rmtree(filepath)
                    print("            [ !! ] -> Block attempt removed")
        elif "6" in menuChoice:
            system("title " + "SpencerTool - Extension Remover")
            os.system('cls')
            print(banner)
            user = os.getlogin()
            print("            [ !! ] -> Input an extension id (tuto in links)")
            id = input("            [ ?? ] -> ")
            filepath = fr"C:\Users\{user}\AppData\Local\Microsoft\Edge\User Data\Default\Extensions\{id}"
            while True:
                if os.path.exists(filepath):
                    shutil.rmtree(filepath)
                    print("            [ !! ] -> Extension removed")

        elif "7" in menuChoice:
            system("title " + "SpencerTool - File Spammer")
            os.system('cls')
            print(banner)
            count = 0
            print("            [ !! ] -> What name will the files be? ")
            name = input("            [ ?? ] -> ")
            print("            [ !! ] -> Input target directory (enter for none)")
            directory = input("            [ ?? ] -> ")
            endofdir = len(directory)
            endofdir = endofdir -1
            if directory[endofdir] == "/":
                print("            [ !! ] -> File path check success.")
                
            else:
                directory = directory + "/"
                
            while True:
                    count = count + 1
                    temp = open(f"{directory}{name}{count}.txt", "a")
                    for i in range(0, random.randint(1,3)):
                        text = "Storage gobbled by SpencerTool\n"
                        text = text + text
                        with open(f"{directory}{name}{count}.txt", "a") as temp:
                           temp.write(text)
                        print(f"            [ !! ] -> File : {name}{count} created!")
                        
        elif "8" in menuChoice:
            system("title " + "SpencerTool - File Spammer")
            os.system('cls')
            print(banner)
            print("     [ !! ] -> Not implemented as it requires requests, a non default installed python lib.")
        elif "9" in menuChoice:
            system("title " + "SpencerTool - Process remover")
            os.system('cls')
            print(banner)
            print("      [ !! ] -> Enter the process name")
            process = input("         [ !! ] -> ")
            if ".exe" not in process:
                process = process + ".exe"
            os.system(f"taskkill -f /im {process}")
            print("            [ !! ] -> Done! output is above!")
            print("")
            input("            [ !! ] -> Press enter to continue . . .")
        elif "A" in menuChoice.upper():
            system("title " + "SpencerTool - Process Creator")
            os.system('cls')
            print(banner)
            print("     [ !! ] -> Please input your file path, with your process.exe on the end.")
            process = input("     [ !! ] -> ")
            print(os.system(f"start {process}"))
            print("     [ !! ] -> Your process should be starting now. if not please check the log for errors.")
            input("     Press enter to return . . . ")

        elif "B" in menuChoice.upper():
            system("title " + "SpencerTool - Sys Terminal")
            os.system('cls')
            print(banner)
            terminal = True
            while terminal == True:
                terminalInput = input(f"    {os.path.dirname(os.path.realpath(__file__))}> ")
                if terminalInput == "EXIT":
                    terminal = False
                    
                elif terminalInput == "cls":
                    os.system('cls')
                    print(banner)
                else:
                    try:
                        os.system(f"{terminalInput}")
                    except Exception as err:
                        print(err)
        elif "C" in menuChoice.upper():
            system("title " + "SpencerTool - ChadGPT")
            os.system('cls')
            print(banner)
            while True:
                prompt = input("> ")
                try:
                    encoded_prompt = urllib.parse.quote(prompt)
                    api_url = f"https://text.pollinations.ai/{encoded_prompt}"

                    # Run curl command and capture output
                    result = subprocess.run(
                        ["curl", "-s", "--max-time", "15", api_url],
                        capture_output=True,
                        text=True
                    )

                    # Handle curl exit codes
                    if result.returncode != 0:
                        print("⚠️ Failed to get AI response (curl error).")
                        continue

                    ai_response = result.stdout.strip()
                    if not ai_response:
                        print("⚠️ Empty response from AI.")
                        continue

                    formatted_response = ai_response + "\n"
                    print(f"""{formatted_response}""")

                except subprocess.TimeoutExpired:
                    print("⌛ The AI took too long to respond. Please try again later.")
                except Exception as e:
                    print(f"❌ An unexpected error occurred: {str(e)}")
            


Startup()

              
              
          

Startup()
