"""
Methods to construct a matrix corresponding to a chemical equation.


Functions:
    process_equation(string) -> tuple[tuple[list[str], list[str]], ndarray]
    findAtoms(string) -> list[string]
    separateSides(string) -> list[string]
    getTerms(string) -> list[string]
    half_matrix(string, string) -> ndarray
    count(string, tuple[string, int]) -> int
    split(string) -> tuple[tuple[string, int], tuple[string, int], tuple[string, int]]
git b
"""
import numpy as np
import re

def equationToMatrix(equation_units):
    '''
    Produce a matrix encoding the equations inherent in a chemical equation.

    Arguments:
        equation_units: A tuple with a tuple corresponding to the chemical equation and a list of the atoms d
            [tuple(tuple(list[str], list[str]), list[str]]

    Returns:
        processed_equation: A matrix corresponding to the chemical equation [ndarray]
    '''
    # unpack
    rect, prodt = equation_units[0]
    atoms = equation_units[1]
    # count instances of atoms into matrix
    m1, m2 = half_matrix(atoms, rect), -half_matrix(atoms, prodt)
    # combine: this is the diophantine matrix
    system = np.concatenate((m1, m2), axis=1)
    return system.astype(int)

def processEquation(raw_equation):
    '''
    Produce a tuple with lists of terms of each side of the equatino

    Arguments:
        raw_equation: unbalanced chemical equation [str]
    Returns:
        equation_units: A tuple with a tuple corresponding to the chemical equation and a list of the atoms
            [tuple(tuple(list[str], list[str]), list[str]]
    '''
    # Get terms
    rec, prod = separateSides(raw_equation)
    equation_sides = getTerms(rec), getTerms(prod)
    return equation_sides, findAtoms(raw_equation)

def findAtoms(chemical_expression):
    '''
    Return an alphabetically ordered list of atoms in equation
    
    Arguments:
        raw_equation: chemical expression [str]
    Return:
        atoms: the atoms in a chemical equation [list(str)]
    '''
    atoms = set()
    atom = ""
    for i in range(len(chemical_expression)):
        cchar = chemical_expression[i]
        if cchar.isupper():
            atoms.add(atom)
            atom = ""
        if cchar.isalpha():
            atom += cchar
    atoms.add(atom)
    atoms.remove("")
    return sorted(atoms)

def separateSides(raw_equation):
    """
    Convert raw_equation (string) to a list containing the reactant and product sides of the equation.

        Parameters:
            raw_equation (string) : chemical equation
        Returns:
            list (string) : each side of the chemical equation
    """
    return [side.strip() for side in raw_equation.split(":")]

def getTerms(equation_side):
    '''
    Return a list of terms of a chemical equation
    
    Accepts empty terms, ignores these (e.g. "...+ +..")
    Argument:
        equation_side: a side of a chemical equation [str]
    Return:
        terms: terms in a chemical equation [list(str)]
    '''
    return [i for i in [term.strip() for term in equation_side.split("+")] if i]

def half_matrix(atoms, side_terms):
    '''
    Create a matrix counting the instances of an atom per term on a side of a chemical equation
    
    Argument:
        atoms: A list of the atoms in the equation [list(str)]
        side_terms: terms on the side of the chemical equation [list(str)]
    Return:
        half_m: the matrix representing half of a chemical equation [array(float64)]
    '''
    half_m = np.zeros((len(atoms), len(side_terms)))
    for atom_idx in range(len(atoms)):
        for term_idx in range(len(side_terms)):
            half_m[atom_idx][term_idx] = count(atoms[atom_idx], (side_terms[term_idx], 1))
    return half_m

def count(atom, term_tuple):
    """
    Count the occurences of an atom in a term (input as `term tuple`.)
    
    `term tuple` : tuple(term (string), multiplier (int))
    
    Parameters:
        atom (string) : the atom to be counted
        term_tuple : See above.
    Returns:
        ct (int) : number of atoms in group

    """
    # unpack
    term, mult = term_tuple
    # establish running total
    ct = 0
    # proceed if atom in term
    if getInstanceIdx(term, atom) != -1:
        # base case: no parenthetical groups
        if term.find(')') == -1:
            # add numbers immediately after atom to total, or 1 if no number present
            while idx != -1:
                if idx + len(atom) < len(term) and term[idx+len(atom)].isnumeric():
                    ct += int(re.findall("[0-9]+", term[idx:])[0])
                else:
                    ct += 1
                idx = getInstanceIdx(term, atom, idx+1)
        # recursive step: look at each group
        else:
            for term_tuple in split(term):
                ct += count(atom, term_tuple)
    return ct*mult

def split(term):
    """
    Split a term containing parenthetical group into three: group before, within, and after parentheses.
    
    Store multiplier with each parenthetical group. Ex:
    split('A3(BE)3C') = (('A3', 1), ('BE', 3), ('C',1))
    
    Parameters:
        term (string): term in a chemical equation
    Return:
        tuple(term tuple, term tuple, term tuple) : groups defined by parenthesis
    
    """
    # first break is first instance of '('
    idx1 = term.find('(')
    # parenthesis group is closed when ct is zero
    ct = 1
    for idx2 in range(idx1+1, len(term)):
        if term[idx2] == ')':
            ct -= 1
        if term[idx2] == '(':
            ct += 1
        # extract term tuples
        if ct == 0:
            try:
                tmp = int(re.findall('[0-9]+', term[idx2+1:])[0])
            except IndexError:
                tmp = 1
            try:
                crt = list(filter(lambda d: not d[1].isnumeric(), enumerate(term[idx2+1:])))[0][0]
            except IndexError:
                crt = 1
            return (term[:idx1], 1), (term[idx1+1:idx2], tmp), (term[idx2+1+crt:], 1)
    print(f"Invalid String: Unbalanced parentheses in {term}")
    return []


def getInstanceIdx(term, atom, idx=0):
    """
    Wrap the term.find(atom, idx) to include checks against accidental matches (e.g. "Ca" for "C")

    Arguments: 
        term (string) The chemical expression to search
        atom (string) The atom to search for
        idx (int) The index from which to search from. Defaults to zero.
    Return:
        idx (int) The index of the first match of `atom` in `term` beyond `idx`
    
    Returns -1 if no matches are found
    """
    idx = term.find(atom,idx)
    if idx+len(atom) < len(term):
        while term[idx+len(atom)].islower() :
            idx = getInstanceIdx(term, atom, idx+1)
    return idx
