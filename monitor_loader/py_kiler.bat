@echo off
powershell.exe -NoProfile -Command "Get-Process -Name python, pythonw, firefox -ErrorAction SilentlyContinue | Stop-Process -Force"
