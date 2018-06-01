import librosa
import matplotlib.pyplot as plt
from librosa import display
import numpy as np

path='SW3.ogg'
y, sr = librosa.load(path)

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
    if i<=1500:
        if AmpAbZer[i]>=max(AmpAbZer[0:1500]) and AmpAbZer[i]>0.03:
            dur[count]=i
            count=count+1
            maximum=maximum+1
    if i>1500 and i<AmpAbZer.size-1500:
        if AmpAbZer[i]>=max(AmpAbZer[i-1500:i+1500]) and AmpAbZer[i]>0.03:
            dur[count]=i
            count=count+1
            maximum=maximum+1

dur=dur[1:maximum:1]-dur[0:maximum-1:1]


AmpAbZer=y
D = librosa.amplitude_to_db(librosa.stft(y))
Time2=D.shape[1]
t=0
fr=49
freq=np.empty(Time2)
        
while t<Time2:
    fr=49
    while fr<100:
        if D[fr][t]==max(D[49:100,t]):
            freq[t-1]=fr
            break
        fr=fr+1
    t=t+1

BPM=60
EPB=60/BPM *13500
n=4
d=4

print('X:0')
print('M:',n,'/',d,sep="")
print('L:1/1')
print('K:C')

t=0
count=0.0
Time1=AmpAbZer.shape

for i in dur:
    t = t + 1.7*i
    NewTime=t/Time1*Time2
    NewTime=int(NewTime)
    note=freq[NewTime+1]
    t = t - 1.7*i + 2*i
    if note > 45 and note <= 52:
        print("C",sep="",end="")
    if note > 52 and note <= 58:
        print("D",sep="",end="")
    if note > 58 and note <= 63:
        print("E",sep="",end="")
    if note > 63 and note <= 68:
        print("F",sep="",end="")
    if note > 68 and note <= 76:
        print("G",sep="",end="")
    if note > 76 and note <= 85:
        print("A",sep="",end="")
    if note > 85 and note <= 95:
        print("B",sep="",end="")
    
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
note=freq[NewTime+20]
if note > 45 and note <= 50:
    print("C",sep="",end="")
if note > 50 and note <= 55:
    print("D",sep="",end="")
if note > 55 and note <= 61:
    print("E",sep="",end="")
if note > 61 and note <= 70:
    print("F",sep="",end="")
if note > 70 and note <= 75:
    print("G",sep="",end="")
if note > 75 and note <= 85:
    print("A",sep="",end="")
if note > 85 and note <= 95:
    print("B",sep="",end="")
     
rem=(n/d)-count
if rem==n/d:
    print("/",2,'||',sep="")
if rem==0.25:
    print("/",4,'||',sep="")
if rem==0.125:
    print("/",8,'||',sep="")
if rem==0.0625:
    print("/",16,'||',sep="")
