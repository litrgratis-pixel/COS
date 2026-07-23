---
protocol: cognitive-os-v0
type: active_work
id: WORK-2026-07-21-001
status: active
owner: user
created_at: YYYY-MM-DD
---

# AKTYWNY OBIEKT

## Rezultat

Po dziesięciu sesjach mieć dowód, czy minimalny protokół skraca wznowienie pracy, ogranicza powtarzanie decyzji i zatrzymuje przedwczesne budowanie.

## Dlaczego teraz

Kolejne projektowanie systemu bez użycia grozi dokładnie tym dryfem, który system ma ograniczać.

## Zakres

- pliki stanu w `COS/`;
- closer i handoff po każdej sesji;
- brama ponownego użycia dla co najmniej jednego wyboru narzędzia;
- pomiar czasu, kosztu i błędów weryfikacji.

## Czego nie dodajemy

- stałych agentów;
- automatycznych commitów do kanonu;
- pamięci semantycznej;
- rozbudowy produktu przed wynikami pilota.

## Definicja ukończenia (Definition of Done)

- [ ] przeprowadzono 10 sesji na rzeczywistej pracy;
- [ ] zapisano baseline i metryki końcowe;
- [ ] co najmniej jeden pomysł zaparkowano z warunkiem powrotu;
- [ ] co najmniej raz wybrano gotowe rozwiązanie zamiast budowy;
- [ ] każda sesja ma closer i jeden następny krok;
- [ ] koszt protokołu był mniejszy niż koszt pracy właściwej.

## Najwyżej trzy otwarte pytania

1. Jaki jeden rzeczywisty projekt jest celem pilota?
2. Jak zmierzymy baseline bez protokołu?
3. Kto zatwierdza decyzje w trybie CRITICAL?

## Ryzyka i blokady

- Ryzyko zbyt dużego tarcia / czas protokołu > czas pracy / użytkownik

## Jeden następny krok

Zmierz baseline i wpisz wynik do pierwszego pliku sesji.

## Warunek zamknięcia lub zaparkowania

Po dziesięciu sesjach, albo wcześniej tylko po jawnej decyzji o przerwaniu pilota.
