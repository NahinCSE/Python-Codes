# class Student:
#     def __init__(self,name):
#         self.name=name

# s1=Student("Junaid")
# print(s1.name)  # This will print "Junaid"
# del s1.name
# print(s1.name)  # This will raise an AttributeError since 'name' has been deleted
class Account:
    def __init__(self,acc_no,acc_pass):
        self.acc_no = acc_no
        self.__acc_pass=acc_pass
        
    def reset_pass(self):
        print(self.__acc_pass)
        
a1=Account("123456","abcde")
print(a1.acc_no)  # This will print the account number
print(a1.__acc_pass)
#print(a1.reset_pass())#This will print the account password
        
    
                
     