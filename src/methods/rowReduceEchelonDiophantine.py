'''
Row reduce matrices for homogenous linear diophantine systems. 

See module numpy for ndarray objects

Functions:
    row_reduce_diophantine(ndarray) -> ndarray
    removeZeroRows(ndarray) -> ndarray
'''
import numpy as np
def diophantineRowReduce(i_matrix):
    """
    Reduce a homogenous linear diophantine system matrix.

        Parameters:
            matrix (ndarray): A matrix representing a diophantine linear system
        
        Returns:
            matrix (ndarray): A matrix in row reduced echelon form with rows scaled such that all entries are integers 
    """
    matrix=i_matrix
    n, m = np.shape(matrix)
    # Row Reduce
    for k in range(np.min([n,m])):
        # If zero pivot, switch with earliest non zero in column
        if matrix[k][k] == 0:
            nonzeros = list(filter(lambda d: d[1] != 0, enumerate(matrix.transpose()[k])))
            if len(nonzeros) == 0:
                # potential error here....
                # later functions divide by this element, so potential / 0 error
                continue
            else:
                try:
                    swp = list(filter(lambda d: d[0] > k, nonzeros))[0][0]
                    matrix[[k, swp]] = matrix[[swp, k]]
                except IndexError:
                    # If there are no nonzero pivots below, do nothing
                    continue
        # Cancel columns
        for i in range(n):
            if matrix[i][k] != 0:
                if i != k:
                    alpha = np.lcm(matrix[k][k], matrix[i][k])
                    matrix[i] = alpha / matrix[i][k] * matrix[i] -  alpha / matrix[k][k] * matrix[k]
    # Simplify
    for k in range(np.min([n,m])):
        # Divide row by gcd
        if matrix[k][k] != 0:
            matrix[k] = matrix[k] / np.gcd.reduce(matrix[k]) 
        # Ensure positive pivots
        if matrix[k][k] < 0:
            matrix[k] *= -1
    return matrix