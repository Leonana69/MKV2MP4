# MKV2MP4  
Use ffmpeg to transform format  
将一个(或多个)x264编码的mkv拖到mkv2mp4_h264.bat上，若无需音频输出，可选择mkv2mp4_h264_NoAudio.bat  
hevc(x265)编码的mkv选择mkv2mp4_hevc.bat或mkv2mp4_hevc_NoAudio.bat  

ffmpeg:
	-i: input file name
	-c: codec name
	-codec: codec name
	-vcodec: coding, h264, mpeg4, wmv1, wmv2...
	-r: frame rate
	-s: frame size
	-b: bit rate
	-ar: audio rate
	-ac: audio channel number
	-ss: start time 00:00:00.0, with -t or -to, put -ss before -i can make clip more accurate
				   | h: m: s.ms |
	-t: clip duration
	-to: end time, should after -i
