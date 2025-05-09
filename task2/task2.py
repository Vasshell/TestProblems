#считывание путей к файлам и их открытие
while True:
    circleFilePath = input("Circle coords file: ")
    pointsFilePath = input("Points coords file: ")
    try:
        circleCoords = open(circleFilePath)
        pointCoords = open(pointsFilePath)
        circleX, circleY = circleCoords.readline().split()
        circleX = float(circleX)
        circleY = float(circleY)
        circleR = float(circleCoords.readline())
    except:
        print("Error opening the files and reading coords")
    else:
        break
#расчет для каждой точки по формуле окружности и сравнение с радиусом
for points in pointCoords:
    pointX, pointY = points.split()
    pointX = float(pointX)
    pointY = float(pointY)
    circleEq = (pointX - circleX)**2+(pointY-circleY)**2
    R = circleR ** 2
    if circleEq == R:
        print(pointX,pointY)
        print(0)
    elif circleEq < R:
        print(pointX, pointY)
        print(1)
    else:
        print(pointX, pointY)
        print(2)
#закрытие файла
circleCoords.close()
pointCoords.close()