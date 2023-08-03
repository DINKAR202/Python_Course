import random

a = 20
b = 30
c = a+b
d = 50 + c
print(d)


a = 4
A = "Sally"
print(a)
print(A)
    
    # if else
# if a > b:
#     print("a is greater than b");
# else:
#     print("b is less than a");

# Many Values to Multiple Variables
print("Many Values to Multiple Variables")

x, y, z = "Aditi", "Raju", "Adi"
print(x)
print(y)
print(z)

# many variable is to one value
print("many variable is to one value")
x = y = z = "Adi"
print(x)
print(y)
print(z)

# Unpack a Collection
print("Unpack a Collection")
fruits = ["apple", "bannana", "cherry"]
x,y,z = fruits
print(x)
print(y)
print(z)


# Global Variables
print("1. Global Variables")

x = "awesome"

def myfunc():
    # x = "Dinkar"
    print("Python is " + x)
    
myfunc();

print("Python is " + x)


def myfunc():
      global d
      d = "fantastic"

myfunc()

print("Python is " + d)



f = 20
print(f)
g = float(f)
print(g)
z = complex(f)
print(z)

print(random.randrange(1, 50))