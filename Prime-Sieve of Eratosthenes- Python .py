#Python Sieve of Eratosthenes

import math
def getPrimes():
    n = 10**6+1
    seive = [0]*(n+1)
    # 0 and 1 are not primes
    seive[0] = 1
    seive[1] = 1
 
    for i in range(2, int(math.sqrt(n))+1):
        if seive[i] == 0:
            for j in range(i, n+1):
                if j*i>n:
                    break
                else:
                    if seive[i*j]==0:
                        seive[i*j] = 1
    return seive


primes=getPrimes()
n=17

if primes[n]==0:
	print("Prime")
else:
	print("Not Prime")


   

#######################################
'''
from math import *

def genprimes(n):
    primes = [True]*(n+1)
    primes[0] = False
    primes[1] = False
    for p in range(2,int(sqrt(n))+1):
        if primes[p] == True:
            for i in range(p*p,n+1,p):
                primes[i] = False

            
    for i in range(0,len(primes)):
        if primes[i] == True:
            print(i,end=" ")


t = int(input())
while t:
    n = int(input())
    genprimes(n)
    print()
    t=t-1
    

'''
########################################################################
   
'''
#Python Sieve of Eratosthenes

from math import *

def genprimes(n):
    primes = [True]*(n+1)
    primes[0] = False
    primes[1] = False
    for p in range(2,int(sqrt(n))+1):
        if primes[p] == True:
            for i in range(p*p,n+1,p):
                primes[i] = False


            
    if primes[n] == True:
    	return False
    else:
    	return True

t = int(input())
while t:
    n = int(input())
    print(genprimes(n))
    print()
    t=t-1
