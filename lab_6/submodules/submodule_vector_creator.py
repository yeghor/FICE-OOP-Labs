import tkinter as tk
from tkinter import ttk
from math import isfinite
from typing import List, Tuple
import sys


class Window(tk.Tk):
    @staticmethod
    def extract_min_max_parameters(argv: List[str]) -> Tuple[float, float]:
        arguments = argv[1:]
        if len(arguments) != 4:
            raise SystemExit(2)

        parameters = dict(zip(arguments[::2], arguments[1::2]))
        if set(parameters) != {"-min", "-max"}:
            raise SystemExit(2)

        try:
            minimum = float(parameters["-min"])
            maximum = float(parameters["-max"])
        except ValueError:
            raise SystemExit(2) from None

        if not isfinite(minimum) or not isfinite(maximum) or minimum >= maximum:
            raise SystemExit(2)
        return minimum, maximum

    def __init__(
        self,
        screenName=None,
        baseName=None,
        className="Tk",
        useTk=True,
        sync=False,
        use=None,
    ):
        super().__init__(screenName, baseName, className, useTk, sync, use)

        self._min, self._max = self.extract_min_max_parameters(sys.argv)
        self._vector = self._calculate_vector()

        table_frame = ttk.Frame(self, padding=8)
        table_frame.pack(fill=tk.BOTH, expand=True)

        self._table = ttk.Treeview(
            table_frame,
            columns=("value",),
            show="headings",
        )
        self.title(f"Computed Vector (min={self._min}, max={self._max})")
        self._table.heading("val    ue", text="Values")
        self._table.column("value", anchor=tk.W, width=150)

        scrollbar = ttk.Scrollbar(table_frame, orient=tk.VERTICAL, command=self._table.yview)
        self._table.configure(yscrollcommand=scrollbar.set)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self._table.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self._fill_table()

    def _calculate_vector(self) -> List[float]:
        vector = []

        factor = 0.01
        curr_vector_val = self._min
        while curr_vector_val <= self._max:
            vector.append(curr_vector_val)
            curr_vector_val += factor
            curr_vector_val = round(curr_vector_val, 2)

        return vector

    def _fill_table(self) -> None:
        for val in self._vector:
            self._table.insert("", "end", values=(val,))


if __name__ == "__main__":
    window = Window()
    window.mainloop()
        