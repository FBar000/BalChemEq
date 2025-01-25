The `methods` package contains code for the individual steps of the calculation. The procedure is as follows. 

Suppose the user wants to balance `'H2 + O2 : H2O'`.

- First, `validateChemEq.py` ensures that the input string satisfies the input criteria.

- Then, `constructSystemMatrix.py` identifies the terms (`H2`, `O2`, `H2O`) and the atoms (`H`, `O`). For each atom, a list is created counting its occurence in each term. Occurence in reactants is counted positively and in products is counted negatively. 

```
   | H2 | O2 | H2O
 - | -- | -- | -- 
 H |  2 |  0 | -2
 O |  0 |  2 | -1

```


- Next, `rowReduceEchelonDiophantine.py` reduces this matrix to row echelon form with the rule that numbers remain integers. This is validated by `validateRREDMatrix.py`


```
   | H2 | O2 | H2O
 - | -- | -- | -- 
 H |  1 |  0 | -1
 O |  0 |  2 | -1

```

- Finally, the pair of coefficients is extracted by `extractSolution.py`. The idea is that the reduced matrix shows the ratio between the coeficients of each term to the last one. Then, all the ratios are scaled so that the coefficient of the last term is multiplied by the same amount. This allows the reading of a sequence of integers that satisfy all equations. 

For example, if `A`, `B`, and `C` are the coefficients of the terms, the reduced matrix above says that `A = C` and `2B = C`. Here, `C` is multiplied by one in both equations, so `A = 2B = C`. The smallest integer solution is `(A B C) = (2 1 2)`.

- A further step by `wrapSolution.py` would incorporate this information into the original equation