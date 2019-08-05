@echo off
@rem --parallel 4
@rem --build-exe
@rem U:\Users\JasonD\venv\wxPython\Scripts\activate

@rem region START VIRTUALENV

echo "Setting up env"
echo "##############"

rem This file is UTF-8 encoded, so we need to update the current code page while executing it
for /f "tokens=2 delims=:." %%a in ('"%SystemRoot%\System32\chcp.com"') do (
    set "_OLD_CODEPAGE=%%a"
)
if defined _OLD_CODEPAGE (
    "%SystemRoot%\System32\chcp.com" 65001 > nul
)

set "VIRTUAL_ENV=U:\Users\JasonD\venv\wxPython"

if not defined PROMPT (
    set "PROMPT=$P$G"
)

if defined _OLD_VIRTUAL_PROMPT (
    set "PROMPT=%_OLD_VIRTUAL_PROMPT%"
)

if defined _OLD_VIRTUAL_PYTHONHOME (
    set "PYTHONHOME=%_OLD_VIRTUAL_PYTHONHOME%"
)

set "_OLD_VIRTUAL_PROMPT=%PROMPT%"
set "PROMPT=(wxPython) %PROMPT%"

if defined PYTHONHOME (
    set "_OLD_VIRTUAL_PYTHONHOME=%PYTHONHOME%"
    set PYTHONHOME=
)

if defined _OLD_VIRTUAL_PATH (
    set "PATH=%_OLD_VIRTUAL_PATH%"
) else (
    set "_OLD_VIRTUAL_PATH=%PATH%"
)

set "PATH=%VIRTUAL_ENV%\Scripts;%PATH%"

:END
if defined _OLD_CODEPAGE (
    "%SystemRoot%\System32\chcp.com" %_OLD_CODEPAGE% > nul
    set "_OLD_CODEPAGE="
)



rem endregion

echo "Starting build"
echo "##############"

rem  -c, --console, --nowindowed
rem  	Open a console window for standard i/o (default)
rem  -w, --windowed, --noconsole
rem  --upx-dir dist
rem SysInfoDashboard.spec

rem     --onefile ^

python -m PyInstaller ^
    --onefile ^
    --add-binary dist\dash-ico-01.ico;. ^
    -i dist\dash-ico-01.ico ^
    --icon dist\dash-ico-01.ico ^
    --clean ^
    --console ^
    --name SysInfoDashboard^
    GW2_MappingTool.py

pause
exit