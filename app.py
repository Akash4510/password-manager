from tkinter import *
from theme import *


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

        self.title("MyPass - PasswordManager")
        self.wm_iconbitmap("Assets/Logo/padlock.ico")
        self.config(bg=BACKGROUND_COLOR)
        self.call("source", "Assets/Theme/proxttk-dark.tcl")

        # Setting up a default x_padding for the whole application
        self.x_padding = 60

        # Now we will create a container for the frames, which itself would be a frame.
        container = Frame(self, width=app_width, height=app_height, bg=BACKGROUND_COLOR)
        container.pack(side=TOP, fill=BOTH, expand=TRUE)

        container.grid_rowconfigure(index=0, weight=1)
        container.grid_columnconfigure(index=0, weight=1)

        container.config(bg=BACKGROUND_COLOR)
        self.nav_bar_logo = PhotoImage(file="Assets/Logo/nav_bar_logo.png")

        # Now we will create a list of all the windows for our application.
        self.windows = []
        self.frames = {}

        # All the windows for our application would be a class inherited from the frame class, which will take two
        # arguments - parent and controller, and the class PasswordManager is the controller so we will pass "self" as
        # the controller for all our windows.
        for F in self.windows:
            frame = F(container, self)
            # In the above line we passed parent as the container and self as the controller.
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky=NSEW)

    def show_window(self, cont):
        """This function will display the window we want."""
        frame = self.frames[cont]
        frame.tkraise()

    def run(self):
        self.mainloop()


if __name__ == '__main__':
    app = PasswordManager()
    app.run()
