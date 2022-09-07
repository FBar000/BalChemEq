"""
Balance a chemical equation.

Equations must contain exactly one reaction. All atoms must be present on both reactant and product sides of the equation.

"""
from methods import *

def balanceChemicalEquation(equation):
    """
    Balance a chemical equation.

    Equations must contain exactly one reaction. All atoms must be present on both reactant and product sides of the equation.
    
    Arguments:
        equation: unbalanced chemical equation [string]
    Return:
        balanced_equation: balanced chemical equation [string]
    """
    # Find coefficients
    coefficients = findBalancingCoefficients(equation)
    # Construct system matrix
    sides_terms = processEquation(equation)[0]
    # Inefficiency to address: lines 21 and 23 both call `processEquation(equation)`
    # Rewrite equation
    bal_eq = wrapSolvedEquation(sides_terms, coefficients)
    return bal_eq

def solutionCoefficients(equation):
    """
    Balance a chemical equation.

    Equations must contain exactly one reaction. All atoms must be present on both reactant and product sides of the equation.
    
    Arguments:
        equation: unbalanced chemical equation [string]
    Return:
        balanced_equation (dict) Solution information (term : coefficient)
    """
    # Find coefficients
    coefficients = findBalancingCoefficients(equation)
    # Construct system matrix
    sides_terms = processEquation(equation)[0]
    # Inefficiency to address: lines 21 and 23 both call `processEquation(equation)`
    # Rewrite equation
    bal_eq = getCoefficients(sides_terms, coefficients)
    return bal_eq


def findBalancingCoefficients(equation):
    """
    Find coefficients that balance a chemical equation

    Equations must contain exactly one reaction. All atoms must be present on both reactant and product sides of the equation.
    
    Arguments:
        equation: unbalanced chemical equation [string]
    Return:
        coefficients: list of balancing coefficients [ndarray(int32)]
    """
    # Catch illegal expressions
    if not validateChemicalEquation(equation):
        return 0
    # Construct system matrix
    equation_units = processEquation(equation)
    mat = equationToMatrix(equation_units)
    # Reduce system matrix
    dr_mat = diophantineRowReduce(mat)
    dr_mat = removeZeroRows(dr_mat)
    # Validate result
    if not validateDRMat(dr_mat):
        return 1
    # Extract solution
    coefficients = extract_smallest_solution(dr_mat)
    return coefficients

def writeBCESteps(equation, wrap=True):
    """
    Write the steps to solve a chemical equation.
    
    Equations must contain exactly one reaction. All atoms must be present on both reactant and product sides of the equation.
    
    Arguments:
        equation: unbalanced chemical equation [string]
        wrap: a switch to include the balanced chemical equation, in addition to the coefficients [boolean]
    Return:
        text : address to text file [string]
    """
    with open('BCESteps.txt', 'w') as f:
        # Catch illegal expressions
        if not validateChemicalEquation(equation):
            return 0
        f.write(f"Equation\n{equation}\n")
        # Construct system matrix
        equation_units = processEquation(equation)
        mat = equationToMatrix(equation_units)
        f.write(f"Matrix\n{mat}\n")
        # Reduce system matrix
        dr_mat = diophantineRowReduce(mat)
        dr_mat = removeZeroRows(dr_mat)
        f.write(f"Reduced Matrix\n{dr_mat}\n")
        # Validate result
        if not validateDRMat(dr_mat):
            return 1
        # Extract solution
        coefficients = extract_smallest_solution(dr_mat)
        f.write(f"Coefficients\n{coefficients}\n")
        if wrap:
            # Inefficiency to address: Lines 85 and 81 both call `processEquation(equation)`
            bal_eq = wrapSolvedEquation(equation_units[0], coefficients)
            f.write(f"Balanced Equation\n{bal_eq}\n")
        return f.name


if __name__ =="__main__":

    
    equation = "NH3 + H3PO4 : (NH4)3PO4"
    writeBCESteps(equation)