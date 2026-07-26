# Patientenverwaltung
### Softwareentwickler:  Azlan Ainto
### Github Repo erstellt am 26.07.2026

Eine moderne Software zur Verwaltung von Patienten in einem Krankenhaus. Das System ermöglicht die Erfassung, Verwaltung und Suche von Patientendaten und dient als praxisnahes Beispiel für die Entwicklung einer objektorientierten Anwendung mit Python.

## Funktionen

- Patienten anlegen, bearbeiten und löschen
- Patientensuche nach Nachname oder Patienten-ID
- Verwaltung von Adress- und Kontaktdaten
- Übersicht aller gespeicherten Patienten
- Objektorientierter Aufbau mit mehreren Klassen
- Einfache Erweiterbarkeit für zukünftige Funktionen

## Technologien

- **Programmiersprache:** Python 3
- **Entwicklungsumgebung:** Visual Studio Code
- **Versionsverwaltung:** Git & GitHub

## Projektstruktur

```text
patientenverwaltung/
│
├── daten/
│   └── patienten.json
│
├── modelle/
│   ├── patient.py
│   ├── adresse.py
│   └── versicherung.py
│
├── verwaltung/
│   └── patientenverwaltung.py
│
├── utils/
│   └── dateiverwaltung.py
│
├── tests/
│   ├── test_patient.py
│   └── test_patientenverwaltung.py
│
├── main.py
├── README.md
├── requirements.txt
└── .gitignore
```

## Installation

Repository klonen:

```bash
git clone https://github.com/<dein-github-username>/patientenverwaltung.git
```

In das Projektverzeichnis wechseln:

```bash
cd patientenverwaltung
```

Programm starten:

```bash
python main.py
```

## Entwicklungsumgebung

Das Projekt wurde für **Visual Studio Code** entwickelt und kann dort direkt geöffnet werden.


## Projektziel

Dieses Projekt dient als Lern- und Demonstrationsprojekt für die objektorientierte Programmierung (OOP) mit Python. Anhand einer realitätsnahen Patientenverwaltung werden wichtige Konzepte wie Klassen, Objekte, Vererbung, Aggregation, Komposition sowie der strukturierte Aufbau größerer Softwareprojekte vermittelt.

## Lizenz

Dieses Projekt dient ausschließlich Lern- und Ausbildungszwecken.
