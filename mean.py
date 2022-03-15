import csv

with open('PassengerKilometers.csv') as f:
    csv_reader = csv.reader(f)
    next(csv_reader)

    C = []
    for row in csv_reader:
        if row[1] != ':':
            data = float(row[1])
            C.append(data)
        
    C_ave = sum(C) / len(C)
    print(f"C average: {C_ave}")
    