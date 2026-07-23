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

## Następny wymagany kontrast

Druga rozmowa powinna różnić się od `AUD-2026-001`: najlepiej być krótsza, mieć jasno określony rezultat i nie dotyczyć rozbudowy architektury. Ma sprawdzić, czy koszt protokołu nie przewyższa korzyści w prostszym przypadku.
