import sys
import json

def processing(tests_1, values_1):
    for values1 in values_1["values"]:
        if "tests" in tests_1:
            for tests1 in tests_1["tests"]:
                if tests1["id"] == values1["id"]:
                    tests1["value"] = values1["value"]
        else:
            for tests1 in tests_1:
                if tests1["id"] == values1["id"]:
                    tests1["value"] = values1["value"]
    if "tests" in tests_1:
        for tests2 in tests_1["tests"]:
            if "values" in tests2:
                tests2["values"] = processing(tests2["values"], values_1)
    else:
        for tests2 in tests_1:
            if "values" in tests2:
                tests2["values"] = processing(tests2["values"], values_1)
    return tests_1

path_tests = sys.argv[1]
path_values = sys.argv[2]
path_report = sys.argv[3]
with open(path_tests, "r") as file1:
    tests = json.load(file1)
with open(path_values, "r") as file2:
    values = json.load(file2)
with open(path_report, "w") as file3:
    report = processing(tests, values)
    json.dump(report, file3, indent=4)