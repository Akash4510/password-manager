from widgets import *


class AddWindow(Window):

    def __init__(self, parent, controller):
        super().__init__(parent, controller)
        # Inheriting from the window class

        # Creating the navigation bar menus
        self.nav_bar.nav_menu(
            "Add",
            action=lambda: self.controller.show_add_window(),
            is_active=True
        )
        self.nav_bar.nav_menu(
            "Retrieve",
            action=lambda: self.controller.show_retrieve_window()
        )
        self.nav_bar.nav_menu(
            "Logout",
            action=lambda: self.controller.show_login_window()
        )

        # Adding the image
        self.add_image(self.controller.add_window_image)

        # Variables for storing inputs
        self.website_name = StringVar()
        self.website_url = StringVar()
        self.username = StringVar()
        self.password = StringVar()

        # Creating input boxes
        self.website_name_input = InputBox(
            self.entry_frame,
            label="App / Website name: ",
            var=self.website_name
        )
        self.website_url_input = InputBox(
            self.entry_frame,
            label="Website url (optional): ",
            var=self.website_url
        )
        self.username_input = InputBox(
            self.entry_frame,
            label="Username / email: ",
            var=self.username
        )
        self.password_input = InputBox(
            self.entry_frame,
            label="Enter the password: ",
            var=self.password
        )

        # Placing the input boxes on the screen
        self.add_inputs(
            inputs=[
                self.website_name_input,
                self.website_url_input,
                self.username_input,
                self.password_input
            ],
            gap=20
        )
        self.entry_frame.config(pady=50)

        # Save button
        self.save_btn = MyButton(
            self.entry_frame,
            text="Save password",
        )

        self.save_btn.grid(row=8, column=0, columnspan=2, pady=(40, 0))
