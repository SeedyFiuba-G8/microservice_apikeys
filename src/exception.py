from src.assets.responses import Error


class APIKeysException(Exception):
    def __init__(self, error: Error):
        self.error = error
        super().__init__()
