import string
import random

def get_code():
	code = ''.join(random.choices(string.ascii_uppercase + string.digits, k=4))
	return code

if __name__ == '__main__':
	print(get_code())
	print(get_code())