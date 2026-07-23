---
protocol: cognitive-os-v0
artifact: pilot_bootstrap
version: 0.1
status: active
last_updated: 2026-07-23
---

# PILOT — samowystarczalna instrukcja eksperymentu Cognitive OS

Ten katalog ma wystarczyć do rozpoczęcia pracy przez dowolny model AI, nawet jeżeli model nie zna instrukcji projektu, wcześniejszych rozmów ani kontekstu użytkownika.

## 1. Cel pilota

Sprawdzić na rzeczywistych rozmowach i sesjach pracy, czy Cognitive OS:

1. skraca czas odzyskania kontekstu;
2. odróżnia fakty, hipotezy, rekomendacje i decyzje;
3. wykrywa ponowne otwieranie decyzji bez nowych danych;
4. zatrzymuje przedwczesne budowanie i rozrost zakresu;
5. zachowuje wartościowe pomysły bez zmiany aktywnego celu;
6. kończy sesję użytecznym stanem, a nie tylko streszczeniem;
7. dostarcza danych potrzebnych do skonfigurowania końcowej wersji protokołu.

Pilot jest aktywny. Wynikiem pilota nie jest maksymalnie rozbudowany system. Wynikiem ma być najmniejsza wersja protokołu, która przynosi mierzalną wartość.

## 2. Źródło prawdy i hierarchia

Gałąź `main` repozytorium `litrgratis-pixel/COS` jest źródłem prawdy.

W przypadku konfliktu obowiązuje kolejność:

1. `COS/02_KANON.md`;
2. aktywne wpisy w `COS/DECYZJE.md`;
3. `COS/03_AKTYWNY.md`;
4. `COS/01_KOMPAS.md`;
5. `COS/PARKING.md` i `COS/BACKLOG.md`;
6. `COS/99_HANDOFF.md`;
7. zaakceptowane raporty sesji w `COS/SESJE/`;
8. dokumentacja w `PILOT/`, `docs/` i `WNIOSKI_I_POMYSLY/`;
9. rozmowy źródłowe i odpowiedzi modeli.

Rozmowa jest materiałem. Nie jest kanonem ani automatycznie obowiązującym zbiorem decyzji.

## 3. Obowiązkowy bootstrap każdego AI

Przed analizą lub zmianą stanu odczytaj:

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

Następnie podaj:

```text
BOOT_ACK
repozytorium:
gałąź:
commit bazowy:
aktywne decyzje:
aktywny rezultat:
tryb: READ_ONLY | PROPOSAL | WRITE_APPROVED
jeden następny krok:
niepewności:
```

Brak `BOOT_ACK` oznacza, że model nie potwierdził źródeł i nie powinien zmieniać stanu.

## 4. Domyślny tryb bezpieczeństwa

Każda analiza rozpoczyna się jako `READ_ONLY`.

Model nie tworzy gałęzi, commitów, pull requestów ani zmian w plikach stanu, dopóki użytkownik nie zatwierdzi konkretnego zakresu zapisu. Zgoda na audyt nie jest automatycznie zgodą na zmianę kanonu.

Kod, dokument lub konfiguracja bez testu otrzymuje status `PROPOSAL`, a nie `WORKING`.

## 5. Standard analizy rozmowy

Każda rozmowa przechodzi pięć etapów.

### Etap A — ślepy inwentarz

Analizuj rozmowę bez dopasowywania jej do teorii COS. Przygotuj:

- mapę tematów;
- chronologię zmian kierunku;
- jawne decyzje użytkownika;
- propozycje AI błędnie brzmiące jak decyzje lub fakty;
- odrzucone kierunki;
- sprzeczności i ponowne otwarcia;
- kandydatów do parkingu;
- twierdzenia wymagające cross-checku;
- miejsca, w których AI rozwijało kierunek bez dowodu.

### Etap B — audyt względem repozytorium

Porównaj inwentarz z aktualnym `main`. Dla każdego istotnego punktu wskaż:

- fragment lub lokalizację w materiale;
- powiązany plik repozytorium;
- typ: `FACT`, `HYPOTHESIS`, `PREFERENCE`, `RECOMMENDATION`, `DECISION`, `PROPOSAL`;
- zgodność lub konflikt ze stanem COS;
- brakujące dowody.

### Etap C — delta

Przygotuj wyłącznie różnice, których obecny COS jeszcze nie obsługuje. Nie proponuj nowej reguły, jeżeli istniejąca reguła już zatrzymuje problem.

Każda propozycja musi mieć:

```text
ID:
plik docelowy:
treść zmiany:
dowód:
powód:
ryzyko i koszt:
warunek usunięcia lub cofnięcia:
status: PROPOSAL
```

### Etap D — decyzja człowieka

Użytkownik wybiera: `accept`, `reject`, `park`, `escalate` albo `no_state_change`.

### Etap E — zapis stanu

Dopiero po decyzji:

- aktualizuj właściwy plik w `COS/`;
- utwórz raport sesji w `COS/SESJE/`;
- zaktualizuj `COS/99_HANDOFF.md`;
- wykonaj walidację;
- przygotuj osobną gałąź i pull request.

## 6. Wymagane artefakty dla każdej rozmowy

Każda analizowana rozmowa powinna mieć:

1. wpis w `PILOT/REJESTR_ROZMOW.md`;
2. raport audytowy w `PILOT/AUDYTY/`;
3. raport sesji w `COS/SESJE/`, jeżeli analiza zmieniła stan lub dostarczyła metryki pilota;
4. wpis w `COS/INCYDENTY.md`, jeżeli wykryto fałszywe przepuszczenie, fałszywe zatrzymanie, konflikt źródeł lub koszt bez wartości;
5. aktualizację `PILOT/METRYKI.md`;
6. `STATE_CHANGE` albo `NO_STATE_CHANGE`.

## 7. Zasady doboru rozmów

Nie wybieraj wyłącznie rozmów, które potwierdzają wartość COS. Zestaw pilota powinien obejmować:

- co najmniej jedną rozmowę techniczną;
- co najmniej jedną rozmowę twórczą lub strategiczną;
- co najmniej jedną rozmowę, która przebiegła dobrze;
- co najmniej jedną rozmowę z błędami lub dużym dryfem;
- co najmniej jedną krótką rozmowę, aby sprawdzić koszt protokołu.

Pierwszy checkpoint wykonaj po 3 audytach, drugi po 6, końcowy po 10 sesjach.

## 8. Metryki obowiązkowe

Mierz przynajmniej:

- czas bootstrapu;
- czas analizy właściwej;
- czas obsługi protokołu;
- liczbę jawnych decyzji;
- liczbę pozornych decyzji lub overclaimów;
- liczbę reopenów bez nowych danych;
- liczbę semantycznych duplikatów pomysłów;
- liczbę propozycji odrzuconych, zaparkowanych i przyjętych;
- false stop i false pass;
- liczbę zmian protokołu wynikających z jednej sesji.

Nie zmieniaj protokołu po każdym pojedynczym odkryciu. Zmiany grupuj na checkpointach, chyba że wystąpi ryzyko bezpieczeństwa lub utraty danych.

## 9. Prywatność i dane

Nie zapisuj w publicznym repo surowych rozmów, sekretów, danych osobowych, tokenów ani pełnych logów bez redakcji i świadomej zgody.

W repo przechowuj:

- identyfikator materiału;
- zakres i typ rozmowy;
- zredagowane cytaty lub lokalizacje;
- wnioski i dowody potrzebne do audytu;
- opcjonalnie hash materiału źródłowego.

## 10. Warunek finalizacji

Nie ogłaszaj wersji końcowej na podstawie jednego udanego audytu. Kryteria są zapisane w `PILOT/FINALIZACJA_V1.md`.

Wersja końcowa ma usuwać zbędne mechanizmy, a nie tylko dodawać nowe.

## 11. Jeden następny krok

Przeanalizować następną, odmienną rozmowę przy użyciu tego samego dwuetapowego standardu i porównać wyniki z audytem `AUD-2026-001`.
