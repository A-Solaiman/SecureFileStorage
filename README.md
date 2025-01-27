# Secure File Storage System

## Overview

The **Secure File Storage System** is a Python-based application designed to securely store files through encryption and decryption. The system includes user authentication, AES-based encryption, and metadata logging to track file actions.
***You can find the source code in the "New" subfolder***
The Terminal_Based subfolder includes the alpha version of the software which was terminal based with some dependencies (like python 3.00 or above and some external libraries e.g. *pycryptodome* ). You can check that out too. :)


## How to run??

- Download the standalone software from Google Drive using this link: https://drive.google.com/file/d/1e7qLY2plxC5ryeOyoFAbFmUbwQc29t8i/view?usp=sharing
- Note that: during download or running process you may get warnings, just ignore them.
- No need to install anything. Just click and run, and you're good to go.
- For first-time users: You need to create an account first. Click the Register Here button in the bottom right corner.
- Input a username and a strong password of your choice.
- After successfully creating an account, you will be redirected to the sign-in window. Use the username and password of the account you created.
- After the user is logged in: Use the "+" icon to select a file, and input a passcode (remember: this passcode is unrecoverable, so write it down somewhere else if the selected file is valuable).
- Encrypt or decrypt files by clicking the corresponding buttons. The log history and log out buttons work as well.

## Features

- **User Authentication**: Users can register and log in securely.
- **File Encryption/Decryption**: AES encryption and decryption for protecting files.
- **Metadata Logging**: Logs file actions, including encryption and decryption, with timestamps.
- **File Manager**: Organizes encrypted and decrypted files in separate directories (`SecureFiles` and `DecryptedFiles`).

## Requirements

**Hardware Requirements:**
- Processor: Dual-core or better
- RAM: 4 GB minimum
- Storage: 100 MB of free space
**Software Requirements:**
- Operating System: Windows 10 or Windows 11


## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/A-Solaiman/SecureFileStorage.git
