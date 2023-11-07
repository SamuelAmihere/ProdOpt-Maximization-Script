import json

def load_json_data(filename)->json:
    try:
        with open(filename, 'r') as f:
            return(json.load(f))
    except:
        print("Data not read")
        return (None)