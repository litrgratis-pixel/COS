---
protocol: cognitive-os-v0
artifact: failure_patterns_and_gates
version: 0.1
status: active
last_updated: 2026-07-23
---

# ANTYWZORCE I BRAMY ZAPOBIEGAWCZE

Każda brama ma zatrzymywać konkretny, zaobserwowany błąd. Brama bez późniejszego przykładu użycia jest tylko teorią i może zostać usunięta podczas finalizacji.

## 1. Pełna analiza bez pełnego źródła

**Antywzorzec:** model ogłasza pełną diagnozę repozytorium po otrzymaniu listy plików, nazw, rozmiarów albo kilku fragmentów.

**Sygnały językowe:** „to wystarczy”, „pełna wizja”, „znam całą architekturę”, „pełna analiza kodu”.

**Brama:**

```text
SOURCE_COVERAGE: full | partial | metadata_only | summary_only
FILES_READ:
FILES_NOT_READ:
CLAIMS_OUTSIDE_COVERAGE:
```

Przy `metadata_only` wolno opisać strukturę i pytania do audytu, ale nie działanie kodu.

## 2. Szkic lub kompilacja przedstawione jako działająca funkcja

**Antywzorzec:** wygenerowane pliki, mock albo kompilujący się szkielet otrzymują etykietę „gotowe” lub „działa”.

**Brama dowodowa:**

- `CLAIMED` — tylko deklaracja;
- `COMPILES` — kompilacja zakończona;
- `RUNS_LOCALLY` — uruchomienie w środowisku;
- `E2E_TESTED` — sprawdzono oczekiwany przepływ;
- `EXTERNALLY_VERIFIED` — niezależny test lub źródło.

Nie wolno przeskakiwać poziomów bez wskazania artefaktu.

## 3. Semantic reopen

**Antywzorzec:** odrzucony kierunek wraca pod nową nazwą, metaforą albo zestawem modeli.

**Brama:** przed rozwinięciem pomysłu sprawdź `MAPA_ALIASOW.md` i podaj:

```text
EXISTING_CLUSTER:
OLD_DECISION_OR_PARKING:
NEW_EVIDENCE:
REOPEN_CONDITION_MET: YES | NO
```

`NO` oznacza powrót do aktywnego celu albo parking, nie nową architekturę.

## 4. Oferta kolejnej funkcji po domknięciu zakresu

**Antywzorzec:** AI pyta „czy zamykamy?”, a następnie samo proponuje następny moduł.

**Brama końca:** po spełnieniu Definition of Done model może zaproponować wyłącznie:

- test;
- closer;
- parking;
- następny krok zgodny z KOMPASEM;
- `NO_STATE_CHANGE`.

Nowe funkcje są zakazane w tej samej odpowiedzi, chyba że użytkownik jawnie otwiera nowy zakres.

## 5. Greenfield bez porównania

**Antywzorzec:** czysty rewrite jest rekomendowany jako szybszy i bezpieczniejszy bez pomiaru działającej logiki i kosztu migracji.

**Brama:** wymagaj małego eksperymentu porównawczego:

- jedna funkcja naprawiona w istniejącym systemie;
- ta sama funkcja odtworzona w spike'u greenfield;
- czas, regresje, ryzyko, rollback;
- decyzja dopiero po wyniku.

## 6. Zgodność modeli jako dowód

**Antywzorzec:** debate, voting albo synteza wielu modeli jest przedstawiana jako prawda lub niezależna ekspertyza.

**Brama:** określ niezależność:

- inne źródło;
- inne narzędzie;
- inny kontekst;
- test deterministyczny;
- ekspert domenowy.

Jeżeli modele bazują na tej samej rozmowie bez nowych dowodów, wynik to triangulacja opinii, nie weryfikacja.

## 7. Rekomendacja narzędzia lub modelu bez benchmarku

**Antywzorzec:** modelom przypisuje się role typu creative, coding, verify na podstawie reputacji lub stylu odpowiedzi.

**Brama:** porównaj kandydatów na reprezentatywnych zadaniach i zapisz:

- kryterium;
- próbkę;
- koszt;
- jakość;
- odsetek ręcznych override;
- ograniczenia.

Bez testu przypisanie jest `HYPOTHESIS`.

## 8. Prywatne logi jako paliwo dla automatyzacji

**Antywzorzec:** pełne prompty i logi są automatycznie wysyłane do wielu modeli albo zapisywane bez klasyfikacji.

**Brama danych:** przed użyciem logów wymagaj:

- minimalizacji;
- redakcji;
- zgody;
- listy dostawców;
- retencji;
- polityki usunięcia;
- testu, czy mniejszy zakres danych wystarcza.

## 9. Rozbudowa protokołu po jednym przypadku

**Antywzorzec:** każda sesja dodaje nową regułę, plik albo status.

**Brama checkpointu:**

- bezpieczeństwo i utrata danych: popraw natychmiast;
- pozostałe obserwacje: zbieraj do checkpointu po 3, 6 i 10 sesjach;
- nowa reguła wymaga powtórzenia problemu albo bardzo wysokiego kosztu pojedynczego incydentu;
- każda nowa reguła musi mieć warunek usunięcia.

## 10. Dokumentacja bez użycia

**Antywzorzec:** pliki są aktualizowane, ale modele ich nie czytają, a użytkownik nadal wkleja instrukcje ręcznie.

**Brama bootstrapu:** nowe AI musi wykonać `BOOT_ACK` wyłącznie z repo. Jeżeli nie potrafi, popraw nawigację albo usuń martwe dokumenty.

## 11. Zatrzymanie bez wartości

**Antywzorzec:** protokół blokuje prostą, odwracalną pracę przez nadmierną formalizację.

**Brama proporcjonalności:**

- `LITE` dla niskiej stawki;
- `STANDARD` dla decyzji projektowych;
- `CRITICAL` dla wysokiej stawki;
- false stop zapisuj w `COS/INCYDENTY.md`;
- uprość regułę, jeżeli koszt powtarza się bez wykrywania ryzyka.

## Test skuteczności bramy

Dla każdej bramy prowadź minimalny zapis:

| Brama | Incydent źródłowy | Późniejszy przypadek | Zadziałała? | Koszt | Decyzja |
|---|---|---|---|---|---|
| SOURCE_COVERAGE | INC-2026-001 | — | UNKNOWN | UNKNOWN | testować w następnych audytach |
| poziomy dowodu | INC-2026-002 | — | UNKNOWN | UNKNOWN | kandydat do v1 |
| semantic reopen | INC-2026-003 | — | UNKNOWN | UNKNOWN | testować z mapą aliasów |
