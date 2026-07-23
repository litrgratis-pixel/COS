# „Fajnie wymyślone — teraz wdrożmy tak, żeby działało”

Poniższe elementy są trafnymi intuicjami. Każdy ma jednak tryb, w którym atrakcyjna metafora zaczyna szkodzić. Druga kolumna mówi, jak przenieść pomysł z narracji do działania.

| Intuicja z rozmowy | Dlaczego wygląda świetnie | Jak wdrożyć lepiej niż brzmi w głowie | Dowód działania |
|---|---|---|---|
| **Cognitive OS / egzoszkielet** | Nadaje całości mocną kategorię i obietnicę odciążenia | Nazwij v0 „protokół decyzji i pamięci”; nazwę produktu odłóż do czasu, gdy pilot pokaże zmianę zachowania | po 10 sesjach mierzalnie mniej powrotów i krótsze wznowienie |
| **Rozmowa = procesor, repo = konstytucja** | Rozdziela działanie od pamięci | Dodaj hierarchię źródeł, wersję, hash, PR i walidator; markdown sam nie egzekwuje konstytucji | konflikt handoff/kanon zostaje wykryty przed pracą |
| **Kartograf–Architekt–Adwersarz–Walidator–Turbo** | Daje język dla różnych trybów myślenia | Traktuj role jako funkcje i kontrakty wyjścia, nie jako pięciu gadających agentów | każda funkcja wykrywa inny typ błędu na zestawie testowym |
| **Adaptive loop** | Chroni przed biurokracją i bezmyślnym „zawsze pełny audyt” | Zdefiniuj progi stawki, budżet rund i stop rule; nie wybieraj trybu po długości tekstu | dwie osoby/model potrafią sklasyfikować przypadki tak samo |
| **AI weryfikuje AI** | Redukuje ciężar oceny po stronie użytkownika | Generator ≠ kontroler; wymagaj niezależności, referencji/testu, `NEEDS_EVIDENCE` i człowieka przy wysokiej stawce | false accept i false reject są mierzone na znanych przypadkach |
| **Brama „czy koło istnieje?”** | Chroni przed kosztownym wynajdywaniem | Dodaj fit-gap, zakres i datę wyszukiwania, próbę użycia, TCO, prywatność i kryterium wartości | zapisano co najmniej jedną odrzuconą budowę na rzecz reuse |
| **WIP = 1** | Odcina przełączanie kontekstu | Ogranicz jeden rezultat, ale dopuść osobny lane `BLOCKED/MAINTENANCE` z limitem | wyjątki nie stają się drugim backlogiem aktywnym |
| **Append-only decyzje** | Chroni historię i utrudnia ciche przepisywanie | Dodaj status, supersedes, indeks bieżący, datę przeglądu i retencję | każda decyzja ma jedną aktualną wersję i ślad zmian |
| **Parking z warunkiem powrotu** | Pozwala nie tracić dobrych pomysłów | Warunek musi być obserwowalny, mieć datę i sygnał; bez tego wpis wygasa | pomysł zostaje reaktywowany tylko po spełnieniu sygnału |
| **Closer po każdej sesji** | Zamienia rozmowę w trwały rezultat | Zapisuj zmianę stanu, nie pełne streszczenie; dołącz diff, koszt i `NO_STATE_CHANGE` | kolejna sesja potrafi wskazać jeden następny krok bez archeologii |
| **Handoff 1000–1500 słów** | Przenosi kompatybilność między sesjami | Traktuj go jak cache: wersja, hash, valid-until, źródła; kanon zawsze wygrywa | stary handoff jest oznaczony `STALE`, a nie cicho użyty |
| **AI ma prawo zatrzymać rozmowę** | Chroni uwagę przed rozpędzonym projektem | Stop musi zawierać dowód/brak dowodu, koszt, najmniejszy test i możliwość świadomego override | zatrzymanie prowadzi do reuse/test/parking/eskalacji, nie do pustej odmowy |
| **Dziesięć sesji eksperymentu** | Wymusza użycie zamiast dalszego projektowania | Dodaj baseline, metryki, kontrolę, kryterium stop/go i rejestr incydentów | decyzja o rozbudowie wynika z danych, nie z entuzjazmu |
| **„Nie automatyzuj decyzji”** | Zachowuje odpowiedzialność człowieka | Automatyzuj przygotowanie, walidację struktury i patch; wymuś approval gate uprawnieniami | bot nie może sam zmienić kanonu |
| **Repo jako pamięć** | Daje ciągłość po utracie sesji | Rozdziel sterowanie od archiwum i wprowadź typy artefaktów; inaczej repo staje się śmietnikiem | notatka nie awansuje do decyzji bez promocji |

## Najważniejsza korekta kolejności

W rozmowie kolejność intuicyjnie prowadzi od metafory do architektury. Wdrożenie powinno prowadzić odwrotnie:

1. jedna realna awaria;
2. najmniejszy test;
3. jeden artefakt stanu;
4. dopiero potem nazwa mechanizmu;
5. dopiero po powtarzalności — automatyzacja.

## Trzy elementy, które najłatwiej przereklamować

### 1. Wieloagentowość

Więcej ról może zwiększyć koszt, opóźnienie i korelację błędów. Jeśli jedna rubryka i jeden test rozstrzygają sprawę, dodatkowe agenty są dekoracją.

### 2. Wysoka pewność sędziego

Liczba bez kalibracji jest ozdobą. W v0 ważniejsze jest, czy system umie wskazać brak dowodu, niż czy umie wystawić `0.93`.

### 3. Handoff jako „pamięć osobowości”

Handoff przenosi stan roboczy, nie całe docieranie się ludzi i modeli. Zachowanie kompatybilności wymaga krótkiego kontraktu, jawnych reguł i plików źródłowych; nie da się zagwarantować identycznego stylu między narzędziami.

## Test odporności na „ładnie brzmiące bzdury”

Przed dodaniem dowolnej funkcji zadaj cztery pytania:

```text
Jaką konkretną awarię widzieliśmy?
Jaki dowód odróżni poprawę od pozoru poprawy?
Co stanie się, jeśli kontroler się myli w tę samą stronę co generator?
Jak wyłączymy funkcję, jeśli zwiększy tarcie?
```

Brak odpowiedzi oznacza: parking, nie implementację.

