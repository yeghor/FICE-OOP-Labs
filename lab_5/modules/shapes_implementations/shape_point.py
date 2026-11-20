import tkinter as tk
from .shape_abstract import ShapeAbstract


class ShapePoint(ShapeAbstract):
    _DEFAULT_COLOR = "blue"
    _NAME = "Point"

    def __init__(self, canvas):
        super().__init__(canvas)

    def show(self) -> None:
        self._internal_canvas_id = self._canvas.create_oval(
            self._x1 - 2,
            self._y1 - 2,
            self._x1 + 2,
            self._y1 + 2,
            fill=self._DEFAULT_COLOR,
            outline=self._DEFAULT_COLOR,
        )
        self._is_rendered = True
