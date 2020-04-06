# Individual-Project

<h3>Data Description: </h3>

For my dataset, I chose to model a car dealership and tracking all the vehicles on the lot.
At the dealership I work at, we have an offsite lot which holds nearly 600 cars as well as an
onsite lot that is divided into 6 sub-lots (main lot, auto shine, Ford sales, Toyota sales, top lot,
road). With over a thousand cars on site, it is difficult to keep track of vehicles and our current
system for keeping track of vehicles is via pen and paper, an excel spreadsheet, and
communication via a work flip phone. 

Needless to say this process is outdated, so for this project I will be using the following
entities to model Vehicles, Lots, and Employees to keep track of vehicle data and their locations.
Vehicles can reside on a lot or with an Employee (if the employee is transferring the car from lot
to lot or giving a customer a test drive). While lots can have multiple vehicles at once,
Employees can only have one vehicle at a time. The lot entity also has a current capacity, max
capacity, and full attributes so employees can know where there is space to store vehicles. 

<h3>Entities: </h3>

* Vehicle
    * make: string
    * model: string
    * year: int
    * vin: string
    * color: string
    
* Lot
    * name: string
    * vehicles: set<Vehicle>
    * numVehicles: int
    * maxCapacity: int
    
* Employee
    * name: string
    * vehicle: Vehicle
    
* Dealership
    * name: string
    * lots: set<Lot>

<h3>Operations: </h3> 

* Vehicle
    * Constructor
    * Getters and Setters for all 5 entities
    
* Lot 
    * Constructor
    * Getters for all 4 entities
    * Setters for name, vehicles, and maxCapacity
        * numVehicles automatically updated when vehicles added or removed
    * isVehicle method returns True if vehicle is on lot or False otherwise
    * removeVehicle method removes vehicle from vehicles list and returns that Vehicle
    * addVehicle method takes a Vehicle object and adds it to vehicles
    * pickUpVehicle method takes a vin number and returns a vehicle 
    
* Employee
    * Constructor 
    * getters and setter for both entities
    * hasVehicle method returns true if employee has a Vehicle
    * removeVehicle method removes vehicle and returns copy of vehicle
    
* Dealership
    * Constructor
    * Getters for both attributes
    * Setter for name
    * addLot method adds lot to lots
    * removeLot method removes lot if it exists in lots and returns true, otherwise returns false
    * findVehicle method returns Lot location or error message 
