import numpy as np


class sigmoid_neuron_recap:
    def __init__(self, w_init, b_init, algo):
        self.w = w_init
        self.b = b_init
        self.w_h = []
        self.b_h = []
        self.e_h = []
        self.algo = algo

    def sigmoid(self, w=None, b=None):
        # Logistic function
        if w is None:
            w = self.w
        if b is None:
            b = self.b

        return 1 / (1 + np.exp(- w * x + b))

    def error(self, X, Y, w=None, b=None):
        # Loss Function
        if w is None:
            w = self.w
        if b is None:
            b = self.b

        err = 0

        for x, y in zip(X, Y):
            err += 0.5 * (self.sigmoid(x, w, b) - y) ** 2

        return err


class gradient_descent:
    def __init__(self):
        pass

    def cost_function(self, X_train, y_train):
        # Compute linear regression cost
        n = len(X)

        for x, y in zip(X_train, y_train):
