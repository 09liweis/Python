#!/bin/sh

echo "<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">" >> mkpic.html
echo "<html>" >> mkpic.html
echo " <head>" >> mkpic.html
echo "  <title>Pictures</title>" >> mkpic.html
echo " </head>" >> mkpic.html
echo " <body>" >> mkpic.html
echo "  <h1>Pictures</h1>" >> mkpic.html
echo "<table>" >> mkpic.html
echo "<tr>" >> mkpic.html

columns=$1
i=1
shift
while test ${#} -gt 0
do
    pic=$1
    if [ -e "$pic" ]
    then
        i=`expr $i + 1`
        echo "<td><img src=\"$pic\" height=100></td>" >> mkpic.html
    fi
    if [ `expr $i % $columns` = 0 ]
    then
        echo "</tr>" >> mkpic.html
        echo "<tr>" >> mkpic.html
    fi
    shift
done
echo "</tr>" >> mkpic.html
echo "</table>" >> mkpic.html
echo " </body> </html>" >> mkpic.html