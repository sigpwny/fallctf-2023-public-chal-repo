# Generation file for challenge
from Crypto.Util.number import getPrime, bytes_to_long

p = _ # some prime...
q = _ # some prime...
n = p * q
phi = (p - 1) * (q - 1)
e = 2**16 + 1
d = pow(e, -1, phi)
#                   FIND THIS vvv
m = bytes_to_long("sigpwny{??????????}".encode("utf-8"))
c = pow(m, e, n)

# output saved in output.txt
print(f"{n = }")
print(f"{e = }")
print(f"{c = }")
