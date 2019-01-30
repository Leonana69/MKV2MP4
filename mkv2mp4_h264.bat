@ECHO OFF 
CD/D "%~dp0"

:loop
IF "%~1"=="" GOTO :STOP

ffmpeg -i "%~1" -vcodec copy -acodec libfdk_aac -profile:a aac_he -vbr 2 "%~dpn1.mp4"
shift/1
goto :loop

:STOP
echo Done.
pause>nul