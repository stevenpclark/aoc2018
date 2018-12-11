import numpy as np
from scipy import ndimage
from scipy import signal

def solve(serial, xdim=300, ydim=300, kdims=range(1,300+1)):
    xv, yv = np.meshgrid(range(1,xdim+1), range(1,ydim+1))
    rack_id = xv+10
    power_level = (rack_id*yv + serial)*rack_id/100
    power_level = power_level.astype(np.int)%10 - 5
    result = np.zeros((ydim,xdim,len(kdims)),dtype=np.int)
    for ik, kdim in enumerate(kdims):
        k = np.ones((kdim,kdim), dtype=np.int)
        #result[:,:,ik] = ndimage.convolve(power_level, k, mode='constant', cval=0.0)
        result[:,:,ik] = signal.fftconvolve(power_level, k, mode='same')
    y, x, size = np.unravel_index(np.argmax(result), result.shape)
    kdim = kdims[size]
    offset = kdim//2-1
    return x-offset,y-offset,kdim

def main():
    #print(solve(42, kdims=[3]))
    #print(solve(42))
    print(solve(4151))

if __name__ == '__main__':
    main()
