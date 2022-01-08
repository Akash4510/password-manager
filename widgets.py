from tkinter import *
from tkinter import ttk
from theme import *


X_PADDING = 60


class MyLabel(ttk.Label):
    """Custom label widget for the application."""

    def __init__(self, parent, **kw):
        super().__init__(parent, **kw)
        self.config(
            foreground=TEXT_COLOR,
            font=FONT_STYLES["label"],
            justify=LEFT
        )


class MyEntry(ttk.Entry):
    """Custom entry widget for the application."""

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


class InputBox:
    """Input box with a label and a input field"""

    def __init__(self, parent, label, var):
        self.label = MyLabel(
            parent,
            text=label,
            background=BODY_COLOR
        )
        self.input_box = MyEntry(parent, textvar=var)


class NavigationBar(Frame):
    """Navigation bar of the Application"""

    def __init__(self, parent, **kw):
        super().__init__(parent, **kw)
        self.logo = parent.controller.nav_bar_logo

        self.config(
            padx=X_PADDING,
            pady=15,
            bg=NAV_BAR_COLOR)
        self.nav_menus = []

        # Logo frame
        self.logo_frame = Frame(
            self,
            bg=NAV_BAR_COLOR,
            padx=0
        )
        self.logo_frame.pack(side=LEFT, anchor=W)

        icon_label = MyLabel(
            self.logo_frame,
            background=NAV_BAR_COLOR,
            image=self.logo
        )
        icon_label.grid(row=0, column=0)

        title_label = MyLabel(
            self.logo_frame,
            background=NAV_BAR_COLOR,
            text="MyPass"
        )
        title_label.grid(row=0, column=1)

        # Navigation menus frame
        self.menu_frame = Frame(
            self,
            bg=NAV_BAR_COLOR
        )
        self.menu_frame.pack(side=RIGHT, anchor=E)

        # Adding the navigation menus to the navigation bar.
        self.add_nav_menus()

    def nav_menu(self, label="NavButton", action=lambda: print("Button clicked."), is_active=False):
        """Creates a nav menu"""
        menu_btn = Button(
            self.menu_frame,
            text=label,
            bg=NAV_BAR_COLOR,
            fg=COLORS["pink"] if is_active else TEXT_COLOR,
            font=FONT_STYLES["nav_bar"],
            borderwidth=0,
            activebackground=NAV_BAR_COLOR,
            activeforeground=TEXT_COLOR,
            command=action
        )
        self.nav_menus.append(menu_btn)
        self.add_nav_menus()

    def add_nav_menus(self):
        """Add all the nav menus to the navigation bar"""
        for menu in self.nav_menus:
            menu.grid(row=0, column=self.nav_menus.index(menu), padx=(10, 0))

    def place_on_screen(self):
        """Displays the navigation bar on the top of the window"""
        self.pack(side=TOP, fill=X, expand=TRUE, anchor=N)


class Body(Frame):
    """Body of the window."""

    body_height = 550

    def __init__(self, parent, **kw):
        super().__init__(parent, **kw)
        self.config(
            bg=BODY_COLOR,
            height=self.body_height,
            padx=X_PADDING,
            pady=0,
        )

        # Adding the left frame or the image frame
        self.left_frame = Frame(
            self,
            height=self.body_height,
            bg=BODY_COLOR,
            pady=60
        )
        self.left_frame.pack(side=LEFT, fill=BOTH, anchor=W)

        # Adding the right frame or the entry frame
        self.right_frame = Frame(
            self,
            height=self.body_height,
            bg=BODY_COLOR,
            pady=20
        )
        self.right_frame.pack(side=RIGHT, fill=BOTH, anchor=E)

    def place_on_screen(self):
        """Displays the body frame on the window"""
        self.pack(fill=BOTH, expand=True)


class Window(Frame):
    """Main window/page of the application"""

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller

        self.nav_bar = NavigationBar(self)
        self.nav_bar.place_on_screen()

        self.body = Body(self)
        self.body.place_on_screen()

        self.entry_frame = self.body.right_frame

    def add_image(self, image):
        """Adds the image to the left frame"""
        image_label = Label(self.body.left_frame, image=image, bg=BODY_COLOR)
        image_label.grid(row=0, column=0, sticky=W)

    @staticmethod
    def add_inputs(inputs: list[InputBox], row=0, column=0, gap=30):
        """Adds the input boxes in the entry frame"""
        for inp in inputs:
            inp.label.grid(
                row=row, column=column, columnspan=2, sticky=W,
                pady=(gap, 10) if inputs.index(inp) != 0 else (0, 10), padx=0
            )
            row += 1

            inp.input_box.grid(row=row, column=column, columnspan=2, sticky=W)
            row += 1
