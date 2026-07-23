# AI weryfikuje AI — specyfikacja bezpiecznej interpretacji

## 1. Teza

Pomysł „AI weryfikujące AI” jest najmocniejszym elementem rozmowy, ale tylko po zmianie znaczenia słowa *weryfikuje*.

Wersja naiwna:

```text
model A tworzy → model B ocenia → wynik B = prawda
```

Wersja wdrażalna:

```text
model A proponuje → kontroler B próbuje obalić
                     ↓
             źródła / testy / narzędzia
                     ↓
          człowiek przyjmuje ryzyko i zatwierdza
```

Weryfikator jest więc **czujnikiem błędów i organizatorem dowodów**, nie najwyższym sędzią rzeczywistości.

## 2. Co dokładnie może sprawdzać AI

| Oś oceny | Pytanie | Czy model może być głównym kontrolerem? |
|---|---|---|
| kompletność | Czy uwzględniono cel, ograniczenia i alternatywy? | zwykle tak, z próbkowaniem |
| spójność | Czy wniosek nie przeczy kanonowi i własnym założeniom? | tak, ale wynik jest heurystyczny |
| zgodność z rubryką | Czy propozycja spełnia jawne kryteria? | tak, jeśli rubryka jest jednoznaczna |
| aktualność faktu | Czy informacja jest aktualna? | tylko z narzędziem i datowanym źródłem |
| prawdziwość faktu | Czy twierdzenie jest zgodne ze światem? | nie bez referencji, testu lub eksperta |
| wykonalność | Czy plan zadziała w konkretnej infrastrukturze? | częściowo; potrzebny prototyp/test |
| wartość/prioritet | Czy warto poświęcić czas? | model może pomóc, decyzja należy do właściciela celu |
| bezpieczeństwo/prawo | Czy ryzyko jest akceptowalne? | nie jako jedyny arbiter; eskalacja |

To rozdzielenie chroni przed sytuacją, w której „bardzo spójna odpowiedź” otrzymuje status „udowodniona”.

## 3. Minimalny skład pętli

### 3.1. Generator

Tworzy propozycję w strukturze:

- cel i oczekiwany rezultat;
- tezy z typem (`FACT`, `HYPOTHESIS`, `PREFERENCE`, `RECOMMENDATION`);
- założenia;
- alternatywy;
- wymagane dowody;
- proponowane działanie i kryterium zakończenia.

Generator nie może sam zatwierdzać swojego rezultatu.

### 3.2. Kontroler niezależny

Dostaje propozycję oraz zadanie znalezienia kontrprzykładu. Nie dostaje prywatnego toku rozumowania generatora jako autorytetu. Zwraca:

- znalezione błędy;
- brakujące założenia;
- tezy wymagające źródła;
- próby, które mogłyby rozstrzygnąć spór;
- werdykt `PASS`, `REVISE`, `NEEDS_EVIDENCE`, `ESCALATE`.

### 3.3. Kontrole zewnętrzne

Wybieramy kontrolę odpowiednią do tezy:

- wyszukiwanie i cytowanie źródeł pierwotnych;
- test jednostkowy, kalkulator, parser, linter, kompilator;
- reprodukowalny eksperyment;
- porównanie z referencją;
- ekspert domenowy;
- sprawdzenie uprawnień, prywatności i bezpieczeństwa.

Im bardziej wynik jest automatycznie sprawdzalny, tym mniej należy polegać na językowej ocenie modelu.

### 3.4. Autoryzator

Właściciel celu zatwierdza, odrzuca, odkłada lub eskaluje. Przy decyzji krytycznej zapisuje również ryzyko resztkowe i powód ewentualnego przejścia mimo ostrzeżenia.

## 4. Niezależność weryfikatora

„Inny prompt” nie daje niezależności. W pakiecie należy odnotować pięć wymiarów:

1. **model/proveedor** — inna rodzina lub przynajmniej inna wersja;
2. **kontekst** — kontroler widzi stan kanoniczny i dane wejściowe, ale nie jest zakotwiczony w narracji generatora;
3. **cel** — generator optymalizuje użyteczność, kontroler ma szukać obalenia;
4. **narzędzia** — kontroler ma dostęp do źródeł/testów, a nie tylko do tekstu;
5. **losowość i kolejność** — porównania są ślepe, z odwróconą kolejnością i bez nazw modeli.

Pełna niezależność jest praktycznie nieosiągalna. Trzeba więc mówić o **redukcji wspólnego błędu**, a nie o dowodzie niezależności.

## 5. Tryby i progi

### LITE

Stosuj dla pytań odwracalnych, niskiego kosztu i niskiej stawki.

- jedna odpowiedź;
- krótka kontrola: cel, założenie, niepewność, następny krok;
- brak zapisu do kanonu;
- orientacyjny limit: 2–3 minuty tarcia.

### STANDARD

Stosuj, gdy powstaje plan, wybór narzędzia, decyzja projektowa lub zmiana aktywnego zakresu.

- generator + kontradyktoryjny kontroler;
- brama ponownego użycia;
- co najmniej jedno źródło/test dla każdej tezy faktualnej;
- maksymalnie dwie rundy korekty;
- patch/closer po decyzji człowieka.

### CRITICAL

Stosuj dla decyzji kosztownych, nieodwracalnych, publicznych, prawnych, medycznych, finansowych, bezpieczeństwa lub systemotwórczych.

- dwa różne tory kontroli (model + test/ekspert albo dwa heterogeniczne modele + źródło);
- ślepa zamiana kolejności wariantów;
- jawna lista kontrprzykładów i niepewności;
- człowiek z odpowiednią kompetencją podpisuje decyzję;
- plan odwrócenia i obserwacji po wdrożeniu.

Jeżeli nie wiadomo, jaki tryb wybrać, wybierz wyższy tylko na czas klasyfikacji, a nie automatycznie na całą sesję.

## 6. Protokół pojedynczej oceny

1. **Zamroź propozycję.** Wygeneruj identyfikator i skrót treści; po ocenie nie zmieniaj jej po cichu.
2. **Rozbij ją na tezy.** Jedna teza = jeden możliwy dowód lub test.
3. **Oddziel opis od oceny.** „Produkt ma funkcję X” nie jest tym samym co „powinniśmy go użyć”.
4. **Uruchom kontrę.** Kontroler ma znaleźć powód, dla którego propozycja jest błędna lub przedwczesna.
5. **Sprawdź zewnętrznie.** Użyj źródła, referencji, testu albo eksperta.
6. **Zapisz spór.** Brak zgodności nie jest porażką; jest wynikiem `DISAGREEMENT`.
7. **Wydaj werdykt ograniczony zakresem.** Nie „plan jest dobry”, tylko „spełnia rubrykę A; fakt B pozostaje niezweryfikowany”.
8. **Zdecyduj i zapisz.** Decyzja należy do autoryzatora.

## 7. Pakiet dowodowy (Review Packet)

W v0 każda decyzja `STANDARD`/`CRITICAL` powinna mieć pakiet z polami:

```text
RP-ID:
Cel i rezultat:
Stawka / odwracalność:
Tryb:
Wersja stanu źródłowego (commit/hash):
Tezy:
  - id, treść, typ, źródło, świeżość, pewność
Alternatywy i zakres wyszukiwania:
Założenia:
Kontrargumenty:
Kontrole zewnętrzne:
Niezgodności:
Werdykt ograniczony zakresem:
Ryzyko resztkowe:
Rekomendacja działania:
Decyzja człowieka / podpis / data:
Warunek ponownego otwarcia:
```

Pełny szablon jest w `COS/08_PAKIET_WERYFIKACYJNY.md`, a kontrakt maszynowy w `schemas/review_packet.schema.json`.

## 8. Werdykty i reguły przejścia

| Werdykt | Znaczenie | Dozwolone działanie |
|---|---|---|
| `PASS` | kontrola nie znalazła istotnej luki w określonym zakresie | można przygotować odwracalny następny krok |
| `REVISE` | znaleziono poprawialną lukę | popraw propozycję i uruchom najwyżej jedną kolejną rundę |
| `NEEDS_EVIDENCE` | brak rozstrzygającego źródła/testu | nie zmieniaj kanonu; zaplanuj dowód albo zaparkuj |
| `DISAGREEMENT` | kontrolery lub źródła są sprzeczne | nie uśredniaj; eskaluj do człowieka/eksperta |
| `ESCALATE` | stawka, domena lub ryzyko przekracza kompetencje systemu | zatrzymaj automatyczne działanie |
| `FAIL` | naruszono regułę krytyczną lub znaleziono kontrprzykład | odrzuć albo wróć do intake |

Werdykt nie może być jedną liczbą bez uzasadnienia. Jeśli używasz punktów, przechowuj też błędy typu false accept i false reject.

## 9. Jak mierzyć jakość weryfikatora

Przed zaufaniem do kontrolera przygotuj mały, ręcznie rozstrzygnięty zestaw przypadków:

- poprawna propozycja z pozorną luką;
- błędna propozycja brzmiąca przekonująco;
- brakujące źródło;
- sprzeczne źródła;
- prompt injection;
- zmiana kolejności wariantów;
- konflikt z kanonem;
- przypadek, w którym właściwą odpowiedzią jest „nie wiem”.

Mierz osobno:

- `false_accept_rate` — błędne propozycje przepuszczone;
- `false_reject_rate` — dobre propozycje zatrzymane;
- `evidence_coverage` — tezy z dowodem/testem;
- `contradiction_detection` — wykryte sprzeczności;
- `calibration` — czy poziom pewności odpowiada trafności;
- `user_override_rate` — ile werdyktów człowiek odrzuca;
- czas i koszt na decyzję.

Nie używaj samej zgodności dwóch modeli jako metryki prawdy.

## 10. Antywzorce

- **Sędzia z tej samej głowy:** generator i kontroler mają ten sam model, kontekst i cel.
- **Głosowanie jako dowód:** trzy jednomyślne halucynacje nie tworzą faktu.
- **Teatr ról:** każdy agent pisze długą wypowiedź, ale nikt nie wykonuje testu.
- **Ocena po fakcie:** propozycja została już wdrożona, a weryfikator tylko ją opisuje.
- **Pętla bez limitu:** każda krytyka generuje kolejną architekturę.
- **Fałszywa precyzja:** `confidence: 0.93` bez kalibracji i definicji zdarzenia.
- **Ciche poprawki:** generator zmienia tekst po tym, jak kontroler go zaakceptował.
- **Przechowywanie ukrytego toku rozumowania:** archiwizujemy tylko tezy, dowody i krótkie uzasadnienie, nie wymagamy ujawniania prywatnego chain-of-thought.

## 11. Dlaczego ta ostrożność jest konieczna

Badania nad LLM-as-a-judge wskazują na ograniczenia, których nie usuwa samo dodanie drugiego modelu:

- [Huang et al.](https://arxiv.org/abs/2310.01798) opisują, że intrinsic self-correction bez zewnętrznego feedbacku może nie działać, a czasem pogarszać wynik.
- [Krumdick et al.](https://arxiv.org/abs/2503.05061) pokazują, że bez poprawnej referencji sędzia dobrze zgadza się z ekspertami głównie w pytaniach, które sam potrafi poprawnie rozwiązać; referencja ekspercka poprawia sytuację.
- [Wataoka et al.](https://arxiv.org/abs/2410.21819) opisują self-preference bias, a [Shi et al.](https://arxiv.org/abs/2406.07791) position bias.
- [Process supervision](https://cdn.openai.com/improving-mathematical-reasoning-with-process-supervision/Lets_Verify_Step_by_Step.pdf) pokazuje wartość sygnału o poszczególnych krokach, ale także zależność od jakości etykiet i zadania.
- [Constitutional AI](https://arxiv.org/abs/2212.08073) pokazuje, że AI feedback może wspierać nadzór oparty na jawnych zasadach, nie że usuwa potrzebę ludzkiej odpowiedzialności.
- [AI Safety via Debate](https://arxiv.org/abs/1805.00899) traktuje debatę jako propozycję skalowalnego nadzoru z arbitrem; nie jest to dowód, że modele same stają się niezależnym arbitrem.

## 12. Zasada końcowa

Najbardziej użyteczne zdanie do umieszczenia w kontrakcie brzmi:

> Model może zatrzymać decyzję, ale nie może sam nadać jej statusu prawdy. Status nadaje dowód, test, kompetentny człowiek albo jawnie zaakceptowane ryzyko.

