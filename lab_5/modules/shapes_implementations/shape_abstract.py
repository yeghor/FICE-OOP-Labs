from abc import ABC, abstractmethod
from typing import Tuple
import tkinter as tk


class ShapeAbstract(ABC):
    _NAME = "Shape"

    def __init__(self, canvas: tk.Canvas):
        self._canvas = canvas
        self._x1 = self._x2 = self._y1 = self._y2 = None

        self._internal_canvas_id: int | None = None
        self._internal_canvas_ids: list[int] = []
        self._is_rendered = False

    @property
    def name(self) -> str:
        return self._NAME

    @property
    def position(self) -> tuple[int, int]:
        if self._x1 is None or self._y1 is None:
            raise ValueError("Shape position is not set")
        return int(self._x1), int(self._y1)

    @property
    def coordinates(self) -> tuple[int, int, int, int]:
        if (
            self._x1 is None
            or self._y1 is None
            or self._x2 is None
            or self._y2 is None
        ):
            raise ValueError("Shape coordinates are not set")
        return int(self._x1), int(self._y1), int(self._x2), int(self._y2)

    @property
    def internal_canvas_id(self) -> int | None:
        return self._internal_canvas_id

    @property
    def is_rendered(self) -> bool:
        return self._is_rendered

    @is_rendered.setter
    def is_rendered(self, value: bool) -> None:
        if not isinstance(value, bool):
            raise ValueError(
                f"`is_rendered` attribute is boolean only, received {type(value)}"
            )

        if value is True:
            if self._is_rendered:
                return
            self.show()
            return

        if value is False and self._internal_canvas_id is not None:
            canvas_ids = self._internal_canvas_ids or [self._internal_canvas_id]
            for canvas_id in canvas_ids:
                self._canvas.delete(canvas_id)
            self._internal_canvas_ids.clear()
            self._internal_canvas_id = None
            self._is_rendered = False
            return

        raise ValueError("Couldn't dispose not rendered shape!")

    @abstractmethod
    def show(self) -> None:
        """Must handle internal `_is_rendered` and `_internal_canvas_id` attributes change"""
        ...

    def dispose(self) -> None:
        self.is_rendered = False  # activates setter disposing flow

    def update_position(self, *coords: int) -> None:
        """*cords: List[x1, x2, y1, y2]"""

        if len(coords) != 4:
            raise ValueError(
                f"4 positioning parameters are expected, received {len(coords)}"
            )

        self._x1, self._x2, self._y1, self._y2 = coords
