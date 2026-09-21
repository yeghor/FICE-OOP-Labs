import tkinter as tk

from .options_implementations import FileOption, RefOption, ShapeOption
from .shapes_implementations import SwitchShapeCb


class Options:
    def __init__(self, root: tk.Misc, switch_shape_cb: SwitchShapeCb):
        self.root = root
        self.toolbar = tk.Frame(root, bd=1, relief=tk.SUNKEN)
        self.toolbar.pack(side=tk.TOP, fill=tk.X)

        self.file_option = FileOption(root)
        self.ref_option = RefOption(root)
        self.shape_option = ShapeOption(root, switch_shape_cb)

        self.file_option.render(self.toolbar)
        self.ref_option.render(self.toolbar)
        self.shape_option.render(self.toolbar)