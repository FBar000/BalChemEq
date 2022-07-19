'''
Validate matrices in diophantine row reduced echelon form.

Use prior to extracting solution.

Functions:

    validate(ndarray) -> boolean
    checkNonZeros(ndarray) -> boolean
    checkEchelon(ndarray) -> boolean
    checkPositivePivots(ndarray) -> boolean
    pivIdx(ndarray) -> int

'''
import numpy as np
# A matrix is valid iff 
# Each row has either exactly two non zero elements (last and ) or none
# Leading entry is non zero
# Each element, except for the last, in a row is in its own column
# Each element is to the right of the one in the row above
def validateDRMat(reduced_diophantine_matrix):
    """
    Check that matrix has two or no elements per row, one non-zero element per column, that pivots are in echelon form, and that pivots are positive.
    
        Parameters:
            reduced_diophantine_matrix (ndarray): matrix to be verified
        Returns:
            (boolean)

    """
    return (checkNonZeros(reduced_diophantine_matrix) and 
            all([len(list(filter(lambda d : d != 0, i))) == 1 for i in reduced_diophantine_matrix.transpose()[:-1]]) and # One non-zero per column
            checkEchelon(reduced_diophantine_matrix) and
            checkPositivePivots(reduced_diophantine_matrix))

def checkPositivePivots(matrix):
    """Check that pivots are positive."""
    for row in matrix:
        if list(filter(lambda t: t!=0, row))[0] < 0:
            return False
    return True

def checkNonZeros(matrix):
    """Check that matrix has exactly two or zero non-zero elements per row."""
    for row in matrix:
        if not len(list(filter(lambda d : d != 0, row))) in [0, 2]:
            return False
    return True

def checkEchelon(matrix):
    """Check that pivots in matrix (matrix[:-1]) is in echelon for.m"""
    for n in range(1, len(matrix), 1):
        if pivIdx(matrix[n]) <= pivIdx(matrix[n-1]):
            return False
    return True

def pivIdx(row):
    """Get pivot of first non-zero element in a row."""
    return list(filter(lambda t: t[1]!=0, enumerate(row)))[0][0]