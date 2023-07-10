import csv

with open('bewertungen.csv') as csvdatei:
    csv_reader_object = csv.reader(csvdatei, delimiter=';')
    for row in csv_reader_object:
        for value in row:
            value = value.replace(",",".")


        print(row)
print(csv_reader_object)
      

