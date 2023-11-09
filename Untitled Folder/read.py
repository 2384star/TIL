import json

with open("test.json","r") as fd:
    obj=json.load(fd)

print(obj)
