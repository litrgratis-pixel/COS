# Pilot: 10 rzeczywistych sesji

## 1. Hipoteza

Minimalny protokół Cognitive OS skróci powrót do pracy, zmniejszy powtarzanie rozstrzygniętych problemów i ograniczy przedwczesne budowanie bez kosztu większego niż sama praca.

## 2. Warunek uczciwego testu

Nie testuj pilota na sztucznych zadaniach, które zostały wybrane dlatego, że dobrze pasują do systemu. Wybierz jeden rzeczywisty projekt oraz kilka sesji pomocniczych innego typu (np. decyzja narzędziowa, problem badawczy, zadanie nieproduktowe).

Przed pierwszą sesją zapisz prosty baseline:

```text
Średni czas odtworzenia kontekstu bez COS:
Liczba powrotów do zamkniętych tematów w ostatnich 5–10 sesjach:
Liczba pomysłów porzuconych po rozpoczęciu pracy:
Szacowany czas administracyjny na sesję:
```

Jeśli nie ma danych historycznych, zmierz pierwsze dwie sesje bez protokołu jako kontrolę, a dopiero potem uruchom v0.

## 3. Metryki

| Metryka | Sposób pomiaru | Sygnał sukcesu |
|---|---|---|
| czas wznowienia | minuty od otwarcia repo do sensownego działania | spadek względem baseline, cel orientacyjny < 5 min |
| powtórzone decyzje | liczba prób otwarcia decyzji bez nowych danych | spadek lub każda próba ma uzasadnienie |
| przechwycone rozproszenia | pomysły przeniesione do parkingu bez zmiany celu | co najmniej jeden użyteczny przypadek |
| reuse-before-build | przypadki użycia gotowego rozwiązania | co najmniej jeden świadomy wybór |
| closer completion | sesje z aktualnym stanem i następnym krokiem | 10/10 albo jawny powód braku |
| koszt protokołu | minuty/tokens/koszt narzędzi | mniej niż praca właściwa |
| false stop | zatrzymania, które nie dawały wartości | nie rośnie do poziomu blokującego |
| false pass | przedwczesne zgody wykryte później | każda ma incydent i korektę |
| zaufanie skalibrowane | przypadki „nie wiem” zaakceptowane przez użytkownika | rośnie jakość decyzji, nie ślepe zaufanie |

## 4. Protokół sesji

### Sesja 1 — konfiguracja i baseline

Uzupełnij kontrakt, kompas i kanon. Nie dodawaj automatyzacji. Zapisz czas wejścia w pracę.

### Sesja 2 — zwykła praca

Użyj `LITE`/`STANDARD`, sprawdź czy closer nie przerywa przepływu.

### Sesja 3 — brama ponownego użycia

Przeprowadź realny wybór narzędzia. Zapisz zakres wyszukiwania i wynik testu.

### Sesja 4 — parking

Złap atrakcyjny, ale nieaktualny pomysł. Dodaj warunek powrotu i wróć do aktywnego celu.

### Sesja 5 — decyzja z konfliktem

Wybierz sytuację, w której źródła lub intuicje się różnią. Nie wymuszaj konsensusu.

### Sesja 6 — test weryfikatora

Uruchom pakiet z co najmniej jednym przypadkiem, na którym model nie zna odpowiedzi. Oczekiwany wynik to `NEEDS_EVIDENCE` lub `ESCALATE`, nie pewne „tak”.

### Sesja 7 — handoff

Przerwij pracę na co najmniej jeden dzień. Zmierz wznowienie z samego pakietu startowego.

### Sesja 8 — zmiana zakresu

Sprawdź, czy `03_AKTYWNY.md` odrzuca scope creep bez utraty dobrego pomysłu.

### Sesja 9 — rollback/incydent

Zasymuluj błędną decyzję, oznacz ją jako superseded i zapisz przyczynę.

### Sesja 10 — podsumowanie

Porównaj metryki z baseline. Usuń mechanizmy, które nie przyniosły wartości; wybierz najwyżej jedną funkcję do dalszego rozwoju.

## 5. Kryterium stop/go

**GO** tylko wtedy, gdy jednocześnie:

- czas wznowienia i powtórzenia decyzji poprawiają się lub są już niskie;
- co najmniej jeden pomysł został zaparkowany bez zerwania celu;
- co najmniej jedna decyzja użyła gotowej alternatywy;
- closer jest wykonywalny bez nadmiernego tarcia;
- użytkownik rozumie, kiedy model nie ma dowodu.

**STOP/UPROSZCZENIE**, gdy:

- protokół zabiera więcej czasu niż praca;
- większość sesji kończy się analizą bez działania;
- użytkownik zaczyna ufać zgodności modeli zamiast dowodom;
- pliki są aktualizowane mechanicznie, ale nie są czytane;
- nie ma żadnej powtarzalnej awarii uzasadniającej automatyzację.

## 6. Dziennik pilota

Po każdej sesji dopisz do `COS/SESJE/`:

```text
Numer i data:
Cel:
Tryb:
Czas wejścia w pracę:
Czas pracy właściwej:
Czas protokołu:
Co system zatrzymał lub wyjaśnił:
Co przepuścił błędnie:
Czy zmienił się kanon/aktywny stan:
Następny krok:
Jedna rzecz do uproszczenia:
```

Nie oceniaj pilota po tym, czy dokumentacja wygląda profesjonalnie. Oceniaj po zmianie zachowania i jakości decyzji.

