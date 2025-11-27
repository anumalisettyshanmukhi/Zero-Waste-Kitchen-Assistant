class SessionMemory:
    """
    Session Memory:
    - Stores allergies, staples, and prior context.
    """
    def __init__(self):
        self.data = {
            "allergies": [],
            "staples": ["salt", "oil"]
        }

    def set(self, key, value):
        self.data[key] = value

    def get(self, key, default=None):
        return self.data.get(key, default)
