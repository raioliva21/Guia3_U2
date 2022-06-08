import json

def open_file(file):

    try:
        with open(file, 'r') as fichero:
            data = json.load(fichero)
    except TypeError:
        data = []
    
    return data

# se añade data en archivo json
def save_data(data, file):
    
    try:
        with open(file, "w") as fichero:
            json.dump(data, fichero, indent=4)
    except TypeError:
        file = []