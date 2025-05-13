#библиотеки для упрощения решения
import statistics
import math
import sys

#открытие файла
with open(sys.argv[1]) as f:   #запись чисел в массив
    nums = []
    for line in f:
        nums.append(int(line))

#вычисление медианы и ее целого значения
median = math.ceil(statistics.median(nums))
steps = 0

#подсчет ходов до медианы
for num in nums:
    if num != median:
        steps += abs(median-num)
print(steps)

