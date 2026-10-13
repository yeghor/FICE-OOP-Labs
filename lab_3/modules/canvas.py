import tkinter as tk
from .shapes_implementations import ShapeFactory, ShapeAbstract, ShapesKeys
from typing import List

class Canvas:
    _MAX_SHAPES = 113

    def __init__(self,
        root: tk.Misc,
        render: bool = False
    ):
        self._canvas = tk.Canvas(root, bg="white")

        self._canvas.bind("<ButtonPress>", self._mouse_start_drawing_cb)
        self._canvas.bind("<Motion>", self._mouse_drawing_cb)
        self._canvas.bind("<ButtonRelease>", self._mouse_stop_drawing_cb)

        self._is_drawing = False

        self._curr_shape_key: ShapesKeys | None = None
        self._curr_shape: ShapeAbstract | None = None
        self._shapes_stack: List[ShapeAbstract] = []

        # rubber path
        self._rubber_path_canvas_internal_id: int | None = None

        # coords
        self._x_start: int | None = None
        self._y_start: int | None = None

        if render:
            self.render()

    @property
    def curr_shape(self) -> ShapesKeys | None:
        return self._curr_shape_key

    def render(self) -> None:
        self._canvas.pack()

    def _create_rubber_path(self, x_start: int, y_start: int) -> None:
        self._x_start = x_start
        self._y_start = y_start
        self._rubber_path_canvas_internal_id = self._canvas.create_rectangle(
            self._x_start, self._y_start,
            self._x_start, self._y_start,
            outline="red"
        )

    def _update_rubber_path(self, end_x: int, end_y: int) -> None:
        self._canvas.coords(
            self._rubber_path_canvas_internal_id,
            self._x_start, self._y_start,
            end_x, end_y
        )

    def _remove_rubber_path(self) -> None:
        """handles clear of `_rubber_path_canvas_internal_id`"""

        if self._rubber_path_canvas_internal_id is None:
            return

        self._canvas.delete(self._rubber_path_canvas_internal_id)
        self._rubber_path_canvas_internal_id = None
        
    def _switch_shape_cb(self, key: ShapesKeys | None) -> None:
        if key is None:
            self._curr_shape = None
            return

        self._curr_shape_key = key
        self._reinstantiate_shape()

    def _reinstantiate_shape(self) -> None:
        if self._curr_shape_key is not None:
            self._curr_shape = ShapeFactory().instantiate_shape(self._curr_shape_key, self._canvas)
            return

        self._curr_shape = None

    def _mouse_start_drawing_cb(self, event: tk.Event) -> None:
        self._x_start = event.x
        self._y_start = event.y

        self._is_drawing = True
        self._create_rubber_path(self._x_start, self._y_start)

    def _mouse_drawing_cb(self, event: tk.Event) -> None:
        if self._is_drawing:
            if self._curr_shape:
                self._curr_shape.update_position(
                    self._x_start, event.x,
                    self._y_start, event.y
                )
            self._update_rubber_path(event.x, event.y)

    def _mouse_stop_drawing_cb(self, event: tk.Event) -> None:
        self._x_start = None
        self._y_start = None

        self._is_drawing = False

        self._remove_rubber_path()

        if self._curr_shape:
            if len(self._shapes_stack) < self._MAX_SHAPES:
                self._curr_shape.render()
                self._shapes_stack.append(self._curr_shape)

            self._reinstantiate_shape()

    def undo(self) -> None:
        if len(self._shapes_stack) > 0:
            shape_to_undo = self._shapes_stack.pop()
            shape_to_undo.dispose()

            self._reinstantiate_shape()
