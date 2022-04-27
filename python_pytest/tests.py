
import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
import program

if __name__ == '__main__':
  assert program.is_prime(2), "2 should be prime"
  assert program.is_prime(3), "3 should be prime"
  assert not program.is_prime(4), "4 should not be prime"
  assert not program.is_prime(16), "16 should not be prime"

