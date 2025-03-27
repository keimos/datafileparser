# This script parsess a CSV file and demonstrates listing index

from pathlib import Path
import pandas as pd

# Read CSV and parse specific columns
csv_file = Path('DeliveryReservationFailureFrom_05_27.csv')
try:
    result = pd.read_csv(csv_file, usecols=['Request'])
    print(result)  # prints results of data read from CSV
except FileNotFoundError:
    print("The specified CSV file could not found: {csv_file}")
except ValueError:
    print("The specified CSV file is not valid")

element = [1, 2, 3]
try:
    print(f"Second element = {element[1]}") # Access the second element of the list
    print(f"Fourth element = {element[3]}") # Access the fourth element of the list

except IndexError as e:
    print(f"IndexError: {e}")