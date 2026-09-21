from .option import BaseOption


class RefOption(BaseOption):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def refresh(self, *args, **kwargs):
        return None
