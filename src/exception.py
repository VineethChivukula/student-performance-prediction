import sys

def error_message_detail(error_message, error_detail):
	exc_type, exc_value, exc_tb = error_detail
	file_name = exc_tb.tb_frame.f_code.co_filename
	line_number = exc_tb.tb_lineno
	error_message = f"Error: {file_name} occurred in line number: {line_number} with error message: {error_message}"
	return error_message


class CustomException(Exception):
	def __init__(self, error_message, error_detail):
		self.error_message = error_message_detail(error_message, error_detail)
		super().__init__(self.error_message)

	def __str__(self):
		return self.error_message
