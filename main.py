import hashlib


def is_valid_password(password):
    if len(password) < 8:
        return False, print('Password must be at least 8 characters')

    if not any(char.isupper() for char in password):
        return False, print('Password must have at least one capital character')

    if not any(char.islower() for char in password):
        return False, print('Password must have at least one lower character')

    if not any(char.isdigit() for char in password):
        return False, print('Password must have at least one digit')

    return True, print('Password is valid')


def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()


if __name__ == '__main__':
    user_password = input('Enter your password: ')

    is_valid, message = is_valid_password(user_password)
    if is_valid:
        hashed_password = hash_password(user_password)
        print('Your password hash is: ', hashed_password)
    else:
        print('Your password does not satisfy the conditions')
