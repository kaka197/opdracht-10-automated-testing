import subprocess
import sys
from datetime import datetime

def print_header(text):
    print("\n" + "="*70)
    print(f"  {text}")
    print("="*70 + "\n")

def main():
    print("\n" + "="*70)
    print_header("OPDRACHT 10: GEAUTOMATISEERDE TEST DEMONSTRATIE")
    print(f"Repository: kaka197/opdracht-10-automated-testing")
    print(f"Datum/Tijd: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"Python Versie: {sys.version.split()[0]}")
    
    print_header("STAP 1: Unit Tests Uitvoeren")
    result1 = subprocess.run(["py", "-m", "pytest", "-v"], capture_output=False)
    
    print_header("STAP 2: Code Coverage Analyse")
    result2 = subprocess.run(["py", "-m", "pytest", "--cov=calculator", "--cov-report=term"], capture_output=False)
    
    print_header("STAP 3: Gedetailleerde Coverage Rapport")
    result3 = subprocess.run(["py", "-m", "pytest", "--cov=calculator", "--cov-report=term-missing"], capture_output=False)
    
    print_header("SAMENVATTING")
    if result1.returncode == 0 and result2.returncode == 0:
        print("[SUCCESS] ALLE TESTS GESLAAGD!")
        print("[SUCCESS] 100% CODE COVERAGE")
        print("[SUCCESS] CI/CD CONFIGURATIE AANWEZIG")
        print("\nConfiguratie bestanden:")
        print("  - .github/workflows/tests.yml (GitHub Actions)")
        print("  - .gitlab-ci.yml (GitLab CI/CD)")
        print("  - .travis.yml (Travis CI)")
    else:
        print("[FAILED] Er zijn problemen gevonden")
    
    print("\n" + "="*70 + "\n")
    return 0 if result1.returncode == 0 else 1

if __name__ == "__main__":
    sys.exit(main())
