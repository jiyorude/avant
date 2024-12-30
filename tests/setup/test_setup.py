import subprocess

def test_setup():
    result = subprocess.run(['python', 'setup.py', '--version'], capture_output=True, text=True)
    assert result.returncode == 0
    assert '0.1.2' in result.stdout

# 1 passed in 0.16s, test file temporarily moved to root directory where setup.py was found to test.
