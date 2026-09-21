import tkinter as tk

from .options_implementations import FileOption, RefOption, ShapeOption


class Options:
    def __init__(self, root: tk.Misc | None = None):
        self.root = root
        self.file_option = FileOption()
        self.ref_option = RefOption()
        self.shape_option = ShapeOption()