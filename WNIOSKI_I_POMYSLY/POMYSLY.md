---
protocol: cognitive-os-v0
artifact: idea_landscape
version: 0.1
status: active
last_updated: 2026-07-23
---

# POMYSŁY — ZESTAWIENIE NIEKANONICZNE

Ten plik przechowuje krajobraz pomysłów wykrytych podczas eksperymentów. Żaden wpis nie jest automatycznie aktywny, zatwierdzony ani gotowy do budowy.

Formalne zaparkowanie wymaga osobnego wpisu z ID w `COS/PARKING.md`. Przeniesienie do `COS/BACKLOG.md` wymaga spełnienia kryteriów gotowości i zgody użytkownika.

## Statusy

- `observed` — pomysł wystąpił w materiale;
- `clustered` — połączony z innymi nazwami tego samego kierunku;
- `candidate_for_parking` — warto zachować z warunkiem powrotu;
- `rejected` — nie rozwijać bez jawnego reopen;
- `candidate_for_v1` — mechanizm protokołu do sprawdzenia na checkpointach;
- `ready` — zakazane w tym pliku; gotowość istnieje tylko w kanonicznym backlogu.

## Pomysły produktowe i techniczne

| ID | Kierunek | Klaster | Status | Dlaczego nie teraz | Warunek powrotu |
|---|---|---|---|---|---|
| IDEA-001 | pełny HRM / adaptive planner | ALIAS-01 | candidate_for_parking | brak zmierzonego problemu routingu; wcześniej odrzucony jako overkill | co najmniej 20 przypadków ręcznego wyboru powodującego koszt lub błąd |
| IDEA-002 | Chamber of Chains | ALIAS-01 | candidate_for_parking | wielomodelowa orkiestracja poza zakresem pilota | wynik 10 sesji i benchmark powtarzalnych klas zadań |
| IDEA-003 | AI classifier/router | ALIAS-01 | candidate_for_parking | ryzyko błędnej klasyfikacji i ukrytego kosztu | dataset, accuracy, override rate i porównanie z prostymi regułami |
| IDEA-004 | debate mode / consensus | ALIAS-03 | candidate_for_parking | zgodność modeli nie jest dowodem; konflikt z zakresem v0 | jasno określony cel ideacyjny, benchmark i zewnętrzne kryterium |
| IDEA-005 | dodatkowe LLM i przypisane role | ALIAS-01 | observed | brak testu wartości i koszt utrzymania integracji | ranking potrzeb oraz porównanie najwyżej dwóch kandydatów |
| IDEA-006 | daily AI review | ALIAS-02 | candidate_for_parking | możliwy hałas, koszt i ryzyko danych | polityka danych, metryka jakości i test małej próbki |
| IDEA-007 | self-heal selektorów | ALIAS-02 | candidate_for_parking | automatyczna zmiana zachowania bez bezpiecznej walidacji | sandbox, testy, rollback, human approval i audit trail |
| IDEA-008 | AI feature vote | ALIAS-02/03 | rejected | głosowanie modeli nie ma wykazanej korelacji z wartością | niezależny benchmark pokazujący przewagę nad prostym review |
| IDEA-009 | AI-assisted auto-test | ALIAS-02 | candidate_for_parking | model może oceniać styl zamiast działania | deterministyczne testy rdzenia i zewnętrzne kryteria |
| IDEA-010 | hybrid API/WebView | osobny | observed | bezpieczeństwo, ToS, klucze i koszty niezweryfikowane | threat model i porównanie niezawodności |
| IDEA-011 | produkt do pracy pisarskiej | ALIAS-04 | candidate_for_parking | nieustalona domena produktu | osobny problem statement i co najmniej 5 realnych sesji pisarskich |
| IDEA-012 | cloud/mobile/VS Code/enterprise | ALIAS-04 | candidate_for_parking | brak potwierdzonego rdzenia i segmentu | stabilny core, realne użycie i konkretny segment |
| IDEA-013 | greenfield rewrite | ALIAS-05 | observed | brak eksperymentu porównawczego | spike naprawa vs rewrite, regresje, koszt i rollback |

## Kandydaci do finalnej konfiguracji COS

Poniższe elementy są mechanizmami procesu, nie funkcjami produktu.

| ID | Mechanizm | Status | Dowód początkowy | Co musi się wydarzyć przed v1 |
|---|---|---|---|---|
| COS-CAND-001 | obowiązkowy `BOOT_ACK` | candidate_for_v1 | ręczne prompty dostarczały kontekst, którego nie było w repo | dwa skuteczne bootstrapy nowego AI wyłącznie z repo |
| COS-CAND-002 | dwuetapowy audyt rozmowy | candidate_for_v1 | Prompt 1 i Prompt 2 dały komplementarne wyniki | powtórzyć na co najmniej dwóch odmiennych rozmowach |
| COS-CAND-003 | mapa aliasów przed reopenem | candidate_for_v1 | HRM wracał jako kilka nazw | wykryć i zatrzymać co najmniej jeden późniejszy semantic reopen |
| COS-CAND-004 | poziomy dowodu technicznego | candidate_for_v1 | mock i kompilacja były mylone z działaniem | zastosować w realnej zmianie kodu i ocenić koszt |
| COS-CAND-005 | checkpointy zmian protokołu | candidate_for_v1 | jedna rozmowa wygenerowała wiele propozycji reguł | utrzymać stabilny protokół do checkpointu po 3 audytach |
| COS-CAND-006 | budżet czasu protokołu | candidate_for_v1 | brak pomiaru kosztu pierwszej sesji | zmierzyć minimum trzy sesje |
| COS-CAND-007 | walidator spójności statusów | observed | decyzja `proposed` współistniała z obiektem `active` | najpierw potwierdzić, że błąd powtarza się lub ma wysoki koszt |

## Reguła promocji

Pomysł może przejść dalej tylko wtedy, gdy:

1. ma nazwany problem i właściciela;
2. nie jest semantycznym duplikatem bez nowych danych;
3. ma warunek sukcesu;
4. ma minimalny test;
5. mieści się w aktywnym celu i WIP;
6. przeszedł reuse gate;
7. użytkownik zatwierdził jego przeniesienie do kanonicznego `PARKING.md` albo `BACKLOG.md`.

## Reguła usuwania

Na checkpointach usuń lub oznacz jako odrzucone pomysły, które:

- nie mają warunku powrotu;
- nie odpowiadają na powtarzalny problem;
- są tylko nową nazwą istniejącego klastra;
- zostały zastąpione prostszym rozwiązaniem;
- generują większy koszt dokumentacyjny niż potencjalna wartość.
