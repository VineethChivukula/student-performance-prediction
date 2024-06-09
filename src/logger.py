import logging
import os
from datetime import datetime

logs_dir = os.path.join(os.getcwd(), "logs")
os.makedirs(logs_dir, exist_ok=True)

log_file_path = os.path.join(
    logs_dir, f"{datetime.now().strftime('%Y-%m-%d')}.log")

logging.basicConfig(
    filename=log_file_path,
    level=logging.INFO,
    format="%(asctime)s - %(lineno)d - %(name)s - %(levelname)s - %(message)s",
)
