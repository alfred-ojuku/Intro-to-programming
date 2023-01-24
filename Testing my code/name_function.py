def get_formatted_name(first, last, middle=''):
    """Generates a fully formatted name"""
    if middle:
        fullname = f"{first} {middle} {last}"
    else:
        fullname = f"{first} {last}"
    return fullname.title()