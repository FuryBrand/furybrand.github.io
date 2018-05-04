#!/bin/sh
for I in `find /root -size +10000k `
do
	echo > $i
done