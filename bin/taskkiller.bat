@echo off

@REM Get project directory path
SET dir=%~dp0
for %%I in ("%dir%\.") do set "dir=%%~dpI"

call "%dir%\.venv\Scripts\activate"
py "%dir%\src\rdcoder\taskkiller.py"