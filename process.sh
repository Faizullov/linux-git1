#!/bin/bash
rate=$(cat $1 | sed -n '/-1.0$/p' | awk -F, 'BEGIN{x=41}{x+=$18}END{print NR}')
cat $1 | awk -F, 'BEGIN{x=0; y=0} ($18!="-1") && ($18!="-1.0"){ x+=$18; y +=1} END{print "RATING_AVG " x/y}'
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
clean=$(cat $1 | awk -F, '($12!=0) && ($18!="-1") && ($18!="-1.0") {print $12}')
clean2=$(cat $1 | awk -F, '($12!=0) && ($18!="-1") && ($18!="-1.0") {print $18}')
cat $1 | awk -F, '$18 > 0{print $18 "," $12}' >> '/tmp/faiz17.csv'
#echo $tmp
gnuplot << EOP
    set terminal png size 300,400
    set output 'out1.png'
    set datafile separator  comma
    f(x) = m*x + b
    fit f(x) '/tmp/faiz17.csv' using 2:1 via m,b
    plot '/tmp/faiz17.csv' using 2:1 title 'Cleanliness' with points, f(x) title 'fit'
EOP

