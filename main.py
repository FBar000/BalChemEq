import src.BCE as BCE

equation_string = 'H2 + O2 : H2O'

# return balanced equation
print(BCE.balanceChemicalEquation(equation_string))

# return solutions as an array
print(BCE.findBalancingCoefficients(equation_string))

# demonstrate intermediate calculations in `BCESteps.txt`
BCE.writeBCESteps(equation_string)
