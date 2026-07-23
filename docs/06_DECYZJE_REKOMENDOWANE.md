# Rekomendowane decyzje projektowe dla v0

Ten dokument zamienia analizę w ograniczony zestaw decyzji startowych. Nie jest historią rozmowy; jest propozycją do zatwierdzenia przez właściciela repozytorium.

## DEC-001 — Zakres v0

**Decyzja:** v0 jest protokołem i eksperymentem, nie autonomicznym Cognitive OS.

**Wybrano:** pliki stanu, pakiet dowodowy, closer, walidator struktury, pilot 10 sesji.

**Nie wybrano:** graf wiedzy, pamięć semantyczna, stała orkiestracja agentów, automatyczny zapis decyzji.

**Powód:** największe ryzyko to budowa narzędzia zamiast sprawdzenia, czy narzędzie pomaga.

**Ponowne otwarcie:** po 10 sesjach, jeśli metryki pokażą konkretną powtarzalną awarię wymagającą automatyzacji.

## DEC-002 — Znaczenie „AI weryfikuje AI”

**Decyzja:** używamy określenia „weryfikacja dowodowa z udziałem AI”, a nie obietnicy autonomicznego sędziego.

**Wybrano:** generator, niezależny atak, zewnętrzne testy/źródła, jawna niepewność, człowiek jako autoryzator.

**Nie wybrano:** większości głosów modeli jako dowodu, automatycznego przepisywania werdyktu do kanonu.

**Ponowne otwarcie:** tylko po zbudowaniu i zmierzeniu zestawu kalibracyjnego.

## DEC-003 — WIP

**Decyzja:** jeden aktywny rezultat (`WIP=1`) oraz osobny, limitowany lane dla utrzymania i blokad.

**Nie wybrano:** absolutnego zakazu wszystkich równoległych działań.

**Ponowne otwarcie:** gdy pilot pokaże, że wyjątki są częstsze niż główny przepływ.

## DEC-004 — Kanon i handoff

**Decyzja:** kanon jest źródłem prawdy; handoff jest wersjonowanym snapshotem.

**Kontrola:** handoff musi mieć datę, wersję protokołu, commit/hash i listę plików źródłowych.

**Ponowne otwarcie:** gdy przeniesienie sesji regularnie trwa ponad pięć minut mimo aktualnego handoffu.

## DEC-005 — Dane i prywatność

**Decyzja:** surowe transkrypcje nie trafiają do repo bez redakcji i świadomego wyboru.

**Powód:** archiwum może zawierać sekrety, dane osobowe i treści nieprzeznaczone do trwałego przechowywania.

**Ponowne otwarcie:** po zdefiniowaniu klasyfikacji danych i retencji.

## DEC-006 — Kryterium budowy własnego rozwiązania

**Decyzja:** „nie znaleziono gotowego narzędzia” nie wystarcza. Potrzebne są: realny problem, fit-gap, koszt alternatyw, test ręczny i dowód przewagi własnej wersji.

**Ponowne otwarcie:** gdy nowe dane zmienią co najmniej jedną z tych osi.

