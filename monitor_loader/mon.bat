@echo off
timeout /t 20 /nobreak
cd %USERPROFILE%\Desktop\monitor_loader

for %%f in (*.py) do (
    start pythonw %%f
    timeout /t 20 /nobreak
)
