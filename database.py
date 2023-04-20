class DataBase:
    def __init__(self, name="test.db"):
        self.filename = name

    def load(self):
        result = {}
        with open(self.filename, "r") as f:
            result = {"Player1": int(f.read())}
        return result

    def store(self, values):
        with open(self.filename, "w") as f:
            f.write(str(values["Player1"]))

    def close(self):
        pass
