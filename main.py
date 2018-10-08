# Noah Dominic Silvio
# Playing with the Fourier Series (Square Wave)

import matplotlib.pyplot as plt
import numpy as np
import math as math
import constant as const

class Wave:
    def __init__(self, fundamental_freq, precision):
        # stores the fundamental frequency
        # measured in cycles per 8000 samples
        self.fundamental_freq = fundamental_freq
        # how precisely the sine wave is composed to a square wave
        # precision adds the precision-th harmonic to the f.f.
        self.precision = precision

    def wave_func(self, scale_, x_):
        return 0

    def display(self):
        # how many samples are displayed in the graph
        sample = 8000
        # how many samples is one cycle
        scale = 8000
        x = np.arange(sample)
        y = 0

        plt.xlabel('Sample')
        plt.ylabel("Amplitude")
        plt.axhline(y=0, color='k')

        plt.plot(x, self.wave_func(scale, x))
        # displays the final graph
        plt.show()


class SquareWav(Wave):
    def __init__(self, fundamental_freq, precision):
        super(SquareWav, self).__init__(fundamental_freq, precision)
        plt.title("Approximation of a Square Wave up to the " + str(precision) + "th harmonic")

    def wave_func(self, scale_, x_):
        y = 0
        # y = bias + \sum_{i = 0}^{self.precision}(\frac{1}{2i + 1} \sin(x \times freq_{fundamental} \times i))
        #
        #                      __ precision     1
        # y        =  bias  +  \            (-------- sin(x * freq            * i))
        #  square              /__ i  =  0    2i + 1             fundamental
        #
        # and bias = 0
        for i in range(self.precision):
            y = y + (2 / (2 * i + 1)) * (np.sin(2 * np.pi * self.fundamental_freq * (2 * i + 1) * x_ / scale_))
        return y


class SawtoothWav(Wave):
    def __init__(self, fundamental_freq, precision):
        super(SawtoothWav, self).__init__(fundamental_freq, precision)
        plt.title("Approximation of a Sawtooth Wave up to the " + str(precision) + "th harmonic")

    def wave_func(self, scale_, x_):
        # fourier series for sawtooth wave can be found here: http://mathworld.wolfram.com/FourierSeriesSawtoothWave.html
        y = 0
        for i in range(1, self.precision):
            y = y + (-1 / i * np.pi) * (np.sin(2 * np.pi * self.fundamental_freq * i * x_ / scale_))
        return y


class RevSawToothWav(Wave):
    def __init__(self, fundamental_freq, precision):
        super(RevSawToothWav, self).__init__(fundamental_freq, precision)
        plt.title("Approximation of a Reverse Sawtooth Wave up to the " + str(precision) + "th harmonic")

    def wave_func(self, scale_, x_):
        # fourier series for sawtooth wave can be found here: http://mathworld.wolfram.com/FourierSeriesSawtoothWave.html
        y = 0
        for i in range(1, self.precision):
            y = y + (1 / i * np.pi) * (np.sin(2 * np.pi * self.fundamental_freq * i * x_ / scale_))
        return y


class TriangleWav(Wave):
    def __init__(self, fundamental_freq, precision):
        super(TriangleWav, self).__init__(fundamental_freq, precision)
        plt.title("Approximation of a Triangle Wave up to the " + str(precision) + "th harmonic")

    def wave_func(self, scale_, x_):
        # fourier series for trianglewave can be found here: http://mathworld.wolfram.com/FourierSeriesTriangleWave.html
        y = 0
        for i in range(1, self.precision):
            y = y + (8*((-1)**((i-1)/2)))/(np.pi*np.pi*i*i) * (np.sin(2 * np.pi * self.fundamental_freq * i * x_ / scale_))
        return y


# play with this line
# SquareWav(3, 10).display()
# SquareWav(3, 15).display()
SquareWav(3, 50).display()
# SawtoothWav(3, 10).display()
# RevSawtoothWav(3, 10).display()
# TriangleWav(3, 10).display()
