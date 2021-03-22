import nengo
import numpy as np
model = nengo.Network()
with model:
    ens = nengo.Ensemble(n_neurons=100, dimensions=1,
                         neuron_type=nengo.LIF())
                         
    stim = nengo.Node(0)
    nengo.Connection(stim, ens)
    
    def my_function(x):
        if x>0:
            return 1
        else:
            return -1

    ens2 = nengo.Ensemble(n_neurons=100, dimensions=1)
    nengo.Connection(ens, ens2, function=my_function)
    
    output2 = nengo.Node(None, size_in=1)
    
    def myfunc2(x):
        return 0.5+x*0.5
    nengo.Connection(ens2, output2, function=myfunc2)
    
    