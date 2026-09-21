import tkinter as tk
from modules import Canvas, Options


class App(tk.Tk):
    def __init__(self, screenName=None, baseName=None, className="Tk", useTk=True, sync=False, use=None):
        super().__init__(screenName, baseName, className, useTk, sync, use)

        self._canvas = Canvas(self, render=False)
        self._options = Options(self, self._canvas._switch_shape_cb)
        self._canvas.render()

if __name__ == "__main__":
    App(screenName="canvas", baseName="lab-2").mainloop()