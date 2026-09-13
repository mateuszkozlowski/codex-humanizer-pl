# humanizer-pl

Dwujęzyczny (PL + EN) skill do Codex, który usuwa oznaki pisania AI z tekstu, zachowując sens,
fakty i głos autora. To fork [pielas-activy/humanizer-pl](https://github.com/pielas-activy/humanizer-pl),
który z kolei rozszerza [blader/humanizer](https://github.com/blader/humanizer) o pełną warstwę
polskiej naturalności.

> **TL;DR (EN):** A bilingual de-slop skill. Removes AI-writing tells from Polish AND English text
> while preserving meaning and voice. The English patterns come 1:1 from blader/humanizer; the
> Polish layers, the Bielik advisor and the eval harness are new. Auto-detects language.

## Po co to

Każdy de-AI/humanizer w sieci jest po angielsku. Polski AI-slop to jednak NIE przetłumaczony
angielski: GPT i Claude po polsku mają własne tells (kalki, nadmiar imiesłowów, klisze epoki,
parataksa zamiast hipotaksy). `humanizer-pl` celuje w jedno i drugie.

## Instalacja

Skopiuj do katalogu skilli Codex:

```bash
git clone https://github.com/mateuszkozlowski/codex-humanizer-pl \
  ~/.codex/skills/humanizer-pl
```

Działa od razu w trybie domyślnym, bez zależności. Tryb z Bielikiem jest opcjonalny i lokalny;
instalacja Ollama/modelu wymaga osobnego potwierdzenia, bo może pobrać kilka gigabajtów.

## Co robi

1. **Wykrywa język** -> ładuje wzorce PL albo EN (progressive disclosure, czyta tylko to, czego
   potrzebuje).
2. **De-slop, odważnie.** Usuwa myślnik długi, "to nie X, to Y", rule of three, anaforę, watę.
   Przepisuje strukturę zdań, nie tylko interpunkcję.
3. **Przebieg polszczyzny (tylko PL).** Tłumaczy leniwe anglicyzmy (zostawia żargon autora),
   pilnuje czasowników, rozwija kalki-przymiotniki, łapie ukryty "nie X, to Y" i **scala urywane
   zdania w złożone** (parataksa -> hipotaksa, najsilniejszy polski tell). Na końcu osobny **skan
   kalek** (test odwrotnego tłumaczenia, nie zamknięta lista).
4. **Final.** Skan: zero myślnika długiego, pełne ogonki, fakty 1:1.
5. **Uczy się Twojego żargonu (opcjonalnie).** Wykrywa branżowe terminy i może zapamiętać Twoją
   osobistą listę "tego nie ruszaj", per user i lokalnie. Szczegóły w sekcji "Profil żargonu".

## Tryby recenzenta polszczyzny

- **Bez Bielika (domyślny).** Recenzentem jest główny model. Zero zależności, działa wszędzie.
- **Z Bielikiem (opcja).** Lokalny natywny polski LLM (Bielik-11B przez Ollama) DORADZA, główny
  model osądza, a propozycje trafiają do użytkownika do decyzji. Instalator
  `scripts/install-bielik.sh` działa dopiero po potwierdzeniu. Setup:
  [`references/setup-bielik.md`](references/setup-bielik.md).

### Dlaczego Bielik jest tylko doradcą?

Bielik może wskazać możliwe kalki i nienaturalny szyk, ale nie powinien sam przepisywać tekstu.
Główny model ocenia każdą propozycję, pilnuje faktów, a użytkownik decyduje, co przyjąć. Dzięki
temu lokalny model jest dodatkowym sygnałem, nie ukrytym autorem zmian.

## Profil żargonu (opcjonalny, per user)

Skill nie zna z góry niczyjego żargonu i celowo go nie hardkoduje (nie jest "do AI" ani do żadnej
jednej branży). Zamiast tego potrafi **wykryć Twój żargon i go zapamiętać**:

- Gdy w tekście widzi dużo powracających, branżowych terminów (prawnik: "cesja", "rękojmia";
  marketer: "lead", "funnel"), sam proponuje krótką sesję w stylu "zapamiętać, których nie ruszać?".
- Możesz to też odpalić wprost: "zapamiętaj mój żargon" albo "zbuduj mój profil żargonu".
- Potwierdzoną listę zapisuje lokalnie w `references/jargon-profile.local.md` (prywatnie, per
  maszyna, gitignore, nie trafia do repo) i przy kolejnych tekstach pilnuje, żeby tych słów nie
  tłumaczyć ani nie "poprawiać".

Każdy ma swój profil: prawnik prawniczy, marketer marketingowy, Ty swój. Dzięki temu uniwersalny
skill nie przekłada Twojego fachowego słownictwa na siłę.

## Struktura

```
humanizer-pl/
  SKILL.md                  router: wykryj język -> wzorce -> proces -> (PL) polszczyzna
  references/
    patterns-en.md          33 wzorce blader 1:1 (EN) + TOC
    patterns-pl.md          6 kategorii PL + rodzina "manufaktura rytmu"
    polszczyzna-pl.md        warstwa naturalności PL (anglicyzmy, czasowniki, kalki,
                            ukryty "nie X, to Y", parataksa -> hipotaksa, skan kalek)
    przyklady.md            pary PRZED/PO (PL z banku, EN z blader)
    raport-html.md          szablon raportu HTML (side-by-side + lista zmian), tryb opcjonalny
  evals/
    evals.json              6 binarnych asercji + 2 zamrożone case'y
    run_evals.py            deterministyczny runner
  agents/openai.yaml        metadane interfejsu Codex
  scripts/                  tryb "z Bielikiem" (opcjonalny)
    install-bielik.sh, bielik-advisor.py, bielik-review.py
```

## Twarde zasady wyjścia

- Zero myślnika długiego (U+2014) i półpauzy (U+2013), zawsze ASCII `-`.
- Polskie znaki (pełne ogonki) w polskim tekście.
- Nie zmieniaj języka, nie wymyślaj faktów, output nie puszy treści.

Wyjątek: `references/patterns-en.md` i sekcja EN w `przyklady.md` cytują blader 1:1, więc w
negatywnych przykładach "before" mają myślniki - to demonstrowany tell. Wynik skilla ich nie
zawiera.

## Evals

```bash
python3 evals/run_evals.py
```

Sprawdza 6 binarnych asercji na zamrożonych przykładach: brak myślnika, polskie znaki, brak słów
z banów, output nie dłuższy niż input, pierwsza linia nie wypełniacz, brak artefaktów chatbota.

## Użycie

W Codex: `$humanizer-pl` albo "zhumanizuj ten post / wywal AI-slop z tego maila".
Auto-wykrywa PL/EN. Tryb z Bielikiem: "zhumanizuj + sprawdź Bielikiem". Raport HTML ze zmianami
(side-by-side + lista zmian): "zhumanizuj + raport HTML". Profil żargonu (czego nie tłumaczyć):
"zapamiętaj mój żargon".

## Atrybucja

Ten fork Codex bazuje na [pielas-activy/humanizer-pl](https://github.com/pielas-activy/humanizer-pl)
(MIT). Oryginalny projekt zawiera polskie warstwy, integrację z Bielikiem i evals; angielskie
wzorce zostały przejęte z [blader/humanizer](https://github.com/blader/humanizer), który bazuje
na przewodniku "Signs of AI writing". Port Codex dodaje metadane `agents/openai.yaml`, zmienia
ścieżki i dostosowuje zasady uruchamiania opcjonalnych narzędzi. Szczegóły są w `LICENSE`.
