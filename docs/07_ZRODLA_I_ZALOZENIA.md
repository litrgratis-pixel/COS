# Źródła i granice wnioskowania

Ten plik rozdziela to, co wynika bezpośrednio z załączonej rozmowy, od tego, co jest rekomendacją projektową oraz od tego, co wspiera literatura.

## A. Wnioski bezpośrednie z rozmowy

- rozmowa ma pełnić funkcję procesora, repozytorium — pamięci i konstytucji;
- użytkownik chce krytyki, braku zgadywania i ochrony przed ponownym wynajdywaniem;
- proponowane elementy to kontrakt, kompas, kanon, aktywny obiekt, decyzje, parking, backlog, brama budowania, handoff i closer;
- proponowana pętla ma mieć różną głębokość;
- autorzy rozmowy zalecają eksperyment dziesięciu sesji przed rozbudową.

## B. Rekomendacje dodane w tej analizie

- typowanie tez i rejestr dowodów;
- niezależność jako redukcja wspólnego błędu, nie gwarancja;
- jawne werdykty `NEEDS_EVIDENCE`, `DISAGREEMENT`, `ESCALATE`;
- kalibracja false accept/false reject;
- kontrola prompt injection, prywatności i uprawnień;
- patch/PR jako granica między sugestią a zmianą kanonu;
- rejestr incydentów i rollback;
- pilotaż z baseline, a nie sama liczba sesji.

## C. Źródła empiryczne i zakres ich użycia

| Źródło | Co wspiera | Czego nie dowodzi |
|---|---|---|
| [Huang et al. 2024](https://arxiv.org/abs/2310.01798) | ograniczenia intrinsic self-correction | że każda forma iteracji jest nieskuteczna |
| [Krumdick et al. 2025/2026](https://arxiv.org/abs/2503.05061) | znaczenie poprawnych referencji i ludzkiego ugruntowania w LLM-as-a-judge | że model nigdy nie może być użytecznym kontrolerem |
| [Wataoka et al. 2024](https://arxiv.org/abs/2410.21819) | ryzyko self-preference bias | że każdy model ma identyczną wielkość biasu |
| [Shi et al. 2024](https://arxiv.org/abs/2406.07791) | ryzyko position bias | że zamiana kolejności rozwiązuje wszystkie biasy |
| [Lightman et al.](https://cdn.openai.com/improving-mathematical-reasoning-with-process-supervision/Lets_Verify_Step_by_Step.pdf) | wartość procesu i etykiet krokowych w określonym zadaniu | że ten sam wynik przenosi się automatycznie na zarządzanie projektami |
| [Bai et al.](https://arxiv.org/abs/2212.08073) | możliwość użycia AI feedback przy jawnej konstytucji | że ludzka odpowiedzialność znika |
| [Irving et al.](https://arxiv.org/abs/1805.00899) | intuicję kontradyktoryjnego nadzoru/debaty | że mnogość agentów sama daje prawdę |
| [NIST AI 600-1](https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf) | governance, provenance, testy, incydenty jako elementy zarządzania ryzykiem | gotową implementację tego pakietu |
| [OWASP LLM Top 10 2025](https://genai.owasp.org/resource/owasp-top-10-for-large-language-model-applications-2025/) | klasy zagrożeń aplikacji LLM | pełny threat model konkretnego repo |

## D. Zasada interpretacji

Wnioski z pojedynczych prac są ograniczone do opisanego zadania i konfiguracji. Nie używamy ich jako dowodu, że określony dostawca lub model jest „dobry” albo „zły”. Służą do uzasadnienia architektury, która zakłada możliwość wspólnego błędu, wymaga dowodu i mierzy skuteczność na własnych przypadkach.

