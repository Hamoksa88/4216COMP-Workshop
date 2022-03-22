import csv

with open('PassengerKilometers.csv', 'r') as A:
    csv_reader = csv.reader(A)
    next(csv_reader)
    
    B = []
    for row in csv_reader:
        if row[1] != ':':
         data = float(row[1])
         B.append(data)
    
    B_min = min(B)
    B_max = max(B)
    print(f"Least travelled in a year: {B_min}")
    print(f"Most travelled in a year: {B_max}")