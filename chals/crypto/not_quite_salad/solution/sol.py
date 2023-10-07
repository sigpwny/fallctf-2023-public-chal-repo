#!/usr/bin/env python3

c1 = 'hixo_ciu_gbo_otlicwts_dgppkfd'
c2 = 'tuevobq_gbo_muwfo_hgbz'
decode_this = 'qwsxytc{fvh_kgoqob_yiupz_hgjo_voot_yibqo}'

p1 = "hope_you_are_enjoying_fallctf"
p2 = "numbers_are_quite_hard"

# try all possible k1 and k2
for k1 in range(26):
    for k2 in range(26):

        c1_ = ""
        for c in p1:
            if 97 <= ord(c) <= 122:
                n = ord(c) - 97
                n = n * k1 + k2
                n = n % 26
                c1_ += chr(n + 97)
            else:
                c1_ += c

        c2_ = ""
        for c in p2:
            if 97 <= ord(c) <= 122:
                n = ord(c) - 97
                n = n * k1 + k2
                n = n % 26
                c2_ += chr(n + 97)
            else:
                c2_ += c

        # we've found the correct k1 and k2!
        if c1_ == c1 and c2_ == c2:
            k1_ = pow(k1, -1, 26)
            k2_ = 26 - k2

            flag = ""
            for c in decode_this:
                if 97 <= ord(c) <= 122:
                    n = ord(c) - 97
                    n = (n + k2_) % 26
                    n = (n * k1_) % 26
                    flag += chr(n + 97)
                else:
                    flag += c

            print(f"{flag = }")
