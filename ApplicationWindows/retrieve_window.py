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

        self.logged_in_account = StringVar()

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
        user_account = self.logged_in_account.get()

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

        self.config(pady=60, padx=135)

        self.heading_label = MyLabel(
            self,
            text="Enter the name of the website you want to search password for.",
            background=BODY_COLOR
        )
        self.heading_label.grid(row=0, column=0, columnspan=2, pady=(20, 20))

        self.website_name_entry = TwoRowsInputBox(
            self,
            label="Website / Application name: ",
            var=self.parent_window.website_name
        )
        self.website_name_entry.entry.config(width=64)

        self.add_inputs([self.website_name_entry], from_row=1)

        self.website_name_label = MyLabel(self, text="Website: ", background=BODY_COLOR)
        self.website_name_label.grid(row=2, column=0, sticky=W, pady=(30, 0))

        self.username_label = MyLabel(self, text="Username: ", background=BODY_COLOR)
        self.username_label.grid(row=3, column=0, sticky=W, pady=(30, 0))

        self.password_label = MyLabel(self, text="Password: ", background=BODY_COLOR)
        self.password_label.grid(row=4, column=0, sticky=W, pady=(30, 0))

        self.search_btn = MyButton(
            self,
            text="Search",
            command=lambda: self.parent_window.retrieve_password()
        )
        self.search_btn.grid(row=5, column=0, columnspan=2, pady=(30, 0))
        self.search_btn.config(width=20)

    def update_labels(self):
        self.website_name_label.config(text=self.parent_window.website_name.get())
        self.username_label.config(text=self.parent_window.username.get())
        self.password_label.config(text=self.parent_window.password.get())
