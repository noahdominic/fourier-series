# fourier-series (a.k.a <em>Playing around with the Fourier Series</em>)
I play around with the Fourier Series by trying to make a square wave by combining multiple sine waves.

## why?
This was a course lab activity. 

## class `SquareWave`
respresents a square wave that is a composite of several sine waves, as dictated by the Fourier Series.
this class generates the wave with this formula:

<a href="https://www.codecogs.com/eqnedit.php?latex=\sum_{n=0}^{i}(\frac{2}{2n&plus;1}\sin(\frac{2\pi&space;\cdot&space;F_{fundamental}&space;\cdot&space;(2n&space;&plus;&space;1)}{s}))" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\sum_{n=0}^{i}(\frac{2}{2n&plus;1}\sin(\frac{2\pi&space;\cdot&space;F_{fundamental}&space;\cdot&space;(2n&space;&plus;&space;1)}{s}))" title="\sum_{n=0}^{i}(\frac{2}{2n+1}\sin(\frac{2\pi \cdot F_{fundamental} \cdot (2n + 1)}{s}))" /></a>

Where:
* f[fundamental] := fundamental frequency
* i := number of harmonics to be added
* s := the scale of the wave


## Future Plans
In the future other periodic waves (i.e. sawtooth waves, triangle waves, other versions of the pulse wave, etc) could be added, but since I'm a lazy dude with a lot on his plate, don't get your hopes up just yet.
