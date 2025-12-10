import subprocess
import sys

def run_command(command, description):
    print(f"\n{'='*60}")
    print(f"Running: {description}")
    print(f"{'='*60}")
    result = subprocess.run(command, shell=True)
    return result.returncode == 0

def main():
    print("Geautomatiseerde Test Suite")
    print("="*60)
    
    all_passed = True
    
    if not run_command("pytest -v", "Unit Tests"):
        all_passed = False
    
    if not run_command("pytest --cov=calculator --cov-report=term", "Coverage Report"):
        all_passed = False
    
    if not run_command("flake8 calculator.py test_calculator.py --max-line-length=88", "Linting Check"):
        print("Warning: Linting issues found (non-blocking)")
    
    if not run_command("black --check calculator.py test_calculator.py", "Code Formatting Check"):
        print("Warning: Formatting issues found (non-blocking)")
    
    print("\n" + "="*60)
    if all_passed:
        print("✓ All tests passed successfully!")
        print("="*60)
        return 0
    else:
        print("✗ Some tests failed!")
        print("="*60)
        return 1

if __name__ == "__main__":
    sys.exit(main())
