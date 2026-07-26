""" Verwatungslogik für die Patienten der Arztpraxis."""
from patient import Patient
from datetime import date

class PatientVerwaltung:

    def __init__(self)-> None:
        self._patienten : list[Patient] = []
        self._naechste_id = 1

    def patient_hinzufuegen(self,
            vorname: str,
            nachname: str,
            geburtsdatum: date,
            telefonnummer: str=""
    )-> Patient:
        neuer_patient = Patient(
            patient_id = self._naechste_id,
            vorname = vorname,
            nachname = nachname,
            geburtsdatum = geburtsdatum,
            telefonnummer = telefonnummer
        )
        self._patienten.append(neuer_patient)
        self._naechste_id += 1
        return neuer_patient
    
    def alle_patienten_anzeigen(self) -> list[Patient]:
        return self._patienten

    def patient_suchen(self, nachname:str) -> list[Patient]:
        # gesuchte_patienten = nachname.strip().casefold()
        gesuchte_patienten = nachname.strip().lower()
        return [
            patient
            for patient in self._patienten 
            if patient.nachname.lower() == gesuchte_patienten
        ]

    def patient_entfernen(self, patient_id:int) -> bool:
        for index, patient in enumerate(self._patienten):
            if patient.patient_id == patient_id:
                del self._patienten[index]
                return True
        return False

    def patient_telefonnummer_aendern(self, patient_id:int, neue_telefonnummer:str) -> bool:
        for patient in self._patienten:
            if patient.patient_id == patient_id:
                patient.telefonnummer = neue_telefonnummer
                return True
        return False

    def patient_anzahl(self) -> int:
        return len(self._patienten)
    