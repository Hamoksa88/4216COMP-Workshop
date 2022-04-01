##Import modules:

from asyncio import protocols
import csv
import matplotlib.pyplot as plt

#Sample Data
year = [1946, 1947, 1948, 1949, 1950, 1951, 1952, 1953, 1954, 1955, 1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966, 1967, 1968, 1969, 1970, 1971, 1972, 1973, 1974, 1975, 1976, 1977, 1978, 1979, 1980, 1981, 1982, 1983, 1984, 1985, 1986, 1987, 1988, 1989, 1990, 1991, 1992, 1993, 1994, 1995, 1996, 1997, 1998, 1999, 2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020]
kilometres = [47.0, 37.0, 34.2, 34.0, 32.5, 33.5, 33.3, 33.5, 33.3, 32.7, 34.0, 36.4, 35.0, 35.8, 34.7, 33.9, 31.8, 31.5, 32.0, 30.1, 29.7, 29.1, 28.7, 29.6, 30.4, 30.1, 28.3, 29.8, 30.9, 30.3, 28.6, 29.3, 30.7, 32.0, 30.3, 29.7, 27.2, 29.5, 29.5, 30.4, 30.8, 32.4, 34.3, 33.3, 33.2, 32.5, 31.7, 30.4, 28.7, 30.0, 32.1, 34.7, 36.3, 38.6, 38.3, 39.3, 39.8, 41.0, 41.8, 43.3, 46.3, 49.1, 50.9, 51.5, 54.5, 57.1, 58.3, 60.2, 62.9, 64.7, 66.0, 66.2, 67.7, 66.8, 12.5]
year2 = ['1986', '1987', '1988', '1989', '1990', '1991', '1992', '1993', '1994', '1995', '1996', '1997', '1998', '1999', '2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020']
ticket = [1047, 1168, 1291, 1357, 1483, 1514, 1551, 1577, 1559, 1720, 1870, 2048, 2242, 2463, 2463, 2585, 2693, 2890, 3088, 3323, 3714, 4120, 4443, 4608, 4965, 5447, 5816, 6162, 6649, 7008, 7269, 7584, 8106, 8133, 1560]
s_ticket = [395, 454, 512, 550, 574, 603, 603, 616, 611, 660, 702, 773, 847, 905, 950, 964, 970, 1011, 1071, 1170, 1298, 1434, 1561, 1571, 1654, 1782, 1890, 2041, 2153, 2205, 2171, 2072, 2136, 2076, 333]

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


#Menu Dedicated to Passenger Kilometre Data
def pkMenu():
    print("You Have Selected the Passenger Kilometre Options")
    print("Please Select From the Following4")
    print("Data Visualisation on a Graph (1)")
    print("Mean Values of Data (2)")
    print("Highest and lowest values of data (3)")
    print("View the data (4)")
    user_input = input("What would you like to access?")

    if(user_input == '1'):
        print("You Have Chosen Data Visualisation on a Graph")
        pk_DataVisualisation()

    elif(user_input == '2'):
        print("You Have Chosen Mean Values of Data")
        pk_Mean()

    elif(user_input == '3'):
        print("You Have Chosen highest and lowest values of data.")
        pk_HighestLowest()
        
    elif(user_input == '4'):
        print("You Have Chosen to View the Data")
        pk_ViewData()

    else:
        print('You Have Entered an Incorrect Value')
        pkMenu()

#Menu Dedicated to Passenger Revenue Data
def prMenu():
    print('''You Have Selected the Passenger Revenue Options
    Please Select From the Following
    Graph visualisation of data (1)
    Mean values of data (2)
    Lowest and highest values of data (3)
    View the Data (4)
    ''')
    user_input = input("What would you like to access?")
    
    if user_input == '1':
        print("You have selected graph visualisation of data.")
        pr_DataVisualisation()
    
    elif user_input == '2':
        print("You have selected the mean amounts of data.")
        pr_Mean()
    
    elif user_input == '3':
        print("You have selected the lowest and highest amounts of data.")

    elif user_input == '4':
        print("You have selected to view the data.")
        pr_ViewData()
    
    else:
        print("You have entered an incorrect value.")
        prMenu()



#-------------Passenger Kilometre Functions--------------


#Calculates the Mean Using Passenger Kilometre Data
def pk_Mean():
    temp = []
    for val in pkData:
        if val[1] != ":":
            temp.append(float(val[1]))

    mean = sum(temp) / len(temp)
    print("The mean kilometres travelled from 1938-2021 is", mean)


#Calculates the Highest and Lowest Using Passenger Kilometre Data
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


#Creates a Graph Using Passenger Kilometre Data
def pk_DataVisualisation():

    fig, ax = plt.subplots()

    fig.suptitle("Passenger Kilometres Travelled in Great Britain", fontsize=16)

    ax.set_title("1946-2020", fontsize=14)

    ax.set_xlabel("Year", fontsize=12)

    ax.set_ylabel("Kilometres (Billions)", fontsize=12)

    ax.plot(year, kilometres, 'ro-')

    ax.xaxis.grid()
    ax.yaxis.grid()

    plt.show()

#Prints the Passenger Kilometre Data to the User
def pk_ViewData():
    for r in pkData: print(r)




#----------Passenger Revenue Functions------------


#Calculates the Mean Using Passenger Revenue Data
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


#Prints the Passenger Revenue Data to the User
def pr_ViewData():
    for r in prData: print(r)


#Creates a Graph Using Passenger Revenue Data
def pr_DataVisualisation(): 
    fig1, ax1 = plt.subplots()

    fig1.suptitle("Passenger Revenue by Ticket Type", fontsize=16)

    ax1.set_title("Apr1986 - Apr2020", fontsize=14)

    ax1.set_xlabel("Year", fontsize=12)

    ax1.set_ylabel("(£ million)", fontsize=12)

    ax1.plot(year2, ticket)
    ax1.plot(year2, s_ticket)

    ax1.xaxis.grid()
    ax1.yaxis.grid()

    plt.show()


#Main:
print("Welcome")
print("Passenger Kilometre Data Options (1)")
print("Passenger Revenue Data Options(2)")
user_choice = int(input("Which Data Would You Like to Access?"))

if(user_choice == 1):
    pkMenu()
elif(user_choice == 2):
    prMenu()