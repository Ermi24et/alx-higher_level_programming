#!/usr/bin/python3

""" a module that divides all elements of a matrix by div """


def matrix_divided(matrix, div):
    """ a function that divides all elements by div """
    err_msg = "matrix must be a matrix (list of lists) of integers/floats"
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    final = []
    for i in range(len(matrix)):
        if len(matrix[0]) != len(matrix[i]):
            raise TypeError("Each row of the matrix must have the same size")
        temp = []
        for j in range(len(matrix[i])):
            if not isinstance(matrix[i][j], (int, float)):
                raise TypeError(err_msg)

            temp.append(round(matrix[i][j] / div, 2))

        final.append(temp)

    return final
