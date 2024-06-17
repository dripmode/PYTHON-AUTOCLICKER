import os
import time
from pynput.mouse import Button, Controller
import keyboard

R = "\033[91m"
Y = "\033[93m"
G = "\033[92m"
CY = "\033[96m"
W = "\033[0m"

mouse = Controller()

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def click():
    mouse.press(Button.left)
    mouse.release(Button.left)

def main():
    clear_screen()
    print(CY + """
____________________________________________________________
    """ + R + """      nohaksjustping clicker """ + CY + """v1""" + CY + """
""" + R + """    >>""" + Y + """------------------------------------------------""" + CY + """
        dev: nohaksjustping | https://github.com/dripmode
""" + Y + """    ------------------------------------------------<<""" + R + """
____________________________________________________________
""")
    print("""
""" + Y + """1. Hold down the 'X' key to start clicking.
""" + CY + """2. Release the 'X' key to stop clicking.

    """)
    while True:
        if keyboard.is_pressed('x'):
            time.sleep(0.05)
            click()
            break

if __name__ == "__main__":
    main()