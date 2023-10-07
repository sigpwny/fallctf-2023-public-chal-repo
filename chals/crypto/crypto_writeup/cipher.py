message = "sigpwny"
shift = 4
ciphertext = ""
for c in message:           # loop through our message
    x = ord(c) - 97         # get ASCII and subtract 97
    x = (x + 4) % 26        # modular arithmetic!
    x += 97                 # Add 97
    ciphertext += chr(x)    # Convert back
print(ciphertext)           # Prints wmktarc
