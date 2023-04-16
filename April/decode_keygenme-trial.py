import hashlib
from cryptography.fernet import Fernet
import base64

# key_base64 = base64.b64encode(key_str.encode())
# f = Fernet(key_base64)

key_part_static1_trial = "picoCTF{1n_7h3_|<3y_of_"
key_part_dynamic1_trial = "01582419"
key_part_static2_trial = "}"
key_full_template_trial = key_part_static1_trial + key_part_dynamic1_trial + key_part_static2_trial

username_trial = "ANDERSON"
bUsername_trial = b"ANDERSON"


def check_key(username_trial):
        key = {}

        i = 0

        key[i] = hashlib.sha256(username_trial).hexdigest()[4]
        i += 1

        key[i] = hashlib.sha256(username_trial).hexdigest()[5]
        i += 1

        key[i] = hashlib.sha256(username_trial).hexdigest()[3]
        i += 1

        key[i] = hashlib.sha256(username_trial).hexdigest()[6]
        i += 1

        key[i] = hashlib.sha256(username_trial).hexdigest()[2]
        i += 1

        key[i] = hashlib.sha256(username_trial).hexdigest()[7]
        i += 1

        key[i] = hashlib.sha256(username_trial).hexdigest()[1]
        i += 1

        key[i] = hashlib.sha256(username_trial).hexdigest()[8]

        print(''.join(key))

check_key(bUsername_trial)