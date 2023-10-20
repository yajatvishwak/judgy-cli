import logging

file_logger = logging.getLogger("file_logger")
file_logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler("output.log")
file_handler.setLevel(logging.DEBUG)
formatter = logging.Formatter("%(asctime)s - [%(levelname)s] - %(message)s")
file_handler.setFormatter(formatter)
file_handler.setFormatter(formatter)
file_logger.addHandler(file_handler)
console_logger = logging.getLogger("console_logger")
console_logger.setLevel(logging.INFO)
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)
console_formatter = logging.Formatter("%(levelname)s - %(message)s")
console_handler.setFormatter(console_formatter)
console_logger.addHandler(console_handler)

# Example usage
# file_logger.debug('This will be logged to the file')
# file_logger.info('This will be logged to the file')
# file_logger.warning('This will be logged to the file')
# file_logger.error('This will be logged to the file')

# console_logger.info('This will be logged to the console')
# console_logger.warning('This will be logged to the console')
# console_logger.error('This will be logged to the console')
