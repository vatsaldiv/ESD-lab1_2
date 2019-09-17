
import csv
import os
import urllib.request
from datetime import date,time,datetime
import serial


today = date.today()
now = datetime.now()

current_date = today.strftime("%d/%m/%Y")
current_time = now.strftime("%H:%M:%S")
current_datetime = current_date + "_" + current_time

def updateDB(last_count, last_temp, last_light, current_datetime):
    row = [last_count, last_temp, last_light, current_datetime]
    csv.register_dialect('myDialect', lineterminator = '\n')
    exists = os.path.isfile('data.csv')

    if not exists:
        row_top = ['count', 'last_temp', 'last_light', 'last_datetime']
        with open('data.csv', 'w') as csvFile:
            writer = csv.writer(csvFile, dialect='myDialect')
            writer.writerow(row_top)
        csvFile.close()

    with open('data.csv', 'a') as csvFile:
        writer = csv.writer(csvFile, dialect='myDialect')
        writer.writerow(row)
    csvFile.close()

    url = "https://us-central1-esd-lab1.cloudfunctions.net/setData?count="+str(last_count)+"&data1="+str(last_temp)+"&data2="+str(last_light)+"&data3="+str(current_datetime)

    with urllib.request.urlopen(url) as response:
        response_text = response.read()
        print(response_text.decode("utf-8"))

def findAvg():
    avg_temp = 0.0
    avg_light = 0.0
    current_date = today.strftime("%d/%m/%Y")
    exists = os.path.isfile('data.csv')
    if not exists:
        return 0.0, 0.0
    with open('data.csv', 'r') as csvFile:
        reader = csv.reader(csvFile)
        count = 0
        for row in reader:
            data_date = row[3][:10]
            if data_date == current_date:
                avg_temp = avg_temp*count + float(row[1])
                avg_light = avg_light*count + float(row[2])
                count += 1
                avg_temp /= count
                avg_light /= count
    csvFile.close()
    avg_temp = round(avg_temp, 8)
    avg_light = round(avg_light, 8)
    return avg_temp, avg_light

def findAvg_hrs(hour):
    avg_temp_hrs = 0.0
    avg_light_hrs = 0.0
    current_date = today.strftime("%d/%m/%Y")
    exists = os.path.isfile('data.csv')
    if not exists:
        return 0.0, 0.0
    with open('data.csv', 'r') as csvFile:
        reader = csv.reader(csvFile)
        count = 0
        for row in reader:
            data_date = row[3][:10]
            data_hour = row[3][11:13]
            if data_date == current_date and data_hour == hour:
                avg_temp_hrs = avg_temp_hrs*count + float(row[1])
                avg_light_hrs = avg_light_hrs*count + float(row[2])
                count += 1
                avg_temp_hrs /= count
                avg_light_hrs /= count
    csvFile.close()
    avg_temp_hrs = round(avg_temp_hrs, 8)
    avg_light_hrs = round(avg_light_hrs, 8)
    return avg_temp_hrs, avg_light_hrs

def getLastData():
    current_date = today.strftime("%d/%m/%Y")
    exists = os.path.isfile('data.csv')
    data = 0.0, 0.0
    if not exists:
        return 0.0, 0.0

    with open('data.csv', 'r') as csvFile:
        reader = csv.reader(csvFile)
        for row in reader:
            data_date = row[3][:10]
            if data_date == current_date:
                data = float(row[1]), float(row[2])

    csvFile.close()
    return data
