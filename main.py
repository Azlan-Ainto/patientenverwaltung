
"""Einstiegspunkt zum manuellen Testen der Patientenverwaltung."""
from datetime import date
from patverw import PatientVerwaltung

def main() -> None:
    praxis = PatientVerwaltung()
    praxis.patient_hinzufuegen(
        "Anna",
        "Muster",
        date(1980, 6, 15),
        "1234567890"
    )
    praxis.patient_hinzufuegen(
        "Ben",
        "Beispiel",
        date(1975, 3, 22),
        "0987654321"
    )
    praxis.patient_hinzufuegen(
        "Max", 
        "Mustermann", 
        date(1990, 1, 1), 
        "0123456789")
    praxis.patient_hinzufuegen(
        "Erika", 
        "Musterfrau", 
        date(1995, 5, 15), 
        "9876543210")
    praxis.patient_hinzufuegen(
        "John",
        "Doe",
        date(1985, 12, 31),
        "5551234567")
    # Patienten nach Nachnamen suchen
    # Alle Patienten anzeigen
    print("Alle Patienten in der Praxis:")
    for patient in praxis.alle_patienten_anzeigen():
        print(patient)

    print("\nSuche nach Nachnamen suchen:")
    nachname = "Muster"
    for patient in praxis.patient_suchen(nachname):
        print(patient)
    

if __name__ == "__main__":
    main()