
import os
import subprocess
import webbrowser

def cmd(*tokens):
  subprocess.run(list(tokens), check=False)

if __name__ == '__main__':
  # Just run tests & report commands verbatim
  cmd('dotnet', 'test')
  cmd('minicover', 'instrument', '--sources', '**/*.cs', '--tests', '**/*.cs')
  cmd('dotnet', 'test', '--no-build')
  cmd('minicover', 'htmlreport')

  webbrowser.open(os.path.abspath(os.path.join('coverage-html', 'index.html')))

  

