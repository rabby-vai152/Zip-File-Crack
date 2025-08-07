import zipfile
import os
import time

# Clear screen
os.system("clear")

# Logo & Header
print("""\033[1;32m
  ____  ___    ____  ______  __
 / __ \/   |  / __ )/ __ ) \/ /
/ /_/ / /| | / __  / __  |\  / 
/ _, _/ ___ |/ /_/ / /_/ / / /  
/_/ |_/_/  |_/_____/_____/ /_/   

\033[0m\033[1;36m""" + "-"*48)

# Profile Info
print("\033[0m\033[1;33m👑 Owner   : \033[1;37mRabby")
print("\033[0m\033[1;33m💻 Github  : \033[1;37mRabby-152")
print("\033[0m\033[1;33m📘 Facebook: \033[1;37mMd Rabby")
print("\033[0m\033[1;36m" + "-"*48)

# Facebook follow prompt
print("\033[0m\033[1;35m📢 FOLLOW MY TELEGRAM:")
time.sleep(2)

# Horizontal line
print("\033[0m\033[1;36m" + "-"*48)

# Wait for user input
input("\033[1;33m[•] PRESS ENTER TO CONTINUE...\033[0m")

# Open Facebook profile
os.system("termux-open-url https://t.me/RABBY_VAI152")

# ANSI color codes
GREEN = '\033[92m'
RED = '\033[91m'
CYAN = '\033[96m'
YELLOW = '\033[93m'
RESET = '\033[0m'

# Header
print(f"{CYAN}╔═════════════════════════════════════════════════════╗")
print(f"║           🔐 ZIP Password Cracker🔐           ║")
print(f"╚═════════════════════════════════════════════════════╝{RESET}")

# User Input
zip_filename = input(f"{YELLOW}📦 Enter zip File Name          👉  : ")
passlist_filename = input("📄 Enter Password List File Name 👉 :")

# Try to open ZIP file
try:
    zip_file = zipfile.ZipFile(zip_filename)
    print(f"{GREEN}✅ ZIP File Loaded Successfully!{RESET}")
except FileNotFoundError:
    print(f"{RED}❌ ZIP File Not Found! Make sure the file exists.{RESET}")
    exit()
except:
    print(f"{RED}❌ Invalid ZIP file format! Please use a valid .zip file.{RESET}")
    exit()

# Try to open password list
try:
    with open(passlist_filename, "r") as file:
        passwords = file.readlines()
        print(f"{GREEN}📑 Password List Loaded! {len(passwords)} passwords found.{RESET}")
except FileNotFoundError:
    print(f"{RED}❌ Password File Not Found!{RESET}")
    exit()

# Brute Force Start
print(f"{YELLOW}🔍 Starting brute-force attack... Please wait!{RESET}\n")

for password in passwords:
    password = password.strip()
    try:
        zip_file.extractall(pwd=bytes(password, 'utf-8'))
        print(f"\n{GREEN}✅ Password Cracked Successfully! 🔓 Password: {password} 🔑{RESET}")
        break
    except:
        print(f"{RED}❌ Wrong Password: {password}{RESET}")
else:
    print(f"\n{YELLOW}⚠️ Password not found in the list! Try another wordlist.{RESET}")
