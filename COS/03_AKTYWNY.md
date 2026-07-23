---
protocol: cognitive-os-v0
type: active_work
id: WORK-2026-07-21-001
status: active
owner: user
created_at: 2026-07-21
last_updated: 2026-07-23
---

# AKTYWNY OBIEKT

## Rezultat

Po dziesięciu rzeczywistych sesjach mieć dowód, czy minimalny protokół skraca wznowienie pracy, ogranicza powtarzanie decyzji i zatrzymuje przedwczesne budowanie, a następnie skonfigurować najmniejszą końcową wersję COS opartą na wynikach, nie na jednej atrakcyjnej teorii.

## Dlaczego teraz

Pierwszy audyt pokazał, że duża rozmowa może zawierać jednocześnie wartościowe obserwacje, pseudo-decyzje, semantic reopen, scope creep i mock przedstawiony jako działanie. Kolejne projektowanie systemu bez porównania kilku rozmów grozi dokładnie tym dryfem, który system ma ograniczać.

## Zakres

- pliki stanu w `COS/`;
- samowystarczalny bootstrap i metodologia w `PILOT/`;
- seria zróżnicowanych audytów rozmów;
- closer i handoff po każdej sesji zmieniającej stan;
- rejestr błędów, aliasów pomysłów i mechanizmów zapobiegawczych;
- brama ponownego użycia dla co najmniej jednego wyboru narzędzia;
- pomiar czasu, kosztu, false pass, false stop i błędów weryfikacji;
- checkpointy po 3, 6 i 10 sesjach;
- propozycja `v1-rc` dopiero po spełnieniu kryteriów z `PILOT/FINALIZACJA_V1.md`.

## Czego nie dodajemy

- stałych agentów;
- automatycznych commitów do kanonu;
- pamięci semantycznej;
- wielomodelowej orkiestracji jako produktu;
- rozbudowy interfejsu;
- automatycznego publikowania surowych rozmów lub logów;
- kolejnych reguł po każdym pojedynczym odkryciu, poza bezpieczeństwem i utratą danych;
- wersji v1 przed zebraniem porównywalnych wyników.

## Definicja ukończenia (Definition of Done)

- [ ] przeprowadzono 10 rzeczywistych sesji;
- [x] aktywowano pilot decyzją użytkownika;
- [x] wykonano pierwszy audyt rozmowy i zapisano jakościowy baseline;
- [x] repo zawiera samowystarczalny bootstrap dla nowego AI;
- [ ] przeprowadzono co najmniej 3 zróżnicowane audyty rozmów;
- [ ] co najmniej jedna rozmowa kontrolna była krótka i przebiegała dobrze;
- [ ] zapisano czas bootstrapu, analizy i protokołu dla minimum 3 sesji;
- [ ] co najmniej jeden pomysł zaparkowano z warunkiem powrotu;
- [ ] co najmniej raz wybrano gotowe rozwiązanie zamiast budowy;
- [ ] przetestowano handoff po co najmniej jednodniowej przerwie;
- [ ] sprawdzono mapę aliasów na późniejszym semantic reopen;
- [ ] każda sesja ma closer albo jawny `NO_STATE_CHANGE`;
- [ ] koszt protokołu był mniejszy niż koszt pracy właściwej;
- [ ] przygotowano decyzję `GO_V1`, `SIMPLIFY_V0`, `EXTEND_PILOT` albo `STOP`.

## Najwyżej trzy otwarte pytania

1. Jaki jest koszt protokołu w krótkiej, prostej rozmowie?
2. Które awarie powtarzają się w różnych domenach, a które są specyficzne dla 4-AI Lab?
3. Które elementy obecnego protokołu można usunąć bez utraty wartości?

## Ryzyka i blokady

- protokół może zabierać więcej czasu niż praca właściwa;
- wybór głównie problematycznych rozmów może zawyżyć ocenę wartości COS;
- katalog wiedzy może zacząć dublować kanoniczny stan;
- każda nowa obserwacja może kusić do dodania kolejnej reguły;
- surowe rozmowy mogą zawierać dane wrażliwe;
- finalizacja może zostać ogłoszona przed pomiarem wznowienia i kosztu.

## Jeden następny krok

Wybrać krótszą rozmowę o jasno określonym rezultacie, wykonać audyt według `PILOT/SZABLON_AUDYTU_ROZMOWY.md` i zmierzyć trzy czasy: bootstrap, analiza, protokół.

## Warunek zamknięcia lub zaparkowania

Po dziesięciu sesjach i decyzji końcowej, albo wcześniej wyłącznie po jawnej decyzji użytkownika z uzasadnieniem, metrykami i ryzykiem resztkowym.
