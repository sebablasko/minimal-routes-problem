# Minimal-routes-problem
A solution for minimal routes problem using dijsktra and dijsktra dial's implementation.

In this repository you can find multiple files:

- `main.py`: The main program to execute the program to solve the minimal routes problem.
- `dijsktra.py`: A file that contains an implementation of dijsktra algorithm.
- `dial.py`: A file that contains an implementation of dijsktra algorithm with dial's flavor.
- `utils.py`: A file with a collection of methods usefull for simple shared operations between both algorithms.
- `validate.py`: A script to compare two output files of the minimal routes problem that compare the first and third columns, to check if the costs are the same for each node.
- `test.sh`: A bash script that runs a collection of test based on data supplied in each attached folder that runs some algoritm and check the correctness of the result with the provided results file.

## Execution

The program has a user manual:

```bash
$ python main.py -h

usage: main.py [-h] [--dial] [--so] nodosfile arcosfile originnode

Runs Dijsktra algorithm. Stores the output in a file.

positional arguments:
  nodosfile   file with nodos information
  arcosfile   File with arcos information
  originnode  Number of the origin node

optional arguments:
  -h, --help  show this help message and exit
  --dial      Use the Dial Dijsktra implementation
  --so        print results in standard output instead create a file
```

### Examples

A simple execution of the dijsktra version with results in a single file *salida.txt* is: 
`python main.py 6/nodos.txt 6/arcos.txt 1`

A simple execution of the dial's version with results in standard output is: `python main.py 6/nodos.txt 6/arcos.txt 1 --dial --so`

## Validation

As is well  known, the dijsktra algorithm can have multiple results with the same (optimal) cost. In the practice, that means that could exists more than one way to achieve the trip from source node to target node that share the same cost.

This property means a problem at the moment of check the correctness of the solution: The previous node visited for every trip from the source node to every other node could be different in two solutions, but both could be correct. What is always same (for all solutions) is the cost of the trip for the specified node from the source node.

## Performance

The dial's optimization has a great impact in my implementation of dijsktra algorithm. At check the test cases, the performance of dial's optimization means -in many cases- a save of XX%. In general terms, all the datasets has better results using the dial's version of the dijsktra algorithm.
