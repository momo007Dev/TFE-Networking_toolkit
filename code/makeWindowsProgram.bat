@echo off
title makeWindowsProgram
mode con cols=80 lines=16
color 02

:: Get the User's Desktop path
SETLOCAL
FOR /F "usebackq" %%f IN (`PowerShell -NoProfile -Command "Write-Host([Environment]::GetFolderPath('Desktop'))"`) DO (
    SET "DESKTOP_FOLDER=%%f"
)

echo [*] This script will attempt to build all python depencies into one windows executable
echo (*) The output will be available on the desktop (exe + img folder)

echo Creating one file executable...

:: Removes the current executable
if exist "%DESKTOP_FOLDER%\Networking Toolkit.exe" (
    DEL /S/Q "%DESKTOP_FOLDER%\Networking Toolkit.exe"
)
:: Removes the current img folder
if exist "%DESKTOP_FOLDER%\img\" (
    rmdir /S/Q "%DESKTOP_FOLDER%\img\"
)

XCOPY %CD%\img %DESKTOP_FOLDER%\img /Q /I
python -m PyInstaller --noconfirm --onefile --windowed --distpath "%DESKTOP_FOLDER%" --icon "C:/@Projet/TFE-Networking_toolkit/code/img/logo.ico" --name "Networking Toolkit" --add-data "C:/@Projet/TFE-Networking_toolkit/code/config_page.py;." --add-data "C:/@Projet/TFE-Networking_toolkit/code/exam_functions.py;." --add-data "C:/@Projet/TFE-Networking_toolkit/code/exam_page.py;." --add-data "C:/@Projet/TFE-Networking_toolkit/code/home_page.py;." --add-data "C:/@Projet/TFE-Networking_toolkit/code/subnet_functions.py;." --add-data "C:/@Projet/TFE-Networking_toolkit/code/subnet_page.py;." --add-data "C:/@Projet/TFE-Networking_toolkit/code/utils.py;." "C:/@Projet/TFE-Networking_toolkit/code/main.py"
rmdir /S/Q %cd%\build
rmdir /S/Q %cd%\__pycache__
DEL /S/Q "%CD%\Networking Toolkit.spec"

echo Finished !
color 06