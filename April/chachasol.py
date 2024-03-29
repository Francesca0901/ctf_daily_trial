import secrets
from Crypto.Cipher import ChaCha20_Poly1305

a = "939acb56cdda59984ccf6a494629324df8c76c2727640a32e0ad201b5fb11229388dd533932d607e0e2af1d598984405609a37257984e589e4"
b = "9aa5ff7fdbcb76b7668a523670750b17cfb851011d072e6ada9a400f6c81256a08bcfe6ea616560d1264826b142fb7d9f94c91b03dec59018b7566ab87f29c197d8cbf6ac778f969ade894f9295b6f005ada68e3fe2ce6d106d680bb5b5947e82d87c4670c6ac1952c73b2bd3bba0ca24caf6d58fea8b318ceea7422b5148f650e22d9d768dd390c1dd357"
output1 = bytes.fromhex(a)
output2 = bytes.fromhex(b)
message2 = b"Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."
message1 = b"EPFL{XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX}"

# Create a new byte array of the same length as the input message1
result = bytearray(len(message1))

# XOR the corresponding bytes from the three byte arrays
for i in range(len(message1)):
    result[i] = output1[i] ^ output2[i] ^ message2[i]

# Print the result as a string
print(result.decode())
