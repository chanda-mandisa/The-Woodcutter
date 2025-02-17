# The Woodcutter: Cybersecurity for Grandma

## Overview
The Woodcutter is an intuitive, fully automated security tool designed for Tor users—simple enough for Grandma, yet strong enough for cybersecurity enthusiasts. It enforces VPN protection, blocks leaks, simulates fake browsing traffic, and prevents tracking with zero effort from the user.

## Features
- **Automated VPN Enforcement**: Ensures a VPN is active before allowing Tor usage.
- **Kill Switch**: Blocks all network activity if the VPN disconnects.
- **Fake Traffic Generation**: Simulates browsing activity to mask real usage (future update will make this dynamic based on trending sites).
- **Screen Size Randomization**: Prevents fingerprinting by adjusting browser dimensions.
- **User-Friendly Interface**: One-click security setup with no technical knowledge required.
- **Support and Troubleshooting**: Built-in diagnostic tools to resolve common issues (not yet tested).

---

## Scripts Breakdown
### 1. `setup.py` - Installation and System Check
**Purpose**: This script ensures that all prerequisites are met before running The Woodcutter.

**Key Functions:**
- **Python Installation**: Detects if Python is installed. If not, it downloads and installs it automatically.
- **Library Installation**: Installs required dependencies, including `pyautogui`, `cryptography`, and `tk`.
- **Automated Setup**: Runs all checks and installations with minimal user intervention, making it accessible for non-technical users.

**Important Notes:**
- Everything **after the VPN check in `privacy_wizard.py` is untested**, so its effectiveness is still unknown.

### 2. `privacy_wizard.py` - Tor Security Automation
**Purpose**: Launches a secure Tor browsing session with enhanced privacy protections.

**Key Functions:**
- **VPN Enforcement**: Ensures a VPN connection is active before launching Tor by checking external IP changes.
- **Automated Security Features**: Implements fake browsing traffic and randomized screen sizes to prevent tracking.
- **Kill Switch**: Monitors VPN status and shuts down Tor and internet access if VPN disconnects.
- **User Interface**: Provides a simple GUI for easy operation.
- **Real-Time Monitoring**: Continuously checks for VPN stability and prevents leaks.

**Important Notes:**
- The **VPN detection mechanism has failed in all tests so far**, meaning we haven't been able to verify whether the rest of the script functions as intended.
- Future updates will improve **fake traffic generation** by dynamically pulling trending sites instead of using a static list.

### 3. `support.py` - Maintenance and Troubleshooting
**Purpose**: Provides tools for diagnosing issues, troubleshooting connection problems, and maintaining The Woodcutter’s security features.

**Key Functions:**
- **Log Analysis**: Scans system logs and VPN status to identify connection issues.
- **Manual VPN Status Check**: Confirms VPN connectivity outside the automated process.
- **Dependency Fixes**: Detects and reinstalls missing or outdated components.
- **Tor Connection Test**: Ensures Tor is configured correctly and running securely.
- **Network Reset Option**: Provides a fallback mechanism to restore network connectivity in case of a forced kill switch activation.

**Important Notes:**
- `support.py` **has not been tested yet**, and we are unsure how well it functions.

---

## Installation
### Step 1: Download & Run `setup.py`
1. Download `setup.py` and run it with Python.
2. Follow any prompts to install Python (if required).
3. Allow the script to install necessary dependencies.
4. Once setup is complete, proceed to the next step.

### Step 2: Start Secure Browsing
- Run `privacy_wizard.py` to launch a protected Tor session.
- The script will attempt to handle security automatically.
- Due to current VPN detection failures, **this step may not function properly**.

Important Notes:

- VPN detection has failed in all tests so far, meaning we haven’t verified whether the rest of the script functions as intended.
- Future updates will improve fake traffic generation by dynamically pulling trending sites instead of using a static list.

### Step 3: Troubleshoot Issues (Optional)
- If you experience connection issues or VPN detection failures, run `support.py`.
- Check the logs for error messages or missing dependencies.
- Use the manual VPN status check to confirm a stable connection.
- Restart The Woodcutter if necessary.

---

## Security Considerations
- Ensure your VPN is running **before** launching the tor browser.
- Always keep the software up to date for the latest security patches.
- The Woodcutter is designed to be intuitive—no complex configurations needed!

For any issues, check `support.py` or open a GitHub issue.

---

## License
This project is licensed under the MIT License—free to use and modify while ensuring privacy and security for all users.

**Contribute**: If you have improvements, feel free to submit a pull request!

