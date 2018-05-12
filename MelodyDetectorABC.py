import librosa
import matplotlib.pyplot as plt
from librosa import display
import numpy as np

#path = 'cymbals.ogg'
#path='The blister exists.ogg'
path='Triad3.ogg'
y, sr = librosa.load(path)

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
        if AmpAbZer[i]>=max(AmpAbZer[i-1000:i+1000]) and AmpAbZer[i]>0.045:   #!!
            dur[count]=i
            count=count+1
            maximum=maximum+1
            
dur=dur[1:maximum:1]-dur[0:maximum-1:1]


AmpAbZer=y
D = librosa.amplitude_to_db(librosa.stft(y))
Time2=D.shape[1]
t=0
fr=48
freq=np.empty(Time2)
        
while t<Time2:
    fr=48
    while fr<100:
        if D[fr][t]==max(D[48:100,t]):
            freq[t-1]=fr
            break
        fr=fr+1
    t=t+1


BPM=60
EPB=60/BPM *13500
n=2
d=4

print('X:0')
print('M:',n,'/',d,sep="")
print('L:1/1')
print('K:C')

t=0
count=0.0
Time1=AmpAbZer.shape

for i in dur:
    t = t + i
    NewTime=t/Time1*Time2
    NewTime=int(NewTime)
    note=freq[NewTime+1]
    t = t - i + 2*i
    if note > 45 and note <= 50:
        print("c",sep="",end="")
    if note > 50 and note <= 55:
        print("d",sep="",end="")
    if note > 55 and note <= 61:
        print("e",sep="",end="")
    if note > 61 and note <= 70:
        print("f",sep="",end="")
    if note > 70 and note <= 75:
        print("g",sep="",end="")
    if note > 75 and note <= 85:
        print("a",sep="",end="")
    if note > 85 and note <= 95:
        print("b",sep="",end="")
    
    if i>EPB-4500 and i<EPB+3100:
        print("/",d,sep="",end=" ")
        count = count + 1/d
    if i>(EPB/2)-1555 and i<(EPB/2)+1700:
        print("/",(2*d),sep="",end=" ")
        count = count + 1/(2*d)
    if i>(EPB/4)-2500 and i<(EPB/4)+1555:
        print("/",(4*d),sep="",end=" ")
        count = count + 1/(4*d)
    if count==n/d:
        print("|",end=" ")
        count=0
 
NewTime=t/Time1*Time2
NewTime=int(NewTime)
note=freq[NewTime+10]
if note > 45 and note <= 50:
    print("c",sep="",end="")
if note > 50 and note <= 55:
    print("d",sep="",end="")
if note > 55 and note <= 61:
    print("e",sep="",end="")
if note > 61 and note <= 70:
    print("f",sep="",end="")
if note > 70 and note <= 75:
    print("g",sep="",end="")
if note > 75 and note <= 85:
    print("a",sep="",end="")
if note > 85 and note <= 95:
    print("b",sep="",end="")
     
rem=(n/d)-count
if rem==n/d:
    print("/",2,'||',sep="")
if rem==0.25:
    print("/",4,'||',sep="")
if rem==0.125:
    print("/",8,'||',sep="")
if rem==0.0625:
    print("/",16,'||',sep="")
        
#plt.figure(figsize=(10, 8))
#D = librosa.amplitude_to_db(librosa.stft(y))
#plt.subplot(1, 1, 1)

#librosa.display.waveplot (y, sr)
#plt.title('Linear-frequency power spectrogram')   

#librosa.display.specshow(D, y_axis='linear')
#plt.colorbar(format='%+2.0f dB')
#plt.title('Linear-frequency power spectrogram')

#chroma = librosa.feature.chroma_cqt(y=y, sr=sr)
#librosa.display.specshow(chroma, x_axis='time', y_axis='chroma')
#plt.colorbar()'''
