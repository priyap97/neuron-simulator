# Hodgkin-Huxley Simulator
# Completed for Rutgers University Brain-Inspired Computing (198:525)
# Priya Pamnani (pp572@rutgers.edu)

import plotter
from numpy import exp


# Helper function computes a_m(V)
def a_m(V):
    return round(float(0.1 * (V + 40)) / (1 - exp((V + 40)/(-10))), 6)


# Helper function computes b_m(V)
def b_m(V):
    return round(float(4 * exp((-V + 65) / 18)), 6)


# Helper function computes a_h(V)
def a_h(V):
    return round(float(0.07 * exp((V + 65) / (-20))), 6)


# Helper function computes b_h(V)
def b_h(V):
    return round(float(1 / (1 + ((exp(-V - 35)) / 10))), 6)


# Helper function computes a_n(V)
def a_n(V):
    return round(float(0.01*(V + 55) / (1 - exp((V + 55) / (-10)))), 6)


# Helper function computes b_n(V)
def b_n(V):
    return round(float(0.125 * exp((V + 65) / (-80))), 6)


def simulate():
    # Create list of times to run simulation
    times = [0]
    dt = float(0.1)

    # Create lists to track V, m, h, n over time
    V = [0.0]
    m = [0.0]
    h = [0.0]
    n = [0.0]

    # Set variables for use in calculation
    C = 30  # capacitance

    g_Na = 10  # Sodium conductance
    g_K = 10  # Potassium conductance
    g_L = 10  # Leak conductance

    V_Na = 100  # Sodium potential
    V_K = -10  # Potassium potential
    V_L = 10  # Leak potential


    # User selects current to be injected
    print("Enter desired current: ")
    I = float(input())


    # Integrate from 0.0ms to 500.0ms
    while times[-1] < 500:
        times.append(round(times[-1] + dt, 1))

        V_old = V[-1]

        # Update m
        dm = ((a_m(V_old) * (1 - m[-1])) - (b_m(V_old) * m[-1])) * dt
        dm = round(dm, 6)
        m.append(m[-1] + dm)

        # Update h
        dh = ((a_h(V_old) * (1 - h[-1])) - (b_h(V_old) * h[-1])) * dt
        dh = round(dh, 6)
        h.append(h[-1] + dh)

        # Update n
        dn = ((a_n(V_old) * (1 - n[-1])) - (b_n(V_old) * n[-1])) * dt
        dh = round(dh, 6)
        n.append(n[-1] + dn)

        dV = (I - g_Na*(m[-1]**3)*h[-1]*(V_old-V_Na) - g_K*(n[-1]**4)*(V_old-V_K) - g_L*(V_old-V_L)) * (dt/C)
        dV = round(dV, 6)
        V.append(V_old + dV)

    # Plot results
    plotter.plot(times, V, 'Hodgkin-Huxley Model with I='+str(I))