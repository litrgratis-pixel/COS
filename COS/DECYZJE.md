---
protocol: cognitive-os-v0
type: decision_log
version: 0.1
policy: append_only_with_supersession
last_updated: 2026-07-23
---

# DECYZJE

Wpisuj tylko decyzje, które zmieniają sposób działania lub stan projektu. Luźny pomysł trafia do `PARKING.md` albo `BACKLOG.md`.

## Indeks bieżący

| ID | Data | Decyzja | Status | Supersedes | Reopen if |
|---|---|---|---|---|---|
| DEC-2026-000 | 2026-07-21 | Uruchomienie pilota Cognitive OS v0 | active | — | po 10 sesjach lub przy nieakceptowalnym koszcie protokołu |
| DEC-2026-001 | 2026-07-23 | Seria audytów rozmów i finalizacja COS na podstawie danych | active | — | po checkpointach 3/6/10 albo po wykryciu ryzyka bezpieczeństwa |

## Szablon nowej decyzji

```markdown
### DEC-YYYY-NNN — krótka nazwa

- Data:
- Status: proposed | active | superseded | closed
- Wybrano:
- Nie wybrano:
- Dlaczego:
- Dane i źródła:
- Pakiet weryfikacyjny:
- Ryzyko resztkowe:
- Warunek ponownego otwarcia:
- Zatwierdził:
- Commit/patch:
```

Nie usuwaj starych decyzji. Jeśli przestała obowiązywać, oznacz `superseded` i wskaż nową.

## DEC-2026-000 — uruchomienie pilota

- Data: 2026-07-21; zatwierdzenie użytkownika 2026-07-23.
- Status: active.
- Wybrano: dziesięć rzeczywistych sesji z minimalnym protokołem v0.
- Nie wybrano: budowy pełnego systemu, stałych agentów, automatycznego zapisu i ogłoszenia wersji końcowej przed pomiarem.
- Dlaczego: najpierw trzeba zmierzyć, które awarie rzeczywiście się powtarzają i czy protokół przynosi wartość większą niż koszt.
- Dane i źródła: `docs/05_PLAN_PILOTA_10_SESJI.md`, `COS/SESJE/2026-07-23-001.md`, `PILOT/AUDYTY/AUD-2026-001_4AI.md`.
- Pakiet weryfikacyjny: pierwszy audyt rozmowy, jakościowy baseline awarii procesu.
- Ryzyko resztkowe: pilot może nie reprezentować wszystkich typów pracy; pierwsza rozmowa jest długa i problematyczna.
- Warunek ponownego otwarcia: wynik metryk po dziesiątej sesji, powtarzalny false stop albo koszt protokołu większy od pracy właściwej.
- Zatwierdził: USER.
- Commit/patch: `agent/pilot-reports-and-lessons`; docelowo PR do `main`.

## DEC-2026-001 — seria audytów i finalizacja oparta na danych

- Data: 2026-07-23.
- Status: active.
- Wybrano:
  - przeanalizować kilka zróżnicowanych rozmów;
  - stosować dwuetapowy proces: ślepy inwentarz, następnie audyt względem repo;
  - przechowywać całą wiedzę operacyjną projektu w GitHubie;
  - utrzymywać osobny katalog wniosków, aliasów pomysłów i bram zapobiegawczych;
  - przygotować końcową konfigurację COS dopiero po danych z checkpointów.
- Nie wybrano:
  - automatycznego przeniesienia wszystkich wniosków pierwszego audytu do kanonu;
  - rozbudowy produktu COS przed zakończeniem pilota;
  - uznawania zgodności modeli za niezależny dowód;
  - przechowywania surowych prywatnych rozmów w publicznym repo bez redakcji.
- Dlaczego: dwa prompty dały komplementarne wyniki, ale pojedynczy przypadek nie wystarcza do finalizacji protokołu.
- Dane i źródła: `PILOT/README.md`, `PILOT/SZABLON_AUDYTU_ROZMOWY.md`, `PILOT/METRYKI.md`, `PILOT/FINALIZACJA_V1.md`, `COS/SESJE/2026-07-23-001.md`.
- Pakiet weryfikacyjny: porównanie Promptu 1 i Promptu 2 dla `AUD-2026-001`.
- Ryzyko resztkowe: wzrost kosztu dokumentacji, przeuczenie na audytach błędnych rozmów i rozbudowa protokołu zamiast jego testowania.
- Warunek ponownego otwarcia: checkpoint po 3, 6 i 10 sesjach; natychmiast tylko przy bezpieczeństwie lub utracie danych.
- Zatwierdził: USER.
- Commit/patch: `agent/pilot-reports-and-lessons`; docelowo PR do `main`.
