# ENEL320_Assignment1
<h2>ENEL320: Communications and Signals</h2>
<h2>Trent Kamper, tka77, 93737083</h2>
<h2>Jonathan Nicholas, jni68, 93133260</h2>

<h2>Q1:</h2>
<h3>A:</h3>
<p>
The selected waveform for this assignment was a commutation cycle in a single phase rectifier circuit. In essence, this is the waveform produced when the rectification has some source impedance that causes a non-conduction period in the output voltage.
</p>
<h3>B:</h3>
<p>
  This is simply an absolute sinusoid turned on at some point before the end of its period. The piece wise approximation of this function is as follows:
</p>

![equation](https://latex.codecogs.com/svg.image?f(t)=%5Cbegin%7Barray%7D%7Bcc%7D%5C%7B&%5Cbegin%7Barray%7D%7Bcc%7D%7Csin(t)%7C&t%25T%5Cleq%5Cmu%5C%5C0&else%5C%5C%5Cend%7Barray%7D%5Cend%7Barray%7D)

<p>
Where T is the period of the waveform and u is the point on that period where the turning on occurs.  
</p>

![image](/figures/SinglePhase.png)

<h3>C:</h3>
<p>
  This signal is catagorised as both continuous and periodic. To complete a fourier transform, the fourier series is the appropriate transform to complete. 
</p>

![Fourier Transform](https://latex.codecogs.com/svg.image?F(f)=%5Cint_%7B-%5Cinfty%7D%5E%7B%5Cinfty%7Df(t)e%5E%7B-j2%5Cpi%20ft%7D)
![Fourier Transform Substitutions](https://latex.codecogs.com/svg.image?F(f)=%5Cint_%7B0%7D%5E%7B%5Cmu%7D0%20e%5E%7B-j2%5Cpi%20ft%7D&plus;%5Cint_%7B%5Cmu%7D%5E%7BT%7D%7Csin(t)%7Ce%5E%7B-j2%5Cpi%20ft%7D)

<p>
  Ascessing the fourier transform using the provided figure 1 waveform data. 
</p>

![Ascessed Fourier](https://latex.codecogs.com/svg.image?F(f)=%5Cint_%7B0%7D%5E%7B0.1%7D0%20e%5E%7B-j2%5Cpi%20ft%7D&plus;%5Cint_%7B0.1%7D%5E%7B1%7D%7Csin(t)%7Ce%5E%7B-j2%5Cpi%20ft%7D)

![Calculation FT](https://latex.codecogs.com/svg.image?%5Cint_%7B0.1%7D%5E%7B1%7Dsin(2%5Cpi%20t)e%5E%7B-j2%5Cpi%20ft%7D=%5Cfrac%7Bj%7D%7B2%7D%5B%5Cdelta(f&plus;1)-%5Cdelta(f-1)%5D)

<p>
  As this signal is practically a sinusoid, the result is also the sinusoid fourier transform as simmilar to that derived in the lectures. This example has the simple carrier frequnecy delta function positions as +1 Hz and -1 Hz.  
</p>

<h3>D:</h3>
<p>
  This approximation is good for small source inductance values which can approximatley be ignored in this signal. However, as this fourier transform is not capable of capturing the zero DC component contained within the signal, it is not especially useful for any real world application predicitons for large source inductances that have some notable effect on output voltages.
</p>

<h2>Q2:</h2>
<h3>A: Block Diagram</h3>

![Block Diagram](/figures/transmitter_reciever.PNG)

<h3>B: Code in repositry ! (SongDecoder.py) </h3>
<h3>C: Tone Modulations </h3>

![Tone modulation: 0.5](/figures/Tonemod_0.5.png)
![Tone modulation: 1](/figures/Tonemod_1.png)

<h3>D: Magic Carpet (Song.wav)</h3>

<h3>E: Noise</h3>
<p>
  For this system, there is a strong correlation between the success of the demodulation and the low pass filter (LPF) used. Due to this, some systems functioned with different LPF values better than others and as such it is difficult to know if a signal has been interpreted incorrectly due to noise of the filter type without some filter editing. However, using an existing case of tone modulation which has already previous been developed, more noise was steadily increased in the signal until the output signal was unintelligble. 
  The results were, as the standard deviation of the gaussian noise added surpassed the signal amplitude, the singal could no longer be perfectly interpreted. At the threshold of three times this, the signal becomes practically un-interpretable. These are seen by the following figures.
</p>

![Noise 1](/figures/addativenoise_1.png)
![Noise 3](/figures/addativenoise_3.png)
![Noise 5](/figures/addativenoise_5.png)

<h2>Q3:</h2>

![Question 3](/figures/3_1.PNG)
![Question 3](/figures/3_2.PNG)



