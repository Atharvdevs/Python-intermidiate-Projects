import main
while True:
    print("1.Add task"
        "\n2.Remove task" 
        "\n3.View task"
        "\n4.Exit")
    try:
        user=int(input("enter the number of the task : "))
    except ValueError:
        print("invalid")
    else:
        if user==1:
            main.add()
        elif user==2:
            main.remove()
        elif user==3:
            main.view()
        elif user==4:
            print("Thanks for Coming")
            break
        else:
            print("Error or Invalid")
