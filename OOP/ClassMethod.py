# class Person:
#     name="Anonymous"

#     def changename(self,name):
#         self.name=name

# p1=Person()
# p1.changename("Junaid")#This will create a different variable
# print(p1.name)
# print(Person.name)#This will print Anonymous because this variable is not changed

# #first type to change the class variable
# class Person:
#     name="Anonymous"
    
#     def changename(self,name):
#         Person.name=name

# p1=Person()
# p1.changename("Junaid")
# print(p1.name)
# print(Person.name)

# #second type to change the class variable
# class Person:
#     name="Anonymous"
    
#     def changename(self,name):
#         self.__class__.name=name
        
# p1=Person()
# p1.changename("Nahin")
# print(p1.name)
# # print(Person.name)
        
#we wil now use class method
class Person:
    name="Anonymous"
    
    @classmethod
    def changename(cls,name):#here cls is the key word of class
       cls.name=name
       
p1=Person()
p1.changename("Junaid")
print(p1.name)
print(Person.name)
       
      