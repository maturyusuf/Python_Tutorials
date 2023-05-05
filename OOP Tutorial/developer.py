from employee import Employee
class Developer(Employee):   # Developer inherits from Employee
    def __init__(self, firstName, lastName, age, salary,pLang,devExp):
        super().__init__(firstName,lastName,age,salary)
        self.pLang =pLang
        self.devExp = devExp