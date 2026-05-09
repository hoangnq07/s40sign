@echo off
REM ========================================
REM S40 Certificate & Signing Tool
REM All-in-one script for Windows
REM ========================================

setlocal

REM Configuration
set KEYSTORE=certs\s40-keystore.jks
set ALIAS=s40cert
set STOREPASS=s40pass123
set KEYPASS=s40pass123
set VALIDITY=3650
set KEYALG=RSA
set KEYSIZE=2048

REM Create directories if not exist
if not exist "certs" mkdir certs
if not exist "apps" mkdir apps

REM Main menu
:menu
cls
echo ========================================
echo S40 Certificate ^& Signing Tool
echo ========================================
echo.
echo 1. Run GUI Application
echo 2. Create Certificate
echo 3. Sign JAR File
echo 4. Remove Signature from JAR
echo 5. Manage Certificate
echo 6. Build .exe
echo 7. Exit
echo.
set /p choice="Select option (1-7): "

if "%choice%"=="1" goto run_gui
if "%choice%"=="2" goto create_cert
if "%choice%"=="3" goto sign_jar
if "%choice%"=="4" goto remove_sig
if "%choice%"=="5" goto manage_cert
if "%choice%"=="6" goto build_exe
if "%choice%"=="7" goto end

echo Invalid choice!
pause
goto menu

REM ========================================
REM 1. Run GUI Application
REM ========================================
:run_gui
cls
echo Starting GUI Application...
echo.

if exist "dist\S40SignTool.exe" (
    echo Running .exe version...
    start "" "dist\S40SignTool.exe"
) else if exist "s40_sign_app.py" (
    echo Running Python version...
    python s40_sign_app.py
) else (
    echo Error: Application not found!
    echo Please build the application first.
)

pause
goto menu

REM ========================================
REM 2. Create Certificate
REM ========================================
:create_cert
cls
echo ========================================
echo Create Certificate
echo ========================================
echo.

if exist "%KEYSTORE%" (
    set /p overwrite="Keystore already exists. Overwrite? (y/N): "
    if /i not "%overwrite%"=="y" (
        echo Cancelled.
        pause
        goto menu
    )
)

echo Creating certificate...
echo.

keytool -genkeypair ^
    -alias %ALIAS% ^
    -keyalg %KEYALG% ^
    -keysize %KEYSIZE% ^
    -validity %VALIDITY% ^
    -keystore %KEYSTORE% ^
    -storepass %STOREPASS% ^
    -keypass %KEYPASS% ^
    -dname "CN=S40 Developer, OU=Mobile Dev, O=MyCompany, L=Hanoi, ST=Hanoi, C=VN"

if %ERRORLEVEL% EQU 0 (
    echo.
    echo ========================================
    echo Certificate created successfully!
    echo ========================================
    echo Keystore: %KEYSTORE%
    echo Alias: %ALIAS%
    echo Password: %STOREPASS%
) else (
    echo.
    echo Error: Cannot create certificate!
    echo Please check Java JDK is installed.
)

echo.
pause
goto menu

REM ========================================
REM 3. Sign JAR File
REM ========================================
:sign_jar
cls
echo ========================================
echo Sign JAR File
echo ========================================
echo.

set /p JAR_FILE="Enter JAR file path (or drag and drop): "

REM Remove quotes if present
set JAR_FILE=%JAR_FILE:"=%

if not exist "%JAR_FILE%" (
    echo Error: File not found: %JAR_FILE%
    pause
    goto menu
)

if not exist "%KEYSTORE%" (
    echo Error: Keystore not found!
    echo Please create certificate first (Option 2).
    pause
    goto menu
)

REM Check for old signature
echo Checking for old signature...
jarsigner -verify "%JAR_FILE%" >nul 2>&1
if %ERRORLEVEL% EQU 0 (
    echo Found old signature. Removing...
    
    REM Create temp directory
    set TEMP_DIR=%TEMP%\jar_temp_%RANDOM%
    mkdir "%TEMP_DIR%"
    
    REM Extract JAR
    jar xf "%JAR_FILE%" -C "%TEMP_DIR%"
    
    REM Remove signature files
    if exist "%TEMP_DIR%\META-INF\*.SF" del /Q "%TEMP_DIR%\META-INF\*.SF"
    if exist "%TEMP_DIR%\META-INF\*.RSA" del /Q "%TEMP_DIR%\META-INF\*.RSA"
    if exist "%TEMP_DIR%\META-INF\*.DSA" del /Q "%TEMP_DIR%\META-INF\*.DSA"
    
    REM Repack JAR
    cd "%TEMP_DIR%"
    jar cf "%JAR_FILE%" *
    cd "%~dp0"
    
    REM Cleanup
    rmdir /S /Q "%TEMP_DIR%"
    
    echo Old signature removed successfully.
)

REM Create signed JAR name
set JAR_DIR=%~dp1
set JAR_NAME=%~n1
set JAR_EXT=%~x1
set SIGNED_JAR=%JAR_DIR%%JAR_NAME%-signed%JAR_EXT%

echo.
echo Signing JAR file...
echo Input: %JAR_FILE%
echo Output: %SIGNED_JAR%
echo.

jarsigner -keystore "%KEYSTORE%" ^
    -storepass %STOREPASS% ^
    -keypass %KEYPASS% ^
    -signedjar "%SIGNED_JAR%" ^
    "%JAR_FILE%" ^
    %ALIAS%

if %ERRORLEVEL% EQU 0 (
    echo.
    echo ========================================
    echo JAR signed successfully!
    echo ========================================
    echo Signed file: %SIGNED_JAR%
    echo.
    echo Verify signature:
    echo jarsigner -verify -verbose -certs "%SIGNED_JAR%"
) else (
    echo.
    echo Error: Cannot sign JAR file!
)

echo.
pause
goto menu

REM ========================================
REM 4. Remove Signature from JAR
REM ========================================
:remove_sig
cls
echo ========================================
echo Remove Signature from JAR
echo ========================================
echo.

set /p JAR_FILE="Enter JAR file path (or drag and drop): "

REM Remove quotes if present
set JAR_FILE=%JAR_FILE:"=%

if not exist "%JAR_FILE%" (
    echo Error: File not found: %JAR_FILE%
    pause
    goto menu
)

REM Check if JAR has signature
jarsigner -verify "%JAR_FILE%" >nul 2>&1
if %ERRORLEVEL% NEQ 0 (
    echo JAR file has no signature.
    pause
    goto menu
)

echo Found signature in JAR.
set /p confirm="Remove signature? (y/N): "
if /i not "%confirm%"=="y" (
    echo Cancelled.
    pause
    goto menu
)

echo Removing signature...

REM Create backup
set BACKUP_FILE=%JAR_FILE%.bak
copy "%JAR_FILE%" "%BACKUP_FILE%" >nul
echo Backup created: %BACKUP_FILE%

REM Create temp directory
set TEMP_DIR=%TEMP%\jar_temp_%RANDOM%
mkdir "%TEMP_DIR%"

REM Extract JAR
jar xf "%JAR_FILE%" -C "%TEMP_DIR%"

REM Remove signature files
if exist "%TEMP_DIR%\META-INF\*.SF" del /Q "%TEMP_DIR%\META-INF\*.SF"
if exist "%TEMP_DIR%\META-INF\*.RSA" del /Q "%TEMP_DIR%\META-INF\*.RSA"
if exist "%TEMP_DIR%\META-INF\*.DSA" del /Q "%TEMP_DIR%\META-INF\*.DSA"

REM Repack JAR
cd "%TEMP_DIR%"
jar cf "%JAR_FILE%" *
cd "%~dp0"

REM Cleanup
rmdir /S /Q "%TEMP_DIR%"

echo.
echo ========================================
echo Signature removed successfully!
echo ========================================
echo Original file: %JAR_FILE%
echo Backup: %BACKUP_FILE%

echo.
pause
goto menu

REM ========================================
REM 5. Manage Certificate
REM ========================================
:manage_cert
cls
echo ========================================
echo Manage Certificate
echo ========================================
echo.
echo 1. View certificate info
echo 2. Check expiry date
echo 3. Delete certificate
echo 4. Export certificate
echo 5. Change password
echo 6. Back to main menu
echo.
set /p cert_choice="Select option (1-6): "

if "%cert_choice%"=="1" goto view_cert
if "%cert_choice%"=="2" goto check_expiry
if "%cert_choice%"=="3" goto delete_cert
if "%cert_choice%"=="4" goto export_cert
if "%cert_choice%"=="5" goto change_password
if "%cert_choice%"=="6" goto menu

echo Invalid choice!
pause
goto manage_cert

:view_cert
cls
echo ========================================
echo Certificate Information
echo ========================================
echo.
if not exist "%KEYSTORE%" (
    echo Keystore not found!
    pause
    goto manage_cert
)
keytool -list -v -keystore "%KEYSTORE%" -storepass %STOREPASS% -alias %ALIAS%
echo.
pause
goto manage_cert

:check_expiry
cls
echo ========================================
echo Check Expiry Date
echo ========================================
echo.
if not exist "%KEYSTORE%" (
    echo Keystore not found!
    pause
    goto manage_cert
)
keytool -list -v -keystore "%KEYSTORE%" -storepass %STOREPASS% -alias %ALIAS% | findstr /C:"Valid from"
echo.
pause
goto manage_cert

:delete_cert
cls
echo ========================================
echo Delete Certificate
echo ========================================
echo.
if not exist "%KEYSTORE%" (
    echo Keystore not found!
    pause
    goto manage_cert
)
set /p confirm="Are you sure you want to delete the certificate? (y/N): "
if /i not "%confirm%"=="y" (
    echo Cancelled.
    pause
    goto manage_cert
)
keytool -delete -alias %ALIAS% -keystore "%KEYSTORE%" -storepass %STOREPASS%
if %ERRORLEVEL% EQU 0 (
    echo Certificate deleted successfully!
) else (
    echo Error deleting certificate!
)
pause
goto manage_cert

:export_cert
cls
echo ========================================
echo Export Certificate
echo ========================================
echo.
if not exist "%KEYSTORE%" (
    echo Keystore not found!
    pause
    goto manage_cert
)
set CERT_FILE=certs\s40-cert.cer
keytool -exportcert -alias %ALIAS% -keystore "%KEYSTORE%" -storepass %STOREPASS% -file "%CERT_FILE%"
if %ERRORLEVEL% EQU 0 (
    echo Certificate exported successfully!
    echo File: %CERT_FILE%
) else (
    echo Error exporting certificate!
)
pause
goto manage_cert

:change_password
cls
echo ========================================
echo Change Password
echo ========================================
echo.
if not exist "%KEYSTORE%" (
    echo Keystore not found!
    pause
    goto manage_cert
)
echo NOTE: You need to update the password in this script!
echo.
set /p oldpass="Enter old password: "
set /p newpass="Enter new password: "
set /p newpass2="Re-enter new password: "

if not "%newpass%"=="%newpass2%" (
    echo Passwords do not match!
    pause
    goto manage_cert
)

keytool -storepasswd -keystore "%KEYSTORE%" -storepass %oldpass% -new %newpass%
if %ERRORLEVEL% EQU 0 (
    echo Keystore password changed successfully!
    echo.
    echo Changing key password:
    keytool -keypasswd -alias %ALIAS% -keystore "%KEYSTORE%" -storepass %newpass% -keypass %oldpass% -new %newpass%
    if %ERRORLEVEL% EQU 0 (
        echo Key password changed successfully!
        echo.
        echo NOTE: Update the password in this script:
        echo - Edit s40tool.bat
        echo - Change STOREPASS and KEYPASS values
    )
) else (
    echo Error changing password!
)
pause
goto manage_cert

REM ========================================
REM 6. Build .exe
REM ========================================
:build_exe
cls
echo ========================================
echo Build .exe Application
echo ========================================
echo.

if not exist "s40_sign_app.py" (
    echo Error: s40_sign_app.py not found!
    pause
    goto menu
)

echo Checking PyInstaller...
python -c "import PyInstaller" 2>nul
if %ERRORLEVEL% NEQ 0 (
    echo PyInstaller not found. Installing...
    pip install pyinstaller
)

echo.
echo Building application...
echo This may take a minute...
echo.

pyinstaller --onefile --windowed --name "S40SignTool" --clean s40_sign_app.py

if %ERRORLEVEL% EQU 0 (
    echo.
    echo ========================================
    echo Build successful!
    echo ========================================
    echo.
    echo File: dist\S40SignTool.exe
    echo.
    echo You can now run the .exe without Python!
) else (
    echo.
    echo Error building application!
)

echo.
pause
goto menu

REM ========================================
REM Exit
REM ========================================
:end
cls
echo.
echo Thank you for using S40 Certificate ^& Signing Tool!
echo.
timeout /t 2 >nul
exit /b 0
