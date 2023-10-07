# Generation file for challenge
from Crypto.Util.number import getPrime, bytes_to_long

p = 2
q = getPrime(512)
n = p * q
phi = (p - 1) * (q - 1)
e = 2**16 + 1
d = pow(e, -1, phi)
m = bytes_to_long("sigpwny{tw0_1s_th3_0dd35t_pr1m3_0f_th3m_4ll}".encode("utf-8"))
c = pow(m, e, n)

print(f"{n = }")
print(f"{e = }")
print(f"{c = }")
