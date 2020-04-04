class Employee:
    # CONSTRUCTOR
    def __init__(self, name):
        self.name = name

    # GETTERS
    def getName(self):
        return self.name

    def getVehicle(self):
        return self.vehicle

    # SETTERS
    def setName(self, name):
        self.name = name

    def setVehicle(self, vehicle):
        self.vehicle = vehicle

    # METHODS
    def hasVehicle(self):
        if self.vehicle is None:
            return False
        else:
            return True

    def removeVehicle(self):
        vehicleCopy = self.vehicle
        self.vehicle = None
        return vehicleCopy
