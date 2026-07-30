
"""Einstiegspunkt zum manuellen Testen der Patientenverwaltung."""
from datetime import date
from patient import Patient
from patverw import PatientVerwaltung

def datum_einlesen(text:str)->date:
    jahr, monat, tag = map(int, input(text).split("-"))
    return date(jahr, monat, tag)
# ----------------------------------------------------------
# --------Menü und Auswahl der ptionen----------------------
def zeige_menue() -> None:
    print("\n--- Patientenverwaltung ---")
    print("1. Patient hinzufügen")
    print("2. Alle Patienten anzeigen")
    print("3. Patient suchen")
    print("4. Patient entfernen")
    print("5. Telefonnummer aktualisieren")
    print("6. Notiz hinzufügen")
    print("7. Patienten sortiert anzeigen (nach Nachname)")
    print("8. Statistik anzeigen")
    print("9. Patient nach ID anzeigen")
    print("10. Beenden")

def main() -> None:
    praxis = PatientVerwaltung()
    praxis.patienten_laden()

    while True:
        zeige_menue()
        auswahl = input("Auswahl: ").strip()

        if auswahl == "1":
            vorname = input("Vorname: ").strip()
            nachname = input("Nachname: ").strip()
            if not vorname or not nachname:
                print("Vorname und Nachname dürfen nicht leer sein.")
                continue
            geburtsdatum = datum_einlesen("Geburtsdatum (JJJJ-MM-TT): ")
            telefonnummer = input("Telefonnummer (optional): ")
            praxis.patient_hinzufuegen(vorname, nachname, geburtsdatum, telefonnummer)
            praxis.patienten_speichern()
            print("Patient hinzugefügt und gespeichert.")

        elif auswahl == "2":
            for patient in praxis.alle_patienten():
                print(patient)

        elif auswahl == "3":
            nachname = input("Nachname: ")
            for patient in praxis.patient_suchen(nachname):
                print(patient)

        elif auswahl == "4":
            patient_id = int(input("Patienten-ID: "))
            if praxis.patient_entfernen(patient_id):
                praxis.patienten_speichern()
                print("Patient entfernt.")
            else:
                print("Kein Patient mit dieser ID gefunden.")

        elif auswahl == "5":
            patient_id = int(input("Patienten-ID: "))
            telefonnummer = input("Neue Telefonnummer: ")
            if praxis.patient_aktualisieren(patient_id, telefonnummer):
                praxis.patienten_speichern()
                print("Telefonnummer aktualisiert.")
            else:
                print("Kein Patient mit dieser ID gefunden.")

        elif auswahl == "6":
            patient_id = int(input("Patienten-ID: "))
            text = input("Notiz: ")
            if praxis.notiz_setzen(patient_id, text):
                praxis.patienten_speichern()
                print("Notiz gespeichert.")
            else:
                print("Kein Patient mit dieser ID gefunden.")

        elif auswahl == "7":
            for patient in praxis.patienten_sortiert():
                print(patient)

        elif auswahl == "8":
            stats = praxis.statistik()
            print(f"Anzahl Patienten: {stats['anzahl']}")
            if stats["anzahl"] > 0:
                print(f"Durchschnittsalter: {stats['durchschnittsalter']:.1f} Jahre")
                print(f"Ältester Patient: {stats['aeltester']}")
                print(f"Jüngster Patient: {stats['juengster']}")

        elif auswahl == "9":
            patient_id = int(input("Patienten-ID: "))
            gefunden = praxis.patient_suchen_nach_id(patient_id)
            if gefunden:
                print(gefunden)
                if gefunden.notizen:
                    print(f"Notizen: {gefunden.notizen}")
            else:
                print("Kein Patient mit dieser ID gefunden.")

        elif auswahl == "10":
            print("Bis bald in der Patientenverwaltung!")
            break

if __name__ == "__main__":
    main()