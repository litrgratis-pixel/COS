# Luki, ryzyka i niedopowiedzenia

Poniższa lista jest celowo ostra. Nie oznacza, że pomysł jest zły; wskazuje miejsca, w których atrakcyjna narracja może dać fałszywe poczucie, że problem został rozwiązany.

| Priorytet | Luka / ryzyko | Co może pójść źle | Kontrola w v0 | Test akceptacyjny |
|---|---|---|---|---|
| P0 | Model ocenia własny błąd | dwa podobne modele powtarzają tę samą halucynację | niezależność, referencja/test, eskalacja | dla 10 znanych przypadków system nie może uznać braku dowodu za fakt |
| P0 | Brak rozdzielenia prawdy od spójności | spójny plan zostaje uznany za prawdziwy | typy tez + źródła + poziom pewności | każda teza faktualna ma źródło lub status `UNKNOWN` |
| P0 | „Drugi model” nie jest niezależny | wspólny dostawca, dane i prompt tworzą wspólny błąd | karta niezależności w pakiecie weryfikacyjnym | krytyczna ocena używa innego kontekstu i innego toru kontroli |
| P0 | Brak mechanizmu zatwierdzania | model zmieni kanon albo decyzję przez automatyczny commit | patch/PR + człowiek + walidator | bez podpisu nie da się zaktualizować pliku kanonicznego |
| P0 | Prompt injection w materiałach | dokument źródłowy instruuje kontrolera, aby zignorował reguły | granica zaufania, oznaczanie danych jako nieinstrukcyjnych, brak uprawnień zapisu | próba wstrzyknięcia nie zmienia werdyktu ani plików |
| P1 | Brama budowania jest tylko listą pytań | pytania są „odhaczone” bez testu alternatyw | log wyszukiwania + fit-gap + timebox | wpis zawiera datę, zakres i wynik próby użycia |
| P1 | Brak kryterium wartości | budujemy coś, czego nikt wystarczająco nie potrzebuje | problem/beneficjent/metryka w aktywnym obiekcie | nie można przejść do budowy bez mierzalnego rezultatu |
| P1 | Niejasne tryby LITE/STANDARD/CRITICAL | pełna procedura wszędzie albo zbyt mała kontrola w ważnym miejscu | progi stawki i budżet rund | dwie osoby/model potrafią tak samo sklasyfikować przykładowe zadania |
| P1 | Brak końca pętli | krytyka generuje kolejną krytykę bez działania | limit rund, budżet czasu, stop rule | po maks. dwóch rundach jest decyzja, eskalacja albo parking |
| P1 | Brak kalibracji sędziego | „confidence 0.9” nie oznacza 90% poprawności | metryki false accept/false reject i kalibracja | wynik pilota pokazuje odrębnie błędy przyjęcia i odrzucenia |
| P1 | Zgodność zastępuje dowód | trzy modele zgodnie powtarzają popularną bzdurę | głosowanie nie jest dowodem; wymagane źródło/test | jednomyślność bez referencji kończy się `NEEDS_EVIDENCE` |
| P1 | Zwycięża styl i długość | sędzia nagradza ton, pewność albo obszerność | ślepe, znormalizowane porównania i rubryka | ocena nie zmienia się po zamianie kolejności/formatu |
| P1 | Append-only bez indeksu | decyzje rosną, sprzeczne wpisy są trudne do znalezienia | ID, status, supersedes, indeks aktywny | wyszukanie tematu zwraca bieżący wpis i historię |
| P1 | Handoff staje się źródłem prawdy | snapshot jest nieaktualny, a nowa sesja mu ufa | hash/commit, data generacji, kanon wygrywa | stary handoff jest oznaczony jako `STALE` |
| P1 | Archiwum staje się śmietnikiem | odzyskiwanie przywraca luźny pomysł jako decyzję | typy artefaktów i reguły retencji | notatka nie trafia do sterowania bez jawnej promocji |
| P1 | WIP = 1 blokuje konieczne utrzymanie | drobne zadania lub blokery są sztucznie ukrywane | osobny lane `MAINTENANCE/BLOCKED` | wyjątek ma właściciela i limit, nie otwiera drugiego celu |
| P1 | Brak zarządzania konfliktem | model i człowiek lub dwa źródła mają sprzeczne wnioski | `DISAGREEMENT` + eskalacja, nie wymuszamy konsensusu | spór zostaje zapisany zamiast rozstrzygnięty pozornie |
| P1 | Brak wersji modelu/promptu | nie da się odtworzyć, dlaczego zapadła decyzja | metadane uruchomienia | krytyczny pakiet ma model, wersję, datę i narzędzia |
| P1 | Brak prywatności i retencji | transkrypcja ujawnia sekrety lub dane osobowe | redakcja, `.gitignore`, retencja, klasyfikacja danych | test z sekretem nie trafia do commita |
| P2 | Nadmierne „zatrzymywanie” | system staje się paternalistyczny i męczący | komunikat stop + powód + trzy drogi wyjścia | użytkownik może świadomie kontynuować z zapisanym ryzykiem |
| P2 | Kontrakt psychologizuje użytkownika | opis cechy staje się etykietą i zniekształca ocenę | opisuj obserwowalne zachowania, nie diagnozy | kontrakt można zaakceptować sekcja po sekcji |
| P2 | Brak kosztu i limitu | kontrola jest droższa niż błąd, który ma wykrywać | budżet tokenów/czasu i kosztów | każdy tryb ma limit i raport kosztu |
| P2 | Brak planu incydentu | błędna decyzja zostaje tylko w historii | rejestr incydentów, rollback, post-mortem | da się cofnąć decyzję i zapisać przyczynę |
| P2 | Brak testu samego protokołu | system „działa”, bo nikt nie mierzy jego skuteczności | zestaw przypadków kontrolnych | przed pilotem przechodzą testy pozytywne i negatywne |
| P2 | Brak wersjonowania reguł | zmiana kontraktu po cichu zmienia wynik | wersja kanonu i changelog | każda zmiana reguły ma diff i powód |
| P2 | Ograniczenie do scenariuszy/produktów | nie wiadomo, czy protokół działa w innych zadaniach | klasyfikacja typu pracy | pilot zawiera co najmniej jeden przypadek nieproduktowy |

## 1. Rzeczy oczywiste, które łatwo przeoczyć

### Repozytorium nie egzekwuje konstytucji samo z siebie

Plik nazwany `KANON` jest tylko tekstem. Dopóki nie ma walidatora, procesu PR i jawnej hierarchii źródeł, model może go zignorować, a handoff może go nadpisać narracyjnie. Dlatego v0 zawiera kontrolę struktury i instrukcję uprawnień, ale nie udaje, że markdown jest mechanizmem bezpieczeństwa.

### Największym przeciwnikiem nie jest błąd, lecz wiarygodność bez dowodu

Użytkownik nie potrzebuje kolejnego narzędzia, które brzmi rozsądnie. Potrzebuje sygnału, który pozwala odróżnić: fakt, hipotezę, preferencję, rekomendację i decyzję. To wymaga typowania tez, nie tylko lepszych promptów.

### Weryfikacja zwiększa ryzyko automatyzacji błędu

Jeśli system zapisuje wynik weryfikatora jako nowy materiał treningowy lub kanon, błąd może być powielany w kolejnych sesjach. Każdy automatyczny destylat musi mieć pochodzenie i status propozycji.

### „Nie buduj” też ma koszt i granicę

Gotowy produkt może być niedostępny, niebezpieczny, zamknięty, nieprzenośny lub niezgodny z wymaganiami. Brama ma chronić czas, nie zamienić się w dogmat kupowania cudzego rozwiązania.

### Krytyka bez decyzji jest kolejną formą prokrastynacji

Adwersarz musi kończyć się wyborem: popraw, przetestuj, odrzuć, zaparkuj albo eskaluj. Sama lista ryzyk nie jest postępem.

## 2. Największe niebezpieczeństwo architektoniczne

Role, nazwy plików i tryby są intuicyjnie atrakcyjne. To właśnie dlatego mogą stać się substytutem testu. Zasada kontrolna brzmi:

> Nie dodajemy elementu dlatego, że dobrze opisuje problem. Dodajemy go dopiero, gdy powtarzalna awaria i metryka pokażą, że jest potrzebny.

## 3. Minimalna odpowiedź na każdą lukę

Jeśli w przyszłości pojawi się nowa funkcja, wpisz ją najpierw do tabeli:

```text
Awaria:
Dowód, że występuje:
Koszt obecnego obejścia:
Najmniejsza kontrola, która może pomóc:
Jak zmierzymy poprawę:
Warunek wycofania:
```

Brak tych sześciu pól oznacza, że pomysł jest jeszcze hipotezą, a nie wymaganiem.

