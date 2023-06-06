# Dieses Skript ermöglicht das Addieren von unbeschränkt vielen Zahlen.
# Wir arbeiten hier mit 2 unterschiedlichen Methoden / Funktionen.

# In check_input_number lernen wir den sogenannten try catch Block kennen.
# In diesem Block wird das was in "try" steht ausgeführt.
# Falls ein in "except" aufgeführter Fehler auftritt, wird stattdessen
# der dort spezifizierte Code ausgeführt.
# Dadurch kann mit normalerweise kritischen Fehlern gearbeitet werden.

def check_input_number(input_str):
    try:
        input_num = int(input_str)
        return True
    except ValueError:
        return False

# Die folgende Methode wird bei einem Pythonprogramm normalerweise ausgeführt, wenn man es startet.
# Alle Methoden, die ansonsten aufgeführt werden, werden nur deklariert. Ihr Code wird erst ausgeführt,
# sobald sie aufgerufen werden, wie check_input_number im Folgenden.


if __name__ == '__main__':
    print("Gib mir Zahlen!")
    sum = 0 # Mit sum ist die Summe gemeint. Variablennamen auf Englisch sind sinnvoll, um Sonderzeichen zu vermeiden.
    while True: # Eine while True Schleife läuft so lange, bis break aufgerufen wird.
        addition = input()
        if not check_input_number(addition):
            break
        sum += int(addition)
    print("Dein Ergebnis ist " + str(sum))
