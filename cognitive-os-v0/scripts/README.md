# Skrypty

`validate_cos.py` jest celowo mały i nie używa sieci ani modelu. Jego zadaniem jest wyłapać brak pliku, sekcji, duplikat ID i przypadkowy sekret. Nie ocenia prawdy ani jakości decyzji.

Uruchomienie:

```bash
python3 validate_cos.py ../COS
python3 validate_cos.py ../COS --strict
```

Tryb `--strict` ma sens dopiero po wypełnieniu szablonów.

