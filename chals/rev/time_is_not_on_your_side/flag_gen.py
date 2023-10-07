#!/usr/bin/env python3

import hashlib

def hash(b):
    v = hashlib.sha256(str(b).encode()).hexdigest()
    v = int(v, 16)
    return v

def gen_flag(flag):
    all = []
    for i in range(len(flag)):
        all.append(hash(flag[:i+1]))
    return all

def main():
    flag = 'sigpwny{c4Nt_UnD0_a_H4sH}'
    print(gen_flag(flag))

if __name__ == '__main__':
    main()
