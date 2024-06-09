import logging
import os
from datetime import datetime

# Create a directory called "logs" in the current working directory
logs_dir = os.path.join(os.getcwd(), "logs")
os.makedirs(logs_dir, exist_ok=True)

# Generate a log file path with the current date in the format "YYYY-MM-DD"
log_file_path = os.path.join(
    logs_dir, f"{datetime.now().strftime('%Y-%m-%d')}.log")

# Configure the logging module to write logs to the specified file
logging.basicConfig(
    filename=log_file_path,
    level=logging.INFO,
    format="%(asctime)s - %(lineno)d - %(name)s - %(levelname)s - %(message)s",
)
