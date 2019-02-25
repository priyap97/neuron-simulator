# Hodgkin-Huxley Simulator
# Completed for Rutgers University Brain-Inspired Computing (198:525)
# Priya Pamnani (pp572@rutgers.edu)

import plotter
from numpy import exp

def I_t(t):
    return 10 * (t > 100) - 10 * (t > 200) + 35 * (t > 300) - 35 * (t > 400)


# Helper function computes a_m(V)
def a_m(V):
    # numer = 0.1 * (V + 40)
    # denom = 1 - exp(-(V + 40)/10)
    return 0.1*(V+40) / (1 - exp(-(V+40)/10))


# Helper function computes b_m(V)
def b_m(V):
    return 4 * exp(-(V + 65) / 18)


# Helper function computes a_h(V)
def a_h(V):
    return 0.07 * exp(-(V + 65) / 20)


# Helper function computes b_h(V)
def b_h(V):
    return 1 / (1 + exp(-(V + 35)/10))


# Helper function computes a_n(V)
def a_n(V):
    return 0.01*(V + 55) / (1 - exp(-(V + 55) / 10))


# Helper function computes b_n(V)
def b_n(V):
    return 0.125 * exp(-(V + 65) / 80)


# Runs simulation
def simulate():
    # Create list of times to run simulation
    times = [0]
    dt = 0.1

    # Create lists to track V, m, h, n over time
    V = [-65.0]
    m = 0.052
    h = 0.596
    n = 0.317

    # Set variables for use in calculation
    C = 0.1  # capacitance

    g_Na = 120  # Sodium conductance
    g_K = 36  # Potassium conductance
    g_L = 0.3  # Leak conductance

    V_Na = 50  # Sodium potential
    V_K = -77  # Potassium potential
    V_L = -54.38  # Leak potential

    # User selects current to be injected
    print("Enter desired current: ")
    I = float(input())

    # Integrate from 0.0ms to 50.0ms
    while times[-1] < 100:
        print(str(V[-1]) + " " + str(times[-1]))
        times.append(round(times[-1] + dt, 1))

        V_old = V[-1]

        # Update m
        dm = (a_m(V_old) * (1 - m)) - (b_m(V_old) * m)
        m = m + dm*dt

        # Update h
        dh = (a_h(V_old) * (1 - h)) - (b_h(V_old) * h)
        h = h + dh*dt

        # Update n
        dn = (a_n(V_old) * (1 - n)) - (b_n(V_old) * n)
        n = n + dn*dt

        dV_Na = g_Na*(m**3)*h*(V_old - V_Na)
        dV_K = g_K*(n**4)*(V_old - V_K)
        dV_L = g_L*(V_old - V_L)

        dV = I_t(times[-1]) - dV_Na - dV_K - dV_L
        dV = dV * dt / C

        V.append(V_old + dV)

    # Plot results
    plotter.plot(times, V, 'Hodgkin-Huxley Model with I='+str(I))
