import nengo
import numpy as np
model = nengo.Network()
with model:
    stim_a = nengo.Node(0)
    stim_b = nengo.Node(0)
    
    a = nengo.Ensemble(n_neurons=100, dimensions=1)
    
    b = nengo.Ensemble(n_neurons=100, dimensions=1)
    
    nengo.Connection(stim_a, a)
    nengo.Connection(stim_b, b)
    
    
    c = nengo.Ensemble(n_neurons=100, dimensions=2, radius=1.5)
    
    #def funca(x):
    #    return x,0
    #nengo.Connection(a, c, function=funca)
    nengo.Connection(a, c[0])
    
    #def funcb(x):
    #    return 0,x
    #nengo.Connection(b, c, function=funcb)
    nengo.Connection(b, c[1])
    
    d = nengo.Ensemble(n_neurons=100, dimensions=1)
    def product(x):
        return x[0]*x[1]
    nengo.Connection(c, d, function=product)
    
