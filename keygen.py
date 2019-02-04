import random
import string
import os

# generate a random UTF-8 key of defined length
def generate_key(length):
    # key consisting of letters and digits
    key_chars = string.ascii_letters + string.digits # concat letters and digits

    # choose a random choice from key_chars 'length' times
    return ''.join(random.choice(key_chars) for i in range(length))


# check if keys are present and generate them if not
def get_keys(pub_file, priv_file, length = 256):
    files = [pub_file, priv_file]
    keys = ['', '']
    
    for i in range(2): # avoid code duplication

        # Check for public key
        if os.path.isfile(files[i]):
            # key exists, load from file
            with open(files[i], 'r', encoding='utf8') as f:
                try:
                    keys[i] = f.read()
                    f.close()
                except Exception as e:
                    print(e)
        else:
            # key file does not exist, generate a key and safe to file
            keys[i] = generate_key(256)
            
            with open(files[i], 'w+', encoding='utf8') as f:
                try:
                    f.write(keys[i])
                    f.close()
                except Exception as e:
                    print(e)

    return keys
