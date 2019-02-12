# neuron-simulator
Simulates firing rates of Hodgkin-Huxley, Leaky Integration Firing (LIF), and Izhikevich models of neurons based on simulated input current.

## Leaky Integrate and Fire Model
The code to simulate the LIF model can be found in `lif.py`. All of the simulators make use of `plotter.py` to plot the results.

### Algorithm
The algorithm used for this model follows the formulas provided in the project description. Arbitrary values were used for the following: 

| Variable | Value Used |
|----------|------------------------------------------------------------------|
| `I(t)` | Created an arbitrary linear function which decays the current over time |
| `Cm` | Used arbitrary capacitor value of 30 |
| `Rm` | Used arbitrary resistor value of 7 |
| `Vt` | Used arbitrary voltage threshold of 10 |
| `Vr` | Used arbitrary voltage reset value of 0 |

