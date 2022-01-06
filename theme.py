import tkinter.font

COLORS = {
    "dark_grey": "#2B2B2B",
    "white": "#FFFFFF",
    "pink": "#F2575D",
    "darker_grey": "#242424",
}

MASTER_FONT = "helvetica"

FONT_SIZES = {
    "input_font_size": 12,
    "nav_bar_font_size": 16,
    "label_font_size": 14,
}

FONT_STYLES = {
    "nav_bar": (
        MASTER_FONT,
        FONT_SIZES["nav_bar_font_size"],
        "bold"
    ),
    "label": (
        MASTER_FONT,
        FONT_SIZES["label_font_size"],
        "bold"
    ),
    "input": (
        MASTER_FONT,
        FONT_SIZES["input_font_size"],
        "normal"
    ),
}

BACKGROUND_COLOR = COLORS["dark_grey"]
TEXT_COLOR = COLORS["white"]
NAV_BAR_COLOR = COLORS["darker_grey"]
