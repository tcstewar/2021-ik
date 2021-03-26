import nengo


# dy/dt = (x-y)/tau  = x/tau -y/tau

tau_desired = 0.01
tau_synapse = 0.1

model = nengo.Network()
with model:
    stim = nengo.Node([0])
    a = nengo.Ensemble(n_neurons=50, dimensions=1)
    nengo.Connection(stim, a)
    
    b = nengo.Ensemble(n_neurons=50, dimensions=1,
                       radius=1)
    def feedforward(x):
        return tau_synapse*x/tau_desired
    nengo.Connection(a, b, function=feedforward,
                     synapse=tau_synapse)
    def recurrent(y):
        return -y/tau_desired*tau_synapse + y
    nengo.Connection(b, b, function=recurrent,
                     synapse=tau_synapse)

