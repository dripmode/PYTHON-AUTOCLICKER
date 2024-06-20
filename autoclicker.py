import os
import time
from pynput.mouse import Button, Controller
import keyboard
R, Y, G, CY, W = "\033[91m", "\033[93m", "\033[92m", "\033[96m", "\033[0m"
mouse = Controller()
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
def click():
    mouse.press(Button.left)
    mouse.release(Button.left)
def print_ui(cps):
    clear_screen()
    print(f"{CY}\n{'_'*60}\n{R}      nohaksjustping clicker {CY}v1.1\n{R}    >>{Y}{'-'*48}{CY}\n        dev: nohaksjustping | https://github.com/dripmode\n{Y}{'-'*48}{R}\n{'_'*60}\n")
    print(f"{Y}1. Hold down the 'X' key to start clicking.\n{CY}2. Release the 'X' key to stop clicking.\n{G}3. Use 'E' to increase CPS.\n4. Use 'Q' to decrease CPS.\n")
    bar_length = 20
    progress = int((cps / 20) * bar_length)
    progress_bar = G + "█" * progress + Y + "█" * (bar_length - progress)
    print(f"\n{CY}CPS: [{progress_bar}{CY}] {cps}{Y}\n")
def main():
    cps = 14
    click_delay = 1 / cps
    print_ui(cps)
    while True:
        if keyboard.is_pressed('x'):
            while keyboard.is_pressed('x'):
                click()
                time.sleep(click_delay)
        if keyboard.is_pressed('e'):
            cps = min(20, cps + 1)
            click_delay = 1 / cps
            print_ui(cps)
            time.sleep(0.3)
        if keyboard.is_pressed('q'):
            cps = max(1, cps - 1)
            click_delay = 1 / cps
            print_ui(cps)
            time.sleep(0.3)
        time.sleep(0.01)
if __name__ == "__main__":
    main()
