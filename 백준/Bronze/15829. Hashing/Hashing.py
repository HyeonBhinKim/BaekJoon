L = int(input())
s = input()

hash_value = 0

for i in range(L):
    hash_value += (ord(s[i]) - ord('a') + 1) * (31 ** i)

print(hash_value % 1234567891)
