import numpy as np
from sympy import symbols, diff

x=symbols('x')
#örnek fonksiyon
f=x**3-x**4 + x -3
#fonksiyonun türevi
g=diff(f,x)

#newton yöntemi
def my_newton(x0, max_hata, max_iter):
    iter=1
    condition=True

    while condition:
        g0=g.subs(x,x0) #türevi yerleştirme
        f0=f.subs(x,x0) #fonksiyonu yerleştirme

        if g0 == 0: 
            print ("Mathematical Error")
            break

        x1=x0-f0/g0
        f1=f.subs(x,x1)
        print('Iteration %d, x1 = %0.6f and f(x1) = %0.6f' % (iter, x1, f1))
        x0=x1

        condition= np.abs(f1)>max_hata

        iter+=1
        if iter>max_iter:
            print('\nNot Convergent.')
            break
        
        print('\nRequired root is: %0.8f' % x1)

        
            
x0 = input('Enter Guess: ')
max_hata = input('Tolerable Error: ')
max_iter = input('Maximum Step: ')

x0=float(x0)
hata=float(max_hata)
n=int(max_iter)

my_newton(x0=x0,max_hata=hata,max_iter=n)