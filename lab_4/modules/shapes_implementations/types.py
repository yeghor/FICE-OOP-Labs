from typing import Literal, Callable

ShapesKeys = Literal[
    "RECTANGLE",
    "POINT",
    "LINE",
    "ELLIPSE",
    "LINE_WITH_CIRCLES",
    "CUBE_FRAME",
]
SwitchShapeCb = Callable[[ShapesKeys | None], None]
