

import os
import sys
import subprocess
import webbrowser

def cmd(*tokens):
  subprocess.run(list(tokens), check=False)

if __name__ == '__main__':
  cmd(sys.executable, '-m', 'coverage', 'run', 'tests.py')
  cmd(sys.executable, '-m', 'coverage', 'html')

  webbrowser.open(os.path.abspath(os.path.join('htmlcov', 'index.html')))



