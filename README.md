# Opdracht 10: Geautomatiseerde Test in Bestaande Applicatie

## Overzicht
Dit project demonstreert een complete implementatie van testautomatisering met CI/CD-pijplijnen voor een Python Calculator applicatie.

## Projectstructuur
```
opdracht 10/
├── calculator.py           # Hoofdapplicatie
├── test_calculator.py      # Pytest test suite
├── requirements.txt        # Python dependencies
├── pytest.ini             # Pytest configuratie
├── .flake8                # Linting configuratie
├── .gitlab-ci.yml         # GitLab CI/CD pipeline
├── .github/workflows/     # GitHub Actions workflow
│   └── tests.yml
├── .travis.yml            # Travis CI configuratie
└── README.md              # Deze documentatie
```

## Installatie

### Vereisten
- Python 3.8 of hoger
- pip (Python package manager)

### Stappen
1. Clone of download dit project
2. Installeer de dependencies:
```bash
pip install -r requirements.txt
```

## Tests Uitvoeren

### Lokaal testen
```bash
# Alle tests uitvoeren
pytest

# Tests met verbose output
pytest -v

# Tests met coverage rapport
pytest --cov=calculator --cov-report=term

# Coverage rapport in HTML formaat
pytest --cov=calculator --cov-report=html
```

### Linting en code kwaliteit
```bash
# Code formatteren met Black
black calculator.py test_calculator.py

# Linting met Flake8
flake8 calculator.py test_calculator.py
```

## CI/CD Pijplijnen

### GitLab CI/CD (.gitlab-ci.yml)
De GitLab pipeline bestaat uit 3 stages:
1. **Test**: Voert alle pytest tests uit
2. **Lint**: Controleert code kwaliteit met flake8 en black
3. **Coverage**: Genereert coverage rapporten

**Activatie**: Automatisch bij push naar `main` branch of merge requests.

### GitHub Actions (.github/workflows/tests.yml)
De GitHub Actions workflow:
- Test op meerdere Python versies (3.8, 3.9, 3.10, 3.11)
- Voert tests, linting en coverage uit
- Upload coverage rapporten als artifacts

**Activatie**: Bij push of pull request naar `main` of `develop` branches.

### Travis CI (.travis.yml)
De Travis CI configuratie:
- Test op Python 3.8, 3.9, 3.10, 3.11
- Voert volledige test suite uit
- Stuurt email notificaties bij failures

**Activatie**: Automatisch bij elke commit.

## Test Coverage

De test suite dekt de volgende functionaliteiten:
- ✅ Optellen (add)
- ✅ Aftrekken (subtract)
- ✅ Vermenigvuldigen (multiply)
- ✅ Delen (divide)
- ✅ Error handling (division by zero)

## Configuratie Bestanden

### pytest.ini
Configureert pytest gedrag:
- Test discovery patterns
- Verbose output
- Custom markers voor test categorieën

### .flake8
Linting regels:
- Max line length: 88 (compatibel met Black)
- Exclude directories (cache, venv, etc.)

## Workflow

### Voor ontwikkelaars
1. Maak wijzigingen in de code
2. Voer lokaal tests uit: `pytest -v`
3. Controleer code kwaliteit: `flake8` en `black`
4. Commit en push naar repository
5. CI/CD pipeline voert automatisch alle tests uit
6. Bekijk resultaten in CI/CD dashboard

### CI/CD Proces
```
Code wijziging → Push/PR → CI/CD trigger → 
→ Dependencies installeren → Tests uitvoeren → 
→ Linting checks → Coverage rapport → 
→ Resultaat (✓ of ✗)
```

## Leerdoelen Behaald

✅ **Testautomatisering implementeren**
- Pytest framework gebruikt
- Fixtures voor test setup
- Meerdere test cases per functie
- Error handling tests

✅ **CI/CD-pijplijnen opzetten**
- GitLab CI/CD configuratie
- GitHub Actions workflow
- Travis CI setup
- Automatische test executie bij code wijzigingen

✅ **Best practices**
- Code coverage monitoring
- Linting en formatting
- Multi-version testing
- Artifact management

## Troubleshooting

### Tests falen lokaal
```bash
# Controleer Python versie
python --version

# Herinstalleer dependencies
pip install -r requirements.txt --force-reinstall
```

### CI/CD pipeline faalt
- Controleer of alle configuratie bestanden aanwezig zijn
- Verifieer dat requirements.txt correct is
- Bekijk CI/CD logs voor specifieke errors

## Uitbreidingsmogelijkheden

1. **Meer test types**
   - Integration tests
   - Performance tests
   - Parametrized tests

2. **Extra CI/CD features**
   - Deployment stages
   - Security scanning
   - Dependency updates (Dependabot)

3. **Code kwaliteit**
   - Type hints met mypy
   - Documentation coverage
   - Complexity analysis

## Conclusie

Dit project demonstreert een professionele setup voor testautomatisering en CI/CD. Alle tests worden automatisch uitgevoerd bij elke code wijziging, wat zorgt voor hoge code kwaliteit en betrouwbaarheid.
