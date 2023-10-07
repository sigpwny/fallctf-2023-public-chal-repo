p1   = _ # Original Plaintext now saved in p1
key  = _ # Hidden key that you need to find

c1 = bytes(x ^ y for x, y in zip(key, p1))

with open("p1", "wb") as p1_file:
    p1_file.write(p1)
with open("c1", "wb") as c1_file:
    c1_file.write(c1)

flag = _ # FIND THIS!
c2 = bytes(x ^ y for x, y in zip(key, flag))
with open("c2", "wb") as c2_file:
    c2_file.write(c2)
