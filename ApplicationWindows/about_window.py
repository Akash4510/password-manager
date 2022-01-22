from widgets import *


class AboutWindow(Window):
    """About window of the application"""

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
        )
        self.nav_bar.add_nav_menu(
            "About",
            action=lambda: self.controller.show_about_window(),
            is_active=True
        )

        # Adding the page to the body
        self.add_body_frames(PageOne)

        self.body.show_frame(PageOne)


class PageOne(Body):

    def __init__(self, parent, controller):
        super().__init__(parent, controller)

        self.add_image(self.root_controller.about_window_image)
        self.left_frame.config(pady=45)
