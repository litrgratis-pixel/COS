# Sesje

Jedna sesja zmieniająca stan lub dostarczająca metryki pilota = jeden plik `YYYY-MM-DD-NNN.md`. Raport ma umożliwić wznowienie pracy bez dostępu do prywatnej rozmowy i bez znajomości zewnętrznej instrukcji wprowadzającej.

Surową transkrypcję przechowuj tylko po redakcji i świadomej klasyfikacji danych. Publiczne repo powinno zawierać zredagowany ślad dowodowy, nie pełne prywatne logi.

Metodologia analizy rozmów znajduje się w `PILOT/README.md` i `PILOT/SZABLON_AUDYTU_ROZMOWY.md`. Szczegółowe audyty są w `PILOT/AUDYTY/`, a ten katalog przechowuje closer i zmianę stanu.

Minimalny plik sesji:

```markdown
---
protocol: cognitive-os-v0
artifact: session_report
session_id: SES-YYYY-MM-DD-NNN
date: YYYY-MM-DD
status: draft | complete
mode: LITE | STANDARD | CRITICAL
source_commit: SHA
state_change: STATE_CHANGE | NO_STATE_CHANGE
---

# SES-YYYY-MM-DD-NNN

Cel:
Źródła i commit:
Zakres dostępu do materiału:
Najważniejsze tezy:
Decyzje użytkownika:
Incydenty:
Metryki:
Co zadziałało:
Co przepuściło błędnie:
Zmiana stanu:
Closer:
Jeden następny krok:
```

Raport sesji nie powinien powielać pełnego audytu ani całej rozmowy. Ma wskazywać artefakty i zachować to, co potrzebne do kontynuacji.
