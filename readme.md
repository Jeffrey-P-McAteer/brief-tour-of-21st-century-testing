
# A Brief Tour of 21st Century Test Tools

This repository contains sample code for several languages and runtimes. The `run_all.py` script
will:

 - Run `install_tools.py`
 - For all tools which your machine has available:
    - Move into corresponding sub-directory
    - Compile code
    - Run unit tests
    - Generate report
 - Open all reports in your default web browser

Caveat: `install_tools.py` only downloads x86_64 linux versions of tools. TODO: os detection & swap URLs for windows x86_64 systems.

```bash
python run_all.py

```




