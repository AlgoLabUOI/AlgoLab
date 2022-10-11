# An integrated simulation framework for the prevention and mitigation of pandemics caused by airborne pathogens <br>

In this work, we developed an integrated simulation framework for pandemic prevention and mitigation of pandemics caused by airborne
pathogens, incorporating three sub-models, namely the spatial model, the mobility model, and the propagation model, to create a realistic
simulation environment for the evaluation of the effectiveness of different countermeasures on the epidemic dynamics. The spatial model
converts images of real cities obtained from Google Maps into undirected weighted graphs that capture the spatial arrangement of the streets
utilized next for the mobility of individuals. The mobility model implements a stochastic agent-based approach, developed to assign specific
routes to individuals moving in the city, through the use of stochastic processes, utilizing the weights of the underlying graph to deploy
shortest path algorithms. The propagation model implements both the epidemiological model and the physical substance of the transmission of
an airborne pathogen (in our approach, we investigate the transmission parameters of SARS-CoV-2). The deployment of a set of
countermeasures was investigated in reducing the spread of the pathogen, where, through a series of repetitive simulation experiments, we
evaluated the effectiveness of each countermeasure in pandemic prevention.
