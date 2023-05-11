from employee import Employee
class Manager(Employee):
    def __init__(self, firstName, lastName, age, salary,employees=None):
        super().__init__(firstName,lastName,age,salary)
        if employees == None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self,emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self,emp):
        if emp in self.employees:
            self.employees.remove(emp)
    
    def show_employees(self):
        for emp in self.employees:
            print(f"Employee {self.employees.index(emp)}: {emp.display_full_name()}")
