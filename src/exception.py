import sys


def error_message_detail(error_message, error_detail):
    # Extract the exception type, value, and traceback
    exc_type, exc_value, exc_tb = error_detail

    # Get the file name where the exception occurred
    file_name = exc_tb.tb_frame.f_code.co_filename

    # Get the line number where the exception occurred
    line_number = exc_tb.tb_lineno

    # Create the error message with file name, line number, and the provided error message
    error_message = f"Error: {file_name} occurred in line number: {line_number} with error message: {error_message}"

    return error_message


class CustomException(Exception):
    def __init__(self, error_message, error_detail):
        # Call the error_message_detail function to format the error message
        self.error_message = error_message_detail(error_message, error_detail)

        # Call the parent class's __init__ method to initialize the exception
        super().__init__(self.error_message)

    def __str__(self):
        # Return the formatted error message when the exception is converted to a string
        return self.error_message
