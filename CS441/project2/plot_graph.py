import matplotlib.pyplot as plt
# using matplotlib to plot the (x,y) graphs
import numpy as np
# using numpy to get preset array object with a max_size given

def trans_eff(size):
    return(size - 20) /size
def plot_trans_eff(max_size):
    x = np.arange(64, 1518 + 1)
    y = trans_eff(x)
    plt.plot(x,y)
    plt.xlabel('Size of the User Data')
    plt.ylabel('Transfer Efficiency')
    plt.title('Transfer Efficiency vs Size of User Data')
    plt.show()

plot_trans_eff(100)
plot_trans_eff(500)
plot_trans_eff(2000)