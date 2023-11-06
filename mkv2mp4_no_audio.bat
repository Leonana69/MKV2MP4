@ECHO OFF 
CD/D "%~dp0"

:loop
IF "%~1"=="" GOTO :STOP

ffmpeg -i "%~1" -c:v libx264 -crf 20 -an "%~dpn1_x264.mp4"
shift/1
goto :loop

:STOP
echo Done.
pause>nul