import ctypes
import subprocess
import sys
import os
import requests
import time

CURRENT_VERSION = "1.2"

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

def check_for_updates():
    script_url = "https://raw.githubusercontent.com/slimycake/XboxAppResize/main/APPRESIZE.py"
    version_url = "https://raw.githubusercontent.com/slimycake/XboxAppResize/main/version.txt"
    try:
        response = requests.get(version_url)
        latest_version = response.text.strip()
        if latest_version > CURRENT_VERSION:
            print("New version available. Updating...")
            update_script(script_url)
        else:
            print("You are running the latest version.")
    except requests.exceptions.RequestException as e:
        print(f"Failed to check for updates: {e}")

def update_script():
    print("Update available. Starting the updater.")
    try:
        # Exit the current application
        sys.exit("Exiting for update...")
    except SystemExit as e:
        # Start the updater script
        subprocess.run([sys.executable, "updater.exe"], check=True)


if not is_admin():
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
    sys.exit()

check_for_updates()  # Check for updates at the start of the program

# Check and install necessary packages
install("pygetwindow")
install("pyautogui")

import pygetwindow as gw
import pyautogui

def list_all_open_windows():
    print("Listing all open windows:")
    for window in gw.getAllWindows():
        print(f"Title: {window.title}")

def resize_and_reposition_xbox_app(x, y, width, height):
    try:
        list_all_open_windows()
        windows = gw.getWindowsWithTitle('Xbox')
        if not windows:
            print("No window with the title containing 'Xbox' found.")
            return
        window = windows[0]
        if window.isMinimized:
            window.restore()
        window.activate()
        window.resizeTo(width, height)
        window.moveTo(x, y)
        print(f"Window moved and resized to {x}, {y}, {width}x{height}.")
    except Exception as e:
        print(f"An error occurred: {e}")

time.sleep(1)  # Pause the program for 15 seconds before running the rest
x_position = 1100
y_position = 25
width = 800
height = 1000

resize_and_reposition_xbox_app(x_position, y_position, width, height)
