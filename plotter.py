from matplotlib import pyplot


def plot(x, y, model, xlabel='Time in ms', ylabel='Membrane potential V (mV)'):
    pyplot.plot(x,y)
    pyplot.xlabel(xlabel)
    pyplot.ylabel(ylabel)
    pyplot.title(model)
    pyplot.show()
