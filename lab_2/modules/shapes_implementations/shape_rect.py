import tkinter as tk
from .shape_abstract import ShapeAbstract


class ShapeRect(ShapeAbstract):
    _DEFAULT_COLOR = "yellow"

    def __init__(self, canvas):
        super().__init__(canvas)

    def render(self) -> None:
        self._internal_canvas_id = self._canvas.create_rectangle(
            self._x1, self._y1,
            self._x2, self._y2,
            fill=self._DEFAULT_COLOR
        )
        self._is_rendered = True
