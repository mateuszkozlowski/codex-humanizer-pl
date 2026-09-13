# Tryb z Bielikiem

Bielik jest opcjonalnym, lokalnym drugim sygnałem do oceny polszczyzny. Domyślny tryb bez Bielika działa bez zależności i pozostaje preferowany, gdy liczy się kontrola faktów.

## Warunki

Potrzebujesz [Ollama](https://ollama.com/) oraz modelu Bielik. Model działa lokalnie, ale instalacja może pobrać kilka gigabajtów danych i wymaga zasobów sprzętowych. Przed instalacją poinformuj użytkownika o tym koszcie i uzyskaj jego wyraźne potwierdzenie.

## Instalacja po potwierdzeniu

```bash
bash scripts/install-bielik.sh
```

Alternatywnie, jeśli Ollama jest już zainstalowana:

```bash
ollama pull SpeakLeash/bielik-11b-v3.0-instruct:Q4_K_M
```

Lżejszy wariant można wskazać przez `BIELIK_MODEL`, np. `SpeakLeash/bielik-4.5b-v3.0-instruct`.

## Sprawdzenie i użycie

```bash
python3 scripts/bielik-review.py --check
python3 scripts/bielik-review.py --file zhumanizowany.md
python3 scripts/bielik-advisor.py --file zhumanizowany.md --n 6
```

`bielik-review.py` zwraca ocenę i flagi. `bielik-advisor.py` zwraca propozycje zmian. Żaden skrypt nie powinien samodzielnie przepisywać ani zapisywać tekstu.

Główny model ocenia każdą propozycję, trzyma fakty, liczby, cytaty, nazwy własne i żargon, a następnie pokazuje użytkownikowi ryzykowne propozycje. Zmiany Bielika nigdy nie są stosowane po cichu.

## Fallback

Przy braku Ollama lub modelu wróć do recenzji wykonywanej przez główny model. Nie blokuj na tym zwykłej humanizacji.

Zmienne środowiskowe:

- `BIELIK_MODEL` - nazwa modelu w Ollama;
- `OLLAMA_HOST` - adres serwera, domyślnie `http://localhost:11434`.
