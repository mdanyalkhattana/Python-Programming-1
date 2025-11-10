from abc import ABC, abstractmethod

class Vehicle(ABC):
    def __init__(self,vehicle_no):
        self.vehicle_no = vehicle_no
    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass

    @abstractmethod
    def calculate_fare(self, distance):
        pass

# /////// Car class

class Car(Vehicle):
    def start(self):
        print(f"Car {self.vehicle_no} started.")

    def stop(self):
        print(f"Car {self.vehicle_no} stopped.")

    def calculate_fare(self, distance):
        return distance * 15  # Rs 15 per km

# /////// Bike class

class Bike(Vehicle):
    def start(self):
        print(f"Bike {self.vehicle_no} started.")

    def stop(self):
        print(f"Bike {self.vehicle_no} stopped.")

    def calculate_fare(self, distance):
        return distance * 8  # Rs 8 per km
# /////// Rikshaw class

class Rickshaw(Vehicle):
    def start(self):
        print(f"Rickshaw {self.vehicle_no} started.")

    def stop(self):
        print(f"Rickshaw {self.vehicle_no} stopped.")

    def calculate_fare(self, distance):
        return distance * 10  # Rs 10 per km

# ======================================
# 🔹 Driver Class (Encapsulation)
# ======================================
class Driver:
    def __init__(self, name, license_no, vehicle):
        self.name = name
        self.__license_no = license_no  # private attribute
        self.vehicle = vehicle
        self.__earnings = 0  # private variable

    def add_earning(self, amount):
        """Encapsulation: only this method can modify earnings"""
        self.__earnings += amount

    def get_earnings(self):
        return self.__earnings

    def get_license_no(self):
        return self.__license_no

# ======================================
# 🔹 Ride Class
# ======================================
class Ride:
    def __init__(self, pickup, drop, passenger, distance, driver):
        self.pickup = pickup
        self.drop = drop
        self.passenger = passenger
        self.distance = distance
        self.driver = driver
        self.status = "Pending"
        self.fare = 0

    def start_ride(self):
        self.driver.vehicle.start()
        self.status = "Ongoing"
        print(f"Ride started from {self.pickup} to {self.drop}.")

    def end_ride(self):
        self.driver.vehicle.stop()
        # Polymorphism → fare depends on vehicle type
        self.fare = self.driver.vehicle.calculate_fare(self.distance)
        self.status = "Completed"
        self.driver.add_earning(self.fare)
        print(f"Ride ended. Fare = Rs {self.fare}")

# ======================================
# 🔹 RideManager Class (Bonus)
# ======================================
class RideManager:
    def __init__(self):
        self.drivers = []

    def add_driver(self, driver):
        self.drivers.append(driver)

    def assign_driver(self):
        """Find best driver (lowest earnings means more available)"""
        if not self.drivers:
            return None
        return min(self.drivers, key=lambda d: d.get_earnings())


# ======================================
# 🔹 Main Execution
# ======================================
if __name__ == "__main__":
    # Create vehicles
    car = Car("CAR-123")
    bike = Bike("BIKE-456")
    rickshaw = Rickshaw("RICK-789")

    # Create drivers
    d1 = Driver("Ali", "LIC123", car)
    d2 = Driver("Bilal", "LIC456", bike)
    d3 = Driver("Hassan", "LIC789", rickshaw)

    # Ride manager
    manager = RideManager()
    manager.add_driver(d1)
    manager.add_driver(d2)
    manager.add_driver(d3)

    # Assign driver automatically
    assigned_driver = manager.assign_driver()
    print(f"Driver assigned: {assigned_driver.name} ({assigned_driver.vehicle.__class__.__name__})")

    # Create a ride
    ride = Ride("Gulshan", "Saddar", "Ahmed", 12, assigned_driver)

    # Start and end ride
    ride.start_ride()
    ride.end_ride()

    # Show earnings
    print(f"Driver {assigned_driver.name} total earnings: Rs {assigned_driver.get_earnings()}")

