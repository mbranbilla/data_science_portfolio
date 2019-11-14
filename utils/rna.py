import numpy as np


class single_layer_perceptron:
    def __init__(self):
        w = None

    def fit(self, X, y, learn_rate=0.05):
        w = np.random.uniform(low=0.0, high=0.01, size=np.ma.size(X, 1))
        epoch = 0
        err_flag = True

        while err_flag:
            err_flag = False

            for x_i, y_i in zip(X, y):
                u = np.dot(w, x_i)
                v = np.sign(u)

                if v != y_i:
                    w = w + learn_rate * (y_i - v) * x_i
                    err_flag = False

            epoch += 1

        self.w = w

    def predict(self, X):
        u = np.dot(X, self.w)
        y = np.sign(u)

        return y
