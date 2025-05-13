import sys
# Возвращает значение массива определенной длины на данной позиции
def circ_array(length, position):
    return position%length+1

# Получение входных данных
try:
    n = int(sys.argv[1])
    m = int(sys.argv[2])
except:
    print("Wrong input!")
    sys.exit()

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


