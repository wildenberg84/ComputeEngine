import random
import string

# generate a random UTF-8 key of defined length
def generate_key(length):
    # key consisting of letters and digits
    key_chars = string.ascii_letters + string.digits # concat letters and digits

    # choose a random choice from key_chars 'length' times
    return ''.join(random.choice(key_chars) for i in range(length))
