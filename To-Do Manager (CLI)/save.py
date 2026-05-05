import json
def save_data(user):
    with open("F:\Coding\To-Do list\To-Do_data.json","r") as f:
        data=json.load(f)
    if not isinstance(data,list):
        data=[data]
    data.append(user)
    with open("F:\Coding\To-Do list\To-Do_data.json","w") as f:
        json.dump(data,f)

def save_data2(user):
    with open("F:\Coding\To-Do list\To-Do_data.json","w") as f:
        data=json.dump(user,f)