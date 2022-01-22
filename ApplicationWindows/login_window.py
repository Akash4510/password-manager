from widgets import *


class LoginWindow(Window):
    """Login window of the application"""

    def __init__(self, parent, controller):
        super().__init__(parent, controller)

        # Creating the navigation bar menus
        self.nav_bar.add_nav_menu(
            "SignUp",
            action=lambda: self.controller.show_signup_window(),
        )
        self.nav_bar.add_nav_menu(
            "Login",
            action=lambda: self.controller.show_login_window(),
            is_active=True
        )
        self.nav_bar.add_nav_menu(
            "About",
            action=lambda: self.controller.show_about_window(),
        )

        # Variables to store inputs
        self.email = StringVar()
        self.password = StringVar()

        # Adding the page to the body
        self.add_body_frames(PageOne)

        self.body.show_frame(PageOne)


class PageOne(Body):

    def __init__(self, parent, controller):
        super().__init__(parent, controller)

        self.add_image(self.root_controller.login_window_image)

        self.email_input = InputBox(
            self.right_frame,
            label="Enter your email: ",
            var=self.parent_window.email
        )
        self.password_input = InputBox(
            self.right_frame,
            label="Enter your password: ",
            var=self.parent_window.password
        )
        self.password_input.entry.config(show="*")

        self.add_inputs([self.email_input, self.password_input])

        self.show_pass_var = IntVar()
        show_password = ttk.Checkbutton(
            self.right_frame,
            text="Show Password",
            variable=self.show_pass_var,
            command=lambda: self.toggle_password_visibility()
        )
        show_password.grid(row=2, column=0, pady=(20, 0), sticky=W)

        self.login_btn = MyButton(
            self.right_frame,
            text="Login",
            command=lambda: print("Login button clicked!")
        )
        self.login_btn.grid(row=3, column=0, columnspan=2, pady=(30, 0))

        self.right_frame.config(pady=80)

    def toggle_password_visibility(self):
        """Toggles the visibility of the password input"""
        value = self.show_pass_var.get()
        if value == 1:
            self.password_input.entry.config(show="")
        elif value == 0:
            self.password_input.entry.config(show="*")
