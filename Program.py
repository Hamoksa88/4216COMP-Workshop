

#Get data from files:

from asyncio import protocols
import csv

passengerKilometres = open("PassengerKilometres.csv", "r").readlines()
pkYears = []
pkDistance = []

passengerRevenue = open("PassengerRevenueByTicketType.csv")
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



csv_reader = csv_reader(passengerRevenue, delimiter=',', quotechar='"')
i = 0
for row in csv_reader:
    if i in [1,2,3]: i += 1 continue else: i += 1 print(row)
    