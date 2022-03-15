

#Get data from files:

from asyncio import protocols


passengerKilometres = open("PassengerKilometres.csv", "r").readlines()
pkYears = []
pkDistance = []

passengerRevenue = open("PassengerRevenueByTicketType.csv", "r").readlines()
prYears = []
prAdvanced = []
prPeak = []
prOffPeak = []
prOther = []

for line in passengerKilometres: pkYears.append(line[:4])
for i in range(0,3): pkYears.pop(0)
pkYears.pop(-1)

for line in passengerKilometres:
    try: 
        try: pkDistance.append(float(line[5:9]))
        except: pkDistance.append(float(line[8:12]))
    except: pkDistance.append("N/A")
for i in range(0,3): pkDistance.pop(0)
pkDistance.pop(-1)


for line in passengerRevenue[3:38]:
    temp = []
    #if line in [passengerRevenue[0], passengerRevenue[1], passengerRevenue[2]]: continue
    temp = line.split(",")
    
    
    print(temp)

    prYears.append(temp[0])
    prAdvanced.append(temp[1])
    prPeak.append(temp[2])
    prOffPeak.append(temp[3])
    prOther.append(temp[4])

    