import json

# function to add names individually including tags
def add_name(file, name, tags):
    f = open('./data/'+file)
    data = json.load(f)
    if data.get(name)!=None: # check if name already exists
        return 0
    data[name] = tags # create new data
    with open('./data/'+file, 'w') as outfile:
        json.dump(data, outfile) # append data
    return 1

# function to check for repitition throughout the whole json files