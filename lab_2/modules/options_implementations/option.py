import tkinter as tk
from typing import Callable, Any


class BaseOption:
    def __init__(self, compile_cb: Callable[[tk.Button], None] | None = None):
        self.compile_cb = compile_cb
        self.widget: tk.Widget | None = None

    def bind(self, widget: tk.Widget, *args: Any, **kwargs: Any) -> None:
        self.widget = widget
        if self.compile_cb is not None:
            self.compile_cb(widget, *args, **kwargs)

    def render(self) -> None:
        return None
    