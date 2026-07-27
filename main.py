
"""Einstiegspunkt zum manuellen Testen der Patientenverwaltung."""
from datetime import date
from patverw import PatientVerwaltung

def datum_einlesen(text:str)->date:
    jahr, monat, tag = map(int, input(text).split("-"))
    return date(jahr, monat, tag)

def zeige_menue() -> None:
    print("Menü:")
    print("1. Patient hinzufügen")
    print("2. Alle Patienten anzeigen")
    print("3. Patient suchen")
    print("4. Patient entfernen")
    print("5. Telefonnummer ändern")
    print("6. Notizen hinzufügen")
    print("7. Programm beenden")


def main() -> None:
    praxis = PatientVerwaltung()
    zeige_menue()
    auswahl = input ("Bitte wählen Sie eine Option (1-7): ").strip()
    if auswahl == "1":
        vorname = input("Vorname: ")
        nachname = input("Nachname: ")
        if not vorname or not nachname:
            print("Vorname und Nachname dürfen nicht leer sein.")
            return
        geburtsdatum = datum_einlesen("Geburtsdatum (JJJJ-MM-TT): ")
        telefonnummer = input("Telefonnummer: ")    
        praxis.patient_hinzufuegen(vorname, nachname, geburtsdatum, telefonnummer)
    elif auswahl == "2":
        for patient in praxis.alle_patienten_anzeigen():
            print(patient)
    elif auswahl == "3":
        nachname = input("Nachname: ")
        for patient in praxis.patient_suchen(nachname):
            print(patient)
    elif auswahl == "4":
        patient_id = int(input("Patienten-ID: "))
        if praxis.patient_entfernen(patient_id):
            print("Patient erfolgreich entfernt.")
        else:
            print("Patient nicht gefunden.")
    elif auswahl == "5":
        patient_id = int(input("Patienten-ID: "))
        neue_telefonnummer = input("Neue Telefonnummer: ")
        if praxis.patient_telefonnummer_aendern(patient_id, neue_telefonnummer):
            print("Telefonnummer erfolgreich geändert.")
        else:
            print("Patient nicht gefunden.")
    elif auswahl == "6":
        patient_id = int(input("Patienten-ID: "))
        notizen = input("Notizen: ")
        if praxis.patienten_setzen(patient_id, notizen):
            print("Notizen erfolgreich hinzugefügt.")
        else:
            print("Patient nicht gefunden.")
    elif auswahl == "7":
        print("Programm beendet.")
    else:
        print("Ungültige Auswahl. Bitte wählen Sie eine Option von 1 bis 7.")

if __name__ == "__main__":
    main()