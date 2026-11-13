import tkinter as tk
from .modules import MyEditor, Options


class App(tk.Tk):
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

        self._editor = MyEditor(self, render=False)
        self._options = Options(self, self._editor._switch_shape_cb)
        self._editor.render()


if __name__ == "__main__":
    app = App(screenName="canvas", baseName="lab-4")
    app.mainloop()
