from widgets import *
from tkinter import messagebox


class RetrieveWindow(Window):

    def __init__(self, parent, controller):
        super().__init__(parent, controller)

        self.nav_bar.add_nav_menu(
            label="Add",
            action=lambda: self.controller.show_window("AddWindow"),
        )
        self.nav_bar.add_nav_menu(
            label="Retrieve",
            action=lambda: self.controller.show_window("RetrieveWindow"),
            is_active=True
        )
        self.nav_bar.add_nav_menu(
            label="Logout",
            action=lambda: self.logout(),
        )

        self.website_name = StringVar()
        self.username = StringVar()
        self.password = StringVar()

        self.add_pages(PageOne)

    def logout(self):
        """Logout the user"""

        # Take user confirmation
        user_response = messagebox.askyesno(
            title="Confirm Logout",
            message="DO YOU WANT TO LOG OUT OF YOUR ACCOUNT?"
        )

        # If the user confirmed logout, then log him out of the account
        if user_response:
            self.controller.logout_of_the_account()

        self.body.children_frames[PageOne].website_name_entry.entry.focus_set()

    def retrieve_password(self):
        """Retrieves password"""
        website = self.website_name.get().title()
        user_account = self.controller.currently_logged_in_account.get()

        if website.strip() == "":
            messagebox.showerror(
                title="Error",
                message="FIELDS CANNOT BE EMPTY!"
            )
            return

        passwords = self.controller.retrieve_password(user_account, website)
        if passwords is None:
            return

        for account, password in passwords.items():
            self.website_name.set(f"Website:    {website}")
            self.username.set(f"Username:    {account}")
            self.password.set(f"Password:    {password}")
            self.body.children_frames[PageOne].update_labels()
            break


class PageOne(Body):

    def __init__(self, parent, controller, **kw):
        super().__init__(parent, controller, **kw)

        self.heading_label = MyLabel(
            self,
            text="Enter the name of the website:",
            background=BODY_COLOR
        )
        self.heading_label.grid(row=0, column=0, pady=(30, 5), sticky=W)

        self.search_frame = Frame(self, bg=BODY_COLOR)
        self.search_frame.grid(row=1, column=0, pady=(10, 30))

        self.search_box = MyEntry(
            self.search_frame,
        )
        self.search_box.grid(row=1, column=0, sticky=E)
        self.search_box.config(width=66)

        self.search_btn = MyButton(
            self.search_frame,
            text="Search",
            command=lambda: print("Hello World!"),
            width=14,
        )
        self.search_btn.grid(row=1, column=1, padx=(10, 0), sticky=W)

        self.passwords_frame = Frame(self, bg=BODY_COLOR, )
        self.passwords_frame.grid(row=2, column=0, pady=(0, 500))
