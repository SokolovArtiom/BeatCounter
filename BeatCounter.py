import librosa
import matplotlib.pyplot as plt
from librosa import display
import numpy as np

path = 'cymbals.ogg'
#path='The blister exists.ogg'
y, sr = librosa.load(path)

#y=y[25000:100000]   #The blister exixts dx = 1000

y=y[10000:170000]  #cymbals dx = 800

count=0
for e in y:
    if e>0:
        count=count+1
        
z=np.empty(count)

count=0
for e in y:
    if e>=0:
        z[count]=e
        count=count+1
        
a=np.arange(1,z.size+1,1)
 
maximum=0
for i in a:
    if i>800 and i<z.size-800:
        if z[i]>=max(z[i-800:i+800]):
            maximum=maximum+1
            print(i)
print(maximum)
    
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
