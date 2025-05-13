import sys
#считывание путей к файлам и их открытие
try:
    circleCoords = open(sys.argv[1])
    pointCoords = open(sys.argv[2])
    circleX, circleY = circleCoords.readline().split()
    circleX = float(circleX)
    circleY = float(circleY)
    circleR = float(circleCoords.readline())
except:
    print("Error opening the files and reading coords")
    sys.exit()
#расчет для каждой точки по формуле окружности и сравнение с радиусом
for points in pointCoords:
    pointX, pointY = points.split()
    pointX = float(pointX)
    pointY = float(pointY)
    circleEq = (pointX - circleX)**2+(pointY-circleY)**2
    R = circleR ** 2
    if circleEq == R:
        print(0)
    elif circleEq < R:
        print(1)
    else:
        print(2)
#закрытие файла
circleCoords.close()
pointCoords.close()