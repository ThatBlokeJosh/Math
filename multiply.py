x = int(input("Enter number: "))
y = int(input("Enter number: ")) 
i = 1
listx = []
listy = []

for thing in range(100):
    listx.append(x * i)
    listy.append(y * i)
    i += 1
print(listx)

for item in listx:
    if listy.__contains__(item):
        print(item)
        break
    