import os
import os.path
import json
from tkinter import *
from tkinter import ttk, messagebox
from theme import *
from ApplicationWindows import *
from functions import *

DATA_FOLDER = os.path.join(os.getcwd(), "Data")
USERS_FOLDER = os.path.join(DATA_FOLDER, "Users")


class PasswordManager(Tk):

    def __init__(self):
        Tk.__init__(self)

        app_width = 850
        app_height = 570

        # This will give us the screen width and screen height.
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        x = (screen_width / 2) - (app_width / 2)
        y = (screen_height / 2) - (app_height / 2)

        # This will display the application in the center of the screen.
        self.geometry(f"{app_width}x{app_height}+{int(x)}+{int(y)}")
        self.maxsize(width=app_width, height=app_height)

        # Setting title logo and background color
        self.title("MyPass - PasswordManager")
        self.wm_iconbitmap("Assets/Logo/padlock.ico")
        self.config(bg=BODY_COLOR)

        # Setting the style(theme) of the application
        self.style = ttk.Style(self)
        self.call("source", "Assets/Theme/proxttk-dark.tcl")
        self.style.theme_use("proxttk-dark")

        # Setting up a default x_padding for the whole application
        self.x_padding = 60

        # Now we will create a container for the frames, which itself would be a frame.
        container = Frame(self, width=app_width, height=app_height, bg=BODY_COLOR)
        container.pack(side=TOP, fill=BOTH, expand=TRUE)

        container.grid_rowconfigure(index=0, weight=1)
        container.grid_columnconfigure(index=0, weight=1)

        # Creating all the image elements
        self.lock_icon = PhotoImage(file="Assets/Images/lock.png")
        self.nav_bar_logo = PhotoImage(file="Assets/Logo/nav_bar_logo.png")
        self.login_window_image = PhotoImage(file="Assets/Images/add_window.png")
        self.signup_window_image = PhotoImage(file="Assets/Images/signup_window.png")
        self.otp_window_image = PhotoImage(file="Assets/Images/otp_window.png")
        self.reset_window_image = PhotoImage(file="Assets/Images/reset_window.png")
        self.add_window_image = PhotoImage(file="Assets/Images/add_window.png")
        self.retrieve_window_image = PhotoImage(file="Assets/Images/retrieve_window.png")
        self.about_window_image = PhotoImage(file="Assets/Images/otp_window.png")

        self.password_saved_successfully = False

        # Now we will create a list of all the windows for our application.
        self.windows = [LoginWindow, SignupWindow, AboutWindow, AddWindow]
        self.frames = {}

        # All the windows for our application would be a class inherited from the Frame class, which will take two
        # arguments - parent and controller. The class PasswordManager itself is the controller so we will pass "self"
        # as the controller for all our windows.
        for F in self.windows:
            frame = F(container, self)
            # In the above line we passed parent as the container and self as the controller.
            self.frames[F.__name__] = frame
            frame.grid(row=0, column=0, sticky=NSEW)

        self.frames["LoginWindow"].email.set("akash@email.com")
        self.frames["LoginWindow"].password.set("Akash@1234")
        self.show_window("LoginWindow")

    def show_window(self, window):
        """This function will display the window we want."""
        frame = self.frames[window]
        frame.tkraise()

    @staticmethod
    def create_new_account(first_name: str, last_name: str, email: str, password: str):
        """Creates a new user account"""

        # If the user is using the application for the first time, we will make sure all the data folder exists
        if "Data" not in os.listdir(os.getcwd()):
            os.mkdir(DATA_FOLDER)
            os.mkdir(USERS_FOLDER)

        if "Users" not in os.listdir(DATA_FOLDER):
            os.mkdir(USERS_FOLDER)

        # If the user already exists we will display the message and return from the function
        if email in os.listdir(USERS_FOLDER):
            messagebox.showinfo(
                title="USER ALREADY EXISTS!",
                message=f"THE USER :  '{email}'  IS ALREADY REGISTERED\n\n"
                        f"GO TO THE LOGIN PAGE TO LOGIN TO YOUR ACCOUNT."
            )
            return
        # Else we will make the new folder for the user
        else:
            os.mkdir(f"{USERS_FOLDER}/{email}")

        # Path for the key file and the data file for the user.
        key_file_path = os.path.join(USERS_FOLDER, email, f"user_key.key")
        data_file_path = os.path.join(USERS_FOLDER, email, f"user_data.json")

        # Generating the new key for the user
        user_key = generate_new_key()

        # Adding the key into the key file of the user
        with open(key_file_path, "wb") as key_file:
            key_file.write(user_key)

        # Encrypting the master password of the user
        encrypted_master_password = encrypt_password(password, user_key)

        new_data = {
            "user_details": {
                "first_name": first_name.title(),
                "last_name": last_name.title(),
                "name": f"{first_name} {last_name}".title(),
                "email": email,
                "master_password": encrypted_master_password,
            }
        }

        # Adding the new data into the data file of the user
        with open(data_file_path, "w") as data_file:
            json.dump(new_data, data_file, indent=4)

        # Displaying the success message to the user.
        messagebox.showinfo(
            title="Sign Up Successful",
            message=("YOUR ACCOUNT HAS BEEN CREATED SUCCESSFULLY.\n\n\n"
                     "YOU MUST REMEMBER YOUR MASTER PASSWORD YOU JUST CREATED TO LOGIN TO YOUR ACCOUNT. "
                     "IN CASE YOU FORGET IT, YOU CANNOT RETRIEVE YOUR PASSWORDS")
        )

    def login_to_account(self, email, password):
        """Login to the user's account"""

        # Checking if the user entered a valid email address
        if not valid_email(email):
            messagebox.showerror(
                title="Login Error",
                message=f"PLEASE ENTER A VALID EMAIL ADDRESS!"
            )
            return

        # Checking if there exists the data and the users folder
        if "Data" not in os.listdir(os.getcwd()):
            messagebox.showwarning(
                title="Login Error",
                message="THERE ARE NO USERS IN OUR DATABASE.\n"
                        "PLEASE CREATE AN ACCOUNT BY SIGNING UP, TO USE THE APPLICATION"
            )
            self.show_window("SignupWindow")
            return
        if "Users" not in os.listdir(DATA_FOLDER):
            messagebox.showwarning(
                title="Login Error",
                message="THERE ARE NO USERS IN OUR DATABASE.\n\n"
                        "PLEASE CREATE AN ACCOUNT BY SIGNING UP, TO USE THE APPLICATION"
            )
            self.show_window("SignupWindow")
            return

        # Checking if the user is a registered user.
        if email.lower() not in os.listdir(USERS_FOLDER):
            messagebox.showerror(
                title="Login Error",
                message=f"THE USER : '{email}' DOES NOT EXISTS. PLEASE SIGNUP TO CREATE AN ACCOUNT!"
            )
            return

        # Path for the key file and the data file for the user.
        key_file_path = os.path.join(USERS_FOLDER, email, f"user_key.key")
        data_file_path = os.path.join(USERS_FOLDER, email, f"user_data.json")

        # Getting the actual master password and the key of the user
        with open(data_file_path, "r") as data_file:
            users_data = json.load(data_file)
            encrypted_password = users_data["user_details"]["master_password"]

        with open(key_file_path, "rb") as key_file:
            user_key = key_file.read()

        # Decrypting the actual password
        actual_password = decrypt_password(encrypted_password, user_key)

        # Checking if the user entered the correct password
        if password != actual_password:
            messagebox.showerror(
                title="Login Error",
                message=f"INVALID PASSWORD FOR THE USER : {email}!"
            )
            return

        # If everything is correct login to the user's account
        self.show_window("AddWindow")
        self.frames["AddWindow"].logged_in_account.set(email)
        self.frames["AddWindow"].username.set(email)

    def logout_of_the_account(self):
        """Logs the user out of the account"""
        self.show_window("LoginWindow")

    def add_new_password(self, for_user: str, web_name: str, web_url: str, username: str, password: str):
        """Saves a new password in the user's account"""

        if web_name.strip() == "" or username.strip() == "" or password.strip() == "":
            messagebox.showerror(
                title="Error!",
                message="FIELDS CANNOT BE EMPTY!"
            )
            return

        web_name = web_name.title()

        account_email = for_user.lower()
        user_data_file = os.path.join(USERS_FOLDER, account_email, "user_data.json")
        user_key_file = os.path.join(USERS_FOLDER, account_email, "user_key.key")

        # Getting the user's data and the key
        with open(user_data_file, "r") as data_file:
            data = json.load(data_file)

        with open(user_key_file, "rb") as key_file:
            user_key = key_file.read()

        encrypted_password = encrypt_password(password, user_key)

        # If the user has never saved a password before
        if "passwords" not in data.keys():
            data["passwords"] = {}

        if web_name in data["passwords"].keys():
            # If the website url is not present we will add it
            if "website_url" not in data["passwords"][web_name].keys():
                data["passwords"][web_name]["website_url"] = web_url
            else:
                previous_url = data["passwords"][web_name]["website_url"]
                if previous_url.strip() == "":
                    data["passwords"][web_name]["website_url"] = web_url
                else:
                    if web_url != previous_url and web_url.strip() != "":
                        user_res_to_change_url = messagebox.askyesno(
                            title="URL Conflict",
                            message=f"YOU HAVE PREVIOUSLY SAVED THE URL FOR '{web_name.capitalize()}' as "
                                    f"'{previous_url}\nDO YOU WANT TO CHANGE IT TO '{web_url}'"
                        )
                        if user_res_to_change_url:
                            data["passwords"][web_name]["website_url"] = web_url

            # If no password is saved for the given website
            if "accounts" not in data["passwords"][web_name].keys():
                data["passwords"][web_name]["accounts"] = {}

            if username in data["passwords"][web_name]["accounts"].keys():
                user_wants_to_update_password = messagebox.askyesno(
                    title="Confirm Update",
                    message=f"PASSWORD FOR '{web_name.upper()}',\nUSERNAME: {username} ALREADY EXISTS!\n"
                            f"DO YOU WANT TO UPDATE IT?"
                )
                if not user_wants_to_update_password:
                    return

            data["passwords"][web_name]["accounts"][username] = encrypted_password

        else:
            data["passwords"][web_name] = {
                "website_url": web_url,
                "accounts": {
                    username: encrypted_password,
                }
            }

        user_confirmation = messagebox.askyesnocancel(
            title="Confirm Details",
            message="PLEASE CONFIRM THE FOLLOWING DETAILS:\n\n"
                    f"WEBSITE: {web_name}\n"
                    f"URL: {web_url}\n"
                    f"USERNAME: {username}\n"
                    f"PASSWORD: {password}\n\n"
                    f"DO YOU WANT TO SAVE IT?"
        )
        print(f"{user_confirmation=}")

        if user_confirmation:
            with open(user_data_file, "w") as data_file:
                json.dump(data, data_file, indent=4)

            messagebox.showinfo(
                title="Success",
                message="PASSWORD SAVED SUCCESSFULLY!"
            )
            self.password_saved_successfully = True

    def run(self):
        self.mainloop()


if __name__ == '__main__':
    app = PasswordManager()
    app.run()
