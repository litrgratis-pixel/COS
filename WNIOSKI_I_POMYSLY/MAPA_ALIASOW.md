---
protocol: cognitive-os-v0
artifact: idea_alias_map
version: 0.1
status: active
last_updated: 2026-07-23
---

# MAPA ALIASÓW POMYSŁÓW

Celem mapy jest wykrywanie sytuacji, w których wcześniej odrzucony albo zaparkowany kierunek wraca pod atrakcyjniejszą nazwą bez nowych danych.

## Jak używać

Przed uznaniem pomysłu za nowy odpowiedz:

1. Jaki problem ma rozwiązać?
2. Jaki jest mechanizm rozwiązania?
3. Do którego klastra należy?
4. Co jest faktycznie nowe: dane, ograniczenie, technologia czy tylko nazwa?
5. Czy spełniono warunek powrotu istniejącego klastra?

Brak nowych danych oznacza `SEMANTIC_REOPEN`, a nie nową inicjatywę.

## ALIAS-01 — dynamiczne sterowanie modelami i zadaniami

**Problem wspólny:** automatycznie wybrać model, rolę, kolejność albo strategię dla zadania.

**Nazwy wykryte:**

- HRM;
- hierarchical reasoning;
- smart routing;
- smart defaults wybierające chain;
- Chamber of Chains;
- tagged chains;
- AI classifier;
- dynamic chain selection;
- model-role map;
- consensus engine;
- debate mode jako automatyczna droga do finalnego wniosku.

**Status:** parked / poza zakresem pilota.

**Warunek powrotu:** zakończony pilot oraz mierzalny zestaw przypadków, w których ręczny wybór powoduje powtarzalny koszt lub błąd. Potrzebny benchmark jakości, override rate i koszt utrzymania.

## ALIAS-02 — samodoskonalenie i samonaprawa systemu

**Problem wspólny:** system obserwuje swoje działanie i proponuje albo wykonuje poprawki.

**Nazwy wykryte:**

- meta-loop;
- Daily AI Review;
- self-heal;
- selector healing;
- AI Feature Vote;
- self-scan;
- AI-assisted refactoring;
- auto-test & perspective;
- scenario runner oceniany przez LLM;
- autonomous DevOps assistant.

**Status:** parked / poza zakresem pilota.

**Warunek powrotu:** stabilny rdzeń, deterministyczne testy, sandbox, rollback, audyt danych, human approval i udokumentowane awarie ręcznego utrzymania.

## ALIAS-03 — wielomodelowa weryfikacja

**Problem wspólny:** zmniejszyć ryzyko błędu jednego modelu przez użycie kolejnych modeli.

**Nazwy wykryte:**

- AI verifies AI;
- wielu ekspertów;
- debate mode;
- argument–kontrargument–synteza;
- consensus engine;
- model voting;
- independent reviewer bez rzeczywistej niezależności;
- Chamber of Chains jako kontrola jakości.

**Status:** dozwolone wyłącznie jako triangulacja, nie dowód.

**Warunek użycia:** jawny cel, niezależne kryterium, różne źródła lub narzędzia oraz możliwość wyniku `DISAGREEMENT` albo `NEEDS_EVIDENCE`.

## ALIAS-04 — ekspansja produktu przed walidacją rdzenia

**Problem wspólny:** zwiększyć zasięg albo atrakcyjność produktu przed potwierdzeniem podstawowej wartości.

**Nazwy wykryte:**

- open source;
- freemium;
- Stripe;
- enterprise;
- Product Hunt i Hacker News;
- cloud sync;
- shared workspaces;
- mobile app;
- voice input;
- VS Code extension;
- parallel agents;
- specjalizowany produkt pisarski;
- cele typu liczba użytkowników bez baseline.

**Status:** parked.

**Warunek powrotu:** stabilny rdzeń, realne użycie, jasno określony segment i dowód problemu konkretnej grupy.

## ALIAS-05 — greenfield jako ucieczka od złożoności

**Problem wspólny:** rozpocząć od nowa zamiast naprawić lub zrozumieć istniejący system.

**Nazwy wykryte:**

- clean rewrite;
- workspace v2;
- fresh start;
- migration of working logic only;
- clean architecture from scratch;
- zero technical debt reset.

**Status:** wymaga eksperymentu porównawczego.

**Warunek użycia:** zmierzony koszt naprawy, spike migracyjny, lista działającej logiki, test regresji i plan rollbacku.

## ALIAS-06 — „gotowość” bez poziomu dowodu

**Problem wspólny:** opisać szkic, kompilację lub częściowy wynik jako działający system.

**Nazwy i claimy:**

- gotowe pliki;
- działa od razu;
- zero błędów;
- 100% modularności;
- pełna wizja;
- production-ready;
- zero długu;
- prawdziwe chains;
- pełna analiza kodu.

**Status:** zabronione jako niekwalifikowany claim.

**Wymagane oznaczenie:** `CLAIMED`, `COMPILES`, `RUNS_LOCALLY`, `E2E_TESTED` albo `EXTERNALLY_VERIFIED`.

## Historia rozszerzeń mapy

| Data | Audyt | Zmiana |
|---|---|---|
| 2026-07-23 | AUD-2026-001 | utworzono sześć pierwszych klastrów na podstawie rozmowy 4-AI |
