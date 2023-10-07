# script used to generate output.txt

p1 = "hope_you_are_enjoying_fallctf"
p2 = "numbers_are_quite_hard"
flag = "sigpwny{tbh_caeser_would_have_been_worse}"

k1 = 15 # what could be here?
k2 = 6  # what could be here?

# remember, lowercase letters have ascii values between 97 and 122
c1 = ""
for c in p1:
    if 97 <= ord(c) <= 122:
        n = ord(c) - 97
        n = n * k1 + k2
        n = n % 26
        c1 += chr(n + 97)
    else:
        c1 += c
print(f"{c1 = }")

c2 = ""
for c in p2:
    if 97 <= ord(c) <= 122:
        n = ord(c) - 97
        n = n * k1 + k2
        n = n % 26
        c2 += chr(n + 97)
    else:
        c2 += c
print(f"{c2 = }")

decode_this = ""
for c in flag:
    if 97 <= ord(c) <= 122:
        n = ord(c) - 97
        n = n * k1 + k2
        n = n % 26
        decode_this += chr(n + 97)
    else:
        decode_this += c
print(f"{decode_this = }")
