---
protocol: cognitive-os-v0
artifact: conversation_audit_template
version: 0.1
status: active
last_updated: 2026-07-23
---

# SZABLON AUDYTU ROZMOWY

Ten szablon jest docelowym połączeniem dwóch przetestowanych promptów. Rozdziela ekstrakcję materiału od oceny względem repozytorium, aby ograniczyć zarówno brak działania, jak i nadmierne dopasowanie do teorii COS.

## Przed uruchomieniem

1. Wykonaj bootstrap z `PILOT/README.md`.
2. Zapisz commit bazowy `main`.
3. Określ dostęp do źródła: `full`, `partial`, `metadata_only` albo `summary_only`.
4. Rozpocznij w trybie `READ_ONLY`.
5. Nie zapisuj surowej rozmowy do publicznego repo bez redakcji i zgody.

---

# ETAP A — ŚLEPY INWENTARZ

```text
Przeczytaj załączoną rozmowę jako audytor procesu.

Na tym etapie:
- nie używaj repozytorium do interpretowania materiału;
- nie proponuj zmian w Cognitive OS;
- nie twórz podsumowania narracyjnego;
- nie uznawaj twierdzeń AI za fakty techniczne;
- nie zmieniaj żadnych plików.

Klasyfikuj elementy jako:
FACT_MATERIAL — coś rzeczywiście pada w rozmowie, bez potwierdzenia prawdziwości;
HYPOTHESIS — przypuszczenie lub claim wymagający dowodu;
PREFERENCE — preferencja użytkownika;
RECOMMENDATION — rada AI;
DECISION — jawny wybór lub zobowiązanie użytkownika;
PROPOSAL — pomysł, szkic, kod lub konfiguracja bez zatwierdzonego stanu.

Przygotuj:
1. mapę głównych tematów;
2. chronologię zmian kierunku i bodźców zmiany;
3. listę jawnych decyzji użytkownika;
4. listę wypowiedzi AI błędnie brzmiących jak decyzje lub fakty;
5. listę odrzuconych albo supersedowanych kierunków wraz z powodami;
6. kandydatów do parkingu;
7. sprzeczności i ponowne otwarcia wcześniejszych ustaleń;
8. twierdzenia wymagające zewnętrznego cross-checku;
9. miejsca, w których AI rozwijało architekturę, kod lub roadmapę bez dowodu;
10. miejsca, w których użytkownik wykrył błąd, którego AI wcześniej nie oznaczyło.

Dla każdego istotnego punktu wskaż stronę, wiadomość, cytat zredagowany albo inną lokalizację w materiale.

Zakończ:
INVENTORY_COMPLETE
source_coverage:
limitations:
NO_REPO_CHANGE
```

---

# ETAP B — AUDYT WZGLĘDEM REPOZYTORIUM

```text
Użyj repozytorium litrgratis-pixel/COS, gałęzi main, jako źródła obowiązującego stanu.

Najpierw odczytaj:
- README.md
- PILOT/README.md
- COS/00_KONTRAKT_PRACY_Z_AI.md
- COS/01_KOMPAS.md
- COS/02_KANON.md
- COS/03_AKTYWNY.md
- COS/DECYZJE.md
- COS/PARKING.md
- COS/BACKLOG.md
- COS/INCYDENTY.md
- COS/99_HANDOFF.md
- PILOT/REJESTR_ROZMOW.md
- PILOT/METRYKI.md
- WNIOSKI_I_POMYSLY/README.md
- WNIOSKI_I_POMYSLY/MAPA_ALIASOW.md

Podaj BOOT_ACK i commit bazowy.

Następnie porównaj wynik ETAPU A z aktualnym repozytorium.

Przygotuj:
1. zgodności z aktualnym COS;
2. konflikty z kanonem, decyzjami, aktywnym celem albo handoffem;
3. decyzje historyczne, które nie są decyzjami COS;
4. semantic reopen — powrót odrzuconego kierunku pod inną nazwą;
5. mechanizmy, które obecny COS już obsługuje;
6. luki, których obecny COS nie obsługuje;
7. false pass i false stop;
8. propozycje zmian jako PROPOSAL;
9. metryki audytu;
10. werdykt: PASS / REVISE / NEEDS_EVIDENCE / DISAGREEMENT / ESCALATE / FAIL.

Dla każdej propozycji podaj:
- ID;
- plik docelowy;
- dokładną treść zmiany;
- dowód z materiału;
- powód;
- ryzyko i koszt;
- warunek usunięcia lub cofnięcia;
- status PROPOSAL.

Nie zmieniaj repozytorium, nie twórz gałęzi, commitu ani PR.

Zakończ:
AUDIT_COMPLETE
STATE_CHANGE_RECOMMENDED: YES | NO
RECOMMENDED_NEXT_STEP:
NO_REPO_CHANGE
```

---

# ETAP C — PORÓWNANIE DWÓCH ODPOWIEDZI

Po otrzymaniu wyników A i B odpowiedz:

```text
1. Jakie ustalenia wystąpiły w obu odpowiedziach?
2. Jakie ustalenia wystąpiły tylko w A i dlaczego?
3. Jakie ustalenia wystąpiły tylko w B i czy wynikają z repo, czy z nadinterpretacji?
4. Czy B prawidłowo zachowało rozdział rozmowa = materiał, repo = stan?
5. Które propozycje są już obsłużone istniejącą regułą?
6. Jaka jest minimalna delta wymagająca decyzji człowieka?
7. Czy raport da się zrozumieć bez znajomości promptu?
```

## Kryteria jakości

Dobry audyt:

- nie myli cytatu z prawdą techniczną;
- nie myli decyzji AI z decyzją użytkownika;
- nie generuje patcha przed odczytem źródeł;
- wykrywa aliasy pomysłów;
- ogranicza propozycje do rzeczywistej delty;
- ma jawne ograniczenia źródła;
- kończy się jednym następnym krokiem;
- nie używa długości raportu jako dowodu jakości.

## Format nazwy artefaktu

```text
PILOT/AUDYTY/AUD-YYYY-NNN_KROTKI_TEMAT.md
```

## Minimalny front matter raportu

```yaml
---
protocol: cognitive-os-v0
artifact: conversation_audit
id: AUD-YYYY-NNN
status: draft | complete | superseded
source_coverage: full | partial | metadata_only | summary_only
repo_commit: SHA
mode: READ_ONLY
created_at: YYYY-MM-DD
---
```
