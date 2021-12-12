import random
from os import system, name
from time import sleep
import time, sys 
import re 

def clear():

    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')
clear()

def loading():
    print ("\u001b[31;1mLoading PassGen ♪♪ ....\u001b[31;1m")
    print("\u001b[31;1mBe Pateints !\u001b[31;1m")
    for i in range (0,100):
        time.sleep(0.1)
        sys.stdout.write(u"\u001b[1000D" + str(i + 1) +  "%")
        sys.stdout.flush()
    print
loading()

def clear():

    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')
clear()


def banner():
    print(u" \u001b[31m____         _______  ______        ______ ____  __ __ \u001b[31m \u001b[0m")
    print(u"\u001b[31m|\u001b[34m  _  \__ _  /______/ /______/      / __   / __ \|  _  \ \u001b[31m  \u001b[0m")
    print(u"\u001b[31m| \u001b[34m|_) / _  |(/______ (/______      / |__| / ____/| | | | \u001b[31m    \u001b[0m")
    print(u"\u001b[31m|  __/ (_| | ______/) ______/)     \____,/\ ___/ |_| |_| \u001b[31m     \u001b[0m         ")
    print(u"\u001b[31m|_|  \____ |/______/ /______/      ___/ /                \u001b[31m   \u001b[0m ")
    print(u"\u001b[31m                                  /____/      \u001b[36m             \u001b[31m    \u001b[0m   ")
    print("\t \u001b[31m by:- \u001b[36m ♦♣ JOKERS™ \u001b[36m♣♦ \u001b[31m \u001b[0m ")

banner()

print("\n\n\u001b[36;1m[1] Default Length Password Generation")
print("[2] Customized Length Password Generation\u001b[36;1m")
while True:
    try:
        choice = int(input("\n\u001b[33;1m[→] Enter Your Choice : \u001b[33;1m"))
        break
    except ValueError:
        print("\u001b[31;1m[!] Invalid Option.\n[!] Try Again !\u001b[31;1m ")
        continue

while choice < 1:
    print("\u001b[31;1m[!] Invalid Option !\n[!] Try Again !\u001b[31;1m ")
    while True:
        try:
            choice = int(input("\n\u001b[33;1m[→] Enter Your Choice : \u001b[33;1m"))
            break
        except ValueError:
            print("\u001b[31;1m[!] Invalid Option.\n[!] Try Again ! \u001b[31;1m")
while choice < 1 :
    print("\u001b[31;1m[!] Invalid Option ! \n[!] Try Again !\u001b[31;1m ")
    break
    continue
while choice > 2 :
    print("\u001b[31;1m[!] Invalid Option !\n[!] Try Again !\u001b[31;1m ")
    while True:
        try:
            choice = int(input("\n\u001b[33;1m[→] Enter Your Choice : \u001b[33;1m"))
            break
        except ValueError:
            print("\u001b[31;1m[!] Invalid Option.\n[!] Try Again ! \u001b[31;1m")
while choice > 2 :
    print("\u001b[31;1m[!] Invalid Option ! \n[!] Try Again !\u001b[31;1m ")
    break
    continue
while choice == 1:
    len = 18
    chacrs = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!@#$%_-^&*():<?';/.,'[]{}\|/*-++?"
    key = ''.join(random.choice(chacrs)for x in range(len))
    print("\n\u001b[33;1m[+] Password Is Being Generated..! Be Pateints\u001b[33;1m")
    print("\u001b[32;1m[+] Your Authentication Key Is : \u001b[37;1m""[",key, "]")
    client = input("\n\u001b[32;1m[→] Do You Want To Change The PassPhrase y/n [ Default N]: \u001b[32;1m") 
    case = client.upper()
    while not re.match("^[Y&N]*$", case):
        print ("\u001b[31;1m[!] Error! Only letters Y/N allowed!\u001b[31;1m")
        client = input("\n\u001b[32;1m[→] Do You Want To Change The PassPhrase y/n [Default N] : \u001b[32;1m")
        case = client.upper()
        while not re.match("^[Y&N&" "]*$", case):
            print ("\u001b[31;1m[!] Error! Only letters Y/N allowed!\u001b[31;1m")
            break 
            continue
            if (case == "N" or " "):
                print("\t \n \u001b[34m -----------Thank You For Using PassGen ♪♪----------- \u001b[34m  \u001b[32m \t")
    while (case=="Y" ):
        len = 18
        chacrs = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!@#$%_-^&*():<?';/.,'[]{}\|/*-++?"
        key = ''.join(random.choice(chacrs)for x in range(len))
        print("\n\u001b[33;1m[+] Password Is Being Generated..! Be Pateints\u001b[33;1m")
        print("\u001b[32;1m[+] Your Authentication Key Is : \u001b[37;1m""[",key, "]")
        client = input("\n\u001b[32;1m[→] Do You Want To Change The PassPhrase y/n [ Default N]: \u001b[32;1m") 
        case = client.upper()
        while not re.match("^[Y&N]*$", case):
            print ("\u001b[31;1m[!] Error! Only letters Y/N allowed!\u001b[31;1m")
            client = input("\n\u001b[32;1m[→] Do You Want To Change The PassPhrase y/n : \u001b[32;1m")
            case = client.upper()
        while not re.match("^[Y&N&" "]*$", case):
            print ("\u001b[31;1m[!] Error! Only letters Y/N allowed!\u001b[31;1m")
            break 
            continue
            while (case =="Y"):
                continue
    while (case=="N" or " "):
        print("\t \n \u001b[34m -----------Thank You For Using PassGen ♪♪----------- \u001b[34m  \u001b[32m \t")
        break
    break

if choice == 2:
    def password():
        print("\nWelcome To Password Generator Designed By :- \u001b[36m JOKERS™  \u001b[36m\n")
        while True:
            try:
                len = int(input("\u001b[36;1m[→] Enter The Length Of The Password :  "))
                break
            except ValueError:
                print("\u001b[31;1m[!] Enter Length In Numbers.\u001b[31;1m")
                continue
        chacrs = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!@#$%_-^&*():<?';/.,'[]{}\|/*-++?"
        while (len<8):
            print("\u001b[31;1m[!] Cannot Generate Password Less Than 8. It Can Be Hacked Easily !\u001b[31;1m")
            print("\u001b[31;1m[!] Aborting !\u001b[31;1m")
            print("\u001b[32m[+] Continuing..! \u001b[32m ")
            while True:
                try:
                    len = int(input("\n\u001b[36;1m[→] Enter The Length Of The Password : \u001b[36;1m"))
                    break
                except ValueError:
                    print("\u001b[31;1m[!] Enter Length In Numbers. \u001b[31;1m")
                    continue
            chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!@#$%_-^&*():<?';/.,'[]{}\|/*-++?"
            continue
            break
        if (len>=8):
            print("\u001b[33;1m[+] Password Is Being Generated..! Be Pateints\u001b[33;1m")
            authenticationkey = ''.join(random.choice(chacrs)for _ in range (len)) 
            print("\u001b[32;1m[+] Your Authentication Key Is : \u001b[37;1m""[",authenticationkey, "]")
            client = input("\n\u001b[32;1m[→] Do You Want To Change The PassPhrase y/n [ Default N]: \u001b[32;1m") 
            case = client.upper()
            while not re.match("^[Y&N&" "]*$", case):
                print ("\u001b[31;1m[!] Error! Only letters Y/N allowed!\u001b[31;1m")
                client = input("\u001b[32;1m[→] Do You Want To Change The PassPhrase y/n [Default N]: \u001b[32;1m")
                case = client.upper()
            while not re.match("^[Y&N&" "]*$", case):
                print ("\u001b[31;1m[!] Error! Only letters Y/N allowed!\u001b[31;1m")
                break 
                continue
                if (case == "N" or " "):
                    print("\t \n \u001b[34m -----------Thank You For Using PassGen ♪♪----------- \t \n \u001b[34m")
            while (case=="Y"):
                while True:
                    try:
                        len = int(input("\n\u001b[36;1m[→] Enter The Length Of The Password : \u001b[36;1m"))
                        break
                    except ValueError:
                        print("\u001b[31;1m[!] Enter Length In Numbers.\u001b[31;1m")
                chacrs = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!@#$%_-^&*():<?';/.,'[]{}\|/*-++?"
                while (len<8):
                    print("\u001b[31;1m[!] Cannot Generate Password Less Than 8. It Can Be Hacked Easily !\u001b[31;1m")
                    print("\u001b[31;1m[!] Aborting !\u001b[31;1m")
                    print("\u001b[32m[+] Continuing\u001b[32m")
                    len = int(input("\n\u001b[34;1m[→] Enter The Length Of The Password : \u001b[34;1m"))
                    chacrs ="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!@#$%_-^&*():<?';/.,'[]{}\|/*-++?"
                    continue
                    break
                while (len>=8):
                    print("\u001b[33;1m[+] Password Is Being Generated..! Be Pateints\u001b[33;1m")
                    authenticationkey = ''.join(random.choice(chacrs)for _ in range (len)) 
                    print("\u001b[32;1m[+] Your Authentication Key Is : \u001b[37;1m""[",authenticationkey, "]")
                    break
                client = input("\n\u001b[32;1m[→] Do You Want To Change The PassPhrase y/n : \u001b[32;1m")
                case = client.upper()
                while not re.match("^[Y&N&" "]*$", case):
                    print ("\u001b[31;1m[!] Error! Only letters Y/N allowed!\u001b[31;1m")
                    client = input("\u001b[32;1m[→] Do You Want To Change The PassPhrase y/n : \u001b[32;1m")
                    case = client.upper()
                while not re.match("^[Y&N&" "]*$", case):
                    print ("\u001b[31;1m[!] Error! Only letters Y/N allowed!\u001b[31;1m")
                    break 
                    continue
                    while (case=="Y" ):
                        continue
                    while (case=="N" or " "):
                        print("\t \n \u001b[34m -----------Thank You For Using PassGen ♪♪----------- \u001b[34m  \u001b[32m \t")
                        break
            while (case=="N" or " "):
                print("\t \n \u001b[34m -----------Thank You For Using PassGen ♪♪----------- \u001b[34m  \u001b[32m \t")
                break

    password()
    