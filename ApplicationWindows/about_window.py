from widgets import *


class AboutWindow(Window):

    def __init__(self, parent, controller):
        super().__init__(parent, controller)
        # Inheriting from the window class

        # Creating the navigation bar menus
        self.nav_bar.nav_menu(
            "SignUp",
            action=lambda: self.controller.show_signup_window_first_page(),
        )
        self.nav_bar.nav_menu(
            "Login",
            action=lambda: self.controller.show_login_window()
        )
        self.nav_bar.nav_menu(
            "About",
            action=lambda: self.controller.show_about_window(),
            is_active=True
        )

        # Adding the image
        self.add_image(self.controller.about_window_image)
        self.body.left_frame.config(pady=45)
