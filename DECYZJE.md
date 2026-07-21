# DECYZJE — Rejestr decyzji (APPEND-ONLY)

> Nigdy nie edytujesz starego wpisu — tylko `SUPERSEDED BY DEC-xxx`. Każdy wpis ma pole `Odcinek: EP-xxx`, bo `ODCINEK_AKTYWNY.md` nie jest append-only i zniknie — bez tego pola za 3 miesiące nie wiesz, którego odcinka dotyczyła decyzja.

> **Dwa formaty — wybierz świadomie, nie domyślnie pełny:**
> - **DEC-lite** (jedna linijka): dla decyzji odwracalnej w ciągu jednej sesji bez konsekwencji dla innych odcinków.
> - **DEC-full** (pełne pola): dla decyzji wpływającej na całą serię, na Azymut, albo której cofnięcie wymaga przerobienia wcześniejszych odcinków.

---

<a id="DEC-001"></a>
<!-- typ: full | odcinek: EP-001 -->
## DEC-001 — Otwarcie od najmocniejszej sceny, nie od spokojnego wejścia

- **Odcinek:** EP-001
- **Data:** 2026-07-18
- **Typ:** full
- **Kontekst:** Sposób otwarcia odcinka — od razu akcja, czy najpierw krótkie wprowadzenie (biuro)?
- **Decyzja:** Odcinek zaczyna się od najmocniejszej sceny (hook), biuro pokazane skrótowo, jeśli w ogóle.
- **Uzasadnienie:** Format short potrzebuje bodźca w pierwszych 2 sekundach (DoD, `AZYMUT.md`).
- **Wpływ:** Dotyczy formatu WSZYSTKICH odcinków, nie tylko EP-001 — to jest właściwie decyzja na poziomie serii, mimo że powstała przy pracy nad EP-001.
- **Status:** ✅ Aktywna

---

## Wzorzec DEC-lite (kopiuj)

```markdown
- **DEC-XXX** — [treść jednym zdaniem]. Odcinek: EP-xxx. Data: YYYY-MM-DD. Powód: [pół zdania].
```

## Wzorzec DEC-full (kopiuj)

```markdown
<a id="DEC-XXX"></a>
<!-- typ: full | odcinek: EP-xxx -->
## DEC-XXX — [Tytuł jednym zdaniem]

- **Odcinek:** EP-xxx
- **Data:** YYYY-MM-DD
- **Typ:** full
- **Kontekst:** Co spowodowało konieczność decyzji (cytuj pytanie z ODCINEK_AKTYWNY.md, jeśli je zamykasz — ono zniknie).
- **Decyzja:** Konkret.
- **Uzasadnienie:** …
- **Wpływ:** Czy dotyczy tylko tego odcinka, czy całej serii (→ jeśli serii, rozważ czy to nie powinno wejść do AZYMUT.md).
- **Status:** ✅ Aktywna | ⚠️ SUPERSEDED BY DEC-YYY (data, powód)
```
