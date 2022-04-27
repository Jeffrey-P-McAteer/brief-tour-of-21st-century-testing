
import os
import sys
import subprocess
import traceback
import shutil

from . import install_tools

def main(args=sys.argv):

  print('Attempting to install as many runtimes as possible under ./tools/')
  try:
    install_tools.main(args)
  except:
    traceback.print_exc()

  print('Testing which language development runtimes are available on this machine...')

  subdir_if_exists = [
    (['dotnet'], os.path.join('csharp_net_core')),
  ]






if __name__ == '__main__':
  main()


