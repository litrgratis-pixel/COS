# Creative OS — system dowożenia jednego odcinka naraz

To nie jest generyczny system dokumentacji — jest skrojony pod pracę serialną/odcinkową, gdzie głównym ryzykiem jest to, że każdy nowy dobry pomysł dostaje nienależny priorytet. System nie zwiększa kreatywności — reguluje jej dostęp do aktywnej produkcji.

## Zasada nadrzędna

**W danym momencie istnieje tylko 1 aktywny odcinek** (etap kreatywny — koncepcja/scenariusz; etapy czysto produkcyjne jak montaż mogą iść równolegle). Wszystko inne ląduje w `BACKLOG.md` (przyszłe odcinki) albo `PARKING.md` (pomysły/podejścia odłożone z warunkiem powrotu).

## Struktura

```
creative-os/
├── 00_INDEX.md              ← wklejasz do AI na start sesji, razem z ODCINEK_AKTYWNY.md
├── AZYMUT.md                 ← rdzeń marki, obietnica, czego NIE robimy (rzadko zmieniany)
├── BACKLOG.md                 ← przyszłe odcinki, tytuł + 1 zdanie
├── PARKING.md                 ← pomysły/podejścia odłożone, z warunkiem powrotu ⏰
├── ODCINEK_AKTYWNY.md         ← JEDYNY aktywny odcinek + jego otwarte pytania (max 3)
├── DECYZJE.md                 ← DEC-lite / DEC-full, append-only
├── DONE.md                    ← opublikowane odcinki + wnioski, append-only
├── SESJE/
│   └── SZABLON_sesja.md
├── PROMPTY_SESJI.md           ← Opener + Closer
└── INSTRUKCJA_WDROZENIA.md
```

Świadomie NIE ma osobnego pliku na otwarte pytania — żyją wewnątrz `ODCINEK_AKTYWNY.md`, bo są właściwością aktywnego odcinka, nie osobnym bytem, i znikają razem z nim (po przeniesieniu ważnych ustaleń do `DECYZJE.md`/`DONE.md`).

## Zacznij tutaj

1. `INSTRUKCJA_WDROZENIA.md` (krok po kroku, GitHub).
2. Wypełnij `AZYMUT.md` swoimi słowami (już zaczęte — sprawdź, czy nadal aktualne).
3. `ODCINEK_AKTYWNY.md` ma już `EP-001` — „Ryba spod lodu" — jako punkt startowy.
4. Pierwsza sesja: `PROMPTY_SESJI.md` → Opener.
