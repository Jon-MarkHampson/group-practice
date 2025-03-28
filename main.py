from Alex import display_email_address
from jon_mark import get_username
from melody import add_at_symbol_to_username, add_domain_to_username
from amulya import remove_special_characters

def main():
    username = get_username()
    print(f"Your username is: {username}")
    username_and_at = add_at_symbol_to_username(username)
    print(f"Username with '@' added: {username_and_at}")
    full_email = add_domain_to_username(username_and_at)
    print(f"Full email address: {full_email}")
    email_with_speical_characters_renmoved = remove_special_characters(full_email)
    print(f"Email address with special characters removed: {email_with_speical_characters_renmoved}")
    
if __name__ == "__main__":
    main()