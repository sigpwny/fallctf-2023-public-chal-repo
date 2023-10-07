flag = list(b"sigpwny{mis5i0n_acc0mpl1sh3d}")
print(flag)

for i in range(28, -1, -1): flag[(i*2)%29], flag[i] = flag[i], flag[(i*2)%29]

# print(flag)

for i in range(29):
    a = i*2+2304
    a = a ^ (a >> 4)
    a = a ^ ((i << 7) & (2**32-1))
    a = a ^ (a >> 11)
    b = a
    while b != 0:
            a += (a >> 3)
            b >>= 1
    flag[i] = ((flag[i] ^ a) & 0x7f) << 1

print(flag)

for i in range(29):
    a = i*2+2304
    a = a ^ (a >> 4)
    a = a ^ ((i << 7) & (2**32-1))
    a = a ^ (a >> 11)
    b = a
    while b != 0:
        a += (a >> 3)
        b >>= 1
    flag[i] = ((flag[i] >> 1) ^ a) & 0x7f

# print(flag)

for i in range(29):
    flag[(i*2)%29], flag[i] = flag[i], flag[(i*2)%29]

print(flag)
