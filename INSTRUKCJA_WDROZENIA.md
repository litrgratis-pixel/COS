# INSTRUKCJA WDROŻENIA — Creative OS

## Setup (jednorazowy, ~45 min)

1. **Utwórz repo:** GitHub → New repository → `creative-os` → Private → Create.
2. **Sklonuj lokalnie:**
   ```bash
   cd ~/projekty
   git clone git@github.com:twoj-user/creative-os.git
   cd creative-os
   ```
3. **Wrzuć te pliki** do folderu repo (zastępując puste `git init`).
4. **`.gitignore`:**
   ```
   .DS_Store
   .obsidian/workspace*
   ```
   *(Świadomie NIE ignorujemy `SESJE/` — pliki sesji to Wasz dowód, że destylat faktycznie trafił do plików docelowych, nie tylko powstał. Tekst jest tani; ten ślad jest cenny.)*
5. **Pierwszy commit:**
   ```bash
   git add . && git commit -m "init: Creative OS v1" && git push -u origin main
   ```

## Codzienny cykl

```
START  →  wklej 00_INDEX.md + ODCINEK_AKTYWNY.md + Opener Prompt
   ↓
PRACA  →  notatki w SESJE/YYYY-MM-DD_sesja_NNN.md §5
   ↓
KONIEC →  Closer Prompt (OBOWIĄZKOWO) → destylat
   ↓
ZAPIS  →  destylat → DECYZJE / PARKING / ODCINEK_AKTYWNY / INDEX
   ↓
COMMIT →  git add . && git commit -m "EP-XXX: ..." && git push
```

## Sync między urządzeniami

- `git pull` PRZED sesją, `git push` PO. Zawsze, bez wyjątku.
- `DECYZJE.md` / `PARKING.md` / `DONE.md` są append-only → merge trywialny.
- `ODCINEK_AKTYWNY.md` NIE jest append-only → tu będą prawdziwe konflikty, jeśli zapomnisz `pull`. Edytuj z jednego urządzenia naraz.
- `00_INDEX.md` (liczniki) — konflikt = dwie sesje utworzyły ten sam ID. Renumeruj ręcznie tę drugą.

## Częste błędy — czego NIE robić

- ❌ Nie pomijaj Closer Prompta „bo krótka sesja".
- ❌ Nie edytuj starych DEC/PARK — tylko `SUPERSEDED BY` / `REACTIVATED BY`.
- ❌ Nie zostawiaj PARK bez warunku powrotu.
- ❌ Nie rozwijaj pomysłu z BACKLOG-u przy okazji pracy nad innym odcinkiem — to już jest praca nad nim, a WIP = 1.
- ❌ Nie oceniaj sam kryterium DoD „da się obejrzeć bez tłumaczenia" — pokaż komuś z zewnątrz (dla EP-001/002 zawsze, od EP-003 co 3. odcinek — patrz `AZYMUT.md` pkt 6). Twórca ma najgorszy możliwy wgląd w to akurat pytanie, bo ma pełen kontekst, którego widz nie ma.
- ❌ Nie licz na to, że AI samo zapisze zmiany o północy. Żaden mainstream LLM tego nie robi. Jeśli chcesz realnej automatyzacji cyklu (odczyt notatek → destylat → zapis do plików → commit) — to poziom Claude Code / Cursor Agent, nie czatu. Warto rozważyć po 2–3 tygodniach, gdy system się zadomowi, nie na starcie.

## Kiedy system się psuje — sygnały ostrzegawcze

| Objaw | Diagnoza | Naprawa |
|---|---|---|
| 4. otwarte pytanie w `ODCINEK_AKTYWNY.md` | Odcinek za szeroki | Rozstrzygnij jedno z 3 istniejących, albo przenieś wątek do PARKING |
| `BACKLOG.md` > 15 pozycji | Backlog martwy — ambicje sprzed miesięcy | Miesięczny przegląd: usuń albo przenieś do PARKING z warunkiem |
| Pracujesz nad 2 odcinkami naraz (poza etapem czysto produkcyjnym: montaż/eksport) | Złamany WIP=1 na etapie kreatywnym | Wróć do jednego — drugi do BACKLOG/PARKING |
| 3. runda poprawek tego samego odcinka | Perfekcjonizm wygrywa z DoD | Publikuj „nie-idealny" albo świadomie SUPERSEDED i nowy DEC |
| AI nie wie, „w którym jesteśmy poziomie" | Mieszasz poziomy w jednej wypowiedzi | Zatrzymaj się, nazwij poziom jawnie, potem kontynuuj |
| Zmieniłeś `AZYMUT.md`, ale nie przejrzałeś `BACKLOG.md` | Seria się rozjeżdża cicho | Audyt backlogu po KAŻDEJ zmianie Azymutu, bez wyjątku |

## Sprawdzian po 30 dniach

Załóż GitHub issue w tym repo, tytuł „Przegląd Creative OS", z terminem (due date) na 30 dni od dziś: „czy jeszcze używam Creative OS? Jeśli nie — czemu?" Issue z terminem żyje w tym samym miejscu co reszta pracy — kalendarzowe przypomnienie konkuruje o uwagę z całą resztą życia i przegrywa tak samo łatwo, jak sam system, który ma pilnować.
„Zapomniałem" nie jest prawdziwą odpowiedzią. Prawdziwa to jedna z trzech: (1) za dużo ceremonii, (2) nie widzę zwrotu, (3) projekt umarł. Każda wymaga innej reakcji — pierwsza: uprość format (więcej DEC-lite, mniej pól); druga: sprawdź, czy realnie coś publikujesz, czy tylko dokumentujesz; trzecia: to nie jest porażka systemu.

## Jedna uwaga o zakresie tego systemu

Ten system jest skrojony pod pracę odcinkową/serialną. Nie kopiuj go automatycznie do innych projektów o innym kształcie (np. jednorazowy landing page) — tam wystarczy prostszy system albo żaden.
