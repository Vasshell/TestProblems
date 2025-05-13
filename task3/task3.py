#находит результат теста по id объекта и присваивает его
import sys
import json

def assignValue(object, values):
    for value in values:
        if object['id'] == value['id']:
            object["value"] = value["value"]
            break

#находит все вложенные тесты и вложенные в них тесты и присваивает им результаты через функцию выше
def findBottom(object):
    if "values" in object:
        for value in object["values"]:
            findBottom(value)
            assignValue(object,values["values"])
    else:
        return assignValue(object,values["values"])

#открытие файлов
try:
    valuesFile = open(sys.argv[1])
    testsFile = open(sys.argv[2])
    reportFile = open(sys.argv[3],"w")
except:
    print("Error opening the files")
    sys.exit()

values = json.load(valuesFile)
tests = json.load(testsFile)

#цикл проходит по тестам первой очереди и запускает рекурсивную функцию
for test in tests["tests"]:
    findBottom(test)

#сохранение результата и закрытие файлов
json.dump(tests,reportFile, indent=3)
valuesFile.close()
testsFile.close()
reportFile.close()