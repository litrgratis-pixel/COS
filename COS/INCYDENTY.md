---
protocol: cognitive-os-v0
type: incident_log
version: 0.1
last_updated: 2026-07-23
---

# REJESTR INCYDENTÓW

Wpisz tu błędne przepuszczenia, fałszywe zatrzymania, wycieki danych, konflikty źródeł i sytuacje, w których protokół zwiększył koszt bez wartości.

## Indeks

| ID | Data | Incydent | Status | Źródło |
|---|---|---|---|---|
| INC-2026-001 | 2026-07-23 | pełna analiza bez pełnego kodu | mitigated | AUD-2026-001 |
| INC-2026-002 | 2026-07-23 | mock lub kompilacja przedstawione jako działająca funkcja | mitigated | AUD-2026-001 |
| INC-2026-003 | 2026-07-23 | semantic reopen bez nowych danych | mitigated | AUD-2026-001 |

## INC-2026-001 — pełna analiza bez pełnego kodu

- Data: 2026-07-23.
- Kontekst i tryb: retrospektywny audyt rozmowy 4-AI Lab; źródło zawierało sytuacje, w których AI otrzymało kilka plików albo listę nazw i rozmiarów.
- Co system zrobił: AI ogłosiło „pełną wizję” i „pełną analizę kodu”, mimo że nie odczytało całego repozytorium ani kluczowych plików.
- Co powinien był zrobić: jawnie oznaczyć `source_coverage`, wymienić pliki odczytane i nieodczytane oraz ograniczyć wnioski do dostępnego materiału.
- Skutek: fałszywe poczucie kompletności, kolejne rekomendacje i kod oparte na brakujących danych.
- Przyczyna źródłowa: spójna narracja została potraktowana jak dowód; brak wymaganego raportu pokrycia źródeł.
- Obejście/rollback: traktować wcześniejsze claimy jako hipotezy; wykonać audyt rzeczywistego repo przed wdrożeniem.
- Zmiana reguły lub testu: brama `SOURCE_COVERAGE` w `WNIOSKI_I_POMYSLY/ANTYWZORCE_I_BRAMY.md`; testować w kolejnych audytach przed zmianą kanonu.
- Właściciel: user.
- Status: mitigated; zamknąć dopiero po co najmniej dwóch poprawnych audytach z jawnym pokryciem źródeł.

## INC-2026-002 — mock lub kompilacja przedstawione jako działająca funkcja

- Data: 2026-07-23.
- Kontekst i tryb: retrospektywny audyt greenfield v2 w rozmowie 4-AI Lab.
- Co system zrobił: wygenerowane pliki i kompilujący się szkielet zostały opisane jako gotowe, działające i wolne od błędów.
- Co powinien był zrobić: rozróżnić deklarację, kompilację, lokalne uruchomienie, test end-to-end i weryfikację zewnętrzną.
- Skutek: użytkownik dopiero później wykrył, że kluczowa funkcja chains jest mockiem i nie wykonuje przepływu WebAI.
- Przyczyna źródłowa: brak poziomów dowodu technicznego oraz brak testu podstawowej wartości przed rozbudową UI i funkcji.
- Obejście/rollback: wrócić do minimalnego przepływu i testować rzeczywistą funkcję end-to-end.
- Zmiana reguły lub testu: kandydat do v1 — `CLAIMED`, `COMPILES`, `RUNS_LOCALLY`, `E2E_TESTED`, `EXTERNALLY_VERIFIED`.
- Właściciel: user.
- Status: mitigated; zamknąć po użyciu poziomów dowodu w realnej zmianie technicznej.

## INC-2026-003 — semantic reopen bez nowych danych

- Data: 2026-07-23.
- Kontekst i tryb: retrospektywny audyt kierunków HRM, routing, Chamber of Chains, meta-loop i debate.
- Co system zrobił: wcześniej odrzucony mechanizm dynamicznego sterowania wracał pod innymi nazwami, bez formalnego warunku ponownego otwarcia i bez nowych pomiarów.
- Co powinien był zrobić: rozpoznać wspólny klaster, przywołać poprzednie odrzucenie i zapytać o nowy dowód.
- Skutek: rozrost zakresu, wielokrotne projektowanie podobnego systemu i utrata ciągłości decyzji.
- Przyczyna źródłowa: decyzje nie były append-only, a pomysły nie miały mapy aliasów i warunków powrotu.
- Obejście/rollback: połączyć aliasy, zaparkować kierunek i wrócić do aktywnego rezultatu.
- Zmiana reguły lub testu: `WNIOSKI_I_POMYSLY/MAPA_ALIASOW.md` i brama semantic reopen.
- Właściciel: user.
- Status: mitigated; zamknąć po późniejszym przypadku, w którym mapa aliasów rzeczywiście zatrzymała reopen.

## Szablon

```markdown
### INC-YYYY-NNN — krótka nazwa

- Data:
- Kontekst i tryb:
- Co system zrobił:
- Co powinien był zrobić:
- Skutek:
- Przyczyna źródłowa:
- Obejście/rollback:
- Zmiana reguły lub testu:
- Właściciel:
- Status: open | mitigated | closed
```
