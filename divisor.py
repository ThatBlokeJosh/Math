x = int(input("Enter number: "))

i = 1
while i <= x:
    modulusX = x % i
    if modulusX == 0:
        print(i)
    i += 1