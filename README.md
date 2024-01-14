## About the project

A simple script to handle multiple processes and services shutdown.

This script intends to kill processes that runs persistently on background even
if its features are not being used, thus wasting memory.


## How to use

You can call ./bin/taskkiller.bat at the terminal to run the script. It will
simply activate the required virtual environment (venv) and then run the
./src/rdcoder/taskkiller.py script.

The script will prompt for a list of processes you want to ignore, which means
they will be not shutdown this time.

Since some processes requires elevated privileges to be killed, you may run the
script as admin. You can also create a shortcut to the taskkiller.bat script
that automatically runs as such. To do so:

- Create a shortcut to taskkiller.bat;
- Open the shortcut Properties > Advanced...;
- Mark the option "Run as administrator" and press "OK".


## TODO list

- [ ] Implement a more user-friendly interactive mode;
- [ ] Add command line args to:
    - [ ] add, remove and list processes
    - [ ] ignore processes
    - [ ] run and shutdown taskkiller in the background.