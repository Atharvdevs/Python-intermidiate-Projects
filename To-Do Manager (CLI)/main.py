import json,save
def view():
    with open("F:\Coding\To-Do list\To-Do_data.json","r") as f:
        data=json.load(f)
        for i,task in enumerate(data,start=1):
            print(f"{i}.",task)

def add():
    """Allow user to add their task"""
    add=input("enter the task you wanna add : ").lower()
    save.save_data(add)

def remove():
    "Allow user to remove their task if done"
    view()
    with open("F:\Coding\To-Do list\To-Do_data.json","r") as f:
        data=json.load(f)
        try:
            remove=int(input("enter the task you wanna remove : "))
        except ValueError:
            print("index only")
        else:
            if len(data)==0:
                print("list is empty")
            elif remove<1 or remove>len(data):
                print("invalid")
            else:
                data.pop(remove-1)
                save.save_data2(data)