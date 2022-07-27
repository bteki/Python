"""
Concatenating can be difficult and hard to read
2 ways to do this:
    * formate function:
        write the phrase in a single string without concatenating or anything but
        replace the values that contain the variavbles with 2 empty {}
        EX: print("my car is {} and it's plate is {}". formate(car_color, plate))
    * literal strings:
        When constructing a string you add the letter F before the first quotation mark,
        this tells python that this is going to be a literal sting, and then you put variable name inside the braces
        EX: print(f"My car is {car_color} and it's plate is {plate}")

"""

x = 10
y = 5
z = x + y
print("My numbers are {} and {}".format(y,x))
print("The sum of {} and {} is = {}".format(y,x,z))

color = "red"
l_plate = 79686
print(f"The car is {color}  and its License plate is {l_plate}")
