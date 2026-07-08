

import logging

logging.basicConfig(
    filename="logs/etl.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

print("Program Started")

logging.info("ETL Pipeline Started")

print("Log Written Successfully")
