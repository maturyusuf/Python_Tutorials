from employee import Employee
from developer import Developer
from manager import Manager

emp1 = Employee("Yusuf", "Matur", 23, 20000)
emp2 = Employee("Deniz", "Matur", 20, 15000)




print(Employee.raise_amount)
print(emp1.raise_amount)
print(emp2.raise_amount)
print("-------------------------------------------------")

# emp1.raise_amount = 1.06   we only changed instance emp1's raise amount 

print(Employee.raise_amount)
print(emp1.raise_amount)
print(emp2.raise_amount)

print(Employee.num_of_emps)
print("-------------------------------------------------")

 # since it's a class method,it will automatically take the class we specified as the first argument.
 # Alternatively,we can use an instance to instead of class but by convention,using class' name for class method is a better way.
Employee.set_raise_amount(1.05)

print(Employee.raise_amount)
print(emp1.raise_amount)
print(emp2.raise_amount)

print("-------------------------------------------------")

emp3_string ="Ahmet-Ege-15-10000" 

emp3=Employee.from_string(emp3_string) # we used classmethod as alternative constructor

print(emp3.display_full_name())

print("-------------------------------------------------")

import datetime
my_Date = datetime.date(2023,5,4)
print(Employee.is_workday(my_Date)) # it returns if it's workday or off-day.Its from static method,which doenst take class or instance as the first argument.

print("-------------------------------------------------")

dev_1 = Developer("Ege","Avcioglu",15,25000,"Dart",2)
dev_2 = Developer("Hakan","Polat",23,50000,"Python",3)

print(dev_1.email)
print(dev_2.email)

print("Before raise:" + str(dev_1.salary))  #2500
dev_1.apply_raise()
print("After raise:" + str(dev_1.salary))   #2650

print(dev_1.pLang)
print(dev_1.devExp)
print(dev_2.pLang)
print(dev_2.devExp)

manager_1 = Manager("Sue", "Smith", 28, 25000,[dev_1,dev_2])
print(manager_1.email)
manager_1.show_employees()

manager_1.add_emp(Developer("Jonathan", "Brick", 25, 26000, "Java", 5))

manager_1.show_employees()

print(isinstance(manager_1, Manager))  

print(issubclass(Developer, Employee))


print(emp1)

print(repr(emp1))  # == print(emp1.__repr__())
print(str(emp1))   # == print(emp1.__str__())
#above and below are actually the same
print(emp1.__repr__())
print(emp1.__str__())

#example of dunder methods:

print(int.__add__(1, 2))

print(str.__add__("add", " dunder"))


#Our instances:
#emp1 = Employee("Yusuf", "Matur", 23, 20000)
#emp2 = Employee("Deniz", "Matur", 20, 15000)

print(emp1 + emp2)  
#above , the reason we were able to sum two instances and receive their overall salaries as
# result,is that in Employee class,we used a dunder method callaed "__add__".This method allows
# us to add a value to another value.If we didn't use __add__ in the Employee class,in that case,
# this expression would throw an exception. 


print(len(str("test")))
#tis is same as:
print("test".__len__())

print(len(emp1))  
# we were able to use this method on emp1 because
#Employee contains __len__ dunder method which returns full name's length 

print(emp1.full_name_with_property_decorator)
print(emp1.email)
print(emp3.full_name_with_property_decorator)
print(emp3.email)

#Above,we're able to access some methods as they'Re attributes via property decorators.
#we can make amends in these attributes via property decorator.Also this won't allow us to
#directyly change the value of this property.In that case,we have to use setter
print("-------------------------------")
emp1.fullname_setter = "Google Academy"

print(emp1.full_name_with_property_decorator)


print(emp1.fullname_and_email_getter)


print("-----------------------------")

print(emp1.firstName)
print(emp1.lastName)

#Now we use deleter on firstName and lastName attributes of emp1 instance
#so Now we can use "del" expression on attributes
del emp1.name_deleter

print(emp1.firstName)
print(emp1.lastName)