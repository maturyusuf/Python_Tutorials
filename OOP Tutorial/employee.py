
class Employee:
    #class variables
    num_of_emps =0  
    raise_amount=1.04 

    def __init__(self,firstName,lastName,age,salary):
        #instance variables
        self.firstName = firstName   
        self.lastName = lastName
        self.age = age
        self.salary = salary


        Employee.num_of_emps += 1  
        #we used class name for this instead of self because self is for attributes and variables that are unique and dependent regarding instances.
        #in this case,we don't want num_of_emps to be change by the instances.We want it to be owned by class itself so since we dont want it bo be dependent to the instances
        # we dont use "self".Instead we use class' name
        #when an instance is created,it will automatically start the constructor which means add num_of_emps 1

    def display_full_name(self):                            # it's a regular method,which automatically takes instance as the first argument
        return f"{self.firstName} {self.lastName}" 

    def apply_raise(self):
        self.salary = int(self.salary * self.raise_amount)

    @property                                                               #property decorator allows us to access some methods as they're attributes.
    def email(self):                                                        # also ,it allows us to access or change these attributes via getters and setters.   
        return f"{self.firstName}.{self.lastName}@gmail.com"

    @property
    def full_name_with_property_decorator(self):                            # this will allow us to access methods as they're attributes and make changes like getters and setters
        return f"{self.firstName} {self.lastName}" 

    @classmethod
    def set_raise_amount(cls,amount):                       #it's a class method,which autaomatically takes class as the first argument.By convention, 
        cls.raise_amount = amount


    @classmethod                                            #also,class methods can be used as alternative constructor as in this example
    def from_string(cls,emp_string):
        first,last,age,salary = emp_string.split("-")
        return cls(first, last, age, salary)

    @staticmethod                                           # static methods doesnt take any argumetns automatically like in regular or class methods
    def is_workday(day):
        if day.weekday() == 5 or day.weekday == 6:
            return False
        return True

    def __repr__(self):   #dunder methods #1 __repr__:
        return f"__rerp__-Employee({self.firstName},{self.lastName},{self.age},{self.email})"

    def __str__(self):  #dunder mathods #2 __str__:
        return f"__str__-{self.firstName}-{self.email}"

    def __add__(self,other):   #now using dunder method,we'll try to sum two instances' salary and return it
        return self.salary + other.salary

    def __len__(self):
        return len(self.display_full_name())

    @full_name_with_property_decorator.setter   # it's a setter which we use for changing value of an attribute defined by a property decorator.
    def fullname_setter(self,name):                #it's same as setters in other languages
        first , last = name.split(" ")
        self.firstName = first
        self.lastName = last

    @full_name_with_property_decorator.getter  #it'S a getter which we use for getting value of an attribute
    def fullname_and_email_getter(self):
        return f"{self.firstName} {self.lastName} {self.email}"

    @full_name_with_property_decorator.deleter
    def name_deleter(self):
        self.firstName = None
        self.lastName = None