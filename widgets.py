from tkinter import *
from tkinter import ttk
from theme import *


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


class InputBox(Frame):
    """Input box with a label and a input field"""

    def __init__(self, parent, label, var):
        super().__init__(parent)
        self.config(bg=BODY_COLOR)
        self.label = MyLabel(
            self,
            text=label,
            background=BODY_COLOR
        )
        self.entry = MyEntry(self, textvar=var)

        self.label.grid(row=0, column=0, columnspan=2, pady=(30, 10), sticky=W)
        self.entry.grid(row=1, column=0, columnspan=2, sticky=W)


class NavigationBar(Frame):
    """Navigation bar of the Application"""

    def __init__(self, parent, **kw):
        super().__init__(parent, **kw)
        self.logo = parent.controller.nav_bar_logo

        self.config(pady=15, bg=NAV_BAR_COLOR)
        self.nav_menus = []

        # Logo frame
        self.logo_frame = Frame(self, bg=NAV_BAR_COLOR, padx=0)
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
        self.menu_frame = Frame(self, bg=NAV_BAR_COLOR)
        self.menu_frame.pack(side=RIGHT, anchor=E)

        # Adding the navigation menus to the navigation bar.
        self.place_nav_menus()

    def add_nav_menu(self, label="NavButton", action=None, is_active=False):
        """Adds a nav menu"""

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
        self.place_nav_menus()

    def place_nav_menus(self):
        """Place all the nav menus to the navigation bar"""
        for menu in self.nav_menus:
            menu.grid(row=0, column=self.nav_menus.index(menu), padx=(10, 0))


class BodyFrame(Frame):
    """Container for the bodies of the windows of the application"""

    def __init__(self, parent, **kw):
        super().__init__(parent, **kw)

        self.container = Frame(self, bg=BODY_COLOR)
        self.container.pack(side=TOP, fill=BOTH, expand=TRUE)

        self.container.grid_rowconfigure(index=0, weight=1)
        self.container.grid_columnconfigure(index=0, weight=1)

        self.windows = []
        self.children_frames = {}

    def add_children_frames(self):
        """Creates all the children frames from the given Frame objects"""
        for F in self.windows:
            frame = F(self.container, self)
            self.children_frames[F] = frame
            frame.grid(row=0, column=0, sticky=NSEW)

    def show_frame(self, frame):
        """Shows a particular frame from the children frames"""
        self.children_frames[frame].tkraise()


class Body(Frame):

    def __init__(self, parent, controller, **kw):
        super().__init__(parent, **kw)

        self.controller = controller
        self.parent_window = self.controller.master
        self.root_controller = self.parent_window.controller

        self.body_height = 550

        self.config(
            bg=BODY_COLOR,
            height=self.body_height,
            padx=60,
            pady=0,
        )

    @staticmethod
    def add_inputs(input_frames: list[InputBox], from_row=0):
        """Adds all the inputs in the body"""
        for frame in input_frames:
            frame.grid(row=from_row, column=0, columnspan=2)
            from_row += 1


class TwoColumnBody(Body):
    """Body of the window"""

    def __init__(self, parent, controller, **kw):
        super().__init__(parent, controller, **kw)

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

    def add_image(self, image, parent=None):
        """Adds the image to the left frame by default otherwise in the parent"""
        if parent is None:
            parent = self.left_frame
        image_label = Label(parent, image=image, bg=BODY_COLOR)
        image_label.grid(row=0, column=0, sticky=W)


class SingleColumnBody(Body):
    ...


class Window(Frame):
    """Main Window/Page of the application."""

    def __init__(self, parent, controller):
        super().__init__(parent)

        self.controller = controller

        self.x_padding = 60

        self.nav_bar = NavigationBar(self, padx=self.x_padding)
        self.nav_bar.pack(side=TOP, fill=X, expand=TRUE, anchor=N)

        self.body = BodyFrame(self)
        self.body.pack(side=TOP, fill=BOTH, expand=TRUE)

    def add_pages(self, *frames):
        """Adds different bodies/pages of a window in the body frame of the window"""
        for frame in frames:
            self.body.windows.append(frame)
        self.body.add_children_frames()

    def show_page(self, page):
        """Displays the given page"""
        self.body.show_frame(page)
