class A:
    varA="This is variable A"
    
class B:
    varB="This is variable B"
    
class C(A,B):
    varC="This is variable C"
    
c1=C()
print(c1.varA)
print(c1.varB)
print(c1.varC)  # This will print "This is variable C"
