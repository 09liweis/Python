#!/bin/sh

echo "<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">" >> mkpic.html
echo "<html>" >> mkpic.html
echo " <head>" >> mkpic.html
echo "  <title>Pictures</title>" >> mkpic.html
echo " </head>" >> mkpic.html
echo " <body>" >> mkpic.html
echo "  <h1>Pictures</h1>" >> mkpic.html

columns=$1
for yearD in "$2"/*
do
    year=${yearD##*/}
    if [ -d $year ]
    then
        echo "<h2>$year</h2>" >> mkpic.html
        echo "<table>" >> mkpic.html
        echo "<tr>" >> mkpic.html
        i=1
        for dateD in "$yearD"/*
        do
            if [ -d $dateD ]
            then
                for pic in "$dateD"/*
                do
                    echo "<td><img src=\"$pic\" height=100></td>" >> mkpic.html
                    if [ `expr $i % $columns` = 0 ]
                    then
                        echo "</tr>" >> mkpic.html
                        echo "<tr>" >> mkpic.html
                    fi
                    i=`expr $i + 1`
                done
            fi
        done
        echo "</tr>" >> mkpic.html
        echo "</table>" >> mkpic.html
    fi
done


echo " </body> </html>" >> mkpic.html