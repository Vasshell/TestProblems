# Возвращает значение массива определенной длины на данной позиции
def circ_array(length, position):
    return position%length+1

# Получение входных данных
while True:
    try:
        n, m = input("Array length and interval length (n,m): ").split()
        n = int(n)
        m = int(m)
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


