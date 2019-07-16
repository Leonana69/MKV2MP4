@ECHO OFF 
CD/D "%~dp0"

:loop
IF "%~1"=="" GOTO :STOP

ffmpeg -i "%~1" -vcodec copy -acodec aac "%~dpn1.mp4"
shift/1
goto :loop

:STOP
echo Done.
pause>nul