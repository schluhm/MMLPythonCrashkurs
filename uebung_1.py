print('Wie hoch soll ich nachschauen, ob die Zahlen durch 3 teilbar sind')
upper_limit = input()

for i in range(int(upper_limit)):
    if (i % 3) == 0:
        print(i)