from .option import BaseOption


class FileOption(BaseOption):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def open_file(self, *args, **kwargs):
        return None
