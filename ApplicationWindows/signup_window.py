from widgets import *


class SignupWindow1(Window):

    def __init__(self, parent, controller):
        super().__init__(parent, controller)
        # Inheriting from the window class

        # Creating the navigation bar menus
        self.nav_bar.nav_menu(
            "SignUp",
            action=lambda: self.controller.show_signup_window_1(),
            is_active=True
        )
        self.nav_bar.nav_menu(
            "Login",
            action=lambda: self.controller.show_login_window()
        )
        self.nav_bar.nav_menu(
            "About",
            action=lambda: self.controller.show_about_window()
        )

        # Adding the image
        self.add_image(self.controller.signup_window_image)

        # Variables for storing inputs
        self.first_name = StringVar()
        self.last_name = StringVar()
        self.email = StringVar()

        # Creating input boxes
        self.first_name_input = InputBox(
            self.entry_frame,
            label="Enter your first name: ",
            var=self.first_name
        )
        self.last_name_input = InputBox(
            self.entry_frame,
            label="Enter your last name: ",
            var=self.first_name
        )
        self.email_input = InputBox(
            self.entry_frame,
            label="Enter your email: ",
            var=self.email
        )

        # Placing the input boxes on the screen
        self.add_inputs(
            inputs=[
                self.first_name_input,
                self.last_name_input,
                self.email_input,
            ],
            gap=20
        )
        self.entry_frame.config(pady=100)

        # Proceed button
        self.proceed_btn = MyButton(
            self.entry_frame,
            text="Proceed",
            width=18,
            command=self.controller.show_signup_window_2
        )

        self.proceed_btn.grid(row=6, column=0, columnspan=2, pady=(30, 0))


class SignupWindow2(Window):

    def __init__(self, parent, controller):
        super().__init__(parent, controller)
        # Inheriting from the window class

        # Creating the navigation bar menus
        self.nav_bar.nav_menu(
            "SignUp",
            action=lambda: self.controller.show_signup_window_1(),
            is_active=True
        )
        self.nav_bar.nav_menu(
            "Login",
            action=lambda: self.controller.show_login_window()
        )
        self.nav_bar.nav_menu(
            "About",
            action=lambda: self.controller.show_about_window()
        )

        # Adding the image
        self.add_image(self.controller.signup_window_image)

        # Variables for storing inputs
        self.password = StringVar()
        self.confirm_password = StringVar()

        # Creating input boxes
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
                self.password_input,
                self.cnf_pass_input
            ],
            gap=20
        )
        self.entry_frame.config(pady=120)

        # Signup button
        self.signup_btn = MyButton(
            self.entry_frame,
            text="Create account",
            width=18
        )

        self.signup_btn.grid(row=4, column=0, columnspan=2, pady=(30, 0))
