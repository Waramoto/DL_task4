import random as rand
from math import gcd


def is_prime(n):
    if n % 2 == 0:
        return n == 2
    d = 3
    while d * d <= n and n % d != 0:
        d += 2
    return d * d > n


def egcd(a, b):
    if a == 0:
        return b, 0, 1
    else:
        g, y, x = egcd(b % a, a)
        return g, x - (b // a) * y, y


def mod_inv(a, m):
    g, x, y = egcd(a, m)
    if g == 1:
        return x % m


def keys_gen(bits):
    p = rand.getrandbits(bits)
    while not is_prime(p) or p < 3:
        p = rand.getrandbits(bits)
    q = rand.getrandbits(bits)
    while not is_prime(q) or q < 3 or q == p:
        q = rand.getrandbits(bits)
    n = p * q
    f = (p - 1) * (q - 1)
    e = rand.randint(1, f)
    while gcd(e, f) != 1:
        e = rand.randint(1, f)
    d = mod_inv(e, f)
    return (e, n), (d, n)


def encrypt(public_key, m):
    e = public_key[0]
    n = public_key[1]
    if 0 < m < (n - 1) and gcd(m, n) == 1:
        c = (m ** e) % n
        return c
    else:
        return None


def decrypt(private_key, c):
    d = private_key[0]
    n = private_key[1]
    m = (c ** d) % n
    return m


message = 49
key_pair = keys_gen(8)
pub_key = key_pair[0]
print(f"Открытый ключ (e, n): {pub_key}")
priv_key = key_pair[1]
print(f"Закрытый ключ (d, n): {priv_key}")
encrypted_message = encrypt(pub_key, message)
print(f"Шифрование сообщения {message}: {encrypted_message}")
decrypted_message = decrypt(priv_key, encrypted_message)
print(f"Расшифрование сообщения {encrypted_message}: {decrypted_message}")
