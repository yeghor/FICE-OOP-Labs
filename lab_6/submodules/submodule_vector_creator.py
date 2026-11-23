import tkinter as tk
from tkinter import ttk
from math import isfinite
from typing import List, Tuple
import sys
import threading
import queue


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
        self._commands = queue.Queue()

        table_frame = ttk.Frame(self, padding=8)
        table_frame.pack(fill=tk.BOTH, expand=True)

        self._table = ttk.Treeview(
            table_frame,
            columns=("value",),
            show="headings",
        )

        self._table.heading("value", text="Values")
        self._table.column("value", anchor=tk.W, width=150)

        scrollbar = ttk.Scrollbar(
            table_frame,
            orient=tk.VERTICAL,
            command=self._table.yview,
        )

        self._table.configure(yscrollcommand=scrollbar.set)

        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self._table.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self._update_vector()

        self._reader = threading.Thread(
            target=self._read_boundaries,
            daemon=True,
        )
        self._reader.start()

        self.protocol("WM_DELETE_WINDOW", self._on_close)
        self.after(100, self._process_commands)

    def _calculate_vector(self) -> List[float]:
        vector = []

        factor = 0.01
        curr_vector_val = self._min

        while curr_vector_val <= self._max:
            vector.append(curr_vector_val)
            curr_vector_val += factor
            curr_vector_val = round(curr_vector_val, 2)

        return vector

    def _update_vector(self) -> None:
        vector = self._calculate_vector()

        self._table.delete(*self._table.get_children())

        for value in vector:
            self._table.insert("", "end", values=(value,))

        self.clipboard_clear()
        self.clipboard_append(str(vector))
        self.update()

        self.title(
            f"Computed Vector (min={self._min}, max={self._max})"
        )

    def _read_boundaries(self) -> None:
        while True:
            try:
                boundaries = input(
                    "Enter new boundaries (min max): "
                ).split()

                if len(boundaries) != 2:
                    self._commands.put(
                        ("error", "Expected exactly two numbers.")
                    )
                    continue

                minimum, maximum = map(float, boundaries)

                if (
                    not isfinite(minimum)
                    or not isfinite(maximum)
                    or minimum >= maximum
                ):
                    self._commands.put(
                        ("error", "Invalid boundaries.")
                    )
                    continue

                self._commands.put(("update", minimum, maximum))

            except ValueError:
                self._commands.put(
                    ("error", "Please enter valid numbers.")
                )
            except EOFError:
                break

    def _process_commands(self) -> None:
        while not self._commands.empty():
            command = self._commands.get_nowait()

            if command[0] == "update":
                _, self._min, self._max = command
                self._update_vector()

                print(
                    f"Vector updated: min={self._min}, max={self._max}",
                    flush=True,
                )

            elif command[0] == "error":
                print(command[1], flush=True)

        if self.winfo_exists():
            self.after(100, self._process_commands)

    def _on_close(self) -> None:
        self.destroy()


if __name__ == "__main__":
    window = Window()
    window.mainloop()
