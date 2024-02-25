import math

a, b = map(int, input().split())

gcd = math.gcd(a, b)  # 최대공약수
lcm = a * b // gcd  # 최소공배수

print(gcd)
print(lcm)
