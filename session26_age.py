from datetime import date
class person:
    def __init__(self,name,age):
         self.name = name
         self.age = age

    @classmethod
    def birthyear(cls,name,year):
        return cls(name,date.today().year - year)

    @staticmethod
    def isAdult(age):
        return age>18

p1 = person("swara",13)
p2 = person.birthyear("eisha",2007)

print(p1.age)
print(p2.age)

print(p2.isAdult(13))
                  
