# Humanizer PL

Skill Codex do humanizacji tekstów po polsku i angielsku. Usuwa typowe sygnały pisania AI, ale zachowuje sens, fakty, liczby, język, żargon i głos autora.

## Pochodzenie

To repozytorium jest forkiem [`pielas-activy/humanizer-pl`](https://github.com/pielas-activy/humanizer-pl), przeniesionym i dopracowanym pod format skilli Codex. Oryginalny projekt rozwija polską warstwę humanizera, tryb Bielik/Ollama, referencje PL/EN i evals. Angielskie wzorce w oryginale pochodzą z [`blader/humanizer`](https://github.com/blader/humanizer).

Port Codex dodaje `agents/openai.yaml`, instrukcje zgodne z Codex, katalog `scripts/`, bezpieczniejsze zasady dla opcjonalnej instalacji Bielika oraz opis instalacji z `~/.codex/skills`. Referencje językowe i zamrożone evals są zachowane jako materiał źródłowy projektu.

## Instalacja w Codex

Skopiuj katalog `humanizer-pl` do katalogu skillów Codex:

```bash
cp -R humanizer-pl ~/.codex/skills/humanizer-pl
```

Możesz też użyć go z repozytorium jako źródła własnego skilla. Po instalacji uruchom jawnie `$humanizer-pl` albo poproś o humanizację tekstu.

## Zakres

- automatyczne rozpoznanie PL/EN;
- osobne wzorce AI dla obu języków;
- drugi przebieg polszczyzny: kalki, szyk, czasowniki i parataksa;
- ochrona faktów, cytatów, nazw własnych i żargonu;
- opcjonalny raport HTML side by side;
- opcjonalny lokalny doradca Bielik przez Ollama;
- zamrożone evals bez wywołań LLM.

Domyślnie Bielik nie jest potrzebny. Jeśli wybierzesz ten tryb, instalacja Ollama i modelu wymaga osobnego potwierdzenia, a propozycje Bielika nie są stosowane automatycznie.

## Evals

```bash
python3 evals/run_evals.py
```

## Licencja i atrybucja

MIT. Angielskie wzorce pochodzą z [`blader/humanizer`](https://github.com/blader/humanizer). Polska warstwa, integracja z Bielikiem i evals bazują na [`pielas-activy/humanizer-pl`](https://github.com/pielas-activy/humanizer-pl). Szczegóły są w pliku `LICENSE`.
