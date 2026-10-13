from typing import Dict, Literal, Type

from .shape_abstract import ShapeAbstract
from .shape_ellipse import ShapeEllipse
from .shape_line import ShapeLine
from .shape_point import ShapePoint
from .shape_rect import ShapeRect
from .types import ShapesKeys

SHAPES_MAP: Dict[ShapesKeys, Type[ShapeAbstract]] = {
    "RECTANGLE": ShapeRect,
    "POINT": ShapePoint,
    "LINE": ShapeLine,
    "ELLIPSE": ShapeEllipse,
}


class ShapeFactory:
    @staticmethod
    def instantiate_shape(key: ShapesKeys, *args, **kwargs) -> ShapeAbstract:
        ShapeClass = SHAPES_MAP.get(key)

        if not ShapeClass:
            raise ValueError("Couldn't find desired shape")
        if not issubclass(ShapeClass, ShapeAbstract):
            raise ValueError("This shape isn't supported. Shape must be a heir of `ShapeAbstract`")

        return ShapeClass(*args, **kwargs)
