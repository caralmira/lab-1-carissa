import json

def write(new_data, filename='wishlist/fixtures/initial_wishlist_data.json'):
    file = open(filename,'r+')
    all_data = json.load(file)
    all_data.append(new_data)
    file.seek(0)
    json.dump(all_data, file)
