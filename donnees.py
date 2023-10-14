import json


def read_data(path):
    f = open(path, "r")
    donnees = dict(json.load(f))
    print(donnees)
    f.close()

    return donnees
