
import sys
import os
import math

def main(args=sys.argv):
  if len(args) < 2:
    running_binary = os.path.abspath(__file__)
    print('Usage: {} number [number2, number3, ...]'.format(running_binary))
    print('Prints primality test for each integer given.')
  else:
    for arg in args[1:]:
      n = int(arg)
      if is_prime(n):
        print('{} is Prime'.format(n))
      else:
        print('{} is not Prime'.format(n))


def is_prime(n):
  if n == 2 or n == 3:
      return True

  if n <= 1 or n % 2 == 0 or n % 3 == 0:
      return False

  for i in range(5, int(math.sqrt(n))+1, 6):
    if n % i == 0 or n % (i+2) == 0:
      return False

  return True


if __name__ == '__main__':
  main()

