import os
import logging

def setupLogfile (log_file_name,log_file_folder):
    log_path = os.path.join(log_file_folder, 'log')
    from datetime import date
    today = date.today()
    filename = log_file_name+".log"
    filename = os.path.join(log_path, filename)
    logging.basicConfig(filename=filename, format='%(asctime)s - %(levelname)s - %(message)s', level=logging.INFO, datefmt='%Y-%m-%d %H:%M:%S')
    logger = logging.getLogger(__name__)
    return logger
