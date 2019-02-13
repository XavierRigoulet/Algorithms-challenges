n , array  = int(input()) , list(map(int,input().split()))
print(any(str(j) == str(j)[::-1] for j in array) and all(i >=0 for i in array))
