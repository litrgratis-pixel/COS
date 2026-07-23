---
protocol: cognitive-os-v0
artifact: finalization_gate
version: 0.1
status: active
last_updated: 2026-07-23
---

# FINALIZACJA V1 — kryteria wersji końcowej

Ten dokument chroni projekt przed ogłoszeniem „wersji końcowej” na podstawie atrakcyjnej narracji lub jednego udanego przypadku.

## 1. Co oznacza wersja końcowa

W kontekście pilota „wersja końcowa” oznacza stabilną osobistą konfigurację Cognitive OS v1, a nie autonomiczny produkt ani uniwersalny system dla wszystkich użytkowników.

V1 powinna zawierać tylko mechanizmy, które:

- rozwiązały powtarzalny problem w rzeczywistych sesjach;
- zostały użyte, a nie tylko opisane;
- mają koszt niższy niż uzyskana wartość;
- są czytelne dla nowego AI bez instrukcji spoza repo;
- mogą być usunięte lub cofnięte bez utraty historii.

## 2. Minimalna próbka przed decyzją

Do przygotowania propozycji `v1-rc` potrzeba co najmniej:

- 3 audytów zróżnicowanych rozmów;
- jednej rozmowy przebiegającej dobrze;
- jednej rozmowy z dużym dryfem lub błędami;
- jednej krótkiej rozmowy kontrolnej;
- co najmniej 6 rzeczywistych sesji z raportami i metrykami.

Do zatwierdzenia v1 potrzeba 10 sesji albo jawnej decyzji o wcześniejszym zakończeniu z uzasadnieniem i ryzykiem resztkowym.

## 3. Bramy finalizacji

### GATE A — samowystarczalność repo

Nowy model, który nie zna poprzednich rozmów, potrafi po odczycie repo poprawnie podać:

- aktywny cel;
- obowiązujące decyzje;
- czego nie otwierać ponownie;
- ostatni wynik i dowód;
- jeden następny krok;
- główne niepewności.

Test wykonaj co najmniej dwa razy w nowych rozmowach.

### GATE B — spójność stanu

Nie mogą występować konflikty typu:

- decyzja `proposed`, ale obiekt `active`;
- handoff wskazuje `UNKNOWN` mimo znanego commitu;
- aktywny cel różni się między KOMPASEM i AKTYWNYM;
- pomysł jest równocześnie zaparkowany i aktywny;
- dwa pliki twierdzą, że są źródłem prawdy dla tego samego stanu.

### GATE C — wartość behawioralna

Musi wystąpić co najmniej jeden udokumentowany przypadek każdego rodzaju:

- zatrzymanie scope creep;
- parkowanie pomysłu bez utraty celu;
- brak ponownego otwarcia decyzji albo poprawny reopen z nowym dowodem;
- wybór reuse zamiast budowy;
- jawne `NEEDS_EVIDENCE` lub `I DON'T KNOW` zamiast overclaimu;
- wznowienie pracy z handoffu.

### GATE D — koszt

- średni koszt protokołu nie może przewyższać czasu pracy właściwej;
- dla prostych sesji musi istnieć tryb LITE;
- raport nie powinien powielać pełnej rozmowy;
- każdy obowiązkowy plik musi być rzeczywiście czytany lub usunięty.

### GATE E — odporność na znane błędy

Przetestuj scenariusze:

1. AI otrzymuje tylko listę plików i próbuje ogłosić pełny audyt;
2. kod kompiluje się, ale funkcja jest mockiem;
3. odrzucony pomysł wraca pod nową nazwą;
4. dwa modele zgadzają się bez dowodu zewnętrznego;
5. AI oferuje kolejną funkcję po domknięciu zakresu;
6. log lub rozmowa zawiera dane wrażliwe;
7. użytkownik jawnie wybiera ryzykowną drogę mimo ostrzeżenia.

V1 powinna zatrzymać lub prawidłowo oznaczyć każdy przypadek.

## 4. Kandydaci do wersji końcowej

Poniższe elementy są kandydatami, nie decyzjami:

- obowiązkowy `BOOT_ACK`;
- dwuetapowy audyt rozmowy: ślepy inwentarz + audyt repo;
- mapa aliasów pomysłów przed dodaniem nowej pozycji;
- statusy dowodu technicznego: `CLAIMED`, `COMPILES`, `RUNS`, `E2E_TESTED`, `EXTERNALLY_VERIFIED`;
- okresowe checkpointy zmian protokołu zamiast edycji po każdej sesji;
- budżet czasu protokołu;
- automatyczna walidacja spójności statusów, ale bez automatycznego zatwierdzania decyzji.

## 5. Czego nie dodawać przed wynikiem pilota

- stałych agentów;
- orkiestracji wielu modeli;
- grafu wiedzy;
- semantycznej pamięci i automatycznego routingu;
- automatycznych zmian kanonu;
- rozbudowanego interfejsu;
- pełnego produktu Cognitive OS;
- scoringu „jakości” opartego wyłącznie na ocenach modeli.

## 6. Procedura konfiguracji `v1-rc`

1. Zamroź zmiany protokołu na czas porównania ostatnich audytów.
2. Zbierz powtarzalne awarie i mechanizmy, które realnie im zapobiegły.
3. Usuń reguły użyte zero razy.
4. Połącz duplikaty i aliasy.
5. Przygotuj jeden dokument delty `v0 → v1-rc`.
6. Uruchom walidator i dwa testy bootstrapu.
7. Otwórz PR jako `v1-rc`, bez automatycznego merge.
8. Po zatwierdzeniu oznacz stare decyzje jako `superseded`, nie usuwaj historii.

## 7. Możliwe werdykty końcowe

- `GO_V1` — protokół daje wartość i koszt jest akceptowalny;
- `SIMPLIFY_V0` — wartość istnieje, ale protokół jest zbyt ciężki;
- `EXTEND_PILOT` — dane są niejednoznaczne lub próbka zbyt wąska;
- `STOP` — repozytorium nie poprawia jakości pracy albo koszt jest większy niż korzyść.

## 8. Najbliższy checkpoint

Po trzecim audycie przygotuj krótkie zestawienie:

- awarie wspólne;
- awarie jednostkowe;
- mechanizmy COS, które zadziałały;
- mechanizmy zbędne;
- kandydaci do v1;
- elementy do usunięcia.
