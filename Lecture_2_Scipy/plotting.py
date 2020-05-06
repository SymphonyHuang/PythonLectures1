import matplotlib.pyplot as plt

def plot(x, y):
    plt.plot(x, y, 'o-')

def plot_interp(x, y):
    plt.plot(x, y, 'k.-', lw=2)
    
def plot_root(x, y, x0):
    plt.plot(x, y)
    plt.axhline(0, c='k')
    plt.axvline(x0, c='r')
    plt.show()
