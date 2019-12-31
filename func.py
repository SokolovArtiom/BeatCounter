import librosa
import matplotlib.pyplot as plt
from librosa import display
import numpy as np
from librosa import magphase
from keras.models import Sequential
from keras.models import model_from_json
from keras.layers import Dense
from keras.utils import np_utils
import tkinter


def DurOfProp(ns, Amp):

    dur=np.zeros(100)
    maximum=0
    count=0
    for i in ns:
        if i<=300:
            if Amp[i]>0.02 and Amp[i]>=max(Amp[0:300]):
                dur[count]=i
                count=count+1
                maximum=maximum+1
        if i>300 and i<Amp.size-300:
            if Amp[i]>0.02 and Amp[i]>=max(Amp[i-300:i+300]):
                dur[count]=i
                count=count+1
                maximum=maximum+1
    dur=dur[1:maximum:1]-dur[0:maximum-1:1]
    
    return dur


def freqences(FFTArr):
    
    X_train = np.loadtxt("X_train2.txt", delimiter=" ", usecols=(), unpack=True)
    y_train = np.loadtxt("Y_train2.txt", delimiter=" ", usecols=(), unpack=True)
    
    X_train = X_train.reshape(297, 1025)
    y_train = np_utils.to_categorical(y_train, 27)
    
    model = Sequential()
    model.add(Dense(2000, input_dim=1025, init="normal", activation="sigmoid"))
    model.add(Dense(219, init="normal", activation="sigmoid"))
    model.add(Dense(27, init="normal", activation="softmax"))
    model.compile(loss="categorical_crossentropy", optimizer="SGD", metrics=["accuracy"])
    model.load_weights("model.h5")

    FFTArr=FFTArr.reshape(FFTArr.size, order='F')
    FFTArr=FFTArr.reshape((int(FFTArr.size/1025),1025))
    predictions=model.predict_classes(FFTArr)

    return predictions

def ABCstart(n, d):

    n=str(n)
    d=str(d)
    textout=''
    textout=textout+'X:0'+'\n'+'M:'+n+'/'+d+'\n'+'L:1/1'+'\n'+'K:C'+'\n'
    return textout
    
def ABCout(Time1, Time2, freq, dur, EPB, n, d, textout):

    t=0
    count=0.0
    
    for i in dur:
        NewTime=t/Time1*Time2
        NewTime=int(NewTime)
        note=freq[NewTime]
        t = t + i
        if note == 0:
            textout=textout+'C'
        elif note == 1:
            textout=textout+'^C'
        elif note == 2:
            textout=textout+'D'
        elif note == 3:
            textout=textout+'^D'
        elif note == 4:
            textout=textout+'E'
        elif note == 5:
            textout=textout+'F'
        elif note == 6:
            textout=textout+'^F'
        elif note == 7:
            textout=textout+'G'
        elif note == 8:
            textout=textout+'^G'
        elif note == 9:
            textout=textout+'A'
        elif note == 10:
            textout=textout+'^A'
        elif note == 11:
            textout=textout+'B'
        elif note == 12:
            textout=textout+'c'
        elif note == 13:
            textout=textout+'^c'
        elif note == 14:
            textout=textout+'d'
        elif note == 15:
            textout=textout+'^d'
        elif note == 16:
            textout=textout+'e'
        elif note == 17:
            textout=textout+'f'
        elif note == 18:
            textout=textout+'^f'
        elif note == 19:
            textout=textout+'g'
        elif note == 20:
            textout=textout+'^g'
        elif note == 21:
            textout=textout+'a'
        elif note == 22:
            textout=textout+'^a'
        elif note == 23:
            textout=textout+'b'
        elif note == 24:
            textout = textout +'[C ^D G]'
        elif note == 25:
            textout = textout +'[G ^A D]'
        elif note == 26:
            textout = textout +'[D F A]'

        
        if i>EPB-500 and i<=EPB+1000:
            textout=textout+'/'+str(d)+' '
            count = count + 1/d
        if i>(EPB/2)-250 and i<=(EPB/2)+500:
            textout=textout+'/'+str(2*d)+' '
            count = count + 1/(2*d)
        if i>(EPB/4)-125 and i<=(EPB/4)+250:
            textout=textout+'/'+str(d*4)+' '
            count = count + 1/(4*d)
        if count==n/d:
            textout=textout+'|'
            count=0
 
    NewTime=t/Time1*Time2
    NewTime=int(NewTime)
    note=freq[NewTime+5]
    if note == 0:
        textout=textout+'C'
    elif note == 1:
        textout=textout+'^C'
    elif note == 2:
        textout=textout+'D'
    elif note == 3:
        textout=textout+'^D'
    elif note == 4:
        textout=textout+'E'
    elif note == 5:
        textout=textout+'F'
    elif note == 6:
        textout=textout+'^F'
    elif note == 7:
        textout=textout+'G'
    elif note == 8:
        textout=textout+'^G'
    elif note == 9:
        textout=textout+'A'
    elif note == 10:
        textout=textout+'^A'
    elif note == 11:
        textout=textout+'B'
    elif note == 12:
        textout=textout+'c'
    elif note == 13:
        textout=textout+'^c'
    elif note == 14:
        textout=textout+'d'
    elif note == 15:
        textout=textout+'^d'
    elif note == 16:
        textout=textout+'e'
    elif note == 17:
        textout=textout+'f'
    elif note == 18:
        textout=textout+'^f'
    elif note == 19:
        textout=textout+'g'
    elif note == 20:
        textout=textout+'^g'
    elif note == 21:
        textout=textout+'a'
    elif note == 22:
        textout=textout+'^a'
    elif note == 23:
        textout=textout+'b'
    elif note == 24:
        textout = textout +'[C ^D G]'
    elif note == 25:
        textout = textout +'[G ^A D]'
    elif note == 26:
        textout = textout +'[D F A]'

    rem=(n/d)-count
    if rem==n/d:
        textout=textout+'/2'
    elif rem==0.25:
        textout=textout+'/4'
    elif rem==0.125:
        textout=textout+'/8'
    elif rem==0.0625:
        textout=textout+'/16'
    return textout
