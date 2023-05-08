# Zu verwenden: python uebung_2.py
# Modifiziere das Skript so, dass beliebig viele Zahlen addiert werden können.

def check_input_number(input_str):
    try:
        input_num = int(input_str)
        return True
    except ValueError:
        return False


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("Gib mir Zahlen!")
    sum = 0
    while True:
        addition = input()
        if not check_input_number(addition):
            break
        sum += int(addition)
    print("Dein Ergebnis ist " + str(sum))
