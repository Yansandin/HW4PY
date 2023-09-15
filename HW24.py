a=[]
print('Введите количество кустов: ')
n= int(input())
for i in range(n):
    a.append(i+1)
print(a)
max_berr=0
for i in range(len(a)):
    max_berr= a[i]+a[i-1]+a[i-2]
    
    
print(max_berr)
        
