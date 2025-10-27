print("Namaskara Mysuru!")
print("Namaskara Bengaluru!")
print("Namaste, nanna hesaru Puneeth!")
a=19
b=21
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a//b)
print(a%b)
print(a**b)
print(a+b-a-b*2**3//4)

Temp=a
a=b
b=Temp
print("After swapping:")
print("a:", a)
print("b:", b)

name="Puneeth"
age=19
height=5.9
is_student=True
weight=62
print(type(is_student))
s="100"
print(int(s)+age)

boy_name=input("Boy name: ")
boy_age=int(input("Boy age: "))
girl_name=input("Girl name: ")
girl_age=int(input("Girl age: "))

# Using abs because sometimes boy might be younger than girl
age_diff=abs(boy_age-girl_age)
print(boy_name+" loves "+girl_name+" Age difference is "+str(age_diff)+" years.")

print(f"{boy_name} loves {girl_name} Age difference is {age_diff} years.")
