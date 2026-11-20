from typing import Literal, Callable, Dict, Tuple

ShapesKeys = Literal[
    "RECTANGLE",
    "POINT",
    "LINE",
    "ELLIPSE",
    "LINE_WITH_CIRCLES",
    "CUBE_FRAME",
]
ShapesData = Dict[str, Tuple[int, int]]

SwitchShapeCb = Callable[[ShapesKeys | None], None]
ShapesDataCb = Callable[[], ShapesData]