from tkinter import *
from tkinter import ttk
from theme import *


X_PADDING = 60


class MyLabel(ttk.Label):
    """Custom label for the application."""

    def __init__(self, parent, **kw):
        super().__init__(parent, **kw)
        self.config(
            foreground=TEXT_COLOR,
            font=FONT_STYLES["label"],
            justify=LEFT
        )


class MyEntry(ttk.Entry):
    """Custom entry for the application."""

    def __init__(self, parent, **kw):
        super().__init__(parent, **kw)
        self.config(
            font=FONT_STYLES["input"],
            width=30,
        )


class MyButton(ttk.Button):
    """Custom button for the application."""

    def __init__(self, parent, **kw):
        super().__init__(parent, **kw)
        self.config(
            style="AccentButton"
        )


class NavigationBar(Frame):
    """Navigation bar of the Application"""

    def __init__(self, parent, logo, **kw):
        super().__init__(parent, **kw)
        self.logo = logo

        self.config(padx=X_PADDING, pady=15, bg=NAV_BAR_COLOR)
        self.nav_menus = []

        # Logo frame
        self.logo_frame = Frame(self, bg=NAV_BAR_COLOR, padx=0)
        self.logo_frame.pack(side=LEFT, anchor=W)

        icon_label = Label(self.logo_frame, background=NAV_BAR_COLOR, image=self.logo)
        icon_label.grid(row=0, column=0)

        title_label = MyLabel(self.logo_frame, background=NAV_BAR_COLOR, text="MyPass")
        title_label.grid(row=0, column=1)

        # Navigation menus frame
        self.menu_frame = Frame(self, bg=NAV_BAR_COLOR)
        self.menu_frame.pack(side=RIGHT, anchor=E)

        # Adding the navigation menus to the navigation bar.
        self.show_nav_menus()

    def add_nav_menu(self, label="NavButton", action=lambda: print("Button clicked."), is_active=False):
        menu = {
            "label": label,
            "action": action,
            "is_active": is_active,
        }
        self.nav_menus.append(menu)

    def show_nav_menus(self):
        for btn in self.nav_menus:
            Button(
                self.menu_frame,
                text=btn["label"],
                bg=NAV_BAR_COLOR,
                fg=COLORS["pink"] if btn["is_active"] else TEXT_COLOR,
                font=FONT_STYLES["nav_bar"],
                borderwidth=0,
                activebackground=NAV_BAR_COLOR,
                activeforeground=TEXT_COLOR,
                command=btn["action"]
            ).grid(
                row=0, column=self.nav_menus.index(btn), padx=(10, 0)
            )

    def place_on_screen(self):
        self.pack(side=TOP, fill=X, expand=TRUE, anchor=N)


class Body(Frame):
    """Body of the window."""

    def __init__(self, parent, **kw):
        super().__init__(parent, **kw)
        self.config(
            bg=BODY_COLOR,
            padx=X_PADDING
        )

        # Adding the left frame or the image frame
        self.left_frame = Frame(self)
        self.left_frame.pack(side=LEFT, fill=BOTH, anchor=W)

        # Adding the right frame or the entry frame
        self.right_frame = Frame(self)
        self.right_frame.pack(side=RIGHT, fill=BOTH, anchor=E)

    def place_on_screen(self):
        self.pack(fill=BOTH, expand=True)
