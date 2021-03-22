import nengo
import numpy as np
model = nengo.Network()
with model:
    ens = nengo.Ensemble(n_neurons=100, dimensions=1,
                         neuron_type=nengo.Izhikevich())
                         
    stim = nengo.Node(0)
    nengo.Connection(stim, ens)
    
    output = nengo.Node(None, size_in=1)
    
    def my_function(x):
        if x>0:
            return 1
        else:
            return -1

    nengo.Connection(ens, output, 
                     function=my_function, synapse=0.005)
    
    