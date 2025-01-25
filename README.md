# BCE

This is a project for balancing chemical equations. It is intended as a collection of scripts for building other programs rather than as a stand-alone calculator.


Given a chemical equation, presented as a string, these programs will find the balancing coefficients, rewrite the chemical equation to contain them, and show the intermediate steps. At a high level, this is accomplished by interpreting a chemical equation as a system of  equations* and using matrix operations to find the smallest solution. 

Currently, this program supports equations that have a unique solution. Chemically, thi means that it only accepts chemical equations that represent exactly one reaction.

*homogenous diophantine linear equations

## Installation

To install the project, run 

> `$ git clone https://github.com/FBar000/BalChemEq.git`

Then, fetch the dependencies via

> `pip install -r requirements.txt`

## Usage 

This project is intended as a collection of separate tools to be tailored to individual needs; each method has documentation. A summary of the files and their contents follows:



### Equation Criteria

The programs are designed to read equations in a specific format. 

General rules for the equation: 
- It contains only " ", "+", ":", "(", ")", and letters and numbers
- There is one ":" that separates the sides of the equation
- Parentheses are balanced

Specific rules for terms: 
- Terms begin with upper-case letters
- Whitespace does not occur within terms of the equation
- Lower-case letters must only occur after letters


The `main.py` file demonstrates usage of the package's main features.


### Balance a Chemical Equation 


Given an unbalanced chemical equation as a string, `equation_string`,  `BCE.balanceChemicalEquation(equation_string)` evaluates to the string with the balanced chemical equation.

```
import src.BCE as BCE
equation_string = 'H2 + O2 : H2O'
print(BCE.balanceChemicalEquation(equation_string))
'2 H2 + O2 : 2 H2O'
```

### Find Balancing Coefficients

Given an unbalanced chemical equation as a string, `S`, `BCE.findBalancingCoefficients(S)` evaluates to a NumPy array containing the balancing coeffients. The order of the coefficents corresponds to the terms in the equation from left to right.

```
equation_string = 'H2 + O2 : H2O'
BCE.findBalancingCoefficients(equation_string)
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
