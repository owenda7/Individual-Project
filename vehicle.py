class Vehicle:
    # CONSTRUCTOR
    def __init__(self, make, model, year, vin, color):
        self.make = make
        self.model = model
        self.year = year
        self.vin = vin
        self.color = color

    # GETTERS
    def getMake(self):
        return self.make

    def getModel(self):
        return self.model

    def getYear(self):
        return self.year

    def getVin(self):
        return self.vin

    def getColor(self):
        return self.color

    # SETTERS

    def setMake(self, make):
        self.make = make

    def setModel(self, model):
        self.model = model

    def setYear(self, year):
        self.year = year

    def setVin(self, vin):
        self.vin = vin

    def setColor(self, color):
        self.color = color

    # OVERLOAD toString

    def __str__(self):
        rtnString = self.make + " | " + self.model + " | " + str(self.year) + " | " + self.vin + " | " + self.color
        return rtnString
