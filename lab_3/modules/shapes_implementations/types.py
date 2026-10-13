from typing import Literal, Callable

ShapesKeys = Literal["RECTANGLE", "POINT", "LINE", "ELLIPSE"]
SwitchShapeCb = Callable[[ShapesKeys], None]
