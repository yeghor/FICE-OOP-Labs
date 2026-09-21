import tkinter as tk

from .option import BaseDropdownOptions
from ..shapes_implementations import ShapesKeys

class ShapeOption(BaseDropdownOptions):
    def __init__(self, root: tk.Misc, switch_shape_cb):
        self._switch_shape_cb = switch_shape_cb
        options = {
            "Rectangle": lambda _, shape_name="RECTANGLE": self._set_shape(shape_name),
            "Point": lambda _, shape_name="POINT": self._set_shape(shape_name),
            "Line": lambda _, shape_name="LINE": self._set_shape(shape_name),
            "Ellipse": lambda _, shape_name="ELLIPSE": self._set_shape(shape_name),
            "No Shape": lambda _: self._set_shape(None),
        }
        super().__init__(root, options, ["Rectangle", "Point", "Line", "Ellipse", "No Shape"])
        self._label = "No Shape"
        self.button = tk.Button(root, text=self._label, command=lambda: self._menu.post(root.winfo_rootx() + 10, root.winfo_rooty() + 30))

    def render(self, parent: tk.Misc | None = None) -> None:
        target = parent if parent is not None else self.root
        self.button.pack(in_=target, side=tk.LEFT, padx=(0, 8), pady=4)

    def _set_shape(self, shape_name: ShapesKeys | None):
        self._label = shape_name.title()

        if ShapesKeys is None:
            self._label = "No Shape"

        self.button.config(text=self._label)
        self._switch_shape_cb(shape_name)
