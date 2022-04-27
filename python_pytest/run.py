

import os
import subprocess
import webbrowser

def cmd(*tokens):
  subprocess.run(list(tokens), check=False)

if __name__ == '__main__':
  print('TODO pytest example')



