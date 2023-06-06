# Gemeinsam bearbeitete Aufgabe:
# Write a program to iterate the first 10 numbers and in each iteration,
# print the sum of the current and previous number.

previous_i = 0

for i in range(10): # Wir nutzen die built-in Funktion "range" um eine List von Zahlen von 0 bis 9 inkl. zu erzeugen.
    sum = i + previous_i    # Wir addieren die aktuelle und vorherige Zahl.
    print(f"Current Number {i} Previous Number  {previous_i}  Sum:  {sum}") # Wir schreiben die aktuelle und vorherige Zahl, sowie Summe in die Konsole.
    previous_i = i  # Wir setzen die vorherige Zahl erneut.
