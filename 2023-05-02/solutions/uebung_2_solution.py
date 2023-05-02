# LÖSUNG zu:
# Modifiziere das Skript so, dass beliebig viele Zahlen addiert werden können.

# In diesem Skript werden weitere Grundkonzepte der Programmierung (mit Python) dargestellt.
# Die Main Methode, die ausgeführt wird, wenn eine Datei ausgeführt wird, wird genutzt.
# Eine zusätzliche Methode zeigt, wie man Spaghetti-Code verhindert und kleine Funktionalität auslagert.
# Der while loop zeigt zum ersten Mal eine möglicherweise endlose Schleife im Control Flow.
# Datentypen boolean, sowie None werden eingeführt.
# Eine erste Exception wird gefangen und verarbeitet.

# Funktion um zu prüfen, ob user_input zu einer ganzen Zahl umgewandelt werden kann.
def check_user_input(user_input):
    try:
        # Konvertierung zu int
        val = int(user_input)
        # Ist wandelbar, daher wird wahr zurückgegeben.
        return True
    except ValueError:
        # Bei Exception ist es nicht wandelbar, daher wird unwahr zurückgegeben.
        return False


if __name__ == '__main__':
    print("Gib mir so viele Zahlen zum Addieren, wie du magst!")
    print("Sobald was anderes als eine Zahl eingegeben wird, rechne ich aus.")
    number1 = None
    while True:
        number2 = input()
        if not check_user_input(number2):
            break
        if number1 is None:
            number1 = 0
        number1 = number1 + int(number2)

    print("Das Ergebnis ist " + str(number1))
    print("Beep Boop - Programm ist erfolgreich vorbei.")
