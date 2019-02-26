# Izhikevich Simulator
# Completed for Rutgers University Brain-Inspired Computing (198:525)
# Priya Pamnani (pp572)

import plotter


def simulate():
    # Create list of times to run simulation (in ms)
    times = [0.0]
    dt = 0.02

    # Establish lists to track u and v, set threshold voltage
    u = [0.0]  # membrane recovery variable
    v = [-65.0]  # cell voltage
    vt = 30.0  # 30mV threshold


    # User determined variables: a, b, c, d, I
    print('Enter value for a: ')
    a = float(input())
    print('Enter value for b: ')
    b = float(input())
    print('Enter value for c: ')
    c = float(input())
    print('Enter value for d: ')
    d = float(input())
    print('Enter current: ')
    I = float(input())


    # Integrate over 200 ms
    while times[-1] < 200:
        # check for spike
        times.append(round(times[-1] + dt, 2))
        if v[-1] >= vt:
            v.append(c)
            u.append(u[-1] + d)

        else:
            du = a*(b*v[-1] - u[-1])
            u.append(u[-1] + du*dt)
            dv = 0.04*v[-1]*v[-1] + 5*v[-1] + 140 - u[-1] + I
            v.append(v[-1] + dv*dt)


    # Plot results
    plotter.plot(times, v, 'Izhikevich model with a='+str(a)+", b="+str(b)+", c="+str(c)+", d="+str(d)+", I="+str(I))