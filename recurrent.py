import nengo

model = nengo.Network()
with model:
    stim = nengo.Node([0])
    a = nengo.Ensemble(n_neurons=50, dimensions=1)
    nengo.Connection(stim, a)
    
    b = nengo.Ensemble(n_neurons=50, dimensions=1,
                       radius=1)
    def feedforward(x):
        return x
    nengo.Connection(a, b, function=feedforward)
    
    def recurrent(x):
        return x**2
    nengo.Connection(b, b, function=recurrent,
                     synapse=0.1)

#  v + (-x) = x
#  v = 2x
#  x = v/2