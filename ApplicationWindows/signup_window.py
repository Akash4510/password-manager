from widgets import *


class SignupWindow(Window):

    def __init__(self, parent, controller):
        super().__init__(parent, controller)
        # Inheriting from the window class

        # Creating the navigation bar menus
        self.nav_bar.nav_menu(
            "SignUp",
            action=lambda: self.controller.show_signup_window(),
            is_active=True
        )
        self.nav_bar.nav_menu(
            "Login",
            action=lambda: self.controller.show_login_window()
        )
        self.nav_bar.nav_menu(
            "About",
            action=lambda: print("About button clicked")
        )

        # Adding the image
        self.add_image(self.controller.signup_window_image)

        # Variables for storing inputs
        self.name = StringVar()
        self.email = StringVar()
        self.password = StringVar()
        self.confirm_password = StringVar()

        # Creating input boxes
        self.name_input = InputBox(
            self.entry_frame,
            label="Enter your name: ",
            var=self.name
        )
        self.email_input = InputBox(
            self.entry_frame,
            label="Enter your email: ",
            var=self.email
        )
        self.password_input = InputBox(
            self.entry_frame,
            label="Create a password: ",
            var=self.password
        )
        self.cnf_pass_input = InputBox(
            self.entry_frame,
            label="Confirm password: ",
            var=self.confirm_password
        )

        self.password_input.input_box.config(show="*")

        # Placing the input boxes on the screen
        self.add_inputs(
            inputs=[
                self.name_input,
                self.email_input,
                self.password_input,
                self.cnf_pass_input
            ],
            gap=20
        )
        self.entry_frame.config(pady=50)

        # Signup button
        self.signup_btn = MyButton(
            self.entry_frame,
            text="Create account",
            width=18
        )

        self.signup_btn.grid(row=8, column=0, columnspan=2, pady=(40, 0))
