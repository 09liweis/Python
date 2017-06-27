#!/bin/sh

path="/courses/webspace/cscb09w16/bin"

for pic in "$1"/*
do
    picName=${pic##*/}
    picInfo="$($path/exiftime -tg $pic)"
    mkdir "./"
    year=${picInfo:17:4}
    month=${picInfo:22:2}
    dest=$year/$month/$picName
    if [ ! -d "$year" ]
    then
        mkdir "$year"
    fi
    if [ ! -d "$year/$month" ]
    then
        mkdir "$year/$month"
        cp -r "$pic" "$dest"
    else
        cp -r "$pic" "$dest"
    fi
done