import csv

with open('/Users/anjandevara/Desktop/Epics_Stories.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)

    for line in csv_reader:
        print(line)