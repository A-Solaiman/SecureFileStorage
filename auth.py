import re
import os
import hashlib

USERS_DB = "users.db"

def hash_password(password):
    """Hashes the password using SHA-256."""
    return hashlib.sha256(password.encode()).hexdigest()

def password_strength_checker(password):
    """Checks the strength of a password."""
    if len(password) < 8:
        return "Password must be at least 8 characters long."
    if not any(char.isupper() for char in password):
        return "Password must contain at least one uppercase letter."
    if not any(char.islower() for char in password):
        return "Password must contain at least one lowercase letter."
    if not any(char.isdigit() for char in password):
        return "Password must contain at least one number."
    if not any(char in "!@#$%^&*()-_+=<>?/|~`" for char in password):
        return "Password must contain at least one special character."
    return "Strong"

def register(username, password):
    """Registers a new user if the password is strong."""
    # Check password strength
    password_strength = password_strength_checker(password)
    if password_strength != "Strong":
        return f"Registration failed: {password_strength}"

    # Hash the password and save it
    hashed_password = hash_password(password)
    with open(USERS_DB, "a") as db:
        db.write(f"{username},{hashed_password}\n")
    return "Registration successful!"

def login(username, password):
    """Logs in a user if the credentials match."""
    if not os.path.exists(USERS_DB):
        return "No users registered. Please register first."

    hashed_password = hash_password(password)
    with open(USERS_DB, "r") as db:
        for line in db:
            stored_username, stored_hashed_password = line.strip().split(",")
            if stored_username == username and stored_hashed_password == hashed_password:
                return "Login successful!"
    return "Invalid username or password."
