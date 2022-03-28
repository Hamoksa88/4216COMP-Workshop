#Programming the menu

def Menu():
    print("Welcome!")
    print("Data Visualisations on a Graph (1)")
    print("Mean Values of Data (2)")
    print("Data for a specific year (3)")
    print("View the data (4)")
    print("Name of Program (5)")
    user_input = (input("What would you like to access?"))

    if(user_input == '1'):
        #------Insert Graph Program Here-----
        print("You Have Chosen Data Visualisations on a Graph")

    elif(user_input == '2'):
        #------Insert Mean Program Here------
        print("You Have Chosen Mean Values of Data")

    elif(user_input == '3'):
        #------Insert Specific Year Program Here------
        print("You Have Chosen Data for a specific year")

    elif(user_input == '4'):
        #------Insert Data Viewing Program Here------
        print("You Have Chosen to View the Data")

    elif(user_input == '5'):
        print('You have chosen...')
        #------Enter Your Program Here------

    else:
        print('You Have Entered an Incorrect Value')
        Menu()

Menu()