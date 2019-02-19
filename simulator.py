import izhikevich, hodgkin_huxley, lif, firing_rate

print('Which simulator would you like to use? \nEnter L for LIF, F for firing rate of LIF, I for Izhikevich, \
H for Hodgkin-Huxley: ')
sim = input().upper()[0]

if sim == 'I':
    izhikevich.simulate()

elif sim == 'H':
    hodgkin_huxley.simulate()

elif sim == 'L':
    lif.simulate()

elif sim == 'F':
    firing_rate.simulate()
