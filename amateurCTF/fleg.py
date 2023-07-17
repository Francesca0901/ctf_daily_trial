ori = 0x610c6115651072014317463d73127613732c73036102653a6217742b701c61086e1a651d742b69075f2f6c0d69075f2c690e681c5f673604650364023944


# When doing xor with 00000400:
# aLaUePrACWF}sRvSslsCaBezbWtkp\aHnZe]tkiG_olMiG_liNh\_'6DeCdB9

# original
# 610c6115651072014317463d
# amateursCTF{
# 616d6174657572734354467b


original_hex = '610c6115651072014317463d'
encoded_hex = '616d6174657572734354467b'

original = bytes.fromhex(original_hex)
encoded = bytes.fromhex(encoded_hex)

key = []

for i in range(len(original)):
    key.append(original[i] ^ encoded[i])

print("Key: ", key)

# Key:  [0,    97 a, 0,     97 a, 0,     101 e, 0,     114 r, 0,     67 C, 0,     70 F]
#            1100001   1100001     1100101     1110010    1000011    1000110


original_hex = '610c6115651072014317463d73127613732c73036102653a6217742b701c61086e1a651d742b69075f2f6c0d69075f2c690e681c5f673604650364023944'
encoded_hex = '614C6155655072414357467D'

original = bytes.fromhex(original_hex)

res = []

for i in range(len(original)):
    if i % 2 == 1: # apply XOR to every second character starting from the first
        res.append(chr(original[i] ^ original[i - 1]))
    else:
        res.append(chr(original[i]))

print("Key: ", ''.join(res))


