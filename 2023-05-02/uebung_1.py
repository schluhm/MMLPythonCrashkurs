# Dieses Programm entstand in der Übung und illustriert mehrere grundlegende Konzepte von Python
# sowie Programmierung allgemein.
# Es werden sogenannte built-in Funktionen von Python verwendet, wie print(), input(), range() und int().
# Variablen werden erstellt, gefüllt und ausgewertet (i und upper_limit).
# Die Prinzipien des Control Flow werden durch einen for loop und ein if statement angerissen.

print('Wie hoch soll ich nachschauen, ob die Zahlen durch 3 teilbar sind')

upper_limit = input()

for i in range(int(upper_limit)):
    if (i % 3) == 0:
        print(i)
