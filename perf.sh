#!/bin/bash

GEN_CMD="./closure.py -generate"
#NLIN_CL_CMD="./closure.py -naive - "
LIN_CL_CMD="./closure.py -improved - "

TIMEFORMAT=%R;
echo -e "# \t nlin \t lin" 
n=10;
for i in `seq 100 100 1000`; do
  for j in `seq 1 $n`; do
 #   nlin_time=$( $GEN_CMD $i | { time  $NLIN_CL_CMD > /dev/null; } 2>&1)
	  lin_time=$( $GEN_CMD $i | { time $LIN_CL_CMD > /dev/null; } 2>&1)
    echo -e "$i \t $nlin_time \t $lin_time" 
  done
done
