import os
import sys, getopt
import re
import datetime

opts, args = getopt.getopt(sys.argv[1:], 'i:', 'input=')
filename = ''
for o, a in opts:
	if o in ('-i', 'input='):
		filename = a.rstrip('/')

if filename == '':
	print('input filename using -i \"filename.txt\"')
	exit()

preamble = re.findall(r"([a-zA-Z\-0-9]+)\.txt", filename)
f = open(filename, encoding='utf-8')
time_stamp = f.readlines()
inname = time_stamp[0].rstrip()
print(inname)

audio = '-c:a copy'
format_judge = re.findall(r"\.mkv", inname)
if len(format_judge) == 1: # it's mkv
	audio = '-c:a aac -b:a 320k'

for line in time_stamp[1:]:
	if line[0] == '#':
		continue
	be = re.findall(r"\d*:*\d{1,2}:\d{1,2}\.{0,1}?\d{1,2}", line)
	na = re.findall(r"[\u4E00-\u9FA5]+[a-zA-Z0-9]*", line)
	outname = ''.join(na)+'.mp4'
	# print(be)
	bg = re.findall(r"\d+\.*\d*", be[0])
	ed = re.findall(r"\d+\.*\d*", be[1])
	[bgm, bgs] = [edm, eds] = [0, 0]
	if len(bg) > 2:
		bgm = int(bg[1]) + 60 * int(bg[0])
		bgs = float(bg[2])
	else:
		bgm = int(bg[0])
		bgs = float(bg[1])
	
	if len(ed) > 2:
		edm = int(ed[1]) + 60 * int(ed[0])
		eds = float(ed[2])
	else:
		edm = int(ed[0])
		eds = float(ed[1])

	dm = edm - bgm
	ds = eds - bgs
	if ds < 0:
		ds += 60.0
		dm -= 1

	cmd = '%s %s -i \"%s\" -t %d:%.1f -f mp4 -pix_fmt yuv420p -c:v libx264 -crf 14 %s %s -hide_banner -y' %('ffmpeg.exe -ss', be[0], inname, dm, ds, audio, preamble[0] + '-' + outname)
	# -pix_fmt yuv420p for thumbnails
	print(cmd)
	os.system(cmd)
# '.\ffmpeg.exe -ss 00:01:23.40 -i '.\Blue rain.mp4' -c:v libx265 -crf 18 -c:a copy -to 00:03:18.0 output.mp4 -y'