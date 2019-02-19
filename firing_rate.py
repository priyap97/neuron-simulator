# Simulator for Firing Rate of an LIF Neuron
# Completed for Rutgers University Brain-Inspired Computing (198:525)
# Priya Pamnani (pp572@rutgers.edu)

import plotter


def firing_rate(I):
    # Create list of times to run simulation
    times = 0
    dt = 0.1

    # Set vars to be used in calculation
    # Variable names equivalent to those used in assignment description
    Vm = 0.0  # voltage
    Cm = 30  # capacitance
    Rm = 7  # resistance
    tau_m = Rm*Cm  # time constant
    Vt = 10  # threshold of V, neuron fires when exceeding threshold
    Vr = 0.0  # reset to Vr after firing

    spikes = 0

    # Integrate V from 0.0ms to 1000.0ms
    while times < 1000:
        times = round(times + dt, 1)
        old_V = Vm
        Vm = old_V + (((-old_V + I * Rm) / tau_m) * dt)

        # Test for spike, if exceeded threshold return to Vr
        if Vm >= Vt:
            Vm = Vr
            spikes = spikes + 1

    return spikes


def simulate():
    print('Enter minimum current to measure firing rate')
    min = float(input())
    print('Enter maximum current to measure firing rate')
    max = float(input())
    print('Enter step (increment) for current. Suggested 0.125')
    step = float(input())

    I = [min]
    f_rate = [firing_rate(min)]

    while I[-1] < max:
        if I[-1] + step <=max:
            I.append(I[-1] + step)
        else:
            I.append(max)
        f_rate.append(firing_rate(I[-1]))

    # Plot results
    plotter.plot(I, f_rate, 'Firing rate of LIF neuron', xlabel='Current', ylabel='Firing rate per second')