#находит результат теста по id объекта и присваивает его
def assignValue(object, values):
    for value in values:
        if object['id'] == value['id']:
            object["value"] = value["value"]
            break

import json

#находит все вложенные тесты и вложенные в них тесты и присваивает им результаты через функцию выше
def findBottom(object):
    if "values" in object:
        for value in object["values"]:
            findBottom(value)
            assignValue(object,values["values"])
    else:
        return assignValue(object,values["values"])

#открытие файлов
while True:
    valuesFilePath = input("Values file: ")
    testsFilePath = input("Tests file: ")
    reportFilePath = input("Report file: ")
    try:
        valuesFile = open(valuesFilePath)
        testsFile = open(testsFilePath)
        reportFile = open(reportFilePath,"w")
    except:
        print("Error opening the files")
    else:
        break

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