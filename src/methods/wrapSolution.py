"""
Return balanced chemical equation


Functions:
    wrapSolvedEquation(list[string], ndarray) -> string

"""


def wrapSolvedEquation(equation_side_terms, coefficients):
    """
    Returns a string of a balanced chemical equation
    
    Arguments:
        equation_side_terms: a 2-tuple of lists [str]
        coefficients: a one-dimensional numpy array [int] 
    Returns:
        A string with elements of coefficients preceding corresponding terms in equation_side_terms
    """
    reLen, prLen = len(equation_side_terms[0]), len(equation_side_terms[1])
    # Reactants
    reSol = ""
    for idx in range(reLen):
        coef = coefficients[idx]
        if coef != 1:
            reSol += str(coef)+ " " + equation_side_terms[0][idx] + " + "
        else:
            reSol += equation_side_terms[0][idx] + " + "
    # Products
    prSol = ""
    for idx in range(prLen):
        coef = coefficients[idx+reLen]
        if coef != 1:
            prSol += str(coef) + " " + equation_side_terms[1][idx] + " + "
        else:
            prSol += equation_side_terms[1][idx] + " + "
    return reSol[:-2].strip()+" : "+prSol[:-2].strip()

def getCoefficients(equation_side_terms, coefficients):
    """
    Returns a dictionary with the coefficients that correspond to each term. 

    Arguments:
        equation_side_terms: a 2-tuple of lists [str]
        coefficients: a one-dimensional numpy array [int] 
    Returns:
        A dictionary with (term, coefficient) entries
    """
    solution = {}
    reLen, prLen = len(equation_side_terms[0]), len(equation_side_terms[1])
    # Reactants
    for idx in range(reLen):
        coef = coefficients[idx]
        solution[equation_side_terms[0][idx]] = coef
    # Products
    for idx in range(prLen):
        coef = coefficients[idx+reLen]
        solution[equation_side_terms[1][idx]] = coef
    return solution