import librosa
import matplotlib.pyplot as plt
from librosa import display
import numpy as np

#path = 'cymbals.ogg'
#path='The blister exists.ogg'
path='Test1.ogg'
y, sr = librosa.load(path)

#y=y[25000:100000]   #The blister exixts dx = 1000 BPM = 90

#y=y[0:180000]  #cymbals dx = 800 BPM = 75

#y=y[0:280000]  #Test1 dx = 1000 BPM = 65

count=0
for i in y:
    if i>=0:
        count=count+1
        
AmpAbZer=np.empty(count)

count=0
for i in y:
    if i>=0:
        AmpAbZer[count]=i
        count=count+1
        
ns=np.arange(1,AmpAbZer.size+1,1)
dur=np.zeros(100)
 
maximum=0
count=0
for i in ns:
    if i>1000 and i<AmpAbZer.size-1000:
        if AmpAbZer[i]>=max(AmpAbZer[i-1000:i+1000]) and AmpAbZer[i]>0.1:
            dur[count]=i
            count=count+1
            maximum=maximum+1
            
dur=dur[1:maximum:1]-dur[0:maximum-1:1]

BPM=65  
EPB=60/BPM *13500
n=2
d=4

count=0.0
for i in dur:
    if i>EPB-3100 and i<EPB+3100:
        print(1,"/",d)
        count = count + 1/d
    if i>(EPB/2)-1555 and i<(EPB/2)+3100:
        print(1,"/",2*d)
        count = count + 1/(2*d)
    if i>(EPB/4)-2500 and i<(EPB/4)+1555:
        print(1,"/",4*d)
    if count==n/d:
        print("-------")
        count=0
        
if count!=0:
    rem=(n/d)-count
    if rem==0.25:
        print(1,"/",4)
    if rem==0.125:
        print(1,"/",8)
    if rem==0.625:
        print(1,"/",16)
        
plt.figure(figsize=(10, 8))
D = librosa.amplitude_to_db(librosa.stft(y))
plt.subplot(1, 1, 1)

librosa.display.waveplot (y, sr)
plt.title('Linear-frequency power spectrogram')

#y=y[100:10000]
#print(y[:1000])
#print (y.size)    

#librosa.display.specshow(D, y_axis='linear')
#plt.colorbar(format='%+2.0f dB')
#plt.title('Linear-frequency power spectrogram')

#chroma = librosa.feature.chroma_cqt(y=y, sr=sr)
#librosa.display.specshow(chroma, x_axis='time', y_axis='chroma')
#plt.colorbar()


