import unittest

from vehicle import *
from lot import *
from employee import *
from dealership import *

class TestAllClasses(unittest.TestCase):
    def setUp(self):
        self.vehicle1 = Vehicle("Ford","Focus",2019,"ABCD1234WXYZ","Blue")
        self.vehicle2 = Vehicle("Ford", "Focus", 2019, "ABCD5678WXYZ", "Red")
        self.vehicle3 = Vehicle("Ford", "Focus", 2019, "ABCD9101WXYZ", "Yellow")
        self.lot1 = Lot("Onsite", [self.vehicle1, self.vehicle2, self.vehicle3], 200)
        self.lot2 = Lot("Offsite", [], 750)
        self.employee = Employee("New Employee")
        self.dealership = Dealership("Ford Dealership", [self.lot1, self.lot2])

    def testDealershipClass(self):

    def testLotClass(self):

    def testEmployeeClass(self):


    # Method tests all getters and setters for the Vehicle Class
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
