import nengo
model = nengo.Network()
with model:
    food = nengo.Ensemble(n_neurons=200,
                          dimensions=2)
    stim_food = nengo.Node([0,0])
    nengo.Connection(stim_food, food)
    
    light = nengo.Ensemble(n_neurons=100,
                           dimensions=1)
    stim_light = nengo.Node(0)
    nengo.Connection(stim_light, light)
    
    motor = nengo.Ensemble(n_neurons=200,
                           dimensions=2)
                           
    do_food = nengo.Ensemble(n_neurons=300,
                             dimensions=3,
                             radius=1.5)
    nengo.Connection(light, do_food[0])
    nengo.Connection(food, do_food[1:])
    def food_func(x):
        light, food_x, food_y = x
        if light < 0:
            return food_x, food_y
        else:
            return 0, 0
    nengo.Connection(do_food, motor,
            function=food_func)
            
    pos = nengo.Ensemble(n_neurons=500,
                         dimensions=2)
    nengo.Connection(pos, pos, synapse=0.1)
    nengo.Connection(motor, pos, 
                     transform=0.1,
                     synapse=0.1)
    
    do_home = nengo.Ensemble(n_neurons=300,
                            dimensions=3,
                            radius=1.5)
    nengo.Connection(light, do_home[0])
    nengo.Connection(pos, do_home[1:])
    def home_func(x):
        light, pos_x, pos_y = x
        if light > 0:
            return -pos_x, -pos_y
        else:
            return 0, 0
    nengo.Connection(do_home, motor,
            function=home_func)
    
    
    
    