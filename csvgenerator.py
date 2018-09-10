import csv
import random
from faker import Faker


l = Faker('en_GB')
f = open("10M_rows.csv", "a")
w = csv.writer(f)
w.writerow(('id', 'marks'))

for i in range(20000000):
    w.writerow((i+1, random.randint(1, 100)))
f.close()

