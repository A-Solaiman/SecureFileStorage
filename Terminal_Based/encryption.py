from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Protocol.KDF import PBKDF2
import os

SALT_FILE = "salt.bin"  # File to store the encryption salt

def derive_key(password):
    """Derives a 256-bit key from the password using PBKDF2."""
    salt = get_salt()
    key = PBKDF2(password, salt, dkLen=32, count=1000000)
    return key

def get_salt():
    """Generates or retrieves the salt for key derivation."""
    if os.path.exists(SALT_FILE):
        with open(SALT_FILE, "rb") as f:
            return f.read()
    else:
        salt = get_random_bytes(16)
        with open(SALT_FILE, "wb") as f:
            f.write(salt)
        return salt

def encrypt_file(file_path, password):
    """Encrypts a file using AES."""
    key = derive_key(password)
    cipher = AES.new(key, AES.MODE_GCM)
    nonce = cipher.nonce

    if not os.path.exists(file_path):
        return "Encryption failed! File not found."
    
    with open(file_path, "rb") as f:
        plaintext = f.read()

    ciphertext, tag = cipher.encrypt_and_digest(plaintext)

    # Save the encrypted file
    with open(file_path + ".enc", "wb") as f:
        f.write(nonce)
        f.write(tag)
        f.write(ciphertext)

    os.remove(file_path)  # Remove the original file
    return f"File '{file_path}' encrypted successfully!"

def decrypt_file(encrypted_file_path, password):
    """Decrypts an AES-encrypted file."""
    key = derive_key(password)

    if not os.path.exists(encrypted_file_path):
        return "Decryption failed! File not found."

    with open(encrypted_file_path, "rb") as f:
        nonce = f.read(16)
        tag = f.read(16)
        ciphertext = f.read()

    cipher = AES.new(key, AES.MODE_GCM, nonce=nonce)

    try:
        plaintext = cipher.decrypt_and_verify(ciphertext, tag)
    except ValueError:
        return "Incorrect password or file is corrupted!"

    # Save the decrypted file
    decrypted_file_path = encrypted_file_path.replace(".enc", "")
    with open(decrypted_file_path, "wb") as f:
        f.write(plaintext)

    os.remove(encrypted_file_path)  # Remove the encrypted file
    return f"File '{encrypted_file_path}' decrypted successfully!"
