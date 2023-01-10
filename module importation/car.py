#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#the Car class
class Car:
    """a simple attempt to represent a car"""
    def __init__(self, make, model, year):
        """Initializes attributes to describe a car"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
        
    def get_descriptive_name(self):
        """Return neatly formatted descriptive name"""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
    
    def read_odometer(self):
        """Prints a statement showing the car's mileage"""
        print(f"This car has {self.odometer_reading} miles on it")
        
    def update_odometer(self, mileage):
        """Set the odometer reading to the given value.
        Reject the change if it attempts to roll the odometer back."""
        
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can roll back odometer reading")
            
    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading"""
        if miles > 0:
            self.odometer_reading += miles
        else:
            print("You can't roll back the odometer")


class Battery:
    """A simple attempt to model the battery of a car"""
    def __init__(self, battery_size=75):
        """Initializes battery attributes"""
        self.battery_size = battery_size

    def describe_battery(self):
        """Print a statement describing the battery"""
        print(f"This car has a {self.battery_size} KWh battery")

    def get_range(self):
        """Prints statement about the range of of this battery"""
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 315

        print(f"This car can go about {range} miles on a full charge")

    def upgrade_battery(self):
        """Checks the battery capacity and upgrades it"""
        if self.battery_size != 100:
            self.battery_size = 100

class ElectricCar(Car):
    """Represents aspects of a car, specific to electric vehicles"""

    def __init__(self, make, model, year):
        """Initializes the attributes of the parent class"""
        super().__init__(make, model, year)
        self.battery = Battery()

