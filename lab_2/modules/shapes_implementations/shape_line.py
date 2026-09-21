import tkinter as tk
from .shape_abstract import ShapeAbstract

class ShapeLine(ShapeAbstract):
    _DEFAULT_COLOR = "black"

    def __init__(self, canvas):
        super().__init__(canvas)

    def render(self) -> None:
        self.internal_canvas_id = self._canvas.create_line(
            self._x1, self._y1,
            self._x2, self._y2,
        )
