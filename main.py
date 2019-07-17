import librosa
import numpy as np
from librosa import magphase
from func import DurOfProp
from func import freqences
from func import ABCstart
from func import ABCout

def main(path):
    
    y, sr = librosa.load(path, sr=2000)
    
    Amp=y
    
    ns=np.arange(1,Amp.size+1,1)
    
    dur=DurOfProp(ns, Amp)
    
    FFTArr=librosa.amplitude_to_db(magphase(librosa.stft(y))[0])
    
    Time1=float(y.size)
    
    Time2=float(FFTArr.shape[1])
    
    freq=freqences(FFTArr)
    
    BPM=60
    EPB=60/BPM *2000
    n=4
    d=4
    
    textout=ABCstart(n, d)
    
    textout=ABCout(Time1, Time2, freq, dur, EPB, n, d, textout)
    
    return textout