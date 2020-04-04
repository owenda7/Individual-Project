class Lot:
    # CONSTRUCTOR
    def __init__(self,name, vehicles, maxCapacity):
        self.name = name
        self.vehicles = vehicles
        self.numVehicles = len(vehicles)
        self.maxCapacity = maxCapacity

    # GETTERS
    def getName(self):
        return self.name

    def getVehicles(self):
        return self.vehicles

    def getNumVehicles(self):
        return self.numVehicles

    def getMaxCapacity(self):
        return self.maxCapacity

    # SETTERS
    def setName(self, name):
        self.name = name

    def setVehicles(self, vehicles):
        self.vehicles = vehicles
        self.numVehicles = len(vehicles)

    def setMaxCapacity(self, maxCapacity):
        self.maxCapacity = maxCapacity

    # METHODS
    def addVehicle(self, vehicle):
        self.vehicles.append(vehicle)

    def removeVehicle(self, vehicle):
        if vehicle in self.vehicles:
            self.vehicles.remove(vehicle)
            return True
        else:
            return False

    def isVehicle(self, vehicle):
        if vehicle in self.vehicles:
            return True
        else:
            return False
