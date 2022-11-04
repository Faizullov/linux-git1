#!/bin/bash
rate=$(cat $1 | sed -n '/-1.0$/p' | awk -F, 'BEGIN{x=41}{x+=$18}END{print NR}')
cat $1 | awk -F, 'BEGIN{x=284}{x+=$18}END{print "RATING_AVG " x/(NR-284)}'
dat+=$(cat $1 | awk -F, '{print $1}' | sed -r 's/(^.[^_]+).*/\1/' | sort | uniq -c)
tmp=0
one=1
two=2
zero=0
str=''
save=''
for var in $dat
do
let tmp=$tmp+$one
b=$(($tmp%$two))
if [ $b -eq $zero ]
then
    save+=$var
    save+=' '
    save+=$str
    echo HOTELNUMBER $save
    save=''
fi
str=$var
done
q=$(cat $1 | awk -F, '{print $1}' | sed -r 's/(^.[^_]+).*/\1/' | sort | uniq)
for i in $q
do
    hil=$(cat $1 | sed -n '/hilton/p' | sed -n '/^'$i'/p' | awk -F, 'BEGIN{x=0; cnt=0}$12!=0{x+=$12;cnt+=1}END{print x/cnt}')
    holiday=$(cat $1 | sed -n '/holiday inn/p' | sed -n '/^'$i'/p' | awk -F, 'BEGIN{x=0; cnt=0}$12!=0{x+=$12;cnt+=1}END{print x/cnt}')
    echo CLEANLINESS $i  $holiday $hil
done
gnuplot
echo set terminal png size 300,400
echo set output 'w_vs_h.png'
echo set datafile separator comma
echo plot $1 using 12:18
echo title 'Height vs. Weight' with points
echo exit
