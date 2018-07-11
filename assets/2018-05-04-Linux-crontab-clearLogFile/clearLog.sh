#!/bin/sh
for i in `find /root -name '*.log*' -size +10k`
do
	echo > $i
done