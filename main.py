import csv
import random
from vehicle import *
from lot import *
from employee import *
from dealership import *


def main():
    # call setup test function to create a dealership
    burlingtonFord = setupTest()

    # Show that lots are populated properly
    printLots(burlingtonFord)
    printNumVehiclesInLots(burlingtonFord)

    
# function takes in a dealership and prints out all vehicles on all lots
def printLots(dealership):
    for i in range(0, len(dealership.getLots())):
        print("\n--------" + dealership.getLots()[i].getName() + "--------")
        for j in range(0, len(dealership.getLots()[i].getVehicles())):
            print(dealership.getLots()[i].getVehicles()[j])

# function takes in a dealership and prints the number of vehicles on each lot
def printNumVehiclesInLots(dealership):
    for i in range(0, len(dealership.getLots())):
        print("\n" + dealership.getLots()[i].getName() + " Size: " + str(dealership.getLots()[i].getNumVehicles()))

# function creates a dealership and populates two lots randomly
def setupTest():
    # Create Onsite and offsite lots
    onsite = Lot("Onsite", [], 350)
    offsite = Lot("Offsite", [], 750)

    # Populate both lots with random new Ford cars to 4/5 the max capacity for testing
    models = ["Escape", "Focus", "Fiesta", "Ecosport", "F-150", "F-250", "F-350", "F-550", "Transit"]
    colors = ["Blue", "Red", "Green", "Yellow", "White", "Black", "Grey"]
    vinCharacters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
                     'U', 'V', 'W', 'X', 'Y', 'Z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    # Populate onsite
    for x in range(0, int((4 * onsite.getMaxCapacity()) / 5)):
        vin = str(x)
        while len(vin) != 17:
            vin = vin + vinCharacters[random.randint(0, len(vinCharacters) - 1)]
        onsite.addVehicle(Vehicle("Ford", models[random.randint(0, len(models) - 1)], 2020, vin,
                                  colors[random.randint(0, len(colors) - 1)]))

    # Populate offsite
    for x in range(0, int((4 * offsite.getMaxCapacity()) / 5)):
        vin = str(x)
        while len(vin) != 17:
            vin = vin + vinCharacters[random.randint(0, len(vinCharacters) - 1)]
        offsite.addVehicle(Vehicle("Ford", models[random.randint(0, len(models) - 1)], 2020, vin,
                                   colors[random.randint(0, len(colors) - 1)]))

    # Put both lots into a dealership
    burlingtonFord = Dealership("Burlington Ford", [onsite, offsite])

    return burlingtonFord
main()

