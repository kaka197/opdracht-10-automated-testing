# Quick Start Guide

## Snel aan de slag met dit project

### Stap 1: Installatie
```bash
# Installeer Python dependencies
pip install -r requirements.txt
```

### Stap 2: Tests Uitvoeren
```bash
# Optie 1: Direct met pytest
pytest -v

# Optie 2: Met het run_tests.py script
python run_tests.py

# Optie 3: Met coverage
pytest --cov=calculator --cov-report=term
```

### Stap 3: Resultaten Bekijken
Na het uitvoeren van de tests zie je:
```
test_calculator.py::test_add PASSED
test_calculator.py::test_subtract PASSED
test_calculator.py::test_multiply PASSED
test_calculator.py::test_divide PASSED
```

### Verwachte Output
```
============================= test session starts =============================
collected 4 items

test_calculator.py::test_add PASSED                                     [ 25%]
test_calculator.py::test_subtract PASSED                                [ 50%]
test_calculator.py::test_multiply PASSED                                [ 75%]
test_calculator.py::test_divide PASSED                                  [100%]

============================== 4 passed in 0.05s ==============================
```

## CI/CD Setup

### Voor GitLab
1. Push code naar GitLab repository
2. GitLab detecteert `.gitlab-ci.yml` automatisch
3. Pipeline start automatisch
4. Bekijk resultaten in CI/CD → Pipelines

### Voor GitHub
1. Push code naar GitHub repository
2. Ga naar "Actions" tab
3. GitHub detecteert `.github/workflows/tests.yml`
4. Workflow start automatisch bij push/PR

### Voor Travis CI
1. Ga naar travis-ci.com
2. Activeer repository
3. Travis detecteert `.travis.yml`
4. Build start automatisch

## Troubleshooting

### "pytest: command not found"
```bash
pip install pytest
```

### "ModuleNotFoundError: No module named 'calculator'"
Zorg dat je in de juiste directory bent:
```bash
cd "c:\Users\Kevin\Downloads\opdracht 10"
```

### Tests falen
Controleer of alle bestanden aanwezig zijn:
- calculator.py
- test_calculator.py
- requirements.txt

## Volgende Stappen

1. ✅ Tests lokaal uitvoeren
2. ✅ Coverage rapport bekijken
3. ✅ Code naar Git repository pushen
4. ✅ CI/CD pipeline configureren
5. ✅ Automatische tests bij elke commit

## Handige Commando's

```bash
# Alleen multiply tests
pytest -k multiply

# Stop bij eerste failure
pytest -x

# Laatste gefaalde tests opnieuw
pytest --lf

# HTML coverage rapport
pytest --cov=calculator --cov-report=html
# Open htmlcov/index.html in browser
```

## Vragen?
Bekijk de uitgebreide documentatie in:
- README.md - Project overzicht
- DOCUMENTATIE.md - Gedetailleerde uitleg
