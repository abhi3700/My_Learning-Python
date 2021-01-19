@echo off
rem ----------------------------------------------------------
rem This kills port no. - input by user
rem ----------------------------------------------------------
netstat -a -o -n
echo,
set /p pid= Enter PID (from above): 
taskkill /F /PID %pid%
pause
exit