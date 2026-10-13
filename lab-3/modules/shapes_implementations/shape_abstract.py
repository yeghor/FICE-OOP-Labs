from abc import ABC, abstractmethod
from typing import Tuple
import tkinter as tk


class ShapeAbstract(ABC):
    def __init__(self, canvas: tk.Canvas):
        self._canvas = canvas
        self._x1 = self._x2 = self._y1 = self._y2 = None

        self._internal_canvas_id: int | None = None
        self._is_rendered = False

    @property
    def internal_canvas_id(self) -> int | None:
        return self._internal_canvas_id

    @property
    def is_rendered(self) -> bool:
        return self._is_rendered

    @is_rendered.setter
    def is_rendered(self, value: bool) -> None:
        if not isinstance(value, bool):
            raise ValueError(f"`is_rendered` attribute is boolean only, received {type(value)}")

        if value is True:
            self.render()

        if value is False and self._internal_canvas_id is not None:
            self._canvas.delete(self._internal_canvas_id)
            self._internal_canvas_id = None
            self._is_rendered = False
            return

        raise ValueError("Couldn't dispose not rendered shape!")

    @abstractmethod
    def render(self) -> None:
        """Must handle internal `_is_rendered` and `_internal_canvas_id` attributes change"""
        ...

    def dispose(self) -> None:
        self.is_rendered = False # activates setter disposing flow

    def update_position(self, *coords: int) -> None:
        """*cords: List[x1, x2, y1, y2]"""

        if len(coords) != 4:
            raise ValueError(f"4 positioning parameters are expected, received {len(coords)}")

        self._x1, self._x2, self._y1, self._y2 = coords
