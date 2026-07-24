
"""Einstiegspunkt zum manuellen Testen der Patientenverwaltung."""
from datetime import date
from patverw import PatientVerwaltung

def main() -> None:
    praxis = PatientVerwaltung()
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
    for patient in praxis.alle_patienten_anzeigen():
        print(patient)

if __name__ == "__main__":
    main()