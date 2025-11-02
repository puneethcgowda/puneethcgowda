a = 777
a += 100 #a = a + 100 shortform
print(a)
a -= 100 #a = a - 100 shortform
print(a)
a *= 100 #a = a * 100 shortform
print(a)
a /= 100 #a = a / 100 shortform
print(a)
a //= 100 #a = a // 100 shortform
print(a)
a %= 100 #a = a % 100 shortform
print(a)
a **= 100 #a = a ** 100 shortform
print(a)

a=10
b=20
print(a==b)  #equal to
print(a!=b)  #not equal to
print(a>b)   #greater than
print(a<b)   #less than
print(a>=b)  #greater than or equal to
print(a<=b)  #less than or equal to
print(a is b) #identity operator
print(a is not b) #identity operator

print(True and False) #logical and
print(True or False)  #logical or
print(not True)       #logical not
print(not False)      #logical not
print((a<b) and (a!=b)) #combining relational and logical operators
print((a<b) or (a==b))  #combining relational and logical operators
print(not(a<b))          #combining relational and logical operators
print(not(a==b))         #combining relational and logical operators
print((a<b) and not(a==b)) #combining relational and logical operators
print((a<b) or not(a!=b))  #combining relational and logical operators

a = "Puneeth"
b = "Gowda"
print(("P" in a) and ("G" in b)) #membership operator
print(not("P" in a) or ("X" in b))  #membership operator