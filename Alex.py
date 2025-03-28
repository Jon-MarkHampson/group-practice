def display_email_address(email):
    """display the email - checks for string"""
    if isinstance(email, str) and "@" in email:
        print("=" * 30)
        print(f"📧 Email Address: {email}")
        print("=" * 30)
    else:
        print("⚠️ Invalid email address")