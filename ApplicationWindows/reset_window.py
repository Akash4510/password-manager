from widgets import *


class ResetWindow(Window):

    def __init__(self, parent, controller):
        super().__init__(parent, controller)
        # Inheriting from the window class

        # Creating the navigation bar menus
        self.nav_bar.nav_menu(
            "Back to Login",
            action=lambda: self.controller.show_login_window()
        )

        # Adding the image
        self.add_image(self.controller.signup_window_image)

        self.entry_frame.config(pady=120)

        # Variables for storing inputs
        self.new_password = StringVar()
        self.confirm_password = StringVar()

        # Creating input box
        self.new_password_input = InputBox(
            self.entry_frame,
            label="Enter new password: ",
            var=self.new_password
        )
        self.confirm_password_input = InputBox(
            self.entry_frame,
            label="Confirm new password: ",
            var=self.confirm_password
        )

        self.add_inputs(
            inputs=[
                self.new_password_input,
                self.confirm_password_input
            ]
        )

        # Verify button
        self.change_btn = MyButton(
            self.entry_frame,
            text="Change Password",
        )

        self.change_btn.grid(row=4, column=0, columnspan=2, pady=(40, 0))
