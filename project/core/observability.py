class Logger:
    """
    Simple logger for observability.
    """
    def __init__(self):
        self.logs = []

    def log(self, label, data):
        entry = {"label": label, "data": data}
        self.logs.append(entry)
        print(f"[LOG] {label}: {data}")
