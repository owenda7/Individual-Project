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
        self.numVehicles += 1

    def removeVehicle(self, vehicle):
        if vehicle in self.vehicles:
            self.vehicles.remove(vehicle)
            self.numVehicles -= 1
            return True
        else:
            return False

    def pickUpVehicle(self, vin):
        for i in range(0, len(self.vehicles)):
            if self.vehicles[i].getVin() == vin:
                vehicle = self.vehicles[i]
                self.removeVehicle(self.vehicles[i])
                return vehicle
        return None

    def isVehicle(self, vehicle):
        if vehicle in self.vehicles:
            return True
        else:
            return False

    # OVERLOAD toString
    def __str__(self):
        return self.name

