class Product():

    def __init__(self, name, price) -> None:
        self.name = name
        self.price = price 

    def __repr__(self) -> str:
        return f'<product{self.name}>'
    
bread = Product('Bread', 65)

print(bread.price)       


#Use the __init__() function to assign
# values to object properties, or other 
#operations that are necessary to do when
# the object is being created


class Student:
    def __init__(self, name, teacher, age) -> None:
        self.name = name
        self.teacher = teacher
        self.age = age
s1 = Student("Gabriella","Mr.Steve", 18)

print(s1.name)
print(s1.teacher)
print(s1.age)


#The __str__() function controls what
#should be returned when the class 
#object is represented as a string.

class Student:
    def __init__(self, name, age) -> None:
        self.name = name   
        self.age = age

    def __str__(self) -> str:
        return f"{self.name}({self.age})"   


s1 = Student("Gabriella", 18)
s2 = Student("Fatuma", 8)

print(s1)
print(s2)

#Gabriella(18)
#Fatuma(8)