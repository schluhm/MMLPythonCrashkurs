# Boolsche Werte
# and
# or
# not

value = True
print(value)
value = False
print(value)

value = True and False and True and True
print(value)

value = True or False
print(value)

value = not True
print(value)

value = not True and not (False or not False)
print(value)

x = 0
y = 1
z = 2

# value = 1 <= 2 < 3 == 4 > 5 >= 6 != 7
# value = x <= y and y <= z
# print(value)

if x > y:
    print(x)
elif x > z:
    print(z)
else:
    print(y)

i = 0
while i < 100:
    i += 1
    if i / 13 == 2:
        continue
    print(i)

for j in range(100):
    print(j)

for k in range(0, 100, 1):
    print(k)

