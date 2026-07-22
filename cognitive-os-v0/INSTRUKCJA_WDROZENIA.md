# Instrukcja wdrożenia pakietu Cognitive OS v0

Instrukcja zakłada, że katalog `cognitive-os-v0/` został pobrany lub skopiowany do katalogu roboczego. Nie nadpisuj istniejących plików bez porównania ich treści.

## 1. Przygotowanie

Sprawdź, czy repozytorium ma już podobne katalogi:

```bash
find . -maxdepth 2 -type d \( -name 'COS' -o -name 'cos' -o -name 'SESJE' \) -print
find . -maxdepth 2 -type f | rg 'KOMPAS|KANON|DECYZJE|PARKING|HANDOFF|BRAMA'
```

Jeśli istnieje wcześniejszy system, zachowaj go jako wersję archiwalną lub osobną gałąź. Nie migruj automatycznie całej historii; przenieś tylko decyzje, które mają dowód i aktualny status.

## 2. Skopiowanie plików

Najbezpieczniejszy wariant to osobna gałąź i podgląd kopiowania:

```bash
git switch -c cos-v0
rsync -avn cognitive-os-v0/COS/ ./COS/
rsync -av cognitive-os-v0/COS/ ./COS/
rsync -avn cognitive-os-v0/docs/ ./docs/cognitive-os/
rsync -av cognitive-os-v0/docs/ ./docs/cognitive-os/
rsync -avn cognitive-os-v0/schemas/ ./schemas/cognitive-os/
rsync -av cognitive-os-v0/schemas/ ./schemas/cognitive-os/
rsync -avn cognitive-os-v0/scripts/ ./scripts/cognitive-os/
rsync -av cognitive-os-v0/scripts/ ./scripts/cognitive-os/
```

Jeżeli repo ma własną konwencję, zmień ścieżki, ale nie zmieniaj semantyki plików bez wpisu w `COS/02_KANON.md`.

## 3. Uzupełnienie minimum ręcznie

Przed pierwszą sesją uzupełnij:

1. `COS/00_KONTRAKT_PRACY_Z_AI.md` — tylko faktycznie potwierdzone preferencje; usuń zdania, których nie chcesz przenosić między narzędziami.
2. `COS/01_KOMPAS.md` — jeden cel aktywny, jeden następny krok.
3. `COS/02_KANON.md` — zasady obowiązujące niezależnie od modelu.
4. `COS/03_AKTYWNY.md` — rezultat i Definition of Done bieżącej pracy.
5. `COS/BRAMA_BUDOWANIA.md` — wpis dla pomysłu, jeśli rozważasz budowę.

Nie wpisuj do kanonu hipotez, preferencji modelu ani niezweryfikowanych pomysłów.

## 4. Walidacja lokalna

Walidator nie ocenia prawdziwości treści; sprawdza spójność struktury i obecność bezpieczników:

```bash
python3 cognitive-os-v0/scripts/validate_cos.py ./COS
```

Po skopiowaniu skryptu do repozytorium odpowiednią komendą będzie:

```bash
python3 scripts/cognitive-os/validate_cos.py ./COS
```

W CI uruchamiaj go na każdym pull requeście, ale nie blokuj pracy na ostrzeżeniach dotyczących pustych sekcji eksperymentu. Błędy strukturalne powinny blokować merge.

## 5. Bootstrap nowej sesji

Do nowej rozmowy wklej w tej kolejności:

```text
COS/00_KONTRAKT_PRACY_Z_AI.md
COS/02_KANON.md
COS/01_KOMPAS.md
COS/03_AKTYWNY.md
COS/99_HANDOFF.md
```

Dodaj tylko pliki potrzebne do zadania. Na początku poproś model o krótkie potwierdzenie: aktywny cel, tryb, źródła prawdy, otwarte pytania i jeden następny krok. Nie proś o ponowne streszczenie całej historii.

## 6. Przebieg sesji

1. **Intake:** nazwij rezultat, nie temat rozmowy.
2. **Klasyfikacja:** wybierz `LITE`, `STANDARD` albo `CRITICAL` według `COS/08_PAKIET_WERYFIKACYJNY.md`.
3. **Brama ponownego użycia:** wypełnij sekcję alternatyw przed projektowaniem własnego rozwiązania.
4. **Praca właściwa:** model może proponować warianty, ale każdą istotną tezę oznacza jako fakt, hipotezę, preferencję albo decyzję.
5. **Weryfikacja:** uruchom tylko kontrole wymagane przez stawkę; ogranicz liczbę rund.
6. **Autoryzacja:** człowiek wybiera, odrzuca lub odkłada propozycję. Zapisz powód odstępstwa od werdyktu modelu.
7. **Closer:** wypełnij `COS/09_CLOSER_SESJI.md`; aktualizuj pliki kanoniczne dopiero po zatwierdzeniu.
8. **Handoff:** wygeneruj zwięzły pakiet startowy i sprawdź go względem kanonu.

## 7. Migracja ze starego systemu

| Stary element | Miejsce w v0 | Reguła migracji |
|---|---|---|
| zasada WIP = 1 | `02_KANON.md` | zachowaj jako zasadę, dopisz wyjątki |
| decyzje | `DECYZJE.md` | przenieś z identyfikatorem i źródłem |
| pomysły odłożone | `PARKING.md` | dodaj warunek powrotu i datę przeglądu |
| luźne przyszłe prace | `BACKLOG.md` | bez rozwijania architektury |
| bieżąca praca | `03_AKTYWNY.md` | tylko jeden rezultat |
| notatki sesji | `SESJE/` | zachowaj jako materiał dowodowy, nie jako kanon |
| dawne streszczenia | `99_HANDOFF.md` | traktuj jako snapshot; sprawdź świeżość |

Nie przenoś bez kontroli „prawd o użytkowniku” ani ocen modelu. Umieść je w kontrakcie dopiero po świadomym potwierdzeniu.

## 8. Git i uprawnienia

- Zmiany w `00_KONTRAKT`, `02_KANON`, `DECYZJE` i `99_HANDOFF` rób przez osobny commit/PR.
- Model pracuje na branchu lub generuje patch; nie dostaje bezpośredniego zapisu do kanonu.
- Transkrypcje mogą zawierać dane wrażliwe. Trzymaj je poza repo albo redaguj przed commitem.
- Dodaj `.gitignore` dla sekretów, eksportów narzędzi i surowych danych użytkowników.
- Zachowaj datę, wersję modelu i źródła przy każdej decyzji o istotnej stawce.

## 9. Pilot i kryterium kontynuacji

Uruchom `docs/05_PLAN_PILOTA_10_SESJI.md`. Po dziesięciu rzeczywistych sesjach porównaj czas wznowienia, liczbę powtórzonych decyzji, liczbę zaparkowanych rozproszeń, koszt nadzoru i liczbę korekt po weryfikacji.

Nie dodawaj agentów, grafu wiedzy, wyszukiwania semantycznego ani automatycznego zapisu, jeśli pilot nie pokaże konkretnej awarii, której te elementy naprawiają.

## 10. Wycofanie

Pakiet jest dodatkiem do repo. Jeśli zwiększa tarcie, można go wyłączyć przez zmianę aktywnego celu i zachowanie historii commitów. Nie usuwaj zapisów sesji; oznacz eksperyment jako przerwany wraz z przyczyną. Powrót do poprzedniej gałęzi nie wymaga niszczenia danych.

