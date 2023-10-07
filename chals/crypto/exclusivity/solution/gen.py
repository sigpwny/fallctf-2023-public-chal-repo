# File to generate challenge

p1   = b"testing_testing_123_123_is_this_even_on_hello_hello_hello?"
key  = b"whoa_this_should_have_been_kept_a_secret_who_told_you?"
c1 = bytes(x ^ y for x, y in zip(key, p1))

with open("p1", "wb") as p1_file:
    p1_file.write(p1)
with open("c1", "wb") as c1_file:
    c1_file.write(c1)

flag = b"sigpwny{mfw_0ne_t1m3_p4d_wa5n't_0ne_t1me}"
c2 = bytes(x ^ y for x, y in zip(key, flag))
with open("c2", "wb") as c2_file:
    c2_file.write(c2)
