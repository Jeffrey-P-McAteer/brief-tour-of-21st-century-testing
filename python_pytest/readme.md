
# Python pytest example

## Run project (manual testing)

```bash
python program.py 1 2 3 4 5 6 7 8
```


## Run tests (automated testing + reports & metrics)

```bash
python -m pip install --user pytest-cov

python -m coverage run ./tests.py
python -m coverage html

```

