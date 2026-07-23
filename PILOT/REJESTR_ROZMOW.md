---
protocol: cognitive-os-v0
artifact: conversation_audit_registry
version: 0.1
status: active
last_updated: 2026-07-23
---

# REJESTR ROZMÓW PILOTA

Ten plik jest indeksem materiałów użytych do testowania Cognitive OS. Surowe rozmowy nie muszą znajdować się w publicznym repozytorium. Raport ma zawierać wystarczający ślad dowodowy, aby inny model mógł zrozumieć wynik bez dostępu do prywatnej transkrypcji.

## Statusy

- `queued` — materiał wybrany, analiza nie rozpoczęta;
- `inventory_complete` — zakończono ślepy inwentarz;
- `audit_complete` — zakończono audyt względem repo;
- `decision_pending` — istnieją propozycje wymagające decyzji użytkownika;
- `closed` — closer i stan zostały zapisane;
- `excluded` — materiał wyłączony z uzasadnieniem.

## Rejestr

| ID | Materiał | Typ | Zakres | Metoda | Wynik główny | Artefakt | Status |
|---|---|---|---|---|---|---|---|
| AUD-2026-001 | `4AI 2.0.docx` | techniczna / produktowa / wielosesyjna | 163 strony; rozwój 4-AI Lab | Prompt 1: ślepy inwentarz; Prompt 2: audyt repo | rozmowa jest przede wszystkim katalogiem awarii procesu: overclaim, scope creep, semantic reopen, mock przedstawiony jako działająca implementacja | `PILOT/AUDYTY/AUD-2026-001_4AI.md`; `COS/SESJE/2026-07-23-001.md` | closed |
| AUD-2026-002 | rozmowa „AI Collaboration Operating System” | strategiczna / metaprojektowa / kontrolna | krótsza, odrębna rozmowa; audytorom przekazano zwarty rezultat normatywny bez pełnej atrybucji wiadomości | Prompt 3: ślepy inwentarz; Prompt 4: audyt repo i porównanie A/B | ten sam scope creep wystąpił w skompresowanej formie: szybkie zamrożenie uniwersalnego systemu; wykryto też błąd `DECISION_IN_ARTIFACT ≠ USER_DECISION` | `PILOT/AUDYTY/AUD-2026-002_AI_COLLABORATION_OS.md`; `COS/SESJE/2026-07-23-002.md` | closed |

## Minimalne dane dla nowego wpisu

```markdown
| AUD-YYYY-NNN | nazwa zredagowana | typ rozmowy | liczba stron/wiadomości lub przybliżony rozmiar | zastosowane etapy | jednozdaniowy wynik | ścieżka raportu | status |
```

## Zasady porównywalności

1. Stosuj ten sam podstawowy format audytu dla wszystkich rozmów.
2. Zapisuj odstępstwa od promptu lub ograniczenia dostępu do materiału.
3. Nie porównuj surowej liczby wykrytych błędów między rozmowami o skrajnie różnej długości bez normalizacji.
4. Zapisuj również rozmowy przebiegające dobrze; inaczej pilot będzie mierzył wyłącznie porażki.
5. Przy każdej rozmowie odnotuj, czy wynik został uzyskany na podstawie pełnej treści, fragmentów, listy plików czy streszczenia.
6. Oddzielaj rodzaj sesji źródłowej od formy artefaktu przekazanego audytorowi. Rozmowa może zakończyć się zwartym dokumentem, a dokument może zawierać materiał z wielu rozmów.
7. Brak pełnej atrybucji ogranicza metryki decyzji i chronologii, ale nie wyklucza rozmowy z pilota, jeżeli jej pochodzenie zostało potwierdzone.

## Następny wymagany kontrast

Trzecia rozmowa powinna maksymalizować kontrast względem pierwszych dwóch:

- inna domena niż projektowanie systemów AI;
- najlepiej rozmowa przebiegająca dobrze;
- pełna transkrypcja lub jawne etykiety USER/AI;
- jasno określony rezultat;
- zmierzony czas bootstrapu, analizy i protokołu.
