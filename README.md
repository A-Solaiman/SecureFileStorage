# Secure File Storage System

## Overview

The **Secure File Storage System** is a Python-based application designed to securely store files through encryption and decryption. The system includes user authentication, AES-based encryption, and metadata logging to track file actions. It also features a file management module to organize files into designated directories.

## Features

- **User Authentication**: Users can register and log in securely.
- **File Encryption/Decryption**: AES encryption and decryption for protecting files.
- **Metadata Logging**: Logs file actions, including encryption and decryption, with timestamps.
- **File Manager**: Organizes encrypted and decrypted files in separate directories (`SecureFiles` and `DecryptedFiles`).

## Requirements

- Python 3.x
- `pycryptodome` library for AES encryption

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/A-Solaiman/SecureFileStorage.git
