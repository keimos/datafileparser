# This script parsess a CSV file and demonstrates listing index

from pathlib import Path
import pandas as pd

def read_properties(file_path):
    """Read properties from a given file  and returns them as a dictionary"""
    properties = {}
    try:
        with open(file_path, "r") as file:
            for line in file:
                key, value = line.strip().split("_", 1)
                properties[key.strip()] = value.strip()
    except FileNotFoundError:
        print("The specified CSV file could not found: {file_path}")
    return properties

def parse_csv(file_path):
    """Parses the CSV file at the given file path and prints its contents."""
    try:
        result = pd.read_csv(file_path, usecols=["Request"])
        print(result)
    except FileNotFoundError:
        print(f"CSV file not found: {file_path}")
    except ValueError as e:
        print(f"Error reading file: {e}")

if __name__ == "__main__":
    properties_file_path = Path("config.properties")
    properties = read_properties(properties_file_path)

    # get the CSV file path from the properties
    csv_file_path = properties.get("csv_file_path")
    if csv_file_path:
        parse_csv(csv_file_path)
    else:
        print("CSV file path not found in properties.")