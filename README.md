# BalChemEq

This is a project dedicated to balancing chemical equations. It is intended as a tool for building other programs. Given an equation as a string, this project contains programs to find the balancing coefficients, rewrite the chemical equation, as well as show the work. This is possible by representing chemical equations as systems of homogenous diophantine linear equations and using matrix operations. Currently, this program supports equations that have one unique solution. Chemically, this would mean equations that represent exactly one reaction.

## Installation

To install the project, run 

> `$ git clone https://github.com/FBar000/BalChemEq.git`

Then, fetch the dependencies via

> `pip install -r requirements.txt`

## Usage 

First, I=import the scripts into your python project via

```
import balanceChemicalEquation as BCE
```

### Balance a chemical equation

  