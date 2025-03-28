def add_at_symbol_to_username(username):
    """
    Takes a username as an argument, adds the @ symbol to
    the username, and returns the updated username.

    Example: if the username is "user123"
    the function should return "user123@".
    """
    if not username.endswith("@"):
        return username + "@"
    return username


def add_domain_to_username(username):
    """
    Takes a username as an argument and adds a domain name
    to the username and returns the email.

    Example: if the username is "user123@"
    the function should return "user123@email.com".
    """
    if "@" in username and not username.endswith("@email.com"):
        return username + "email.com"
    return username


def display_email_address(email):
    """
    Displays the email address.

    Example:
    display_email_address("user123@email.com")
    Output: Email Address: user123@email.com
    """
    print(f"Email Address: {email}")
