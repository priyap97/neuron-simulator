from matplotlib import pyplot


def plot(x, y, model):
    pyplot.plot(x,y)
    pyplot.xlabel('Time in ms')
    pyplot.ylabel('Membrane potential v')
    pyplot.title(model)
    pyplot.show()
