import numpy as np
import torch.nn as nn


def gen_data(n, d, p, w, gamma=1):
    ys = np.random.multinomial(1, p, n)
    zs = np.random.multivariate_normal(0, np.eye(d), n)
    xs = zs + ys * gamma * w
    return xs, ys


def bayesAccuracy(data_fn, n, d, p, w, gamma):
    xs, ys = data_fn(n, d, p, w, gamma)
    model = # sklearn nn with 2 layers
    model.fit(xs, ys)
    xs, ys = data_fn(n, d, p, w, gamma)
    # calc accu on this new data

def 