import auth
import encryption
import logger as metadata_logger
import file_manager
import os

USERS_DB = "users.db"

def main():
    print("Welcome to Secure File Storage System")
    logged_in_user = None

    # Initialize necessary directories
    file_manager.initialize_directories()

    while True:
        if not logged_in_user:
            print("\nMenu:")
            print("1. Register")
            print("2. Login")
            print("3. Exit")
            choice = input("Enter your choice: ")

            if choice == "1":
                username = input("Enter username: ")
                with open(USERS_DB, "r") as db:
                    userexists = False
                    for line in db:
                        stored_username, _ = line.strip().split(",")
                        if stored_username == username:
                            print("Sorry! Username already exists.")
                            userexists = True
                            break
                    if not userexists:
                        print("Password must contain at least: \n\t8 characters\n\tOne uppercase letter\n\tOne lowercase letter\n\tOne special character\n\tOne number")
                        password = input("Enter password: ")
                        print(auth.register(username, password))
            elif choice == "2":
                username = input("Enter username: ")
                password = input("Enter password: ")
                if auth.login(username, password) == "Login successful!":
                    print("You are now logged in!")
                    logged_in_user = username
                else:
                    print("Login failed! Invalid username or password.")
            elif choice == "3":
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")
        else:
            print("\nSecure File Storage System Menu:")
            print("1. Encrypt File")
            print("2. Decrypt File")
            print("3. View Logs")
            print("4. Manage Files")
            print("5. Logout")
            choice = input("Enter your choice: ")

            if choice == "1":
                file_path = input("Enter the path of the file to encrypt: ")
                password = input("Enter your password: ")
                result = encryption.encrypt_file(file_path, password)
                print(result)
                metadata_logger.log_action(logged_in_user, "Encryption", file_path)
                file_manager.move_to_secure(file_path + ".enc")
            elif choice == "2":
                encrypted_file_path = input("Enter the path of the file to decrypt: ")
                password = input("Enter your password: ")
                result = encryption.decrypt_file(encrypted_file_path, password)
                print(result)
                metadata_logger.log_action(logged_in_user, "Decryption", encrypted_file_path)
                file_manager.move_to_decrypted(encrypted_file_path.replace(".enc", ""))
            elif choice == "3":
                print("\nLog Entries:")
                print(metadata_logger.view_logs())
            elif choice == "4":
                print("\nFile Management Menu:")
                print("1. List Encrypted Files")
                print("2. List Decrypted Files")
                sub_choice = input("Enter your choice: ")

                if sub_choice == "1":
                    files = file_manager.list_files(file_manager.SECURE_DIR)
                    print("Encrypted Files:", files)
                elif sub_choice == "2":
                    files = file_manager.list_files(file_manager.DECRYPTED_DIR)
                    print("Decrypted Files:", files)
                else:
                    print("Invalid choice.")
            elif choice == "5":
                print("Logged out successfully!")
                logged_in_user = None
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
