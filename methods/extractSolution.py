"""
Extract smallest positive solution from reduced diophantine matrix.

Functions:
    extract_smallest_solution(ndarray) -> ndarray
    removeZeroRows(ndarray) -> ndarray
    processor_matrix(int) -> ndarray

"""
import numpy as np

def extract_smallest_solution(reduced_diophantine_matrix):
    """
    Return array with smallest positive solution to the diophantine system represented by input
    
        Parameters:
            reduced_diophantine_matrix (ndarray) : a reduced diophantine matrix
        Returns:
            solution (ndarray) : an array with values corresponding to unknowns 
    """
    reduced_diophantine_matrix = removeZeroRows(reduced_diophantine_matrix)
    # optimization : (n x m) into (n x 2), memory efficient
    n, m = np.shape(reduced_diophantine_matrix)
    rd_mat = np.matmul(reduced_diophantine_matrix, processor_matrix(m)).transpose()
    # Scale all pairs such that coefficients on last variable are equal
    lcmOfLastVarCoefs = np.lcm.reduce(-rd_mat[-1])
    scaler = (lcmOfLastVarCoefs / -rd_mat[-1]).astype(int)
    rd_mat = scaler * rd_mat
    # Find variable values by finding lcm of their coefficients
    coefs = np.append(rd_mat[0], lcmOfLastVarCoefs)
    lcm = np.lcm.reduce(coefs)
    return (lcm / coefs).astype(int)

def removeZeroRows(r_matrix):
    """Remove zero rows in a matrix"""
    top = len(r_matrix)
    for n in range(1, top):
        if n >= len(r_matrix):
            return r_matrix
        if r_matrix[-1][-1] == 0:
            r_matrix = np.delete(r_matrix, -1, 0)
    return r_matrix

def processor_matrix(m):
    """Return auxiliary matrix to be used in (n x m) -> (n x 2) conversion"""
    return np.array([[1]*(m-1)+[0], [0]*(m-1)+[1]]).transpose()