import base64
import codecs
import gmpy
import math
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5

n = 98099407767975360290660227117126057014537157468191654426411230468489043009977
p = 311155972145869391293781528370734636009 # from YAFU
q = 315274063651866931016337573625089033553
e = 12405943493775545863


def long_to_bytes(flag):
    return "".join([chr(int(flag[i:i + 2], 16)) for i in range(0, len(flag), 2)])


def bytes_to_long(str):
    return int(str.encode('hex'), 16)


flag = open("./flag.enc", 'r')
data = flag.read()
msg = base64.b64decode(data)
print('msg', math.log(bytes_to_long(msg), 2))
while True:
	print("looping")
        try:
            print('p*q', math.log(long(p), 2)+math.log(long(q), 2))
            phi = (p - 1) * (q - 1)
            d = gmpy.invert(e, phi)
            key = RSA.construct((long(n), long(e), long(d)))
            key = PKCS1_v1_5.new(key)
            decrypted = key.decrypt(msg, 0x64)
            print(decrypted)
            print(p, q, e)
            print(long_to_bytes(decrypted))
        except Exception as ex:
            print(ex)
            p = gmpy.next_prime(p ** 2 + q ** 2)
            q = gmpy.next_prime(2 * p * q)
            e = gmpy.next_prime(e ** 2)
