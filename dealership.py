class Dealership:
    # CONSTRUCTOR
    def __init__(self, name, lots):
        self.name = name
        self.lots = lots

    # GETTERS
    def getName(self):
        return self.name

    def getLots(self):
        return self.lots

    # SETTERS
    def setName(self, name):
        self.name = name

    # METHODS
    def addLot(self, lot):
        self.lots.append(lot)
