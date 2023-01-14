class ServiceError(Exception):
    meesage: str

    def __init__(self, message):
        self.message = message