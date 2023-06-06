# Gemeinsam bearbeitete Aufgabe:
# Given two integer numbers return their product only if the product is equal to or lower than 1000,
# else return their sum.


print("Nenne zwei Zahlen:") # Wir nehmen 2 ganze Zahlen entgegen.
number1 = int(input("Erste Zahl:"))
number2 = int(input("Zweite Zahl:"))

result = 0
if (number1 * number2) > 1000:  # Wir prüfen, ob das Produkt aus den Zahlen größer ist als 1000
    result = number1 + number2  # Falls ja, geben wir ihre Summe als Ergebnis zurück
else:                           # Sonst
    result = number1 * number2  # Geben wir das Produkt als Ergebnis zurück
print(f"Hier das Ergebnis: {result}")   # In jedem Fall, schreiben wir das Ergebnis in die Konsole.
