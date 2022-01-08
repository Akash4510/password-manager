from widgets import *


class RetrieveWindow(Window):

    def __init__(self, parent, controller):
        super().__init__(parent, controller)
        # Inheriting from the window class

        # Creating the navigation bar menus
        self.nav_bar.nav_menu(
            "Add",
            action=lambda: self.controller.show_add_window()
        )
        self.nav_bar.nav_menu(
            "Retrieve",
            action=lambda: self.controller.show_retrieve_window(),
            is_active=True
        )
        self.nav_bar.nav_menu(
            "Logout",
            action=lambda: self.controller.show_login_window()
        )

        # Adding the image
        self.add_image(self.controller.retrieve_window_image)

        # Variables for storing inputs
        self.website_name = StringVar()
        self.username = StringVar()

        # Creating input boxes
        self.website_name_input = InputBox(
            self.entry_frame,
            label="App / Website name: ",
            var=self.website_name
        )
        self.username_input = InputBox(
            self.entry_frame,
            label="Username / email: ",
            var=self.username
        )

        # Placing the input boxes on the screen
        self.add_inputs(
            inputs=[
                self.website_name_input,
                self.username_input,
            ],
            gap=20
        )
        self.entry_frame.config(pady=120)

        # Retrieve button
        self.retrieve_btn = MyButton(
            self.entry_frame,
            text="Retrieve password",
        )

        self.retrieve_btn.grid(row=5, column=0, columnspan=2, pady=(40, 0))
