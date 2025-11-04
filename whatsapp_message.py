# "import a as b" means that b is declared as an abbreviation of module a

from time import sleep # The sleep submodule is used to pause the script, using sleep(seconds)
import os # The os module is used to interact with the operating system, here it is used to delete files
import pywhatkit as pwk # The pywhatkit module is used to send whatsapp messages
import pyautogui as pag # The pyautogui module is used to control the mouse and keyboard, here it is used to move the mouse cursor

def clearTerminalScreen(): # Inspired by GeeksForGeeks clear terminal screen script
    if os.name == "nt":
        _ = os.system('cls') # For Windows
    else:
        _ = os.system('clear') # For Unix based distros

while True: # This line onwards will always run unless the value of variable menu == 2

    menu = input("Please enter\n1. Send Whatsapp message\n2. Exit\n--> ")
    while (menu.isdigit() == False) or (int(menu) != 1 and int(menu) != 2): # Forces the user to enter exactly 1 or 2
        sleep(2)
        clearTerminalScreen()
        menu = input("Invalid input\nTry again:\n\nPlease enter\n1. Send Whatsapp message\n2. Exit\n--> ")
    menu = int(menu)

    if menu == 1:
        target_phone_number = input("Please enter your recepients international phone number, omitting the leading plus (\"+\")\n--> ")
        while target_phone_number.isdigit() == False:
            target_phone_number = input("That is not a valid phone number\nTry again\n--> ")
            clearTerminalScreen()
        target_phone_number = f"+{target_phone_number}"
        message_to_send = input("What would you like to send your recipient?\n--> ")
        clearTerminalScreen()
        pwk.sendwhatmsg_instantly(target_phone_number,message_to_send,wait_time=5,tab_close=False)
        
        pag.moveTo(0,0)
        
        logfile_keep = input("Message sent!\nWould you like to keep the logfile created by pywhatkit? (y/n)\n--> ")
        while logfile_keep.lower() != "y" and logfile_keep.lower() != "n":
            clearTerminalScreen()
            logfile_keep = input("Invalid input\nTry again\nWould you like to keep the logfile created by pywhatkit? (y/n)\n--> ")
        if logfile_keep.lower() == "n":
            clearTerminalScreen()
            os.remove("pywhatkit_log.txt")
            print("Logfile deleted")

    else:
        False
        clearTerminalScreen()
        break

