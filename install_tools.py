
import os
import sys
import subprocess
import traceback
import shutil
import urllib.request
import zipfile
import tarfile
import io

def directory_contains_data(d):
  if not os.path.exists(d):
    return False
  return len(os.listdir(d)) > 0

def request_as_bytesio(get_url):
  response = urllib.request.urlopen(get_url)
  while len( response.headers.get('Location', '') ) > 1:
    new_url = response.headers.get('Location', '')
    print('Redirecting {} to {}'.format(get_url, new_url))
    get_url = new_url
    response = urllib.request.urlopen(get_url)
  # We have a response object w/o Location redirect header
  print('Downloading {} to :memory:'.format(get_url))
  file_data = response.read()
  return io.BytesIO(file_data)

def download_tar_to(get_url, out_dir):
  os.makedirs(out_dir, exist_ok=True)
  data = request_as_bytesio(get_url)
  t = tarfile.open(fileobj=data)
  print('Extracting to {}'.format(out_dir))
  t.extractall(out_dir)


def install_dotnet_core_runtime():
  dotnet_core_dir = os.path.abspath(os.path.join('tools', 'dotnet_core'))
  if not directory_contains_data(dotnet_core_dir):
    print('Installing .net core runtime to {}'.format(dotnet_core_dir))
    download_tar_to(
      'https://download.visualstudio.microsoft.com/download/pr/9d8c7137-2091-4fc6-a419-60ba59c8b9de/db0c5cda94f31d2260d369123de32d59/dotnet-sdk-6.0.202-linux-x64.tar.gz',
      os.path.abspath(os.path.join('tools', 'dotnet_core'))
    )

  print('Adding {} to PATH'.format(dotnet_core_dir))
  os.environ['PATH'] = dotnet_core_dir+os.pathsep+os.environ.get('PATH', '')

  # Also see if $HOME/.dotnet/tools exists & add it
  dotnet_tools = os.path.abspath( os.path.join(os.environ.get('HOME', ''), '.dotnet', 'tools') )
  if os.path.exists(dotnet_tools):
    print('Adding {} to PATH'.format(dotnet_tools))
    os.environ['PATH'] = dotnet_tools+os.pathsep+os.environ.get('PATH', '')

  print('Setting DOTNET_ROOT={}'.format(dotnet_core_dir))
  os.environ['DOTNET_ROOT'] = dotnet_core_dir





def main(args=sys.argv):
  orig_cwd = os.getcwd()
  script_dir = os.path.dirname(os.path.abspath(__file__))
  if not script_dir == os.getcwd():
    print('WARNING: install_tools.py is not being run from repository root.')
    print('Changing directory to {}'.format(script_dir))
    os.chdir(script_dir)

  install_dotnet_core_runtime()

  if 'spawn-shell' in args or 'interact' in args or 'interactive' in args or 'i' in args:
    print('Spawning bash shell with development environment setup...')
    subprocess.run(['bash'], cwd=orig_cwd)



if __name__ == '__main__':
  main()

