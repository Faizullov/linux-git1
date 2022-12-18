import numpy as np


def get_numeric_grad(f, x, eps):
    based = np.eye(len(x))
    matrix = eps * based + x
    grad_vect = np.array(np.apply_along_axis(f, 1, matrix))
    vect_2 = np.array(np.apply_along_axis(f, 1, np.zeros((len(x), len(x))) + x))
    grad_vect = grad_vect - vect_2
    return grad_vect / eps


def compute_balanced_accuracy(true_y, pred_y):
    possible_y = set(true_y)
    value = 0
    for current_y in possible_y:
        mask = true_y == current_y
        value += (pred_y[mask] == current_y).sum() / mask.sum()
    return value / len(possible_y)
