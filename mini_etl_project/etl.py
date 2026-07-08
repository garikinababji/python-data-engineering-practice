import json
import logging
from validator import is_active

logging.basicConfig(
    filename="logs/etl.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logging.info("ETL Pipeline Started")

with open("input/employees.json", "r") as file:
    employees = json.load(file)

print(employees)
