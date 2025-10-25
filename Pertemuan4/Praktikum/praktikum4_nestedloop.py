''''
a = 5
s =a - 1
for i in range(0, a):
    for j in range(0,s):
        print(' ', end='')

    s -= 1
    for j in range(0, i + 1):
        print('* ', end='')
    print('')

print("Segitiga Biasa")
'''

print("Segitiga Terbalik")
a = 5
s = a - 1
for i in range(a):
    for j in range(i):
        print(' ', end='')
    s -= 5
    for j in range(a - i):
        print('* ', end='')
    print('')
        
