# Cognitive OS v0 — pakiet protokołu pracy z AI

Ten katalog jest gotowym do skopiowania pakietem startowym wynikającym z analizy załączonej rozmowy. Nie jest „gotowym Cognitive OS” ani autonomicznym systemem podejmowania decyzji. Jest małym, przenośnym protokołem, który ma sprawdzić jedną hipotezę:

> Czy jawny stan projektu, brama ponownego użycia, adaptacyjny nadzór i obowiązkowa destylacja sesji pozwalają szybciej i bezpieczniej pracować z różnymi modelami AI?

## Werdykt w jednym akapicie

Rozmowa trafnie rozpoznała problem: model generuje, a człowiek zostaje jednocześnie właścicielem celu, recenzentem, ekspertem, kontrolerem zakresu i archiwistą. Trafnie też zaproponowała rozdzielenie rozmowy (procesor) i repozytorium (stan). Niedopracowane pozostaje „AI weryfikuje AI”: drugi model nie jest automatycznie niezależnym ani prawdziwym arbitrem. W tym pakiecie weryfikacja oznacza triangulację dowodów, kontradyktoryjny atak, testy możliwe do odtworzenia, jawne granice pewności oraz autoryzację człowieka dla decyzji o istotnej stawce.

## Co należy skopiować do właściwego repozytorium

- `COS/` — minimalny stan operacyjny i szablony plików sterujących;
- `docs/` — analiza, luki, specyfikacja pętli weryfikacyjnej, architektura i plan pilota;
- `schemas/` — opcjonalne kontrakty maszynowe dla walidatora;
- `scripts/validate_cos.py` — lokalna kontrola spójności bez wywoływania modelu;
- `INSTRUKCJA_WDROZENIA.md` — kolejność wdrożenia i migracji.

## Najkrótszy model działania

```text
intake → klasyfikacja stawki → sprawdzenie ponownego użycia
       → propozycje → niezależny atak i dowody → decyzja człowieka
       → patch/eksperyment → closer → aktualizacja kanonu i handoff
```

Pętla nie ma obowiązku uruchamiać wszystkich kroków przy każdym pytaniu. Ma obowiązek dobrać głębokość do stawki i zatrzymać się po osiągnięciu kryterium zakończenia.

## Niezbywalne reguły v0

1. **Nie buduj przed sprawdzeniem ponownego użycia.** Brak znalezionego rozwiązania oznacza „nie znaleziono w określonym zakresie”, a nie „nie istnieje”.
2. **Weryfikator nie jest wyrocznią.** Wysoka zgodność dwóch modeli nie zastępuje dowodu ani eksperta domenowego.
3. **Żadna sugestia modelu nie zmienia kanonu samoczynnie.** Model przygotowuje propozycję/patch; człowiek zatwierdza zmianę.
4. **Decyzja musi być typowana i odwracalna, jeśli to możliwe.** Zapisujemy powód, dowody, warunek ponownego otwarcia i ryzyko resztkowe.
5. **Każda sesja kończy się zmianą stanu albo jawnym „brak zmiany”.** Samo streszczenie rozmowy nie jest closerem.
6. **Brak dowodu = jawna niepewność.** Nie wolno zamieniać niewiedzy w pewne „tak/nie”.
7. **Koszt nadzoru jest metryką.** Jeśli protokół zabiera więcej czasu niż praca, upraszczamy go przed dodaniem funkcji.

## Zalecana kolejność czytania

1. `INSTRUKCJA_WDROZENIA.md`
2. `docs/01_ANALIZA_WNIKLIWA.md`
3. `docs/02_LUKI_RYZYKA_I_NIEDOPOWIEDZENIA.md`
4. `docs/03_AI_WERYFIKUJE_AI.md`
5. pliki w `COS/`
6. `docs/05_PLAN_PILOTA_10_SESJI.md`
7. `docs/08_FAJNIE_WYMYSLONE_ALE_WDROZ_INACZEJ.md`

## Zakres i ograniczenia

Pakiet jest przeznaczony do osobistej pracy projektowej i decyzji o niskiej/średniej stawce. Nie zastępuje porady prawnej, medycznej, finansowej, bezpieczeństwa ani przeglądu eksperta. Dla takich zastosowań tryb `CRITICAL` musi wymagać właściwego człowieka lub formalnego procesu.

## Źródła zewnętrzne

Argumentacja o ograniczeniach oceniania przez modele odwołuje się do prac i wytycznych wymienionych w `docs/03_AI_WERYFIKUJE_AI.md`. Linki są zapisane w plikach, aby repozytorium zachowało pochodzenie założeń.
