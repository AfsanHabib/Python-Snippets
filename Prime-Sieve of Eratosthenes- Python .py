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

            
    for i in range(0,len(primes)):
        if primes[i] == True:
            print(i,end=" ")


t = int(input())
while t:
    n = int(input())
    genprimes(n)
    print()
    t=t-1
    

    
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
