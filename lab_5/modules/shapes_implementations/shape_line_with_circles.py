from .shape_abstract import ShapeAbstract


class ShapeLineWithCircles(ShapeAbstract):
    _DEFAULT_COLOR = "black"
    _CIRCLE_RADIUS = 4
    _NAME = "Line with circles"

    def show(self) -> None:
        line_id = self._canvas.create_line(
            self._x1,
            self._y1,
            self._x2,
            self._y2,
            fill=self._DEFAULT_COLOR,
        )
        start_circle_id = self._canvas.create_oval(
            self._x1 - self._CIRCLE_RADIUS,
            self._y1 - self._CIRCLE_RADIUS,
            self._x1 + self._CIRCLE_RADIUS,
            self._y1 + self._CIRCLE_RADIUS,
            outline=self._DEFAULT_COLOR,
            fill="white",
        )
        end_circle_id = self._canvas.create_oval(
            self._x2 - self._CIRCLE_RADIUS,
            self._y2 - self._CIRCLE_RADIUS,
            self._x2 + self._CIRCLE_RADIUS,
            self._y2 + self._CIRCLE_RADIUS,
            outline=self._DEFAULT_COLOR,
            fill="white",
        )

        self._internal_canvas_ids = [line_id, start_circle_id, end_circle_id]
        self._internal_canvas_id = line_id
        self._is_rendered = True
