# This is a CSV file parser script

import pandas as pd

result = pd.read_csv('DeliveryReservationFailureFrom_05_27.csv', usecols=['Request'])

print(result)  # prints results of data read from CSV

a = [1, 2, 3]
try:
    print("Second element = %d" %(a[1]))

    print("Fourth element = %d" %(a[3]))

except IndexError:
    print("An error occurred in the array")

