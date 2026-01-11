import sys

path = sys.argv[1]
with open(path, "r") as file:
    elements = file.readlines()
    for i in range (len(elements)):
        elements[i] = int(elements[i].replace("\n", ""))

average = sum(elements) / len(elements)
closest = min(elements, key=lambda x: abs(x - average))
elements.remove(closest)
moves = 0
for element in elements:
    if element < closest:
        while element != closest and moves <= 20:
            element += 1
            moves += 1
    if element > closest:
        while element != closest and moves <= 20:
            element -= 1
            moves += 1
if moves <=20:
    print(moves)
else:
    print("20 ходов недостаточно для приведения всех элементов массива к одному числу")