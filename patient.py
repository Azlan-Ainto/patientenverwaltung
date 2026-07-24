"""Datenmodell für einen Patienten der Arztpraxis.

"""
from dataclasses import dataclass
from datetime import date

@dataclass
class Patient:
    patient_id: int
    vorname: str
    nachname: str
    geburtsdatum: date
    telefonnummer: str=""

    def __str__(self) -> str:
        datum = self.geburtsdatum.strftime("%d.%m.%Y")
        return f"[{self.patient_id} {self.vorname} {self.nachname}, geb. {datum}, Tel.: {self.telefonnummer}]"
    