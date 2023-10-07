#!/usr/bin/env python3

from main import hash, numbers
import string

flag = ''
for i in range(len(numbers)):
    for c in string.printable:
        # don't need the recursive case; it only slows things down
        if hash(flag + c) == numbers[i]:
            flag += c
            break
print(''.join(flag))
