
import os
import sys
import subprocess
import traceback
import shutil

sys.path.append(
  os.path.dirname(os.path.abspath(__file__))
)
import install_tools

def main(args=sys.argv):

  print('Attempting to install as many runtimes as possible under ./tools/')
  try:
    install_tools.main(args)
  except:
    traceback.print_exc()

  print('Testing which language development runtimes are available on this machine...')

  subdir_if_cmd_exists_map = [
    (['dotnet'], os.path.join('csharp_net_core') ),
    (['python'], os.path.join('python_pytest') ),
  ]
  runnable_subdir_demos = []
  for cmds, subdir in subdir_if_cmd_exists_map:
    if any([shutil.which(cmd) for cmd in cmds]):
      runnable_subdir_demos.append(subdir)

  print('{} demos may be run on this machine'.format(len(runnable_subdir_demos)))
  for demo_subdir in runnable_subdir_demos:
    print('> {}'.format(demo_subdir))






if __name__ == '__main__':
  main()


