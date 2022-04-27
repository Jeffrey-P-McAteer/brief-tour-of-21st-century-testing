
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
    (['dotnet'], os.path.join('csharp_net_core', 'run.py') ),
    (['python'], os.path.join('python_pytest', 'run.py') ),
  ]
  runnable_subdir_demos = []
  for cmds, subdir in subdir_if_cmd_exists_map:
    if any([shutil.which(cmd) for cmd in cmds]):
      runnable_subdir_demos.append(subdir)

  print('')
  print('{} demos may be run on this machine'.format(len(runnable_subdir_demos)))
  for demo_run_py in runnable_subdir_demos:
    print('> {}'.format(demo_run_py))


  print('')
  print('Running all demos...')
  print('')

  for demo_run_py in runnable_subdir_demos:
    print('> {} {}'.format(sys.executable, demo_run_py))
    subprocess.run([
      sys.executable, os.path.abspath(demo_run_py)
    ], check=False, cwd=os.path.dirname(os.path.abspath(demo_run_py)))





if __name__ == '__main__':
  main()


