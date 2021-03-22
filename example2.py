import nengo
import numpy as np
model = nengo.Network()
with model:
    stim = nengo.Node(0)
    a = nengo.Ensemble(n_neurons=50, dimensions=1, radius=2)
    b = nengo.Ensemble(n_neurons=100, dimensions=1, radius=2)
    nengo.Connection(stim, a)
    nengo.Connection(a, b)