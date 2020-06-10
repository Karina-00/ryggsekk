# Solving the Knapsack Problem

> Python 3.5+

## Run

```sh
python3 main.py [-h/-d/-f]
# -h    for value/size heuristic
# -d    for dynamic search (optimised solution)
# -f    for brute force exhaustive search (optimised solution)
```

## Data

```py
# from stdin or from file via stream redirection
c               # max container Capacity
n               # Number of items' characteristics
s(0) v(0)       # characteristics of n elements
… …             # Size and Value of next elements
s(n-1) s(n-1)   # separated by space
```

> Total of `n+2` lines

Data is read by main and `Item` objects are created based on the characteristics.
