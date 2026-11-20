from .shape_abstract import ShapeAbstract
import numpy as np
import itertools


class ShapeCubeFrame(ShapeAbstract):
    _DEFAULT_COLOR = "black"
    _NAME = "Cube frame"

    def show(self) -> None:
        central_point = ((self._x1 + self._x2) // 2, (self._y1 + self._y2) // 2)

        border_distance_for_central_point = min(
            abs(min(self._x1, self._x2) - central_point[0]),
            abs(min(self._y1, self._y2) - central_point[1]),
        )

        spatial_rib_halflength = border_distance_for_central_point * 0.9

        central_spatial_rectangle = np.array(
            [
                central_point[0] - spatial_rib_halflength,
                central_point[1] + spatial_rib_halflength,
                central_point[0] + spatial_rib_halflength,
                central_point[1] - spatial_rib_halflength,
            ]
        )

        octant_rib_length = spatial_rib_halflength // 4

        front_spatial_rectangle = [
            coord - octant_rib_length if i % 2 == 0 else coord + octant_rib_length
            for i, coord in enumerate(central_spatial_rectangle)
        ]
        back_spatial_rectangle = [
            coord - octant_rib_length if i % 2 == 1 else coord + octant_rib_length
            for i, coord in enumerate(central_spatial_rectangle)
        ]

        self._canvas.create_rectangle(
            *front_spatial_rectangle,
        )
        self._canvas.create_rectangle(
            *back_spatial_rectangle,
        )

        connectivity_ribs = [
            (
                front_spatial_rectangle[0],
                front_spatial_rectangle[1],
                back_spatial_rectangle[0],
                back_spatial_rectangle[1],
            ),
            (
                front_spatial_rectangle[2],
                front_spatial_rectangle[1],
                back_spatial_rectangle[2],
                back_spatial_rectangle[1],
            ),
            (
                front_spatial_rectangle[2],
                front_spatial_rectangle[3],
                back_spatial_rectangle[2],
                back_spatial_rectangle[3],
            ),
            (
                front_spatial_rectangle[0],
                front_spatial_rectangle[3],
                back_spatial_rectangle[0],
                back_spatial_rectangle[3],
            ),
        ]

        for conn_rib in connectivity_ribs:
            self._canvas.create_line(
                *conn_rib
            )

        self._is_rendered = True