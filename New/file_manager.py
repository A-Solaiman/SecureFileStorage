import os
import shutil

SECURE_DIR = "SecureFiles"
DECRYPTED_DIR = "DecryptedFiles"

def initialize_directories():
    """Create necessary directories if they don't exist."""
    if not os.path.exists(SECURE_DIR):
        os.makedirs(SECURE_DIR)
    if not os.path.exists(DECRYPTED_DIR):
        os.makedirs(DECRYPTED_DIR)

def list_files(directory):
    """List all files in the specified directory."""
    if not os.path.exists(directory):
        return f"Directory '{directory}' does not exist."
    files = os.listdir(directory)
    if not files:
        return "No files found."
    return files

def move_to_secure(file_path):
    """Move a file to the SecureFiles directory."""
    if not os.path.exists(file_path):
        return f"File '{file_path}' does not exist."
    destination = os.path.join(SECURE_DIR, os.path.basename(file_path))
    shutil.move(file_path, destination)
    return f"File '{file_path}' moved to '{SECURE_DIR}'."

def move_to_decrypted(file_path):
    """Move a file to the DecryptedFiles directory."""
    if not os.path.exists(file_path):
        return f"File '{file_path}' does not exist."
    destination = os.path.join(DECRYPTED_DIR, os.path.basename(file_path))
    shutil.move(file_path, destination)
    return f"File '{file_path}' moved to '{DECRYPTED_DIR}'."
