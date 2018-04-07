

class HueBridge:
    def __init__(self, name, host):
        self.name = name
        self.host = host

    def __hash__(self):
        return hash(self.name) ^ hash(self.host) ^ hash((self.name, self.host))

    def __eq__(self, other):
        return (self.name, self.host) == (other.name, other.host)