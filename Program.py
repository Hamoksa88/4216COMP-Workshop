

#Get data from files:

passengerKilometres = open("PassengerKilometres.csv", "r").readlines()
pkYears = []
pkDistance = []

passengerRevenue = open("PassengerRevenueByTicketType.csv", "r").readlines()

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
