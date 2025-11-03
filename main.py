commando = ""

print('PyDo v1.0')

def nieuwe_taak():
    file = open('tasks.txt', 'a')
    print('Geef je nieuwe taak in')
    toe_te_voegen_taak = input(" : ")
    file.write(toe_te_voegen_taak + "\n")
    file.close()

def taak_klaar():
    # Zoek door de code naar de taak
    # Verwijder de taak
    print("In progress")

def taken_legen():
    file = open("tasks.txt", "w")
    file.write("")
    file.close()

def nieuwe_taak():
    file = open('tasks.txt', 'a')
    print('Geef je nieuwe taak in')
    toe_te_voegen_taak = input(" : ")
    file.write(toe_te_voegen_taak + "\n")
    file.close()

def taak_klaar():
    # Zoek door de code naar de taak
    # Verwijder de taak
    print("In progress")

def taken_legen():
    file = open("tasks.txt", "w")
    file.write("")
    file.close()

while True :
    commando = input(" : ")
    if commando == "nw":
        nieuwe_taak()

    elif commando == "done":
        taak_klaar()

    elif commando == "exit":
        break

    elif commando == "clear":
        taken_legen()

    elif commando == "show":
        file = open("tasks.txt", "r")
        content = file.read()
        print(content)
        file.close()

    elif commando == "help":
        print("Beschikbare commando's:")
        print("  nw   - Nieuwe taak toevoegen")
        print("  done - Een taak markeren als afgerond")
        print("  help - Deze hulp informatie tonen")
        print("  exit - Dit programma afsluiten")
        print("  show - Je taken tonen")
        print("  clear - Je takenlijst leegmaken")

    else :
        print('Dit commando bestaat niet.')
        print("Typ help om een lijst met commando's te zien")



