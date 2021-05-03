import csv
reader = csv.reader(open("2021-04-25_dht22_sensor_3660.csv"), delimiter=";")
for row in reader:
   print('Zeit: {row[5]} Temperatur: {row[6]} Grad°')