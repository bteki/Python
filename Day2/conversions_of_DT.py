"""
The process of converting a specific DT into another is called casting
2 types of casting:
    * Implicit: Python converts the DT to another DT automatically
    * Explict: Python needs the user to do something to convert one DT to another

num1 = 20
num2 = 30.5

num1 = num1+num2 #implict conversion

print(type(num1))
print(type(num2))


num1 = 5.8
print(num1)
print(type(num1))

num2 = int(num1)
print(num2)
print(type(num2))
"""

age = input("Tell me your age: ")
print(type(age))

age = int(age)
print(type(age))

new_age = 1+age
print(new_age)
