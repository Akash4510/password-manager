from widgets import *
from tkinter import messagebox


class AddWindow(Window):

    def __init__(self, parent, controller):
        super().__init__(parent, controller)

        self.nav_bar.add_nav_menu(
            label="Add",
            action=lambda: print("Hello World"),
            is_active=True
        )
        self.nav_bar.add_nav_menu(
            label="Retrieve",
            action=lambda: print("Hello World"),
        )
        self.nav_bar.add_nav_menu(
            label="Logout",
            action=lambda: self.logout(),
        )

    def logout(self):
        """Logout the user"""

        # Take user confirmation
        user_response = messagebox.askyesno(
            title="Confirm Logout",
            message="Do you want to log out from your account?"
        )

        # If the user confirmed logout, then log him out of the account
        if user_response:
            self.controller.show_window("LoginWindow")
