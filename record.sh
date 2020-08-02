#! /usr/bin/env bash
if test -f lockfile; then
	echo found lockfile
	rec_pid=`cat lockfile`
	running=`ps ax |grep "$rec_pid" |grep "mp4"`

	if [ ! $running ]; then
		echo looks old
		rm lockfile && ./record.sh
	else
		echo $running
	fi
else
	ffmpeg -fflags nobuffer -rtsp_transport tcp -i rtsp://192.168.234.1/12 -flags +cgop -g 30 -t 180 $(date +%Y%m%d%Z%H%M%S).mp4 2> /dev/null  </dev/null & jobs -p >lockfile
fi

