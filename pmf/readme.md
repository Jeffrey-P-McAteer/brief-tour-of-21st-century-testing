
# Project Metrics Framework

This is a small python library which supports storing metrics attached to a project
within a directory (defaulting to `.pmf/`, which may or may not be kept under git version control).


# Example Use

An example use is:

 - use `pip` to install `pmf`
 - write the following script, `my_metrics.py`:

```python
import os

import pmf

# The metric I want to count is lines of code over time, so this python code grabs that number:
total_lines = 0
for file_name in os.listdir('pmf'):
  src_file_path = os.path.join('pmf', file_name)
  if src_file_path.endswith('.py'):
    with open(src_file_path, 'r') as fd:
      total_lines += len( [x for x in fd.read().splitlines()] )
      

# Now that I've computed my metric (total_lines), add it to the graph!
pmf.record_metrics(
  total_lines=total_lines,
)

# Optional, the .record_metrics() call is all that is necessary to add a dictionary of keys + values
# to .pmf/metrics.json and generate a new .pmf/metrics.svg grapg.
# .open_report() just opens .pmf/metrics.svg in your default app / web browser.
pmf.open_report()

```

# More uses

The interface is quite simple, and designed to let you focus on measuring metrics (unit test numbers, size of repo, speed tests of some important functions).

TODO concrete unit test / benchmark demos here


