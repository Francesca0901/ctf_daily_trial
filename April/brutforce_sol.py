import secrets
from tqdm import tqdm

MOD = 251  # known prime

key = [secrets.randbelow(MOD) for _ in range(3)]

flag = b"EPFL{XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX}"
ans = [40, 238, 34, 149, 109, 191, 206, 216, 216, 206, 87, 214, 214, 20, 46, 4, 214, 189, 206, 17, 189, 228, 176, 20, 189, 100, 46, 80, 78, 4, 80, 228, 87, 191, 189, 4, 20, 214, 87, 78, 46, 206, 214, 87, 228, 119, 68]


def enc(data, key):
    return [sum(k * pow(2 * x, i, MOD) for i, k in enumerate(key)) % MOD for x in data]


# Custom exception to break out of multiple loops
class KeyFoundException(Exception):
    pass


try:
    for a in tqdm(range(251)):
        for b in range(0, 251):
            for c in range(0, 251):
                keys = [a, b, c]
                ansss = enc(flag, keys)
                if ansss[:5] == ans[:5]:
                    print(keys)
                    raise KeyFoundException()
except KeyFoundException:
    pass
