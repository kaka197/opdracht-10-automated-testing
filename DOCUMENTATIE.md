# Uitgebreide Documentatie: Testautomatisering & CI/CD

## Inhoudsopgave
1. [Introductie](#introductie)
2. [Testautomatisering](#testautomatisering)
3. [CI/CD Pijplijnen](#cicd-pijplijnen)
4. [Implementatie Details](#implementatie-details)
5. [Best Practices](#best-practices)

---

## Introductie

### Wat is Testautomatisering?
Testautomatisering is het proces waarbij software tests automatisch worden uitgevoerd zonder menselijke tussenkomst. Dit zorgt voor:
- **Snellere feedback** bij code wijzigingen
- **Consistente test uitvoering**
- **Hogere code kwaliteit**
- **Minder menselijke fouten**

### Wat is CI/CD?
CI/CD staat voor Continuous Integration / Continuous Deployment:
- **CI (Continuous Integration)**: Automatisch code integreren en testen
- **CD (Continuous Deployment)**: Automatisch deployen naar productie

---

## Testautomatisering

### Pytest Framework

#### Waarom Pytest?
- Eenvoudige syntax
- Krachtige fixtures
- Uitgebreide plugin ecosystem
- Goede error reporting

#### Test Structuur
```python
# test_calculator.py
import pytest
from calculator import Calculator

@pytest.fixture
def calculator():
    """Fixture die een Calculator instance aanmaakt voor elke test"""
    return Calculator()

def test_multiply(calculator):
    """Test de multiply functie met verschillende inputs"""
    assert calculator.multiply(2, 3) == 6
    assert calculator.multiply(-1, 5) == -5
```

#### Fixtures
Fixtures zijn herbruikbare setup code:
```python
@pytest.fixture
def calculator():
    return Calculator()
```

Voordelen:
- DRY principe (Don't Repeat Yourself)
- Automatische cleanup
- Dependency injection

#### Assertions
Pytest gebruikt standaard Python `assert`:
```python
assert calculator.add(2, 3) == 5
assert calculator.divide(10, 2) == 5
```

#### Exception Testing
Test of exceptions correct worden gegooid:
```python
with pytest.raises(ValueError):
    calculator.divide(10, 0)
```

### Code Coverage

#### Wat is Coverage?
Coverage meet welk percentage van je code door tests wordt uitgevoerd.

#### Coverage Commando's
```bash
# Basis coverage
pytest --cov=calculator

# Met terminal rapport
pytest --cov=calculator --cov-report=term

# Met HTML rapport
pytest --cov=calculator --cov-report=html
```

#### Coverage Interpretatie
- **90-100%**: Uitstekend
- **80-90%**: Goed
- **70-80%**: Acceptabel
- **<70%**: Verbetering nodig

---

## CI/CD Pijplijnen

### GitLab CI/CD

#### Configuratie (.gitlab-ci.yml)
```yaml
stages:
  - test
  - lint
  - coverage
```

#### Stages Uitleg
1. **Test Stage**: Voert alle pytest tests uit
2. **Lint Stage**: Controleert code kwaliteit
3. **Coverage Stage**: Genereert coverage rapporten

#### Variables
```yaml
variables:
  PIP_CACHE_DIR: "$CI_PROJECT_DIR/.cache/pip"
```
Caching versnelt pipeline uitvoering.

#### Artifacts
```yaml
artifacts:
  paths:
    - htmlcov/
  expire_in: 1 week
```
Bewaart coverage rapporten voor 1 week.

### GitHub Actions

#### Workflow Structuur
```yaml
name: Python Tests
on:
  push:
    branches: [ main, develop ]
  pull_request:
    branches: [ main, develop ]
```

#### Matrix Testing
```yaml
strategy:
  matrix:
    python-version: ['3.8', '3.9', '3.10', '3.11']
```
Test op meerdere Python versies tegelijk.

#### Steps
1. **Checkout**: Code ophalen
2. **Setup Python**: Python versie installeren
3. **Install Dependencies**: Packages installeren
4. **Run Tests**: Tests uitvoeren
5. **Upload Artifacts**: Resultaten bewaren

### Travis CI

#### Configuratie (.travis.yml)
```yaml
language: python
python:
  - "3.8"
  - "3.9"
  - "3.10"
  - "3.11"
```

#### Lifecycle
1. **before_install**: Pre-setup
2. **install**: Dependencies installeren
3. **script**: Tests uitvoeren
4. **after_success**: Success acties

---

## Implementatie Details

### Project Setup

#### 1. Dependencies Installeren
```bash
pip install -r requirements.txt
```

#### 2. Tests Schrijven
- Gebruik duidelijke test namen
- Test één functionaliteit per test
- Gebruik fixtures voor setup
- Test edge cases

#### 3. Lokaal Testen
```bash
pytest -v
```

#### 4. CI/CD Configureren
- Kies een platform (GitLab, GitHub, Travis)
- Maak configuratie bestand
- Push naar repository
- Controleer pipeline resultaten

### Test Best Practices

#### 1. AAA Pattern
```python
def test_add():
    # Arrange
    calc = Calculator()
    
    # Act
    result = calc.add(2, 3)
    
    # Assert
    assert result == 5
```

#### 2. Descriptive Names
```python
# Goed
def test_divide_by_zero_raises_value_error():
    pass

# Slecht
def test_div():
    pass
```

#### 3. Test Isolation
Elke test moet onafhankelijk zijn:
```python
@pytest.fixture
def calculator():
    return Calculator()  # Nieuwe instance per test
```

#### 4. Edge Cases
Test grenzen en speciale gevallen:
```python
def test_multiply_edge_cases(calculator):
    assert calculator.multiply(0, 10) == 0
    assert calculator.multiply(-1, -1) == 1
    assert calculator.multiply(1, 1) == 1
```

---

## Best Practices

### Code Kwaliteit

#### 1. Linting (Flake8)
Controleert code stijl en potentiële bugs:
```bash
flake8 calculator.py test_calculator.py
```

#### 2. Formatting (Black)
Automatische code formatting:
```bash
black calculator.py test_calculator.py
```

#### 3. Type Hints
Verbeter code leesbaarheid:
```python
def multiply(self, a: int, b: int) -> int:
    return a * b
```

### CI/CD Best Practices

#### 1. Fast Feedback
- Houd tests snel (<5 minuten)
- Gebruik caching
- Parallelliseer waar mogelijk

#### 2. Fail Fast
- Stop bij eerste failure
- Duidelijke error messages
- Logboeken bewaren

#### 3. Consistent Environment
- Pin dependency versies
- Gebruik containers
- Test op target platforms

#### 4. Security
- Geen secrets in code
- Gebruik environment variables
- Scan dependencies

### Workflow Tips

#### 1. Pre-commit Hooks
Run tests voor commit:
```bash
# .git/hooks/pre-commit
pytest -v
```

#### 2. Branch Protection
- Require passing tests
- Code review verplicht
- Up-to-date branches

#### 3. Notifications
- Email bij failures
- Slack integratie
- Dashboard monitoring

---

## Conclusie

Deze implementatie demonstreert:
- ✅ Complete testautomatisering met pytest
- ✅ Meerdere CI/CD platforms (GitLab, GitHub, Travis)
- ✅ Code coverage monitoring
- ✅ Linting en formatting
- ✅ Best practices en documentatie

### Volgende Stappen
1. Voeg meer test cases toe
2. Implementeer integration tests
3. Setup deployment pipeline
4. Monitor test metrics
5. Continuous improvement

---

## Resources

### Documentatie
- [Pytest Documentation](https://docs.pytest.org/)
- [GitLab CI/CD](https://docs.gitlab.com/ee/ci/)
- [GitHub Actions](https://docs.github.com/en/actions)
- [Travis CI](https://docs.travis-ci.com/)

### Tools
- **pytest**: Testing framework
- **pytest-cov**: Coverage plugin
- **black**: Code formatter
- **flake8**: Linter

### Commando Referentie
```bash
# Tests
pytest                          # Run alle tests
pytest -v                       # Verbose output
pytest -k "multiply"           # Run specifieke tests
pytest --lf                    # Run alleen failed tests

# Coverage
pytest --cov                   # Coverage rapport
pytest --cov-report=html       # HTML rapport

# Linting
flake8 .                       # Lint alle files
black .                        # Format alle files
black --check .                # Check formatting
```
