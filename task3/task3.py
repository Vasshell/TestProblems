def assignValue(object, values):
    for value in values:
        if object['id'] == value['id']:
            object["value"] = value["value"]
            break

import json

def findBottom(object):
    if "values" in object:
        for value in object["values"]:
            findBottom(value)
            assignValue(object,values["values"])
    else:
        return assignValue(object,values["values"])


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

for test in tests["tests"]:
    findBottom(test)

json.dump(tests,reportFile, indent=4)
valuesFile.close()
testsFile.close()
reportFile.close()