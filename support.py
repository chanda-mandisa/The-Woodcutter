import os
import sys
import hashlib
import json
import time
import logging
from cryptography.fernet import Fernet

"""
Support Script for Privacy Wizard Security
Ensures:
- Unique encryption for each instance of the executable
- Log generation for debugging and security testing
- Integrity verification for open-source transparency

This script handles:
1. Encryption of executable downloads to prevent tracking
2. Logging system health, debugging info, and errors
3. Generating and verifying hashes for integrity checks
"""

# Setup Logging
LOG_DIR = "logs"
os.makedirs(LOG_DIR, exist_ok=True)
logging.basicConfig(
    filename=os.path.join(LOG_DIR, "support.log"),
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def generate_unique_key():
    """ Generates a unique encryption key for each instance. """
    key = Fernet.generate_key()
    with open("encryption_key.key", "wb") as key_file:
        key_file.write(key)
    logging.info("Unique encryption key generated.")
    return key

def encrypt_file(file_path, key):
    """ Encrypts a given file using the provided key. """
    with open(file_path, "rb") as file:
        data = file.read()
    cipher = Fernet(key)
    encrypted_data = cipher.encrypt(data)
    
    with open(file_path, "wb") as file:
        file.write(encrypted_data)
    
    logging.info(f"File {file_path} encrypted successfully.")

def generate_hash(file_path):
    """ Generates a SHA256 hash of the given file. """
    sha256_hash = hashlib.sha256()
    try:
        with open(file_path, "rb") as f:
            for byte_block in iter(lambda: f.read(4096), b""):
                sha256_hash.update(byte_block)
        file_hash = sha256_hash.hexdigest()
        logging.info(f"Generated hash for {file_path}: {file_hash}")
        return file_hash
    except Exception as e:
        logging.error(f"Failed to generate hash for {file_path}: {e}")
        return None

def verify_integrity(file_path, expected_hash):
    """ Verifies if the file's hash matches the expected hash. """
    actual_hash = generate_hash(file_path)
    if actual_hash == expected_hash:
        logging.info(f"Integrity check PASSED for {file_path}.")
        return True
    else:
        logging.warning(f"Integrity check FAILED for {file_path}.")
        return False

def system_check():
    """ Collects system information for debugging purposes. """
    system_info = {
        "os": os.name,
        "platform": sys.platform,
        "python_version": sys.version,
        "timestamp": time.strftime("%Y-%m-%d %H:%M:%S")
    }
    with open(os.path.join(LOG_DIR, "system_info.json"), "w") as sys_file:
        json.dump(system_info, sys_file, indent=4)
    logging.info("System information logged successfully.")

def main():
    logging.info("Starting Support Script...")
    system_check()
    
    # Encrypt the executable
    key = generate_unique_key()
    file_to_encrypt = "privacy_wizard.exe"  # Modify based on actual file name
    if os.path.exists(file_to_encrypt):
        encrypt_file(file_to_encrypt, key)
        
    # Generate and store hash for integrity verification
    hash_value = generate_hash(file_to_encrypt)
    if hash_value:
        with open("integrity_check.txt", "w") as hash_file:
            hash_file.write(hash_value)
        logging.info("Integrity hash stored.")
    
    logging.info("Support script execution complete.")

if __name__ == "__main__":
    main()
