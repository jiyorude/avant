from unittest.mock import patch
import os

def clear():
    return os.system('cls' if os.name == 'nt' else 'clear')

def test_clear():
    with patch('os.system') as system:
        clear()
    system.assert_called_once_with('cls' if os.name == 'nt' else 'clear')

# 1 test passed in 0.01s
