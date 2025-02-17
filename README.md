# The Woodcutter: Cybersecurity for Grandma

## Features
- **Automated VPN Enforcement**: Ensures a VPN is active before allowing Tor usage.
- **Kill Switch**: Blocks all network activity if the VPN disconnects.
- **Fake Traffic Generation**: Simulates browsing activity to mask real usage (future update will make this dynamic based on trending sites).
- **Screen Size Randomization**: Prevents fingerprinting by adjusting browser dimensions.
- **User-Friendly Interface**: One-click security setup with no technical knowledge required.
- **Support and Troubleshooting**: Built-in diagnostic tools to resolve common issues (not yet tested).

## Getting Started
This project provides an automated security tool to ensure safe browsing through Tor by preventing leaks, automating VPN enforcement, and masking user behavior.

## Installation
### Clone the Repository
```sh
git clone https://github.com/yourusername/the-woodcutter.git
cd the-woodcutter
```

### Running the Script
1. Run `setup.py` to install dependencies:
   ```sh
   python setup.py
   ```
2. Start a secure browsing session:
   ```sh
   python privacy_wizard.py
   ```
3. If issues occur, run the troubleshooting script:
   ```sh
   python support.py
   ```

## System Requirements
- **Python 3.x**
- **A reliable VPN connection**
- **Tor Browser installed**

## Usage
- Running `privacy_wizard.py` enforces VPN usage before Tor can be accessed.
- The script automates security features like fake browsing traffic and fingerprint prevention.
- `support.py` helps diagnose issues related to VPN detection, network status, and dependencies.

## Customization
- Modify `privacy_wizard.py` to adjust the fake traffic generation behavior.
- Customize VPN enforcement parameters in `setup.py`.
- Future updates will allow for dynamic fake traffic pulling from trending sites.

## Troubleshooting
### Common Issues
- **VPN detection failures**: Ensure your VPN is connected before launching `privacy_wizard.py`.
- **Tor not launching**: Verify that Tor is installed and properly configured.
- **Dependency issues**: Run `setup.py` to reinstall missing dependencies.

## License
This project is licensed under the MIT License—free to use and modify while ensuring privacy and security for all users.

## Contributions
Contributions are welcome! Feel free to submit a pull request or report issues.

## Author
Developed by [chanda-mandisa].

