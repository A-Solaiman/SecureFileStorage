from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox, QFileDialog, QLineEdit
from signinUI import Ui_MainWindow as signin_Ui_MainWindow  # Import the generated UI class for sign-in
from signupUI import Ui_MainWindow as signup_Ui_MainWindow  # Import the generated UI class for sign-up
from mainUI import Ui_MainWindow as mainui_Ui_MainWindow  # Import the generated UI class for main menu
import logger as metadata_logger
import auth, encryption

USERS_DB = "users.db"


class LoginWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = signin_Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.passwordField.setEchoMode(QLineEdit.EchoMode.Password)

        # Connect buttons to their respective methods
        self.ui.signinButton.clicked.connect(self.handle_login)
        self.ui.regHereButton.clicked.connect(self.open_signup_window)
        self.ui.eyeButton.clicked.connect(self.toggle_password_visibility)

        # Track password visibility state
        self.password_visible = False

    def toggle_password_visibility(self):
        """Toggle the visibility of the password field."""
        if self.password_visible:
            self.ui.passwordField.setEchoMode(QLineEdit.EchoMode.Password)
            self.password_visible = False
        else:
            self.ui.passwordField.setEchoMode(QLineEdit.EchoMode.Normal)
            self.password_visible = True

    def handle_login(self):
        username = self.ui.usernameField.text().strip()
        password = self.ui.passwordField.text().strip()

        if not username or not password:
            self.ui.statLeb.setText("All fields must be filled!")
            return

        try:
            result = auth.login(username, password)
        except Exception as e:
            self.ui.statLeb.setText(f"An error occurred: {e}")
            return

        if result == "Login successful!":
            self.ui.statLeb.setText("You are now logged in!")
            self.open_main_menu(username)
        else:
            self.ui.statLeb.setText(result)

    def open_signup_window(self):
        self.close()  # Close the login window
        self.signup_window = SignupWindow()  # Open the signup window
        self.signup_window.show()

    def open_main_menu(self, username):
        self.close()  # Close the login window
        self.main_menu = MainMenu(username)  # Open the main menu
        self.main_menu.show()


class SignupWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.login_window = None
        self.ui = signup_Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.passwordField.setEchoMode(QLineEdit.EchoMode.Password)

        # Connect buttons to their respective methods
        self.ui.signUpButton.clicked.connect(self.handle_signup)
        self.ui.signInHere.clicked.connect(self.open_login_window)
        self.ui.eyeButton.clicked.connect(self.toggle_password_visibility)

        # Track password visibility state
        self.password_visible = False

    def toggle_password_visibility(self):
        """Toggle the visibility of the password field."""
        if self.password_visible:
            self.ui.passwordField.setEchoMode(QLineEdit.EchoMode.Password)
            self.password_visible = False
        else:
            self.ui.passwordField.setEchoMode(QLineEdit.EchoMode.Normal)
            self.password_visible = True

    def handle_signup(self):
        # Get user input from fields
        username = self.ui.usernameField.text().strip()
        password = self.ui.passwordField.text().strip()

        # Validate input fields
        if not username or not password:
            self.ui.statLeb.setText("All fields must be filled!")
            return

        # Attempt registration
        try:
            result = auth.register(username, password)  # Call the registration function
        except Exception as e:
            self.ui.statLeb.setText(f"An error occurred: {e}")  # Handle unexpected exceptions
            return

        # Handle registration result
        if result == "Registration successful!":
            QMessageBox.information(self, "Success", "Registration successful! You can now log in.")
            self.open_login_window()  # Return to login window after successful registration
        elif result == "Sorry, username already exists :(":
            self.ui.statLeb.setText(result)
        else:
            self.ui.statLeb.setText(
                "Password must be at least 8 characters long and must contain at least one of the each followings: A-Z, a-z, 0-9 and a special character (#, $, %, ^, & etc)"
            )  # Display error message from auth.register()

    def open_login_window(self):
        self.close()  # Close the signup window
        self.login_window = LoginWindow()  # Open the login window
        self.login_window.show()


class MainMenu(QMainWindow):
    def __init__(self, username):
        super().__init__()
        self.ui = mainui_Ui_MainWindow()  # Use the main menu UI class
        self.username = username  # Store the username for later use
        self.ui.setupUi(self)

        # Set the username in the window title or somewhere on the UI
        self.setWindowTitle(f"Welcome {username}")
        self.ui.welcomeLabel.setText(f"Welcome, {username}!")  # Assuming there is a welcome label in the UI

        # Variable to store the selected file path
        self.selected_file = None

        # Connect UI buttons to their respective functions
        self.ui.selectButton.clicked.connect(self.select_file)  # "+" button to select a file
        self.ui.encButton.clicked.connect(lambda: self.encrypt_file(self.username))  # Pass username explicitly
        self.ui.decButton.clicked.connect(lambda: self.decrypt_file(self.username))  # Pass username explicitly
        self.ui.histButton.clicked.connect(self.view_log_history)
        self.ui.logOutButton.clicked.connect(self.logout)

    def select_file(self):
        """Opens a file picker dialog and stores the selected file path."""
        file_path, _ = QFileDialog.getOpenFileName(self, "Select File to Encrypt")
        if file_path:  # If a file is selected
            self.selected_file = file_path
            self.ui.filePathField.setText(file_path)  # Update the UI to show the selected file path
        else:
            self.ui.filePathField.setText("No file selected")

    def encrypt_file(self, username):
        """Handles the encryption of the selected file."""
        if not self.selected_file:
            QMessageBox.warning(self, "Error", "Please select a file to encrypt.")
            return

        password = self.ui.passcodeField.text().strip()  # Get the password from the input field
        if not password:
            QMessageBox.warning(self, "Error", "Please enter a password.")
            return

        # Call the encryption function
        result = encryption.encrypt_file(self.selected_file, password)
        metadata_logger.log_action(username, "Encryption", self.selected_file)
        self.ui.statLeb.setText(result)  # Show the result in a message box

    def decrypt_file(self, username):
        """Handles the decryption of the selected file."""
        if not self.selected_file:
            QMessageBox.warning(self, "Error", "Please select a file to decrypt.")
            return

        password = self.ui.passcodeField.text().strip()  # Get the password from the input field
        if not password:
            QMessageBox.warning(self, "Error", "Please enter a password.")
            return

        # Call the decryption function
        result = encryption.decrypt_file(self.selected_file, password)
        metadata_logger.log_action(username, "Decryption", self.selected_file)
        self.ui.statLeb.setText(result)  # Show the result in a message box

    def view_log_history(self):
        """Opens a dialog to show the content of actions.log"""
        try:
            with open("actions.log", "r") as log_file:
                log_data = log_file.read()  # Read the log file
        except FileNotFoundError:
            log_data = "Log file not found."

        # Display log in a message box
        QMessageBox.information(self, "Log History", log_data)

    def logout(self):
        """Handles logging out and redirecting to the sign-in window."""
        self.close()  # Close the main menu
        self.login_window = LoginWindow()  # Open the login window
        self.login_window.show()


if __name__ == "__main__":
    app = QApplication([])
    window = LoginWindow()
    window.show()
    app.exec()
