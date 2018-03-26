import bme280
import time
import csv

with open('result.csv', 'w') as csvfile:
    field = ['timestamp', 'temperature', 'pressure']
    writer = csv.DictWriter(csvfile, fieldnames=field)
    writer.writeheader()
    while True:
        temperature, pressure, humidity = bme280.readBME280All()
        print(temperature)
        print(pressure)
        print(humidity)
        writer.writerow({'timestamp': int(time.time()), 'temperature': temperature, 'pressure' : pressure})
        time.sleep(5)
