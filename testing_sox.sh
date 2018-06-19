#! /bin/sh
num=0

while read arg1 arg2; do
  printf "Num: $num\n"
	printf "Start: ${arg1} End : ${arg2}\n"
  dif=$(python -c "print($arg2-$arg1)")
  printf "Difference is: $dif\n"
  ~/downloads/sox-14.4.2/sox 16k_1.wav 16k_1_$num.wav trim $arg1 $dif
  num=$((num+1))
# Pipe data into the while loop
done < /Users/albertzhang/desktop/text_files/biggerintervals.txt
