from widgets import *


class OtpWindow(Window):
    """Otp Window of the application"""

    def __init__(self, parent, controller):
        super().__init__(parent, controller)
        # Inheriting from the window class

        # Creating the navigation bar menus
        self.nav_bar.nav_menu(
            "Back to Login",
            action=lambda: self.controller.show_login_window()
        )

        # Adding the image
        self.add_image(self.controller.otp_window_image)

        self.body.left_frame.config(pady=45)
        self.entry_frame.config(pady=160)

        # Variables for storing inputs
        self.otp = StringVar()

        # Creating input box
        self.opt_input = InputBox(
            self.entry_frame,
            label="Enter the OTP: ",
            var=self.otp
        )

        self.add_inputs(
            inputs=[
                self.opt_input
            ]
        )

        # Verify button
        self.verify_btn = MyButton(
            self.entry_frame,
            text="Verify",
        )

        self.verify_btn.grid(row=2, column=0, columnspan=2, pady=(40, 0))
