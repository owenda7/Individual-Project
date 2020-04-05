class Employee:
    # CONSTRUCTOR
    def __init__(self, name):
        self.vehicle = None
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
    def hasAVehicle(self):
        if self.vehicle is None:
            return False
        else:
            return True

    def hasVehicle(self, vehicle):
        if self.vehicle == vehicle:
            return True
        else:
            return False

    def removeVehicle(self):
        vehicleCopy = self.vehicle
        return vehicleCopy
