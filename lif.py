# LIF Simulator
# Completed for Rutgers University Brain-Inspired Computing (198:525)
# Priya Pamnani (pp572)

import plotter

# Create list of times to run simulation
# Set up to run for 50 ms, stepping by 0.1 ms
times = [0]
dt = 0.1


# Set vars to be used in calculation
# Variable names equivalent to those used in assignment description
Vm = [0.0]  # voltage
Cm = 15  # capacitance
Rm = 1.5  # resistance
tau_m = Rm*Cm  # time constant
Vt = 10  # threshold of V, neuron fires when exceeding threshold
Vr = 0.0  # reset to Vr after firing


# User selects current to be injected
print("Enter desired current")
I = float(input())


while times[-1] < 50:
    times.append(round(times[-1] + dt, 1))
    old_V = Vm[-1]
    Vm.append(old_V + (((old_V + I * Rm) / tau_m) * dt))

    # Test for spike, if exceeded threshold return to Vr
    if Vm[-1] >= Vt:
        Vm[-1] = Vr


# Display plot
plotter.plot(times, Vm, 'LIF Simulation with I='+str(I))
