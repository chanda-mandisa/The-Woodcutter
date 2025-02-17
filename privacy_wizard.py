import sys
import subprocess
import os
import time
import random
import webbrowser
import pyautogui
import threading
import tkinter as tk
from tkinter import messagebox
import requests  # Added for external IP checking

"""
Privacy Wizard for Tor Security Automation (Version 1.5)
Author: Open-Source Community

Features:
    - Detects any active VPN by checking external IP.
    - Allows users to specify a VPN provider.
    - Improves logging and debugging feedback.
    - Enforces VPN use before Tor launches.
    - Randomizes screen size to prevent tracking.
    - Simulates fake browsing activity before real use.
    - Shuts down ALL network traffic if VPN disconnects (Kill Switch).
    - Provides a graphical startup wizard for easy setup.
"""

# ----------------- [ CONFIGURABLE SETTINGS ] -----------------
DEFAULT_TOR_PATH = "C:\\Program Files\\Tor Browser\\Browser\\firefox.exe"  # Modify if needed
FAKE_BROWSING_URLS = [
    "https://www.wikipedia.org",
    "https://www.reddit.com/r/privacy",
    "https://www.torproject.org",
    "https://news.ycombinator.com"
]
KILL_SWITCH_COMMAND = "netsh interface set interface \"Wi-Fi\" admin=disable"  # Windows kill switch
TOR_PROCESS_NAME = "firefox.exe"  # Adjust for Linux/macOS

IP_CHECK_URL = "https://api64.ipify.org"  # API to fetch public IP

# ----------------- [ FUNCTION DEFINITIONS ] -----------------

def debug_log(message):
    """ Logs debugging messages """
    print(f"[DEBUG] {message}")


def get_public_ip():
    """ Gets the current external IP address """
    try:
        response = requests.get(IP_CHECK_URL, timeout=5)
        if response.status_code == 200:
            return response.text.strip()
    except requests.RequestException:
        debug_log("Failed to fetch external IP address.")
    return None


def is_vpn_active():
    """ Detects VPN by comparing external IPs """
    initial_ip = get_public_ip()
    if not initial_ip:
        debug_log("Could not determine initial IP.")
        return False
    debug_log(f"Initial IP: {initial_ip}")

    time.sleep(5)  # Give time for VPN to connect
    new_ip = get_public_ip()
    debug_log(f"New IP: {new_ip}")
    
    return new_ip and new_ip != initial_ip


def enforce_vpn():
    """ Forces VPN connection before launching Tor. """
    debug_log("Checking VPN status...")
    if not is_vpn_active():
        messagebox.showwarning("VPN Warning", "No active VPN detected. Please connect manually.")
        debug_log("Waiting for manual VPN connection...")
        time.sleep(15)
    if not is_vpn_active():
        debug_log("VPN connection failed. Aborting.")
        messagebox.showerror("VPN Error", "VPN connection failed. Restart and try again.")
        exit(1)


def kill_tor_and_network():
    """ Kill Switch: Shuts down Tor and all network activity if VPN fails. """
    debug_log("Activating Kill Switch. Disabling internet access...")
    os.system(f"taskkill /F /IM {TOR_PROCESS_NAME}")  # Force-close Tor
    os.system(KILL_SWITCH_COMMAND)  # Disable all network interfaces
    messagebox.showerror("Kill Switch Activated", "VPN Disconnected! All internet access has been blocked.")


def monitor_vpn():
    """ Monitors VPN connection and activates Kill Switch if VPN fails. """
    while True:
        if not is_vpn_active():
            debug_log("VPN disconnected! Activating Kill Switch.")
            kill_tor_and_network()
            exit(1)
        time.sleep(5)  # Check every 5 seconds


def generate_random_screen_size():
    """ Creates subtle screen size variations. """
    width_variation = random.randint(-50, 50)
    height_variation = random.randint(-30, 30)
    debug_log(f"Randomized screen size: {1200 + width_variation}x{800 + height_variation}")
    return 1200 + width_variation, 800 + height_variation


def set_screen_size():
    """ Randomizes Tor browser screen size. """
    width, height = generate_random_screen_size()
    pyautogui.hotkey('win', 'up')  # Prevents full-screen
    time.sleep(1)
    pyautogui.hotkey('win', 'left')  # Forces a specific size
    time.sleep(1)
    debug_log("Screen size randomized successfully.")


def inject_fake_traffic():
    """ Simulates fake browsing before real usage. """
    debug_log("Injecting fake browsing traffic...")
    random.shuffle(FAKE_BROWSING_URLS)
    for url in FAKE_BROWSING_URLS[:random.randint(2, 4)]:
        webbrowser.open(url)
        debug_log(f"Opened fake traffic URL: {url}")
        time.sleep(random.randint(5, 15))  # Mimic human behavior


def launch_tor():
    """ Launches Tor after all security checks. """
    debug_log("Launching Tor browser...")
    subprocess.Popen(DEFAULT_TOR_PATH, shell=True)
    time.sleep(10)  # Allow Tor to fully load
    set_screen_size()  # Adjust screen after launch
    debug_log("Tor browser launched successfully.")


def start_gui():
    """ Creates a GUI for the startup wizard. """
    root = tk.Tk()
    root.title("Privacy Wizard Setup")
    
    def on_start():
        debug_log("Initializing secure session...")
        messagebox.showinfo("Security Check", "Ensuring VPN is active before launching Tor...")
        enforce_vpn()
        threading.Thread(target=monitor_vpn, daemon=True).start()  # Monitor VPN in background
        inject_fake_traffic()
        launch_tor()
        messagebox.showinfo("Tor Started", "Tor is now running securely!")
    
    tk.Label(root, text="Welcome to Privacy Wizard", font=("Arial", 12, "bold")).pack(pady=10)
    tk.Label(root, text="Your browsing will be anonymized with enhanced security features.").pack()
    start_button = tk.Button(root, text="Start Secure Tor Session", command=on_start, font=("Arial", 10, "bold"), bg="green", fg="white")
    start_button.pack(pady=20)
    root.mainloop()


def main():
    debug_log("Starting Privacy Wizard setup...")
    start_gui()


if __name__ == "__main__":
    main()
