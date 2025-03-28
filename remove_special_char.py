import re

def remove_special_characters(username):
    """ takes username as an argument, removes all special characters,
    	and returns the updated username.
    	Example: if the username is user&123_ @
    	         the function should return user123
    	"""
    return re.sub(r'[^a-zA-Z0-9]', '', username)