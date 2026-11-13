from typing import Dict, List, Tuple
import tkinter as tk

from .option import BaseOption
from ..shapes_implementations import ShapesKeys, SwitchShapeCb


class ShapeOption(BaseOption):
    """Toolbar section with a separate toggle button for every shape."""

    _ICON_SIZE = 24

    # (shape key, readable label, icon file name)
    _SHAPES: List[Tuple[ShapesKeys, str, str | None]] = [
        ("POINT", "Point", "point_shape_option.png"),
        ("LINE", "Line", "line_shape_option.png"),
        ("LINE_WITH_CIRCLES", "Line with circles", "line_with_circles_shape_option.png"),
        ("RECTANGLE", "Rectangle", "rectangle_shape_option.png"),
        ("ELLIPSE", "Ellipse", "ellipse_shape_option.png"),
        ("CUBE_FRAME", "Cube frame", "cube_shape_option.png"),
    ]

    def __init__(self, root: tk.Misc, switch_shape_cb: SwitchShapeCb):
        super().__init__(root, self._ICON_SIZE)
        self._switch_shape_cb = switch_shape_cb
        self._chosen_shape: ShapesKeys | None = None

        self._buttons: Dict[ShapesKeys, tk.Button] = {}
        self._tooltip_window: tk.Toplevel | None = None

        for key, label, icon_name in self._SHAPES:
            button = self._create_button(key, label, icon_name)
            self._buttons[key] = button
            button.bind(
                "<Enter>",
                lambda event, text=f"{label} tool": self._show_tooltip(event, text),
            )
            button.bind("<Leave>", self._hide_tooltip)

    @property
    def chosen_shape(self) -> ShapesKeys | None:
        return self._chosen_shape

    def _create_button(
        self, key: ShapesKeys, label: str, icon_name: str | None
    ) -> tk.Button:
        command = lambda shape_key=key: self._toggle_shape(shape_key)
        return super()._create_button(icon_name, command, label)

    def _show_tooltip(self, event: tk.Event, text: str) -> None:
        self._hide_tooltip()
        self._tooltip_window = tk.Toplevel(self._root)
        self._tooltip_window.wm_overrideredirect(True)
        self._tooltip_window.wm_geometry(f"+{event.x_root + 12}+{event.y_root + 12}")
        tk.Label(
            self._tooltip_window,
            text=text,
            background="#ffffe0",
            relief=tk.SOLID,
            borderwidth=1,
            padx=4,
            pady=2,
        ).pack()

    def _hide_tooltip(self, _event: tk.Event | None = None) -> None:
        if self._tooltip_window is not None:
            self._tooltip_window.destroy()
            self._tooltip_window = None

    def render(self, parent: tk.Misc | None = None) -> None:
        self._render_buttons(list(self._buttons.values()), parent, (0, 4))

    def _toggle_shape(self, key: ShapesKeys) -> None:
        # clicking the already chosen shape deselects it
        self._set_shape(None if self._chosen_shape == key else key)

    def _set_shape(self, shape_name: ShapesKeys | None) -> None:
        self._chosen_shape = shape_name

        for key, button in self._buttons.items():
            button.config(relief=tk.SUNKEN if key == shape_name else tk.RAISED)

        self._switch_shape_cb(shape_name)
