import os
import subprocess
import sys

def is_python_installed():
    """ Checks if Python is installed by running `python --version`. """
    try:
        subprocess.run(["python", "--version"], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return True
    except subprocess.CalledProcessError:
        return False
    except FileNotFoundError:
        return False

def install_python():
    """ Downloads and installs the latest version of Python. """
    print("Python is not installed. Downloading and installing...")
    python_installer_url = "https://www.python.org/ftp/python/3.11.4/python-3.11.4-amd64.exe"  # Modify for latest version
    installer_path = os.path.join(os.getcwd(), "python_installer.exe")
    
    subprocess.run(["powershell", "-Command", f"Invoke-WebRequest -Uri {python_installer_url} -OutFile {installer_path}"], check=True)
    subprocess.run([installer_path, "/quiet", "InstallAllUsers=1", "PrependPath=1"], check=True)
    print("Python installed successfully. Reboot required.")
    os.remove(installer_path)
    sys.exit("Reboot and run this script again.")

def install_required_libraries():
    """ Installs required Python libraries and ensures NumPy compatibility. """
    required_libraries = ["pyautogui", "cryptography", "tk"]
    for lib in required_libraries:
        subprocess.run(["python", "-m", "pip", "install", lib], check=True)
    
    # Fix NumPy compatibility by installing a version that works with TensorFlow
    subprocess.run(["python", "-m", "pip", "install", "numpy==1.26.4"], check=True)

def check_vpn_status():
    """ Checks if a VPN connection is active using Windows network settings. """
    try:
        output = subprocess.check_output("ipconfig", shell=True, text=True)
        if "ProtonVPN" in output or "TAP-Windows Adapter" in output:
            print("VPN is active.")
            return True
        else:
            print("No active VPN detected. Please connect manually.")
            return False
    except subprocess.CalledProcessError:
        print("Error checking VPN status.")
        return False

def main():
    print("Checking for Python installation...")
    if not is_python_installed():
        install_python()
    
    print("Checking and installing required Python libraries...")
    install_required_libraries()
    
    print("Checking VPN status...")
    check_vpn_status()
    
    print("Setup complete! Python, dependencies, and VPN checks are ready.")

if __name__ == "__main__":
    main()
