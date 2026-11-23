import tkinter as tk

from .options_implementations import (
    FileOption,
    TableModalOption,
    RefOption,
    ShapeOption,
)
from .shapes_implementations import ShapesDataCb, ShapesFileDataCb, SwitchShapeCb


class Options:
    def __init__(
        self,
        root: tk.Misc,
        switch_shape_cb: SwitchShapeCb,
        get_shapes_data_cb: ShapesDataCb,
        get_shapes_for_save_cb: ShapesFileDataCb,
    ):
        self.root = root
        self.toolbar = tk.Frame(root, bd=1, relief=tk.SUNKEN)
        self.toolbar.pack(side=tk.TOP, fill=tk.X)

        self.file_option = FileOption(root, get_shapes_for_save_cb)
        self.table_option = TableModalOption(root, get_shapes_data_cb)
        self.ref_option = RefOption(root)
        self.shape_options = ShapeOption(root, switch_shape_cb)

        self.file_option.render(self.toolbar)
        self.table_option.render(self.toolbar)
        self.ref_option.render(self.toolbar)
        self.shape_options.render(self.toolbar)
