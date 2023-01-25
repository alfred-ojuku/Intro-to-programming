class Employee:
    """
    This class creates employee objects with different names and salaries
    """
    def __init__(self, f_name, l_name, annual_salary):
        """Stores name and salary attributes """
        self.f_name = f_name
        self.l_name = l_name
        self.annual_salary = annual_salary


    def give_raise(self, raise_amount=5000):
        """Adds $5000 to the annual salary but also accepts a different value"""
        self.annual_salary += raise_amount
        return self.annual_salary

    def show_salary(self):
        """Shows the current amount of salary"""
        print(self.annual_salary)






