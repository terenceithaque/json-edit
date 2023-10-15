import json


def read_data(path):
    f = open(path, "r", encoding="utf-8")
    donnees = json.load(f)
    print(donnees)
    f.close()

    return dict(donnees)
