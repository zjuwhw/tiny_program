alias awk="awk -F '\t' -v OFS='\t'"

input=$1

awk '$1!~/^#/{a="";b="";split($10,x,",");split($11,y,",");for(i=1;i<=$9;i++){a=a""(y[i]-x[i])",";b=b""(x[i]-$5)","};print $3,$5,$6,$13,$2,$4,$7,$8,0,$9,a,b}' $input > ${input%bed}.txt2bed.bed
