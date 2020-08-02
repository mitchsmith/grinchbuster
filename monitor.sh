#!/bin/env bash

export GRINCH_BASE="/home/john/Projects/grinchbuster/"
export GRINCH_MEDIA="app/static/media/"
cd $GRINCH_BASE$GRINCH_MEDIA

if ps ax | grep ffmpeg | grep png
    
rm *.png
cd $GRINCH_BASE

