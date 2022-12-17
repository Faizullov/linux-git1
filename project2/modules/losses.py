import numpy as np
import scipy
from scipy.special import expit
from scipy.special import logsumexp


class BaseLoss:
    """
    Base class for loss function.
    """

    def func(self, X, y, w):
        """
        Get loss function value at w.
        """
        raise NotImplementedError('Func oracle is not implemented.')

    def grad(self, X, y, w):
        """
        Get loss function gradient value at w.
        """
        raise NotImplementedError('Grad oracle is not implemented.')


class BinaryLogisticLoss(BaseLoss):
    """
    Loss function for binary logistic regression.
    It should support l2 regularization.
    """

    def __init__(self, l2_coef):
        """
        Parameters
        ----------
        l2_coef - l2 regularization coefficient
        """
        self.l2_coef = l2_coef

    def func(self, X, y, w):
        """
        Get loss function value for data X, target y and coefficient w; w = [bias, weights].

        Parameters
        ----------
        X : 2d numpy.ndarray
        y : 1d numpy.ndarray
        w : 1d numpy.ndarray

        Returns
        -------
        : float
        """
        w_to_scal = w[1:]
        tmp_arr = np.zeros(len(y))
        L = np.mean(np.logaddexp(tmp_arr, -y * (w_to_scal @ X.T + w[0]))) + self.l2_coef * \
            np.linalg.norm(w_to_scal)**2
        return L

    def grad(self, X, y, w):
        """
        Get loss function gradient for data X, target y and coefficient w; w = [bias, weights].

        Parameters
        ----------
        X : 2d numpy.ndarray
        y : 1d numpy.ndarray
        w : 1d numpy.ndarray

        Returns
        -------
        : 1d numpy.ndarray
        """

        bias = np.mean(-y * expit(-y * (w[1:] @ X.T + w[0])))
        ans = np.mean(-y*X.T * expit(-y * (w[1:] @ X.T + w[0])), axis=1) + 2*self.l2_coef*w[1:]
        return np.concatenate([bias, ans], axis=None)
