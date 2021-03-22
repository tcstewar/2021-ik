import nengo
import numpy as np
model = nengo.Network()
with model:
    stim = nengo.Node([0,0])
    a = nengo.Ensemble(n_neurons=100, dimensions=2, radius=1.5)
    def func(x):
        return x[0]*x[1]
    b = nengo.Ensemble(n_neurons=100, dimensions=1)
    nengo.Connection(stim, a)
    nengo.Connection(a, b, function=func)