import random
import string


def get_secret_key(length):
    """ This function used for generate rendom secret key """
    letters = string.ascii_letters
    return 'TR-'.join(random.choice(letters) for i in range(length))
