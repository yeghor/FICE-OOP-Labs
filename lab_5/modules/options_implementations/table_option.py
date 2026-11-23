import tkinter as tk
from tkinter import ttk

from .option import BaseOption
from ..shapes_implementations import ShapesDataCb
from typing import Callable


class DraftModalWindow(tk.Toplevel):
    def __init__(self, root: tk.Misc, get_shapes_data_cb: ShapesDataCb, on_close):
        super().__init__(root)
        self._on_close = on_close

        self.title("Table representation of the Editor")
        self.geometry("360x180")
        self.minsize(360, 180)
        self.resizable(False, False)
        self.transient(root)

        shapes_data = get_shapes_data_cb()

        table_frame = ttk.Frame(self, padding=8)
        table_frame.pack(fill=tk.BOTH, expand=True)

        table = ttk.Treeview(
            table_frame,
            columns=("name", "value_1", "value_2"),
            show="headings",
        )
        table.heading(0, text="Shape Name")
        table.heading(1, text="X")
        table.heading(2, text="Y")
        table.column(0, anchor=tk.W, width=150)
        table.column(1, anchor=tk.CENTER, width=80)
        table.column(2, anchor=tk.CENTER, width=80)

        scrollbar = ttk.Scrollbar(table_frame, orient=tk.VERTICAL, command=table.yview)
        table.configure(yscrollcommand=scrollbar.set)
        table.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        for name, (x, y) in shapes_data.items():
            table.insert("", tk.END, values=(name, x, y))

        self.protocol("WM_DELETE_WINDOW", self.close)
        self.grab_set()
        self.focus()

    def close(self) -> None:
        self.grab_release()
        self._on_close()
        self.destroy()


class TableModalOption(BaseOption):
    _ICON_SIZE = 24

    def __init__(self, root: tk.Misc, get_shapes_data_cb: ShapesDataCb):
        super().__init__(root)
        self._get_shapes_data_cb = get_shapes_data_cb
        self._modal: DraftModalWindow | None = None
        self.button = self._create_button("table_option.png", self.open_modal, "Modal")

    def open_modal(self) -> None:
        if self._modal is not None and self._modal.winfo_exists():
            self._modal.lift()
            self._modal.focus()
            return

        self._modal = DraftModalWindow(
            self._root, self._get_shapes_data_cb, self._clear_modal
        )

    def _clear_modal(self) -> None:
        self._modal = None

    def render(self, parent: tk.Misc | None = None) -> None:
        self._render_buttons([self.button], parent, (0, 8))
