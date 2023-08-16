#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = matrix.copy()

    for itr in range(len(matrix)):
        new_matrix[itr] = list(map(lambda x: x**2, matrix[itr]))

    return (new_matrix)
