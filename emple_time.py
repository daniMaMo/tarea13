import threading
import time
import datetime
import csv

def f():
    print("¡Hola, mundo!")
# Ejecutar la función luego de 3 segundos.
t = threading.Timer(3, f)
t.start()
print("Esto se ejecuta antes que la función f().")


if 7 <= datetime.datetime.today().hour <= 16:
    while True:
        with open('exchange_rate.csv', mode='a') as csv_file:
            csv_writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            csv_writer.writerow(['John Smith', datetime.datetime.today().time()])
            #writer.writerow({'rate': 'lo estoy haciendo', 'date': datetime.datetime.today().time()})
        print('lo estoy haciendo', datetime.datetime.today().time())
        time.sleep(60)

#with open('employee_file.csv', mode='w') as employee_file:
#    employee_writer = csv.writer(employee_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

#    employee_writer.writerow(['John Smith', 'Accounting', 'November'])
