# This is a CSV file parser script

import pandas as pd

result = pd.read_csv('DeliveryReservationFailureFrom_05_27.csv', usecols=['Request'])

print(result)
