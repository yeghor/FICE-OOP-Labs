from math import ceil
from pathlib import Path
from typing import Dict, List, Tuple
import tkinter as tk

from ..shapes_implementations import ShapesKeys, SwitchShapeCb


class ShapeOption:
    """Toolbar section with a separate toggle button for every shape."""

    _ICON_SIZE = 16
    _ICONS_DIR = Path(__file__).parent / "icons"

    # (shape key, readable label, icon file name)
    _SHAPES: List[Tuple[ShapesKeys, str, str]] = [
        ("POINT", "Point", "point_shape_option.png"),
        ("LINE", "Line", "line_shape_option.png"),
        ("RECTANGLE", "Rectangle", "rectangle_shape_option.png"),
        ("ELLIPSE", "Ellipse", "ellipse_shape_option.png"),
    ]

    def __init__(self, root: tk.Misc, switch_shape_cb: SwitchShapeCb):
        self._root = root
        self._switch_shape_cb = switch_shape_cb
        self._chosen_shape: ShapesKeys | None = None

        self._images: Dict[ShapesKeys, tk.PhotoImage] = {}
        self._buttons: Dict[ShapesKeys, tk.Button] = {}

        for key, label, icon_name in self._SHAPES:
            self._buttons[key] = self._create_button(key, label, icon_name)

    @property
    def chosen_shape(self) -> ShapesKeys | None:
        return self._chosen_shape

    def _load_icon(self, icon_name: str) -> tk.PhotoImage | None:
        icon_path = self._ICONS_DIR / icon_name
        if not icon_path.exists():
            return None

        image = tk.PhotoImage(master=self._root, file=str(icon_path))
        factor = max(1, ceil(max(image.width(), image.height()) / self._ICON_SIZE))
        return image.subsample(factor, factor)

    def _create_button(self, key: ShapesKeys, label: str, icon_name: str) -> tk.Button:
        command = lambda shape_key=key: self._toggle_shape(shape_key)
        image = self._load_icon(icon_name)

        if image is None:
            # icon is not added yet - fall back to a text button
            return tk.Button(self._root, text=label, command=command)

        self._images[key] = image
        return tk.Button(
            self._root,
            image=image,
            width=self._ICON_SIZE,
            height=self._ICON_SIZE,
            command=command,
        )

    def render(self, parent: tk.Misc | None = None) -> None:
        target = parent if parent is not None else self._root
        for button in self._buttons.values():
            button.pack(in_=target, side=tk.LEFT, padx=(0, 4), pady=4)

    def _toggle_shape(self, key: ShapesKeys) -> None:
        # clicking the already chosen shape deselects it
        self._set_shape(None if self._chosen_shape == key else key)

    def _set_shape(self, shape_name: ShapesKeys | None) -> None:
        self._chosen_shape = shape_name

        for key, button in self._buttons.items():
            button.config(relief=tk.SUNKEN if key == shape_name else tk.RAISED)

        self._switch_shape_cb(shape_name)
