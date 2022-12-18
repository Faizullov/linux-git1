"""Module docstring"""

import numpy as np
from scipy.special import expit


class BaseLoss:
    """
    Base class for loss function.
    """

    def func(self, x_tmp, tmp_y, w):
        """
        Get loss function value at w.
        """
        raise NotImplementedError('Func oracle is not implemented.')

    def grad(self, x_tmp, y, w):
        """
        Get loss function gradient value at w.
        """
        raise NotImplementedError('Grad oracle is not implemented.')


class BinaryLogisticLoss(BaseLoss):
    """
    Loss function for binary logistic regression.
    It should support l2 regularization.
    """

    def __init__(self, l2_c):
        """
        Parameters
        ----------
        l2_coef - l2 regularization coefficient
        """
        self.l2_c = l2_c

    def func(self, x_tmp, tmp_y, w):
        """
        Get loss function value for data X, target y and coefficient w; w = [bias, weights].

        Parameters
        ----------
        x_tmp : 2d numpy.ndarray
        tmp_y : 1d numpy.ndarray
        w : 1d numpy.ndarray

        Returns
        -------
        : float
        """
        w_to_scal = w[1:]
        tmp_arr = np.zeros(len(tmp_y))
        L = np.mean(np.logaddexp(tmp_arr, -tmp_y * (w_to_scal @ x_tmp.T + w[0]))) + self.l2_c * \
            np.linalg.norm(w_to_scal) ** 2
        return L

    def grad(self, x_tmp, y, w):
        """
        Get loss function gradient for data X, target y and coefficient w; w = [bias, weights].

        Parameters
        ----------
        x_tmp : 2d numpy.ndarray
        y : 1d numpy.ndarray
        w : 1d numpy.ndarray

        Returns
        -------
        : 1d numpy.ndarray
        """

        bias = np.mean(-y * expit(-y * (w[1:] @ x_tmp.T + w[0])))
        ans = np.mean(-y * x_tmp.T *
                      expit(-y * (w[1:] @ x_tmp.T + w[0])), axis=1) + 2 * self.l2_c * w[1:]
        return np.concatenate([bias, ans], axis=None)
