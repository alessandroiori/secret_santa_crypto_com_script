'''
Filo Secret Santa Script
Author: Alessandro Iori - 13.12.2021

run me: 
$ python3 secret_santa_script.py

create exe file:
1. $ pip3 install pyinstaller
2. $ pyinstaller --onefile double_click_me.py
3. get exe form dist/ folder

'''
from os import system, name
import sys, time
import webbrowser
 
def print_with_delay(string_to_print): 
    for char in string_to_print: 
        print(char, end='') 
        sys.stdout.flush() 
        time.sleep(0.1)     

def input_function():
    i = input()
    if i == "y":
        None
    elif i == "n":
        print_with_delay("bye bye\n")
        exit()
    else:
       print_with_delay("Do you want continue? y/n\n")
       input_function() 

# define our clear function
def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')
  
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

# https://patorjk.com/software/taag/#p=testall&h=0&f=Abraxis-Big&t=CRO

clear()

str_01 = """

 ________  ______  __         ______  
|        \|      \|  \       /      \ 
| $$$$$$$$ \$$$$$$| $$      |  $$$$$$\\
| $$__      | $$  | $$      | $$  | $$
| $$  \     | $$  | $$      | $$  | $$
| $$$$$     | $$  | $$      | $$  | $$
| $$       _| $$_ | $$_____ | $$__/ $$
| $$      |   $$ \| $$     \ \$$    $$
 \$$       \$$$$$$ \$$$$$$$$  \$$$$$$ 
"""

str_02 = """
  ______   ________   ______   _______   ________  ________ 
 /      \ |        \ /      \ |       \ |        \|        \\
|  $$$$$$\| $$$$$$$$|  $$$$$$\| $$$$$$$\| $$$$$$$$ \$$$$$$$$
| $$___\$$| $$__    | $$   \$$| $$__| $$| $$__       | $$   
 \$$    \ | $$  \   | $$      | $$    $$| $$  \      | $$   
 _\$$$$$$\| $$$$$   | $$   __ | $$$$$$$\| $$$$$      | $$   
|  \__| $$| $$_____ | $$__/  \| $$  | $$| $$_____    | $$   
 \$$    $$| $$     \ \$$    $$| $$  | $$| $$     \   | $$   
  \$$$$$$  \$$$$$$$$  \$$$$$$  \$$   \$$ \$$$$$$$$    \$$   
"""

str_03 = """
  ______    ______   __    __  ________   ______  
 /      \  /      \ |  \  |  \|        \ /      \ 
|  $$$$$$\|  $$$$$$\| $$\ | $$ \$$$$$$$$|  $$$$$$\\
| $$___\$$| $$__| $$| $$$\| $$   | $$   | $$__| $$
 \$$    \ | $$    $$| $$$$\ $$   | $$   | $$    $$
 _\$$$$$$\| $$$$$$$$| $$\$$ $$   | $$   | $$$$$$$$
|  \__| $$| $$  | $$| $$ \$$$$   | $$   | $$  | $$
 \$$    $$| $$  | $$| $$  \$$$   | $$   | $$  | $$
  \$$$$$$  \$$   \$$ \$$   \$$    \$$    \$$   \$$
"""

print(str_01)
time.sleep(1)
print(str_02)
time.sleep(1)
print(str_03)


str_1 = "\n16.12.2021 - Filo Secret Santa for Renie\n"
print_with_delay(str_1)

str_2 = "Do you want to know your gift? y/n\n"
print_with_delay(str_2)
input_function()
clear()

str_31 = """

   /$$    /$$$$$$        /$$$$$$$$ /$$   /$$ /$$$$$$$ 
 /$$$$   /$$$_  $$      | $$_____/| $$  | $$| $$__  $$
|_  $$  | $$$$\ $$      | $$      | $$  | $$| $$  \ $$
  | $$  | $$ $$ $$      | $$$$$   | $$  | $$| $$$$$$$/
  | $$  | $$\ $$$$      | $$__/   | $$  | $$| $$__  $$
  | $$  | $$ \ $$$      | $$      | $$  | $$| $$  \ $$
 /$$$$$$|  $$$$$$/      | $$$$$$$$|  $$$$$$/| $$  | $$
|______/ \______/       |________/ \______/ |__/  |__/
"""
str_32 = """
  /$$$$$$  /$$$$$$$   /$$$$$$ 
 /$$__  $$| $$__  $$ /$$__  $$
| $$  \__/| $$  \ $$| $$  \ $$
| $$      | $$$$$$$/| $$  | $$
| $$      | $$__  $$| $$  | $$
| $$    $$| $$  \ $$| $$  | $$
|  $$$$$$/| $$  | $$|  $$$$$$/
 \______/ |__/  |__/ \______/ 
"""
print(str_31)
print(str_32)
print_with_delay("You have received €10 in CRO cryptocurrency!\n\n")
print_with_delay("How to get them:\n")
print_with_delay("1. Use the referral link https://crypto.com/app/ytpdmwkx9u to register at Crypto.com (*)\n")
print_with_delay("2. Register and wait ~24 hours for your account validation\n")
print_with_delay("3. Once validated, communicate in the Filo Coders group the email and phone number used for registration\n")
print_with_delay("4. Receive the equivalent of €10 in CRO\n")
print_with_delay("(*) The referral code ytpdmwkx9u allows you to obtain an additional $25 USD\n\n")
print_with_delay("Do you want to be redirected to the referral link? y/n\n")
input_function()
webbrowser.open("https://crypto.com/app/ytpdmwkx9u")
print("bye bye\n")






