# Cognitive OS v0 — pakiet protokołu pracy z AI

To repozytorium jest kanonicznym pakietem Cognitive OS v0 i aktywnym środowiskiem pilota. Nie jest autonomicznym systemem podejmowania decyzji. Jest małym, przenośnym protokołem, który ma sprawdzić jedną hipotezę:

> Czy jawny stan projektu, brama ponownego użycia, adaptacyjny nadzór i obowiązkowa destylacja sesji pozwalają szybciej i bezpieczniej pracować z różnymi modelami AI?

Cała wiedza potrzebna do działania projektu ma znajdować się w tym repozytorium. Nowy model nie powinien zależeć od instrukcji wprowadzającej przechowywanej wyłącznie w rozmowie.

## Werdykt w jednym akapicie

Rozmowa trafnie rozpoznała problem: model generuje, a człowiek zostaje jednocześnie właścicielem celu, recenzentem, ekspertem, kontrolerem zakresu i archiwistą. Trafnie też zaproponowała rozdzielenie rozmowy (procesor) i repozytorium (stan). Niedopracowane pozostaje „AI weryfikuje AI”: drugi model nie jest automatycznie niezależnym ani prawdziwym arbitrem. W tym pakiecie weryfikacja oznacza triangulację dowodów, kontradyktoryjny atak, testy możliwe do odtworzenia, jawne granice pewności oraz autoryzację człowieka dla decyzji o istotnej stawce.

## Struktura repozytorium

- `COS/` — kanoniczny stan operacyjny, decyzje, incydenty, parking, handoff i raporty sesji;
- `PILOT/` — samowystarczalna instrukcja eksperymentu, rejestr rozmów, metryki, audyty, szablon i kryteria finalizacji;
- `WNIOSKI_I_POMYSLY/` — przekrojowe lekcje, mapa aliasów, antywzorce, bramy i niekanoniczne zestawienie pomysłów;
- `docs/` — analiza, luki, specyfikacja pętli weryfikacyjnej, architektura i plan pilota;
- `schemas/` — opcjonalne kontrakty maszynowe dla walidatora;
- `scripts/validate_cos.py` — lokalna kontrola spójności bez wywoływania modelu;
- `templates/` — prompty robocze, closer i niezależny reviewer;
- `INSTRUKCJA_WDROZENIA.md` — kolejność wdrożenia i migracji.

Gałąź `main` jest źródłem prawdy dla Cognitive OS. Poprzedni projekt scenariuszowy jest zachowany w gałęzi `archive/creative-os-v1`.

## Bootstrap nowego AI

Model rozpoczynający pracę bez wcześniejszego kontekstu musi najpierw przeczytać `PILOT/README.md` i wykonać opisany tam `BOOT_ACK`.

Minimalna kolejność:

1. `README.md`;
2. `PILOT/README.md`;
3. `COS/00_KONTRAKT_PRACY_Z_AI.md`;
4. `COS/01_KOMPAS.md`;
5. `COS/02_KANON.md`;
6. `COS/03_AKTYWNY.md`;
7. `COS/DECYZJE.md`;
8. `COS/99_HANDOFF.md`;
9. ostatni raport w `COS/SESJE/`;
10. `PILOT/REJESTR_ROZMOW.md` i `PILOT/METRYKI.md`.

## Najkrótszy model działania

```text
intake → klasyfikacja stawki → sprawdzenie ponownego użycia
       → propozycje → niezależny atak i dowody → decyzja człowieka
       → patch/eksperyment → closer → aktualizacja kanonu i handoff
```

Pętla nie ma obowiązku uruchamiać wszystkich kroków przy każdym pytaniu. Ma obowiązek dobrać głębokość do stawki i zatrzymać się po osiągnięciu kryterium zakończenia.

Dla audytu rozmów obowiązuje dodatkowo:

```text
ślepy inwentarz → audyt względem repo → delta → decyzja człowieka → zapis stanu
```

## Niezbywalne reguły v0

1. **Nie buduj przed sprawdzeniem ponownego użycia.** Brak znalezionego rozwiązania oznacza „nie znaleziono w określonym zakresie”, a nie „nie istnieje”.
2. **Weryfikator nie jest wyrocznią.** Wysoka zgodność dwóch modeli nie zastępuje dowodu ani eksperta domenowego.
3. **Żadna sugestia modelu nie zmienia kanonu samoczynnie.** Model przygotowuje propozycję/patch; człowiek zatwierdza zmianę.
4. **Decyzja musi być typowana i odwracalna, jeśli to możliwe.** Zapisujemy powód, dowody, warunek ponownego otwarcia i ryzyko resztkowe.
5. **Każda sesja kończy się zmianą stanu albo jawnym „brak zmiany”.** Samo streszczenie rozmowy nie jest closerem.
6. **Brak dowodu = jawna niepewność.** Nie wolno zamieniać niewiedzy w pewne „tak/nie”.
7. **Koszt nadzoru jest metryką.** Jeśli protokół zabiera więcej czasu niż praca, upraszczamy go przed dodaniem funkcji.
8. **Nowa nazwa nie jest nowym dowodem.** Przed reopenem sprawdzamy `WNIOSKI_I_POMYSLY/MAPA_ALIASOW.md`.
9. **Surowa rozmowa nie jest domyślnym artefaktem publicznym.** W repo trafia zredagowany audyt i niezbędny ślad dowodowy.
10. **Protokół zmieniamy na checkpointach.** Nie dodajemy reguły po każdym pojedynczym odkryciu, poza bezpieczeństwem i utratą danych.

## Zalecana kolejność czytania

### Do rozpoczęcia pracy

1. `PILOT/README.md`
2. pliki stanu w `COS/`
3. ostatni raport w `COS/SESJE/`
4. `PILOT/REJESTR_ROZMOW.md`

### Do zrozumienia projektu

1. `INSTRUKCJA_WDROZENIA.md`
2. `docs/01_ANALIZA_WNIKLIWA.md`
3. `docs/02_LUKI_RYZYKA_I_NIEDOPOWIEDZENIA.md`
4. `docs/03_AI_WERYFIKUJE_AI.md`
5. `docs/05_PLAN_PILOTA_10_SESJI.md`
6. `PILOT/FINALIZACJA_V1.md`
7. `WNIOSKI_I_POMYSLY/README.md`

## Aktualny stan pilota

- pilot jest aktywny;
- zakończono pierwszy audyt: `PILOT/AUDYTY/AUD-2026-001_4AI.md`;
- raport sesji: `COS/SESJE/2026-07-23-001.md`;
- następny krok: krótsza rozmowa kontrolna z pomiarem czasu;
- wersja końcowa nie jest jeszcze zatwierdzona.

## Zakres i ograniczenia

Pakiet jest przeznaczony do osobistej pracy projektowej i decyzji o niskiej/średniej stawce. Nie zastępuje porady prawnej, medycznej, finansowej, bezpieczeństwa ani przeglądu eksperta. Dla takich zastosowań tryb `CRITICAL` musi wymagać właściwego człowieka lub formalnego procesu.

## Źródła zewnętrzne

Argumentacja o ograniczeniach oceniania przez modele odwołuje się do prac i wytycznych wymienionych w `docs/03_AI_WERYFIKUJE_AI.md`. Linki są zapisane w plikach, aby repozytorium zachowało pochodzenie założeń.
