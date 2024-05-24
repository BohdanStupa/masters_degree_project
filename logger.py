import logging
from datetime import datetime


def configure_logger(log_filename: str, log_level=logging.INFO):
    # Create a file handler
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    log_file = f"{log_filename}_{timestamp}.log"
    file_handler = logging.FileHandler(log_file)
    file_handler.setLevel(log_level)

    # Create a formatter and set it for the file handler
    formatter = logging.Formatter('%(message)s')
    file_handler.setFormatter(formatter)

    # Add the file handler to the root logger
    root_logger = logging.getLogger()
    root_logger.setLevel(log_level)
    root_logger.addHandler(file_handler)

def get_custom_logger(logger_name: str, log_filename: str, log_level=logging.INFO):
    # Configure logger
    configure_logger(log_filename, log_level)

    # Return the custom logger
    return logging.getLogger(logger_name)
    