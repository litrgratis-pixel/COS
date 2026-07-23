---
protocol: cognitive-os-v0
type: compass
version: 0.1
status: active
last_updated: 2026-07-23
---

# KOMPAS

## Gdzie jesteśmy

Pilot Cognitive OS v0 jest aktywny. Pierwszy audyt dużej rozmowy został zakończony, a repo jest konfigurowane jako samowystarczalne środowisko do serii porównywalnych audytów i przygotowania końcowej wersji na podstawie danych.

## Aktywny cel

Przeprowadzić dziesięć rzeczywistych sesji, w tym serię zróżnicowanych audytów rozmów, i na tej podstawie skonfigurować najmniejszą końcową wersję COS, która poprawia ciągłość pracy i ogranicza powtarzanie błędów przy akceptowalnym koszcie.

## Co obecnie obowiązuje

- WIP = 1 dla rezultatu: wiarygodna finalizacja pilota, nie równoległa budowa produktu.
- Analiza rozmowy rozpoczyna się `READ_ONLY`.
- Stosujemy dwuetapowy audyt: ślepy inwentarz, następnie audyt względem repo.
- Nie budujemy przed przejściem bramy ponownego użycia.
- Zmiana kanonu wymaga zatwierdzonego patcha/commitu.
- Obserwacje dotyczące protokołu grupujemy na checkpointach po 3, 6 i 10 sesjach, poza ryzykiem bezpieczeństwa lub utraty danych.
- Rozmowa jest materiałem; repozytorium jest stanem.

## Czego nie ruszamy

- wieloagentowa orkiestracja;
- graf wiedzy i wyszukiwanie semantyczne;
- automatyczne zatwierdzanie decyzji;
- budowa pełnego produktu Cognitive OS;
- ogłoszenie v1 na podstawie jednego audytu;
- automatyczne publikowanie surowych rozmów i logów.

## Najbliższy dowód lub działanie

Przeprowadzić drugi audyt na krótszej, mniej problematycznej rozmowie i zmierzyć czas bootstrapu, analizy oraz obsługi protokołu.

## Otwarte pytania (maks. 3)

1. Jaki jest realny koszt czasowy dwuetapowego audytu dla krótkiej rozmowy?
2. Które awarie z `AUD-2026-001` powtórzą się w co najmniej dwóch innych rozmowach?
3. Czy nowe AI potrafi poprawnie rozpocząć pracę wyłącznie na podstawie repo i `BOOT_ACK`?

## Ostatnia zmiana stanu

DEC-2026-001 — seria audytów rozmów i finalizacja COS na podstawie danych; pierwszy raport: `COS/SESJE/2026-07-23-001.md`.
