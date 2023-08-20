class Permissions:
    _instance = None

    def __new__(cls, read=False, write=False, execute=False):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.read = read
            cls._instance.write = write
            cls._instance.execute = execute
        return cls._instance

    def update_permissions(self, read=False, write=False, execute=False):
        self.read = read
        self.write = write
        self.execute = execute
