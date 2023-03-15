import numpy as np

#fonksiyon tanımlama
def f(x):
    return x**3+x**2-x-5

#secant metodu
def my_secant(x0,x1,max_hata,max_iter):
    iter=1
    condition=True

    while condition:
        if f(x0) == f(x1): #değerlerin kontrolü
            print("Mathematical error")
           
            break

        x2 = x1 - (x1-x0) * f(x1) / ( f(x1) - f(x0) )
        print('Iteration %d, x2 = %0.6f and f(x2) = %0.6f' % (iter, x2, f(x2)))
        iter+=1
        x0=x1
        x1=x2

        if iter>max_iter:
            print("Not convergent")
            break
        
        condition= np.abs(f(x2))>max_hata
           
        
        print('\nRequired root is: %0.8f' % x2)


x0 = input('Enter First Guess: ')
x1 = input('Enter Second Guess: ')
e = input('Tolerable Error: ')
N = input('Maximum Step: ')

x0 = float(x0)
x1 = float(x1)
e = float(e)
N= int(N)

my_secant(x0=x0,x1=x1,max_hata=e,max_iter=N)