# Given two integer numbers return their product only if the product is equal to or lower than 1000,
# else return their sum.
print("Nenne zwei Zahlen:")
number1 = int(input("Erste Zahl:"))
number2 = int(input())

result = 0
if (number1 * number2) > 1000:
    result = number1 + number2
else:
    result = number1 * number2
print(f"Hier das Ergebnis: {result}")
