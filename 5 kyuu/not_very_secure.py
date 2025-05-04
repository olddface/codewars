def alphanumeric(password):
    if password == None or password == "":
        return False
    for i in password:
        if i == "" or i == " " or not i.isalpha():
            if not i.isdigit():
                return False
        elif i == None:
            return False
    return True