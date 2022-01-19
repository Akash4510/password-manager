from tkinter import *
from tkinter import ttk
from theme import *
from ApplicationWindows import *


class PasswordManager(Tk):

    def __init__(self):
        Tk.__init__(self)

        app_width = 850
        app_height = 570

        # This will give us the screen width and screen height.
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        x = (screen_width / 2) - (app_width / 2)
        y = (screen_height / 2) - (app_height / 2)

        # This will display the application in the center of the screen.
        self.geometry(f"{app_width}x{app_height}+{int(x)}+{int(y)}")
        self.maxsize(width=app_width, height=app_height)

        # Setting title logo and background color
        self.title("MyPass - PasswordManager")
        self.wm_iconbitmap("Assets/Logo/padlock.ico")
        self.config(bg=BODY_COLOR)

        # Setting the style(theme) of the application
        self.style = ttk.Style(self)
        self.call("source", "Assets/Theme/proxttk-dark.tcl")
        self.style.theme_use("proxttk-dark")

        # Setting up a default x_padding for the whole application
        self.x_padding = 60

        # Now we will create a container for the frames, which itself would be a frame.
        container = Frame(self, width=app_width, height=app_height, bg=BODY_COLOR)
        container.pack(side=TOP, fill=BOTH, expand=TRUE)

        container.grid_rowconfigure(index=0, weight=1)
        container.grid_columnconfigure(index=0, weight=1)

        # Creating all the image elements
        self.nav_bar_logo = PhotoImage(file="Assets/Logo/nav_bar_logo.png")
        self.login_window_image = PhotoImage(file="Assets/Images/login_window.png")
        self.signup_window_image = PhotoImage(file="Assets/Images/signup_window.png")
        self.otp_window_image = PhotoImage(file="Assets/Images/otp_window.png")
        self.reset_window_image = PhotoImage(file="Assets/Images/reset_window.png")
        self.add_window_image = PhotoImage(file="Assets/Images/add_window.png")
        self.retrieve_window_image = PhotoImage(file="Assets/Images/retrieve_window.png")
        self.about_window_image = PhotoImage(file="Assets/Images/otp_window.png")

        # Now we will create a list of all the windows for our application.
        self.windows = [
            LoginWindow,
            SignupWindowFirstPage,
            SignupWindowSecondPage,
            OtpWindow,
            ResetWindow,
            AddWindow,
            RetrieveWindow,
            AboutWindow
        ]
        self.frames = {}

        # All the windows for our application would be a class inherited from the Frame class, which will take two
        # arguments - parent and controller. The class PasswordManager itself is the controller so we will pass "self"
        # as the controller for all our windows.
        for F in self.windows:
            frame = F(container, self)
            # In the above line we passed parent as the container and self as the controller.
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky=NSEW)

        self.show_login_window()

    def _show_window(self, window):
        """This function will display the window we want."""
        frame = self.frames[window]
        frame.tkraise()

    def show_login_window(self):
        self._show_window(LoginWindow)

    def show_signup_window_first_page(self):
        self._show_window(SignupWindowFirstPage)

    def show_signup_window_second_page(self):
        self._show_window(SignupWindowSecondPage)

    def show_otp_window(self):
        self._show_window(OtpWindow)

    def show_reset_window(self):
        self._show_window(ResetWindow)

    def show_add_window(self):
        self._show_window(AddWindow)

    def show_retrieve_window(self):
        self._show_window(RetrieveWindow)

    def show_about_window(self):
        self._show_window(AboutWindow)

    def run(self):
        self.mainloop()


if __name__ == '__main__':
    app = PasswordManager()
    app.run()
