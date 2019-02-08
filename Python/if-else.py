#!/bin/python3

N = int(input())
if N % 2 == 0 and 2<=N<=5:   #num % 2 == 0 is an even number
        print("Not Weird")
elif N % 2 == 0 and 6<=N<=20:
        print("Weird") 
elif N % 2 == 0 and N > 20:
        print("Not Weird")
else: print("Weird") 

