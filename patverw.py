""" Verwatungslogik für die Patienten der Arztpraxis."""
from patient import Patient
from datetime import date
import json
from pathlib import Path
DATENDATEI = Path("patienten.json")
class PatientVerwaltung:



    def __init__(self)-> None:
        self._patienten : list[Patient] = []
        self._naechste_id = 1

    def notiz_setzen(self, patient_id: int, text: str) -> bool:
        text = text.strip()
        if not text:
            return False
        for patient in self._patienten:
            if patient.patient_id == patient_id:
                patient.notizen = text
                return True
        return False
    def statistik(self) -> dict:
        if not self._patienten:
            return {"anzahl": 0, "durchschnittsalter": 0.0, "aeltester": None, "juengster": None}
        heute = date.today()
        alter_liste = [
            heute.year
            - p.geburtsdatum.year
            - ((heute.month, heute.day) < (p.geburtsdatum.month, p.geburtsdatum.day))
            for p in self._patienten
        ]
        return {
            "anzahl": len(self._patienten),
            "durchschnittsalter": sum(alter_liste) / len(alter_liste),
            "aeltester": min(self._patienten, key=lambda p: p.geburtsdatum),
            "juengster": max(self._patienten, key=lambda p: p.geburtsdatum),
        }

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

    def patienten_setzen(self, patient_id: int, text:str)->bool:
        for patient in self._patienten:
            if patient.patient_id == patient_id:
                patient.notizen = text
                return True
        return False

    def patienten_speichern(self, dateipfad: Path=DATENDATEI) -> None:
        daten = [
            {
                "patient_id": patient.patient_id,
                "vorname": patient.vorname,
                "nachname": patient.nachname,
                "geburtsdatum": patient.geburtsdatum.isoformat(),
                "telefonnummer": patient.telefonnummer,
                "notizen": patient.notizen
            }
            for patient in self._patienten
        ]
        dateipfad.write_text(json.dumps(daten, ensure_ascii=False, indent=2), encoding="utf-8")
    def patienten_sortiert(self, absteigend: bool = False) -> list[Patient]:
        return sorted(self._patienten, key=lambda p: p.nachname.lower(), reverse=absteigend)

    def patienten_laden(self, dateipfad: Path=DATENDATEI) -> None:
        if not dateipfad.exists():
            return
        daten = json.loads(dateipfad.read_text(encoding="utf-8"))
        self._patienten = [
            Patient(
                patient_id = eintrag["patient_id"],
                vorname = eintrag["vorname"],
                nachname = eintrag["nachname"],
                geburtsdatum = date.fromisoformat(eintrag["geburtsdatum"]),
                telefonnummer = eintrag.get("telefonnummer", ""),
                notizen = eintrag.get("notizen", "")
            )
            for eintrag in daten
        ]
        if self._patienten:
            self._naechste_id = max(patient.patient_id for patient in self._patienten) + 1
        else:
            self._naechste_id = 1
    

    def patient_suchen_nach_id(self, patient_id: int) -> Patient | None:
        for patient in self._patienten:
            if patient.patient_id == patient_id:
                return patient
        return None