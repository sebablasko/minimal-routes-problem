#!/bin/bash

for folder in 6 30 250 6600 53000 211212; do
  echo "$folder"
  for (( counter=1; counter<6; counter++ ))
  do
    echo "$folder/salida_$counter.txt"
    #python main.py "$folder/nodos.txt" "$folder/arcos.txt" $counter
    python main.py "$folder/nodos.txt" "$folder/arcos.txt" $counter --dial
    python validate.py salida.txt "$folder/salida_$counter.txt"
  done
done 