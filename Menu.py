#Programming the menu

def Menu():
    print("Welcome!")
    print("Data Visualisation on a Graph (1)")
    print("Mean Values of Data (2)")
    print("Data for a specific year (3)")
    print("View the data (4)")
    user_input = (input("What would you like to access?"))

    if(user_input == '1'):
        #------Insert Graph Program Here-----
        print("You have chosen Data Visualisation on a Graph")

    elif(user_input == '2'):
        #------Insert Mean Program Here------
        print("You have chosen Mean Values of Data")

    elif(user_input == '3'):
        #------Insert Specific Year Program Here------
        print("You have chosen Data for a specific year")

    elif(user_input == '4'):
        #------Insert Data Viewing Program Here------
        print("You have chosen View the Data")

    else:
        print('You have entered an incorrect value')
        Menu()

Menu()