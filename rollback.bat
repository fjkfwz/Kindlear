set PYTHONPATH=%~dp0DLLs;%~dp0libs;%~dp0lib
python.exe helper.py
if errorlevel 1 pause&&exit

if exist kindleear goto kindle
if exist kindleear-master\kindleear-master goto master-master
if exist kindleear-master goto master
echo "Cannot find KindleEar"
goto end

:kindle
if not exist kindleear\module-worker.yaml goto kindle-dir
python.exe appcfg.py --skip_sdk_update_check rollback kindleear\app.yaml
python.exe appcfg.py --skip_sdk_update_check rollback kindleear\module-worker.yaml
goto end

:kindle-dir
python.exe appcfg.py --skip_sdk_update_check rollback kindleear
goto end

:master
if not exist kindleear-master\module-worker.yaml goto master-dir
python.exe appcfg.py --skip_sdk_update_check rollback kindleear-master\app.yaml
python.exe appcfg.py --skip_sdk_update_check rollback kindleear-master\module-worker.yaml
goto end

:master-dir
python.exe appcfg.py --skip_sdk_update_check rollback kindleear-master
goto end

:master-master
if not exist kindleear-master\kindleear-master\module-worker.yaml goto mm-dir
python.exe appcfg.py --skip_sdk_update_check rollback kindleear-master\kindleear-master\app.yaml
python.exe appcfg.py --skip_sdk_update_check rollback kindleear-master\kindleear-master\module-worker.yaml
goto end

:mm-dir
python.exe appcfg.py --skip_sdk_update_check rollback kindleear-master\kindleear-master
goto end

:end
pause