class Acount:
 def __init__(self,bal,acc):
    self.bal=bal
    self.acc=acc
    
 def debit(self,amount):
    self.bal-=amount
    
 def credit(self,amount):
     self.bal+=amount
     
a1= Acount(500000,2371)
print("Your account no is:",a1.acc)
print("Your balance is:",a1.bal)
a1.debit(2500)
print("After debit your balance is:",a1.bal)
a1.credit(10000)
print("After credit your balance is:",a1.bal,"Credited on 2025-8-10")

 
    