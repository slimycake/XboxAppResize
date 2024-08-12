import ctypes
import subprocess
import sys
import os

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

##def install(package):
    ##subprocess.check_call([sys.executable, "-m", "pip", "install", package])

# Check and install necessary packages
##install("pygetwindow")
##install("pyautogui")

if not is_admin():
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
    sys.exit()

import pygetwindow as gw
import pyautogui
import time

def list_all_open_windows():
    print("Listing all open windows:")
    for window in gw.getAllWindows():
        print(f"Title: {window.title}")  # Just list the titles

def resize_and_reposition_xbox_app(x, y, width, height):
    try:
        # List all open windows for debugging
        list_all_open_windows()

        # Find the Xbox app window
        windows = gw.getWindowsWithTitle('Xbox')
        if not windows:
            print("No window with the title containing 'Xbox' found.")
            return
        
        window = windows[0]
        # If found, activate the window
        if window.isMinimized:
            window.restore()
        window.activate()
        
        # Resize and move the window
        window.resizeTo(width, height)
        window.moveTo(x, y)
        print(f"Window moved and resized to {x}, {y}, {width}x{height}.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Pause the program for 15 seconds before running the rest
time.sleep(15)

# Set desired position and size
x_position = 1100
y_position = 25
width = 800
height = 1000

resize_and_reposition_xbox_app(x_position, y_position, width, height)
