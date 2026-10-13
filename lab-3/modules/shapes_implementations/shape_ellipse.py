import tkinter as tk
from .shape_abstract import ShapeAbstract


class ShapeEllipse(ShapeAbstract):
    _DEFAULT_COLOR = "yellow"

    def __init__(self, canvas):
        super().__init__(canvas)

    def render(self) -> None:
        if self._x1 != self._x2 and self._y1 != self._y2:
            self._internal_canvas_id = self._canvas.create_oval(
                self._x1, self._y1,
                self._x2, self._y2,
                outline="black",
                fill=self._DEFAULT_COLOR
            )
        