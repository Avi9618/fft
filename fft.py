
#importing libiraries
import numpy as np
import matplotlib.pyplot as plt
import scipy

# N-point
n=int(input("enter value of N in N-point : "))

#input data sequence
g=[]
for i in range(0,n):
    g.append(input("g("+str(i)+") : "))
print('given input g(n) :')
print(g)

#formation of even, odd data sequences
n1=n/2
g1=[]
g2=[]
for i in range(0,n):
    if i%2==0:
        g1.append(g[i])
    else:
        g2.append(g[i])
print('g1(n) : ')
print g1
print('g2(n) : ')
print g2
#combining both data sequences into a sinle complex sequence g1(n) + j g2(n)
h=[]
for i in range(0,n/2):
    h.append(complex(g1[i],g2[i]))
y=[]
#dft of combined data sequence
for i in range(len(h)):
    y.append(0)
    for j in range(len(h)):
        y[i]=y[i]+(h[j]*np.exp(np.complex(0,-1*2*np.pi*i*j/n1)))
#conjugate for obtained dft
y1=np.conjugate(y)
#obtaining (N-K) sequence from conjugate sequence
y2=[]
for i in range (0,n1):
    y2.append(np.complex(0,0))
for i in range(0,n1):
    if((n1-i)==n1):
        y2[i]=y1[i]
    else:
        y2[n1-i]=(y1[i])
        

y3=[]
y4=[]
N=n
#X1(K)=1/2 *[X(K)+X*(N-K)]
for i in range(n1):
    y3.append((0.5*(y[i]+y2[i])))
#X2(K)=1/2j*[X(K)-X*(N-K)]
for i in range(n1):
    y4.append((-0.5*np.complex(0,1)*(y[i]-y2[i])))
g11=[] 
w=np.exp(np.complex(0,-1)*2*np.pi/N)
k=0
for i in range(N):
    g11.append(y3[k]+(np.power(w,i)*y4[k]))
    k=k+1
    if k>=(N/2):
        k=0
#printing of outputs
print("output : ")    
print(g11)
print(' ')
print("justification of output with fft from scipy")
G1=scipy.fft(g)
print G1
        
