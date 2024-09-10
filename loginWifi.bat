@echo off
REM 连接到 Wi-Fi 网络 JXUST-WLAN
netsh wlan connect name="JXUST-WLAN"

REM 等待几秒钟以确保连接成功
timeout /t 2 /nobreak >nul


REM 运行 Python 脚本
python ./loginWifi/loginWifi.py

REM 检查 Python 脚本是否成功运行
echo helloWorld!!

REM 暂停以查看输出
timeout /t 2 /nobreak >nul

pause
