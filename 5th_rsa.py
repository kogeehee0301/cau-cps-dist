
p = 11
q = 13
n = p * q
phi_n = (p-1) * (q-1)

e = 7

d = 0
mod = 0
while True:
    d += 1
    mod = (e * d) % phi_n
    if mod == 1:
        break

print(d)

# Encryption
# C = P^e mod n

plain = "CAU CPS DIST"
plain_list = [ord(x) for x in plain]
# for x in plain:
#     plain_list.append(ord(x)) 와 같다

Cipher = []
for i in plain_list:
    x = (i ** e) % n
    Cipher.append(int(x))

print(Cipher)

# Decryption
# P = C^d mod n

decrypted = []
for i in Cipher:
    x = (i ** d) % n
    decrypted.append(int(x))

print('plain text', plain_list)
print('cipher text', Cipher)
print('decrypted text', decrypted)

print([chr(x) for x in decrypted])
decrypted_text = ''.join([chr(x) for x in decrypted])
print(decrypted_text)
