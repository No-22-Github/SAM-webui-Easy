@echo off
echo Checking Python, pip, and Node.js installation...

python --version 2>&1
if errorlevel 1 (
    echo Error: Python is not installed or not found in the system path.
    pause
    exit /b 1
)

pip --version 2>&1
if errorlevel 1 (
    echo Error: pip is not installed or not found in the system path.
    pause
    exit /b 1
)

node --version 2>&1
if errorlevel 1 (
    echo Error: Node.js is not installed or not found in the system path.
    pause
    exit /b 1
)

echo All dependencies are present. Nice work!

@echo on

rem Create a virtual environment and install requirements
echo Creating virtual environment
python -m venv venv

echo Activating virtual environment

call venv\Scripts\activate.bat

echo Installing requirements

pip install -r requirements-AMD.txt

echo Installing Node.js dependencies
npm install -g typescript
npm install
echo Compiling TypeScript to JavaScript
tsc

echo Setup complete

pause