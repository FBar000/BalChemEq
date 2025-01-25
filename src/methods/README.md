The `methods` package contains code for the individual steps of the calculation. The procedure is as follows. 

Suppose the user wants to balance `'H2 + O2 : H2O'`.

First, `validateChemEq` ensures that the input string satisfies the input criteria.

Then, `constructSystemMatrix.py` identifies the terms (`H2`, `O2`, `H2O`) and the atoms (`H`, `O`). For each atom, a list is created counting its occurence in each term. Occurence in reactants is counted positively and in products is counted negatively. 

```
   | H2 | O2 | H2O
 - | -- | -- | -- 
 H |  2 |  0 | -2
 O |  0 |  2 | -1

```

-- WIP -- 