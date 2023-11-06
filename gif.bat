set filelink=%1
set filecolor=%1.png
ffmpeg -i %filelink% -r 24 -vf fps=24,scale=480:-1:flags=lanczos,palettegen -y %filecolor%
ffmpeg -v warning -i %filelink% -i %filecolor% -r 24 -lavfi fps=12,scale=480:-1:flags=lanczos[x];[x][1:v]paletteuse -y %filelink%.gif && del /F /S /Q %filecolor%
exit