import logging  ## logger is used for tracking all the events while executing the project.
import os
from datetime import datetime


LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"    ## files will be saved with .log naming convention
logs_path = os.path.join(os.getcwd(), "logs", LOG_FILE) ## folder name will be logs and inside log_files are saved with current working directory
os.makedirs(logs_path, exist_ok = True) ## creating folders ##exist_ok is basically even if their are previous logs in directory the new logs will be saved.

LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)
logging.info('The event has been recorded...!')