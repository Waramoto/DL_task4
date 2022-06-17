

def KSA(key):
    s = []
    for i in range(0, 256):
        s.append(i)
    j = 0
    for i in range(0, 256):
        j = (j + s[i] + key[i % len(key)]) % 256
        s[i], s[j] = s[j], s[i]
    return s


def PRGA(s):
    i = j = 0
    while True:
        i = (i + 1) % 256
        j = (j + s[i]) % 256
        s[i], s[j] = s[j], s[i]
        t = (s[i] + s[j]) % 256
        k = s[t]
        yield k


def keystream_gen(key):
    s = KSA(key)
    return PRGA(s)


def encrypt(key, plaintext):
    key = bytearray.fromhex(key).decode()
    key = [ord(c) for c in key]
    keystream = keystream_gen(key)
    res = ''
    for c in plaintext:
        res += '%02X' % (ord(c) ^ next(keystream))
    return res


def decrypt(key, ciphertext):
    ciphertext = bytearray.fromhex(ciphertext).decode('ISO-8859-1').encode('utf-8').decode('utf-8')
    res = encrypt(key, ciphertext)
    res = bytearray.fromhex(res).decode()
    return res


keyword = '4B6579'
print(f'Ключ: "{keyword}"')
text = 'The quick brown fox jumps over the lazy dog'
print(f'Текст: "{text}"')
encrypted_text = encrypt(keyword, text)
print(f'Зашифрованный текст: "{encrypted_text}"')
decrypted_text = decrypt(keyword, encrypted_text)
print(f'Расшифрованный текст: "{decrypted_text}"')
