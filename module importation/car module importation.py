from car import Car

my_car = Car('mistubishi', 'evolution', 2017)
print(my_car.get_descriptive_name())
my_car.odometer_reading = 20000
my_car.read_odometer()


