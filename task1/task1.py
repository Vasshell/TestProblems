# Возвращает значение массива определенной длины на данной позиции
def circ_array(length, position):
    return position%length+1

# Получение входных данных
while True:
    try:
        n = int(input("Array length (n): "))
    except:
        print("Wrong input!")
    else:
        break

while True:
    try:
        m = int(input("Interval length (m): "))
    except:
        print("Wrong input!")
    else:
        break
num = 0
step = 0
answer = ""
# Выяснение пути
while True:
    num = circ_array(n,step)
    answer += str(num)
    step+=(m-1)
    num = circ_array(n, step)
    if num == 1:
        break
print(answer)


