import numpy as np
import matplotlib.pyplot as plt
from gifly import gif_maker

interv = (0,500)
x = np.linspace(interv[0],interv[1],1000)
x = x+(100*np.sin(0.01*x))
y = np.linspace(interv[0],interv[1],1000)+np.random.random(len(x))*20

tot_gifs = 20

x_plot,y_plot = [],[]

for ii in range(0,tot_gifs):
    x_plot.extend(x[ii*int(len(x)/tot_gifs):(ii+1)*int(len(x)/tot_gifs)])
    y_plot.extend(y[ii*int(len(x)/tot_gifs):(ii+1)*int(len(x)/tot_gifs)])
    plt.plot(x_plot,y_plot)
    
    plt.ylim([np.min(y),np.max(y)])
    plt.xlim([np.min(x),np.max(x)])
    gif_maker('straight_line_noise.gif','./gif_maker_png/',ii,tot_gifs)
