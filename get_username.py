import re

def get_username():
    """Prompt user for username, remove special characters/spaces, and return the formatted username."""
    
    username_input = input("Enter your username: ")
    # Remove special characters and spaces
    username = re.sub(r'[^a-zA-Z0-9]', '', username_input)

    # Check if username is empty after removing special characters
    if not username:
        print("Username cannot be empty after removing special characters.")
        return get_username()
    # Check if username is too long
    if len(username) > 20:
        print("Username cannot be longer than 20 characters.")
        return get_username()
    # Check if username is too short
    if len(username) < 3:
        print("Username cannot be shorter than 3 characters.")
        return get_username()
    # Check if username contains only numbers
    if username.isdigit():
        print("Username cannot contain only numbers.")
        return get_username()
    # Check if username contains only letters
    if username.isalpha():
        print("Username cannot contain only letters.")
        return get_username()
    # Check if username contains only special characters
    if not re.search(r'[a-zA-Z0-9]', username):
        print("Username cannot contain only special characters.")
        return get_username()
    # Check if username contains spaces
    if ' ' in username:
        print("Username cannot contain spaces.")
        return get_username()
    # Check if username contains special characters
    if re.search(r'[^a-zA-Z0-9]', username):
        print("Username cannot contain special characters.")
        return get_username()

    print(f"Correctly formatted username: {username}")
    return username

if __name__ == "__main__":
    username = get_username()
    print(f"Your username is: {username}")