import plotter

# Create list of times to run simulation
# Set up to run for 50 ms, stepping by 0.1 ms
times = [0]
dt = 0.1
while times[-1] < 50:
    times.append(times[-1] + dt)


# Set vars to be used in calculation
# Variable names equivalent to those used in assignment description
Vm = [0.0] * len(times)
Rm = 1
Cm = 10
tau_m = Rm*Cm
Vt = 1  # threshold of V, fires when exceeding threshold
Vr = 0.0  # reset to Vr after firing


# User selects current to be injected
print("Enter desired current")
I = float(input())

# Collect data/run simulation
for i in range(len(times)):
    # Update Vm
    Vm[i] = Vm[i-1] + (((-Vm[i-1] + I*Rm) / tau_m) * dt)

    # Test if spike occurred
    if Vm[i] >= Vt:
        Vm[i] = Vr


# plot membrane potential trace
plotter.plot(times, Vm, 'LIF Simulation with I='+str(I))
