# BCE

This is a project dedicated to balancing chemical equations. It is intended as a tool for building other programs. Given an equation as a string, this project contains programs to find the balancing coefficients, rewrite the chemical equation, as well as show the work. This is possible by representing chemical equations as systems of homogenous diophantine linear equations and using matrix operations. Currently, this program supports equations that have one unique solution. Chemically, this would mean equations that represent exactly one reaction.

## Installation

To install the project, run 

> `$ git clone https://github.com/FBar000/BalChemEq.git`

Then, fetch the dependencies via

> `pip install -r requirements.txt`

## Usage 

As mentioned, this project is a tool. Every method has documentation.Anyways, here's a brief startup guide for the main methods of this file, contained in `BCE.py.`

### Equation Criteria

Conceptually, the programs in this project support chemical equations that encode exactly one chemical reaction. The reactant and product sides are separated by a colon (`:`) (E.g. `H2 + O2 : H2O`). 

When implementing such an equation in a string, the following 'mechanical' criteria must also be met:

- The input only contains " ", "+", ":", "(", ")", and letters and numbers
- There is exactly one ":" separating the reactant and product sides of the equation
- If there is whitespace between two letters, there is also a "+"
- Terms begin with uppercase letters
- Parentheses are balanced
- Substrings from lowercase to earliest uppercase (right->left) contain only alphabetical characters
(For a lowercase character, there is an unbroken string of letters to the left that contains an uppercase letter)


### Balance a Chemical Equation

Given an unbalanced chemical equation as a string, `S`,  `BCE.balanceChemicalEquation(S)` evaluates to the string with the balanced chemical equation.

```
>>> import BCE
>>> S = 'H2 + O2 : H2O'
>>> BCE.balanceChemicalEquation(S)
'2 H2 + O2 : 2 H2O'
```

### Find Balancing Coefficients

Given an unbalanced chemical equation as a string, `S`, `BCE.findBalancingCoefficients(S)` evaluates to a NumPy array containing the balancing coeffients. The order of the coefficents corresponds to the terms in the equation from left to right.

```
>>> import BCE
>>> S = 'H2 + O2 : H2O'
>>> BCE.findBalancingCoefficients(S)
array([2, 1, 2])
```

### Write Steps to Solution

To see the steps taken by the machine to balance an equation, `S` (string), `BCE.writeBCESteps(S)` creates a text file in the current directory titled `BCESteps.txt`.


```
>>> import BCE
>>> S = 'H2 + O2 : H2O'
>>> BCE.writeBCESteps(S)
'BCESteps.txt'
```
BCESteps.txt contains

```
Equation
H2 + O2 : H2O
Matrix
[[ 2  0 -2]
 [ 0  2 -1]]
Reduced Matrix
[[ 1  0 -1]
 [ 0  2 -1]]
Coeficients
[2 1 2]
Balanced Equation
2 H2 + O2 : 2 H2O
```
