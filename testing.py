import unittest

from vehicle import *
from lot import *
from employee import *
from dealership import *

# TestAllClasses tests

class TestAllClasses(unittest.TestCase):
    def setUp(self):
        self.vehicle1 = Vehicle("Ford", "Focus", 2019, "ABCD1234WXYZ", "Blue")
        self.vehicle2 = Vehicle("Ford", "Focus", 2019, "ABCD5678WXYZ", "Red")
        self.vehicle3 = Vehicle("Ford", "Focus", 2019, "ABCD9101WXYZ", "Yellow")
        self.lot1 = Lot("Onsite", [self.vehicle2, self.vehicle3], 200)
        self.lot2 = Lot("Offsite", [], 750)
        self.employee = Employee("New Employee")
        self.dealership = Dealership("Ford Dealership", [self.lot1])

    # Method tests the Dealership Class

    def testDealershipClass(self):
        self.dealership.setName("Toyota Dealership")
        assert self.dealership.getName() == "Toyota Dealership", "setName() or getName() methods not working"
        self.dealership.addLot(self.lot2)
        assert self.dealership.getLots() == [self.lot1, self.lot2], "addLot() or getLot() methods not working"

    # Method tests the Lot Class

    def testLotClass(self):
        self.lot1.setMaxCapacity(300)
        assert self.lot1.getMaxCapacity() == 300, "setMaxCapacity() or getMaxCapacity() methods not working"
        self.lot1.addVehicle(self.vehicle1)
        assert self.lot1.isVehicle(self.vehicle1) == True, "isVehicle() method not working"
        assert self.lot1.removeVehicle(self.vehicle1) == True, "removeVehicle() method not working"
        self.lot2.setVehicles([self.vehicle1])
        assert self.lot2.getVehicles() == [self.vehicle1], "setVehicles() and getVehicles() methods not working"
        self.lot2.setName("Autoshine")
        assert self.lot2.getName() == "Autoshine", "setName() or getName() methods not working"

    # Method tests the Employee Class

    def testEmployeeClass(self):
        self.employee.setName("My Name")
        assert self.employee.getName() == "My Name", "setName() or getName() methods not working"
        self.employee.setVehicle(self.vehicle1)
        assert self.employee.hasAVehicle() == True, "hasAVehicle() method not working"
        assert self.employee.hasVehicle(self.vehicle2) == False, "hasVehicle() method not working"
        assert self.employee.removeVehicle() == self.vehicle1, "removeVehicle() method not working"

    # Method tests the Vehicle Class

    def testVehicleClass(self):
        # Change all attributes
        self.vehicle1.setMake("Toyota")
        self.vehicle1.setModel("Prius")
        self.vehicle1.setYear(2020)
        self.vehicle1.setVin("ABCDEF123456")
        self.vehicle1.setColor("Green")

        # Test using getters
        assert self.vehicle1.getMake() == "Toyota", "setMake() or getMake() methods not working"
        assert self.vehicle1.getModel() == "Prius", "setModel() or getModel() methods not working"
        assert self.vehicle1.getYear() == 2020, "setYear() or getYear() methods not working"
        assert self.vehicle1.getVin() == "ABCDEF123456", "setVin() or getVin() methods not working"
        assert self.vehicle1.getColor() == "Green", "setColor() or getColor() methods not working"


if __name__ == "__main__":
    unittest.main()
