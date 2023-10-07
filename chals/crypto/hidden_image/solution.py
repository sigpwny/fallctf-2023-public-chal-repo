from itertools import cycle

XOR = lambda a,b: bytes([i^j for i,j in zip(a,cycle(b))])

cipher_file = open("cipher.bin", "rb").read()

# Note that we know the leading bytes of the PNG filetype, so we can figure out the key
png_header = bytes.fromhex("89504e470d0a1a0a")
key = XOR(cipher_file[:8], png_header)

# Use the key to get the original image
flag = XOR(cipher_file, key)

out_file = open("out.png", "wb")
out_file.write(flag)

