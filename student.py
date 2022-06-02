#Add methods to class student - full_name, year_of_birth, initials. Create two instances and verify the work as expected
# Class Method

class Student:
    school = "AkiraChix"
    def __init__(self,firstname,secondname,age,country):
        self.firstname = firstname
        self.secondname = secondname
        self.age=age
        self.country=country

     # class Method
    def full_name(self):
        return f"{self.firstname} {self.secondname}"
        

    def year_of_birth(self):
        
        Current_year= (int(input("Current year: ")))
        birth_year= Current_year-self.age
        return f"{birth_year}"

        
    def initials(self):
        first = self.firstname[0]
        second = self.secondname[0]
        return f"{first}{second}"


    