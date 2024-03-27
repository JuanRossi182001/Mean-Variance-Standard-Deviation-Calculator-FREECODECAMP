import numpy as np

def calculate(lista):
    matrix = np.array(lista).reshape(3,3)

    mean_matrix = [list(matrix.mean(axis=0)), list(matrix.mean(axis=1)), matrix.mean()]
    variance_matrix = [list(matrix.var(axis=0)), list(matrix.var(axis=1)), matrix.var()]
    std_dev_matrix = [list(matrix.std(axis=0)), list(matrix.std(axis=1)), matrix.std()]
    max_matrix = [list(matrix.max(axis=0)), list(matrix.max(axis=1)), matrix.max()] 
    min_matrix = [list(matrix.min(axis=0)), list(matrix.min(axis=1)), matrix.min()]
    sum_matrix= [list(matrix.sum(axis=0)), list(matrix.sum(axis=1)), matrix.sum()]

    calculations ={
        "mean": mean_matrix,
        "variance": variance_matrix,
        "standar deviation": std_dev_matrix,
        "max": max_matrix,
        "min": min_matrix,
        "sum": sum_matrix   
    }

    return calculations