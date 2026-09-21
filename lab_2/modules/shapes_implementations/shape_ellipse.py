import tkinter as tk
from .shape_abstract import ShapeAbstract


class ShapeEllipse(ShapeAbstract):
    _DEFAULT_COLOR = "black"

    def __init__(self, canvas):
        super().__init__(canvas)

    def render(self) -> None:
        cx, cy = self._x1, self._y1
        rx = abs(self._x2 - cx)
        ry = abs(self._y2 - cy)

        self._internal_canvas_id = self._canvas.create_oval(
            cx - rx, cy - ry,
            cx + rx, cy + ry,
            outline=self._DEFAULT_COLOR,
        )
        