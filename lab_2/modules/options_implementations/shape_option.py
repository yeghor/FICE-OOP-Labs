from .option import BaseOption


class ShapeOption(BaseOption):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def set_shape(self, *args, **kwargs):
        return None
