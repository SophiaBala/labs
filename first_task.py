import math

a = 0.6
b = 0.9
h = 0.02
x = a

while x <= b:
    if x < 0.6:
        result = math.cos(math.sqrt(x))
    elif 0.6 <= x < 0.7:
        result = 1/math.tan(x**2)
    else:
        result = math.atan(x ** 3)

    print(f"x = {round(x, 2)}, сума ряду = {round(result, 6)}")
    x = round(x + h, 2)


