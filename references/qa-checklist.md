# QA humanizera

Mechaniczne bramki nie zastępują lektury. Przed oddaniem finalnego tekstu przejdź przez trzy warstwy.

## 1. Sens i pokrycie

- Czy zostały wszystkie twierdzenia, liczby, daty, URL-e, nazwiska, cytaty i zastrzeżenia?
- Czy nie zmieniła się modalność: `może`, `powinien`, `prawdopodobnie`, `nie`?
- Czy zachowano kolejność przyczyn i skutków oraz relacje między podmiotami?
- Czy żargon autora i nazwy własne pozostały nietknięte, jeśli nie poprosił o zmianę?

## 2. Język i styl

- Czy zdania są konkretne, a akapity nie zaczynają się od waty lub meta-zapowiedzi?
- Czy rozbito powtarzające się schematy, ale nie usunięto celowej emfazy?
- Czy polski nie brzmi jak tłumaczenie: są czasowniki osobowe, naturalny szyk i właściwy rejestr?
- Czy zmiany obejmują strukturę, gdy problem był strukturalny, a nie tylko myślniki i pojedyncze słowa?

## 3. Bramki deterministyczne

Uruchom po zapisaniu wejścia i wyniku do plików:

```bash
python3 scripts/validate_output.py --input input.txt --output output.txt --lang auto
```

Następnie uruchom regresję:

```bash
python3 evals/run_evals.py
python3 evals/run_qa.py
```

Jeśli bramka nie przechodzi, nie maskuj problemu komentarzem. Popraw tekst albo jawnie zgłoś użytkownikowi konflikt między wiernością treści a mechaniczną regułą.
