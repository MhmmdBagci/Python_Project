"""
Projekt: Webserver mit Automatisierung, Backup & Rechteverwaltung

Sachverhalt:
Sie haben kürzlich Ihre Weiterbildung abgeschlossen und arbeiten nun bei der IT-Kaktus Consulting GmbH. 
Ihr erster Auftrag ist es, eine einfache Python-Anwendung zu entwickeln, die eine To-Do-Liste verwaltet. 
Diese Anwendung soll über das Terminal bedient werden und es dem Benutzer ermöglichen, Aufgaben zu einer Liste hinzuzufügen, 
anzuzeigen, als erledigt zu markieren und zu löschen. Alle Aufgaben sollen in einer Datei gespeichert werden, 
damit sie auch nach dem Schließen der Anwendung weiterhin verfügbar sind.

Ihre Aufgabe ist es:
Entwickeln Sie eine Python-Anwendung, die alle oben genannten Funktionen implementiert. Die Anwendung soll über das Terminal gesteuert werden, 
und alle Aufgaben sollen in einer Textdatei gespeichert werden. Sie müssen sicherstellen, dass die Aufgaben in der Datei korrekt gespeichert werden 
und dass der Benutzer die Aufgaben auf einfache Weise verwalten kann.
"""


import os  # Ermöglicht das Arbeiten mit Dateien und Ordnern

# Dateiname für die To-Do-Liste
path = os.path.join("./PYTHON_PRJEKT/todolist.txt") # erstellung eines pfads für die Datei
datei_name = "todo_list.txt"  # variabel für meine liste

"""Fügt eine neue Aufgabe zur Datei hinzu."""
def add_task():
    datei = open(datei_name, "a")  # Datei öffnen, um neue Aufgaben hinzuzufügen, a steht für append also wenn die datei nicht existiert wird sie erstellt
    aufgabe = input("Gib die Aufgabe ein: ")  # Nutzer wird aufgefordert und gibt eine neue Aufgabe ein
    datei.write(aufgabe + "\n")  # Aufgabe in Datei speichern \n steht für neue zeile
    datei.close()  # Datei schließen
    print("Aufgabe hinzugefügt.")

"""Zeigt alle Aufgaben an."""
def show_tasks():
    datei = open(datei_name, "r")  # Datei öffnen, um Aufgaben zu lesen
    liste = datei.readlines()  # Alle Zeilen aus der Datei holen
    datei.close()  # Datei schließen
    
    if len(liste) != 0:  # Falls es Aufgaben gibt
        for index, aufgabe in enumerate(liste, 1):  # Aufgaben nummerieren mit enumerate
            print(f"{index}. {aufgabe.strip()}")  # Aufgaben anzeigen
    else:
        print("Keine Aufgaben vorhanden.")

"""Markiert eine Aufgabe als erledigt."""
def mark_task_done():
    try:
        datei = open(datei_name, "r") # Datei öffnen, um Aufgaben zu lesen
        aufgaben = datei.readlines() # Alle Zeilen aus der Datei holen
    finally:
        datei.close() # Datei schließen
    
    if len(aufgaben) == 0:
        print("Keine Aufgaben vorhanden.")
        return

    show_tasks()
    try:
            nummer = int(input("Welche Aufgabe wurde erledigt? "))  # Nutzer gibt Nummer ein input nimmt es als  string und mit int wandelt er es in eine ganze zahl um bzw integer
    except:
        print("Bitte eine gültige Zahl eingeben")
        return
        
    if not 1 <= nummer <= len(aufgaben ): #
        print("Ungültige Nummer.")
        return
    if aufgaben[nummer - 1].startswith("X "): # wenn es schon markiert ist mit x
        print("Diese Aufgabe ist schon erledigt.")
        return
    aufgaben[nummer - 1] = "X " + aufgaben[nummer - 1]  # "X " hinzufügen
    try:
        datei = open(datei_name, "w") # öffnet die datein um darin rein zu schreiben
        datei.writelines(aufgaben)  # Datei mit neuen Daten überschreiben
    finally:
        datei.close()
    print("Aufgabe erledigt.")

"""Löscht eine Aufgabe."""
def delete_task():
    try:
        datei = open(datei_name, "r") # Datei öffnen, um Aufgaben zu lesen
        aufgaben = datei.readlines() # Alle Zeilen aus der Datei holen
    finally:
        datei.close() # Datei schließen
    
    if len(aufgaben) == 0:
        print("Keine Aufgaben vorhanden.")
    show_tasks()
    nummer = int(input("Welche Aufgabe soll gelöscht werden? "))
        
    if 0 < nummer <= len(aufgaben):
        del aufgaben[nummer - 1]  # Aufgabe entfernen
        datei = open(datei_name, "w")
        datei.writelines(aufgaben)  # Datei neu schreiben
        datei.close()
        print("Aufgabe gelöscht.")
    else:
        print("Ungültige Nummer.")

"""Steuert das Menü."""
def main():
    while True:
        print("\nTo-Do-Liste:")
        print("1. Aufgabe hinzufügen")
        print("2. Aufgaben anzeigen")
        print("3. Aufgabe als erledigt markieren")
        print("4. Aufgabe löschen")
        print("5. Beenden")
        
        auswahl = input("Wähle eine Option: ")
        
        if auswahl == "1":
            add_task()
        elif auswahl == "2":
            show_tasks()
        elif auswahl == "3":
            mark_task_done()
        elif auswahl == "4":
            delete_task()
        elif auswahl == "5":
            print("Programm wird beendet.")
            break
        else:
            print("Ungültige Eingabe, bitte erneut versuchen.")

if __name__ == "__main__":
    main()  # Startet das ganze Programm
