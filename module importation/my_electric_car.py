from car import ElectricCar

tesla1 = ElectricCar('tesla', 'model s', 2020)
print(tesla1.get_descriptive_name())
tesla1.battery.describe_battery()
tesla1.battery.get_range()