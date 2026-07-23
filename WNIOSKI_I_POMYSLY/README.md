---
protocol: cognitive-os-v0
artifact: lessons_and_ideas_index
version: 0.1
status: active
last_updated: 2026-07-23
---

# WNIOSKI I POMYSŁY

Ten katalog przechowuje wiedzę przekrojową z eksperymentów: powtarzalne błędy, aliasy pomysłów, mechanizmy zapobiegawcze i kierunki do ewentualnego powrotu.

## Ważne: ten katalog nie zmienia stanu samodzielnie

- Kanoniczne decyzje są w `COS/DECYZJE.md`.
- Aktywny rezultat jest w `COS/03_AKTYWNY.md`.
- Pomysły formalnie zaparkowane są w `COS/PARKING.md`.
- Zadania gotowe do działania są w `COS/BACKLOG.md`.
- Rzeczywiste błędne przepuszczenia i fałszywe zatrzymania są w `COS/INCYDENTY.md`.

Wpis w tym katalogu jest mapą wiedzy albo kandydatem. Nie jest decyzją, backlogiem ani zgodą na budowę.

## Pliki

- `MAPA_ALIASOW.md` — grupuje różne nazwy tego samego problemu lub pomysłu;
- `ANTYWZORCE_I_BRAMY.md` — opisuje błędy i minimalne mechanizmy zapobiegawcze;
- `POMYSLY.md` — zestawia kierunki wykryte w rozmowach wraz z warunkiem powrotu.

## Procedura przed dodaniem nowego pomysłu

1. Sprawdź `MAPA_ALIASOW.md`.
2. Nazwij problem, nie rozwiązanie.
3. Wskaż nowe dane, których nie było przy wcześniejszym odrzuceniu.
4. Sprawdź aktywny cel i WIP.
5. Sprawdź gotowe rozwiązania.
6. Wybierz: odrzuć, połącz z istniejącym klastrem, zaparkuj, dodaj do backlogu albo eskaluj.
7. Nie rozwijaj architektury pomysłu, jeżeli nie przeszedł bramy aktywacji.

## Reguła semantycznego duplikatu

Dwa pomysły są duplikatami, jeżeli rozwiązują ten sam problem podobnym mechanizmem, nawet gdy mają inne nazwy, modele, interfejs lub metaforę.

Przykład:

```text
HRM → smart routing → Chamber of Chains → AI classifier → consensus engine
```

Nowa nazwa nie jest nowym dowodem.

## Reguła uczenia się z błędu

Błąd uważa się za obsłużony dopiero, gdy istnieją:

1. opis incydentu;
2. przyczyna źródłowa;
3. brama lub test zapobiegawczy;
4. co najmniej jeden późniejszy przypadek, w którym mechanizm zadziałał;
5. warunek usunięcia reguły, jeżeli generuje zbyt wiele false stop.

## Następny krok

Przy każdym kolejnym audycie dopisz tylko nowe klastry albo nowy dowód. Nie przepisuj całej rozmowy do tego katalogu.
