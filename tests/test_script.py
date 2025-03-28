import pytest
from pathlib import Path
from src.main import read_properties, parse_csv

def test_read_properties_valid_file(tmp_path):
    # Create a temporary properties file
    properties_file = tmp_path / "config.properties"
    properties_file.write_text("csv_file_path=test.csv\n")

    # Test function
    result = read_properties(properties_file)
    assert result == {"csv_file_path": "test.csv"}
