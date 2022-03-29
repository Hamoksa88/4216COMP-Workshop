##Import modules:

from asyncio import protocols
import csv


##Get data from files:

passengerKilometres = open("PassengerKilometres.csv", "r").readlines()
pkData = []

passengerRevenue = open("PassengerRevenueByTicketType.csv")
prData = []
prYearly = []
prQuarterly = []

dis_reader = csv.reader(passengerKilometres, delimiter=',', quotechar='"')
for row in dis_reader: pkData.append(row)
for i in range(0,3): pkData.pop(0)
pkData.pop(-1)
#for r in pkData: print(r)

rev_reader = csv.reader(passengerRevenue, delimiter=',', quotechar='"')
for row in rev_reader: prData.append(row)
for i in range(0,3): prData.pop(37)
for i in range(0,2): prData.pop(0)
#for r in prData: print(r)

for i in range(0,35): prYearly.append(prData[i])
for i in range(35,len(prData)): prQuarterly.append(prData[i])
#for r in prYearly: print(r)  
#for r in prQuarterly: print(r)


##Functions:

def pkMenu():
    print("Welcome!")
    print("Data Visualisation on a Graph (1)")
    print("Mean Values of Data (2)")
    print("Highest and lowest values of data (3)")
    print("View the data (4)")
    user_input = input("What would you like to access?")

    if(user_input == '1'):
        #------Insert Graph Program Here-----
        print("You Have Chosen Data Visualisation on a Graph")

    elif(user_input == '2'):
        #------Insert Mean Program Here------
        print("You Have Chosen Mean Values of Data")
        pk_Mean()

    elif(user_input == '3'):
        print("You Have Chosen highest and lowest values of data.")
        pk_HighestLowest()
        
    elif(user_input == '4'):
        #------Insert Data Viewing Program Here------
        print("You Have Chosen to View the Data")
    else:
        print('You Have Entered an Incorrect Value')
        pkMenu()

def prMenu():
    print('''Welome to the "Passenger Revenue from tickets" menu!
    Graph visualisation of data (1)
    Mean values of data (2)
    Lowest and highest values of data (3)
    ''')
    user_input = input("What would you like to access?")
    
    if user_input == '1':
        print("You have selected graph visualisation of data.")
    
    elif user_input == '2':
        print("You have selected the mean amounts of data.")
    
    elif user_input == '3':
        print("You have selected the lowest and highest amounts of data.")
    
    else:
        print("You have entered an incorrect value.")
        prMenu()

def pk_Mean():
    temp = []
    for val in pkData:
        if val[1] != ":":
            temp.append(float(val[1]))

    mean = sum(temp) / len(temp)
    print("The mean kilometres travelled from 1938-2021 is", mean)

def pk_HighestLowest():
    temp = []
    year = []
    for val in pkData:
        if val[1] != ":":
            temp.append(float(val[1]))
            year.append(val[0])

    highestYear = year[temp.index(max(temp))]
    lowestYear = year[temp.index(min(temp))]
    print("The highest and lowest distances travelled were", max(temp), "and", min(temp), "in", highestYear, "and", lowestYear, "respectively.")

def pr_Mean():
    prY_OTA = []
    for val in prYearly:
        if val[1] != "[x]": prY_OTA.append(val[1])
    print("Average yearly revenue for ordinary ticket advanced:", sum(prY_OTA) / len(prY_OTA))

    prY_OTAoP = []
    for val in prYearly:
        if val[1] != "[x]": prY_OTAoP.append(val[1])
    print("Average yearly revenu for ordinary ticket anytime or peak:", sum(prY_OTAoP) / len(prY_OTAoP))

    prY_OTOP = []
    for val in prYearly:
        if val[1] != "[x]": prY_OTOP.append(val[1])
    print("Average yearly revenue for ordinary ticket off peak:", sum(prY_OTOP) / len(prY_OTOP))
    

##Main:

pkMenu()