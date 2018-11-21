import numpy as np 
from skimage.filter import gabor_kernel
from pylab import * 
from matplotlib.widgets import Slider, Button, RadioButtons


ax = subplot(111,axisbg=(0.44,0.44,0.44)) 
subplots_adjust( bottom=0.35) 
gray()

axis([0, 30, 0, 30]) 
theta_init = np.pi/2 
freq_init = 0.25 
sigmax_init = 3 
sigmay_init = 3

nucleo = np.real(gabor_kernel(freq_init, theta=theta_init,sigma_x=sigmax_init, sigma_y=sigmay_init)) 
ax.imshow(nucleo, interpolation='bicubic')

axcolor = 'lightgoldenrodyellow' 
frequencias = axes([0.25, 0.1, 0.65, 0.03], axisbg=axcolor) 
thetas = axes([0.25, 0.15, 0.65, 0.03], axisbg=axcolor) 
sigmasx = axes([0.25, 0.20, 0.65, 0.03], axisbg=axcolor) 
sigmasy = axes([0.25, 0.25, 0.65, 0.03], axisbg=axcolor) 

slider_frequencias = Slider(frequencias, 'Freq', 0.05, 0.50, valinit=freq_init) 
slider_thetas = Slider(thetas, 'Theta', 0, np.pi, valinit=theta_init) 
slider_sigmasx = Slider(sigmasx, 'Sigma X', 1, 6, valinit=sigmax_init) 
slider_sigmasy = Slider(sigmasy, 'Sigma Y', 1, 6, valinit=sigmay_init) 

def update(val): 
	frequencia = slider_frequencias.val 
	theta = slider_thetas.val 
	sigmax = slider_sigmasx.val 
	sigmay= slider_sigmasy.val 
	nucleo = np.real(gabor_kernel(frequencia, theta=theta,sigma_x=sigmax, sigma_y=sigmay))
	ax.imshow(nucleo, interpolation='bicubic') 
	draw()

slider_frequencias.on_changed(update) 
slider_thetas.on_changed(update) 
slider_sigmasx.on_changed(update) 
slider_sigmasy.on_changed(update)
show()
