from widgets import *


class LoginWindow(Window):
    """Login window of the application"""

    def __init__(self, parent, controller):
        super().__init__(parent, controller)
        # Inheriting from the Window Class

        # Creating the navigation bar menus
        self.nav_bar.nav_menu(
            "SignUp",
            action=lambda: self.controller.show_signup_window_1()
        )
        self.nav_bar.nav_menu(
            "Login",
            action=lambda: self.controller.show_login_window(),
            is_active=True
        )
        self.nav_bar.nav_menu(
            "About",
            action=lambda: self.controller.show_about_window()
        )

        # Adding the image
        self.add_image(self.controller.login_window_image)

        # Variables for storing inputs
        self.email = StringVar()
        self.password = StringVar()

        # Creating input boxes
        self.email_input = InputBox(
            self.entry_frame,
            label="Enter your email: ",
            var=self.email
        )
        self.password_input = InputBox(
            self.entry_frame,
            label="Enter your password: ",
            var=self.password
        )
        self.password_input.input_box.config(show="*")

        # Placing the input boxes on the screen
        self.add_inputs(
            inputs=[
                self.email_input,
                self.password_input
            ]
        )
        self.entry_frame.config(pady=115)

        # Variable for toggling the password visibility
        self.show_pass_var = IntVar()

        # Checkbox to control the visibility of the password.
        show_password = ttk.Checkbutton(
            self.entry_frame,
            text="Show Password",
            variable=self.show_pass_var,
            command=lambda: self.toggle_password_visibility()
        )
        show_password.grid(row=4, column=0, pady=(20, 0), sticky=W)

        # Login button
        self.login_btn = MyButton(
            self.entry_frame,
            text="Login",
            command=lambda: self.controller.show_add_window(),
        )
        self.login_btn.grid(row=5, column=0, columnspan=2, pady=(30, 0))

    def toggle_password_visibility(self):
        """Toggles the visibility of the password input"""
        value = self.show_pass_var.get()
        if value == 1:
            self.password_input.input_box.config(show="")
        elif value == 0:
            self.password_input.input_box.config(show="*")
