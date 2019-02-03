#!/bin/bash
# for (( counter=1; counter<7; counter++ ))
# do
# echo "6/$counter "
# python 1.py "$counter" > 6/asd.txt
# diff --strip-trailing-cr 6/asd.txt 6/salida_"$counter".txt
# done
# printf "\n"

# for (( counter=1; counter<6; counter++ ))
# do
# echo "6600/$counter "
# python 3.py "$counter" > aux.txt
# diff --strip-trailing-cr aux.txt 6600/salida_"$counter".txt
# read varname
# done
# printf "\n"

# for (( counter=1; counter<10; counter++ ))
# do
# echo "53000/$counter "
# python main.py "$counter" > aux.txt
# python validate.py aux.txt 53000/salida_"$counter".txt
# done
# printf "\n"

for folder in 6 30 250 6600 53000 211212; do
  echo "$folder"
  for (( counter=1; counter<6; counter++ ))
  do
    echo "$folder/salida_$counter.txt"
    time python main.py "$folder/nodos.txt" "$folder/arcos.txt" $counter --dial
    python validate.py salida.txt "$folder/salida_$counter.txt"
  done
done 