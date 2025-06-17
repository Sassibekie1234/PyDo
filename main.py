'''
Hallo en welkom bij CliDo: de FOSS CLI to-do app geschreven in Python 3

Om te beginnen wil ik vermelden dat dit mijn eerste project is met een tekstgebaseerde programeertaal.
Dit is mijn eerste keer en ik heb geen idee wat ik doe.
Als je een idee hebt voor mijn volgende projecten hoor ik ze graag.

Ik hoop met deze code andere beginners te kunnen motiveren en op weg te helpen.

Deze code is vrij te gebruiken en te kopieren. Ik zou het wel fijn vinden als je de verwijzing naar mijn github laat staan.

Voor meer info: raadpleeg de readme.md
'''

def nieuwe_taak():
    file = open('tasks.txt', 'a')
    print('Geef je nieuwe taak in')
    toe_te_voegen_taak = input(" : ")
    file.write(toe_te_voegen_taak + "\n")
    file.close()

def taak_klaar():
    print("Nog steeds niet afgewerkt")

def taken_legen():
    file = open("tasks.txt", "w")
    file.write("")
    file.close()


commando = ""

print('PyDo v1.0')

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