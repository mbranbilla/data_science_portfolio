import numpy as np


class single_layer_perceptron:
    def __init__(self):
        self.w = None

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


class adaline:
    def __init__(self):
        self.w = None
        self.mean_square_error = []

    def mse(self, X, y, w):
        err = 0

        for x_i, y_i in zip(X, y):
            u = np.dot(np.transpose(w), x_i)
            err += (y_i - u) ** 2

        return err / np.size(X, 0)

    def fit(self, X, y, eps=0.0001, learn_rate=0.05):
        X = np.array(X)
        y = np.array(y)
        n = np.size(X, 1)
        w = np.random.uniform(low=0.0, high=0.01, size=n)
        epoch = 0
        mean_square_error = []
        flag = True

        while flag:
            mean_square_error.append(self.mse(X, y, w))

            for x_i, y_i in zip(X, y):
                u = np.dot(np.transpose(w), x_i)
                w += learn_rate * (y_i - u) * x_i
            
            epoch += 1
            mean_square_error.append(self.mse(X, y, w))

            if np.abs(mean_square_error[epoch - 1] - mean_square_error[epoch]) <= eps:
                flag = False
        
        self.mean_square_error = mean_square_error
        self.w = w

    def predict(self, X):
        X = np.array(X)
        u = np.dot(X, np.transpose(self.w))
        return np.sign(u)
        