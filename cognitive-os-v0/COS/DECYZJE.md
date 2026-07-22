---
protocol: cognitive-os-v0
type: decision_log
version: 0.1
policy: append_only_with_supersession
---

# DECYZJE

Wpisuj tylko decyzje, które zmieniają sposób działania lub stan projektu. Luźny pomysł trafia do `PARKING.md` albo `BACKLOG.md`.

## Indeks bieżący

| ID | Data | Decyzja | Status | Supersedes | Reopen if |
|---|---|---|---|---|---|
| DEC-2026-000 | 2026-07-21 | Uruchomienie pilota Cognitive OS v0 | proposed | — | po 10 sesjach |

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

## DEC-2026-000 — uruchomienie pilota (propozycja)

- Status: proposed
- Wybrano: dziesięć rzeczywistych sesji z minimalnym protokołem v0.
- Nie wybrano: budowy pełnego systemu, stałych agentów i automatycznego zapisu.
- Dlaczego: najpierw trzeba zmierzyć, która awaria rzeczywiście występuje.
- Dane i źródła: `docs/05_PLAN_PILOTA_10_SESJI.md`, analiza załączonej rozmowy.
- Ryzyko resztkowe: pilot może nie reprezentować wszystkich typów pracy.
- Warunek ponownego otwarcia: wynik metryk po dziesiątej sesji.
- Zatwierdził: DO POTWIERDZENIA
- Commit/patch: DO UZUPEŁNIENIA
