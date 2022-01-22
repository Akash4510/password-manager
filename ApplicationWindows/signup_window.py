from widgets import *


class SignupWindow(Window):
    """Signup window for the application"""

    def __init__(self, parent, controller):
        super().__init__(parent, controller)

        # Creating the navigation bar menus
        self.nav_bar.add_nav_menu(
            "SignUp",
            action=lambda: self.controller.show_signup_window(),
            is_active=True
        )
        self.nav_bar.add_nav_menu(
            "Login",
            action=lambda: self.controller.show_login_window()
        )
        self.nav_bar.add_nav_menu(
            "About",
            action=lambda: self.controller.show_about_window()
        )

        # Variables to store inputs
        self.first_name = StringVar()
        self.last_name = StringVar()
        self.email = StringVar()
        self.password = StringVar()
        self.confirm_password = StringVar()

        # Adding the page to the body
        self.add_body_frames(PageOne, PageTwo)

        self.body.show_frame(PageOne)


class PageOne(Body):

    def __init__(self, parent, controller):
        super().__init__(parent, controller)

        self.add_image(self.root_controller.signup_window_image)

        self.first_name_input = InputBox(
            self.right_frame,
            label="Enter your first name: ",
            var=self.parent_window.first_name
        )
        self.last_name_input = InputBox(
            self.right_frame,
            label="Enter your last name: ",
            var=self.parent_window.last_name
        )
        self.email_input = InputBox(
            self.right_frame,
            label="Enter your email: ",
            var=self.parent_window.email
        )

        self.add_inputs([self.first_name_input, self.last_name_input, self.email_input])

        self.proceed_btn = MyButton(
            self.right_frame,
            text="Proceed",
            command=lambda: self.controller.show_frame(PageTwo)
        )
        self.proceed_btn.grid(row=3, column=0, columnspan=2, pady=(30, 0))

        self.right_frame.config(pady=55)


class PageTwo(Body):

    def __init__(self, parent, controller):
        super().__init__(parent, controller)

        self.add_image(self.root_controller.signup_window_image)

        self.password_input = InputBox(
            self.right_frame,
            label="Create a password: ",
            var=self.parent_window.password
        )
        self.cnf_pass_input = InputBox(
            self.right_frame,
            label="Confirm password: ",
            var=self.parent_window.confirm_password
        )

        self.password_input.entry.config(show="*")

        self.add_inputs([self.password_input, self.cnf_pass_input])

        self.previous_btn = ttk.Button(
            self.right_frame,
            text="Go back",
            width=12,
            command=lambda: self.controller.show_frame(PageOne)
        )
        self.previous_btn.grid(row=2, column=0, columnspan=1, sticky=W, pady=(30, 0))
        self.previous_btn.config(style=None)

        self.signup_btn = MyButton(
            self.right_frame,
            text="Create account",
            width=20,
            command=lambda: print("Signup button clicked!")
        )
        self.signup_btn.grid(row=2, column=1, columnspan=1, sticky=E, pady=(30, 0))

        self.right_frame.config(pady=90)
