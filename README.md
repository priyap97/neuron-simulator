# neuron-simulator
Simulates firing rates of Hodgkin-Huxley, Leaky Integrate and Fire (LIF), and Izhikevich models of neurons based on simulated input current.

## Leaky Integrate and Fire Model
The code to simulate the LIF model can be found in `lif.py`. All of the simulators make use of `plotter.py` to plot the results.

### Algorithm
The algorithm used for this model follows the formulas provided in the project description. Arbitrary values were used for the following: 

| Variable | Value Used |
|----------|--------------------------------|
| `I(t)` | Created an arbitrary linear function which decays the current over time |
| `Cm` | Used arbitrary capacitor value of 30 |
| `Rm` | Used arbitrary resistor value of 7 |
| `Vt` | Used arbitrary voltage threshold of 10 |
| `Vr` | Used arbitrary voltage reset value of 0 |

## Izhikevich Model
The code to simulate the Izhikevich model can be found in `izhikevich.py`. All of the simulators make use of `plotter.py` to plot the results.

### Algorithm
The algorithm used for this model follows the formulas provided in the project description. No arbitrary values were used, except for initial values of `u` and `v`. 
Initially, `u = 0.0` and `v = -65.0`. 

The user is able to control values of `a`, `b`, `c`, `d`, and `I`.
However, suggested values are: 

| Variable | Value Suggested |
|----------|--------------------------------|
| `a` | 0.02 to 0.04 |
| `b` | 0.2 to 0.4 |
| `c` | -55.0 to -80.0 |
| `d` | 2 to 4 |
| `I` | Any amount, however depending on the above values the neuron should spike at approximately 4 |
