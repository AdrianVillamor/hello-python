# a = bin(4)
# b = hex(10)
# c = max([1,2,3,4,5])
# d = sum([1,2,3,4,5])
# e = sorted([1,2,3,4,5,2])

# print(d)

# def square(x):
#     return x ** 2

# #x = 10
# for y in range(10):
#     print("{}**2 == {}".format(y, square(y)))
import math
def area_circle(radius):
    return math.pi * radius ** 2

data = input("Enter the radius of " + " a circle: ")

f = float(data)

print("Area of the cicle: {:.2f}".format(area_circle(f)))