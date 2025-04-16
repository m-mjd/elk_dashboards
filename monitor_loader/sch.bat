@echo off
set "filepath=%USERPROFILE%\Desktop\monitor_loader\mon.bat"

:: Check if the file exists
if not exist "%filepath%" (
    echo The specified file does not exist: "%filepath%"
    pause
    exit /b
)

reg add "HKCU\Software\Microsoft\Windows\CurrentVersion\Run" /v "MonitorStartup" /t REG_SZ /d "%filepath%" /f

:: Confirm if the operation was successful
if %errorlevel% equ 0 (
    echo The file has been successfully added to startup.
) else (
    echo There was an error adding the file to startup.
)

pause
