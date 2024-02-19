scale = list(map(str, input().split()))
scale = ''.join(map(str, scale))

if scale == '12345678':
    print('ascending')
elif scale == '87654321':
    print('descending')
else:
    print('mixed')

