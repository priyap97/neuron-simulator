# Izhikevich Simulator
# Completed for Rutgers University Brain-Inspired Computing (198:525)
# Priya Pamnani (pp572)

import plotter

# Create list of times to run simulation
times = [0]
dt = 0.1

u = []  # membrane recovery variable
v = []  # cell voltage
vt = 30  # 30mV threshold


# User determined variables: a, b, c, d, I
print('Enter value for a: ')
a = float(input())
print('Enter value for b: ')
b = float(input())
print('Enter value for c: ')
c = float(input())
print('Enter value for d: ')
d = float(input())
print('Enter voltage: ')
I = float(input())




