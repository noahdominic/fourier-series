# Noah Dominic Silvio
# Playing with the Fourier Series (Square Wave)

import matplotlib.pyplot as plt
import numpy as np
import math as math


class SquareWave:
    def __init__(self, fundamental_freq, precision):
        # stores the fundamental frequency
        # measured in cycles per 8000 samples
        self.fundamental_freq = fundamental_freq
        # how precisely the sine wave is composed to a square wave
        # precision adds the precision-th harmonic to the f.f.
        self.precision = precision

    def display(self):
        # how many samples are displayed in the graph
        sample = 8000
        # how many samples is one cycle
        scale = 8000
        x = np.arange(sample)
        y = 0

        plt.xlabel('Sample')
        plt.ylabel("Amplitude")

        # slowly builds each odd harmonic
        for i in range(self.precision):
            # 2 * i + 1 makes sure that even harmonics aren't added
            # formula for square wave can be found here: http://www.dspguide.com/graphics/F_13_10.gif
            y = y + (2 / (2 * i + 1)) * (np.sin(2 * np.pi * self.fundamental_freq * (2 * i + 1) * x / scale))

            if ((i/self.precision) * 100) % 10 == 0:
                print("yah")
                plt.plot(x, y)

        # displays the final graph
        plt.show()


# play with this line
sq = SquareWave(2, 1000)

sq.display()
