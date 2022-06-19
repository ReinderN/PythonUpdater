# PythonUpdater

## What is it?

The Python Updater is a tool that can automaticaly update your python scripts without actually having to stop your program.

## How does it work?

It works by initiating a subprocess that runs your actual program and another process is running an updater. If an update is found it wil download the update and restart the process automatically and thus updating your script without needing to start an entire new python instance.

## Why do I need this?

This can be usefull if you have a program running on a lot of servers or computers and don't want to manually update everything.

## How can I implement this in my own project?

Well, it is really simple, just change the target ```p = multiprocessing.Process(target=program.main, args=(current_version,))``` on line 56 with your existing program that you want to have automatically update and that's it.
