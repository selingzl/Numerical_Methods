import numpy as np

#fonksiyonu tanımlama
def f(x):
    return x

#regula falsi yönteminin fonksiyon hali
def my_regula_falsi(xl, xh, max_hata, max_iter):
   
    iter=1 #adım sayısı 
    condition=True # durum kontrolü

    while condition:
        xt=xl-f(xl)*(xh-xl)/(f(xh)-f(xl)) 
        print('Iteration %d, xt = %0.6f and f(xt) = %0.6f' % (iter, xt, f(xt))) #kökün ne olduğu ve kaçıncı adımda bulunduğu

        if f(xt)*f(xl)<0:
            xh=xt 
            
        elif f(xt)*f(xh)<0:
            xl=xt
        
        hata=np.abs(f(xl)-f(xh)) #hata hesaplaması
        iter+=1
        condition = abs(f(xt)) > hata 
    #durumun değiştiği yerler
        if iter>max_iter or hata>max_hata: 
            break

    #kökün değeri
    print('\nRequired root is: %0.8f' % xt)
    
    
     
#kullanıcıdan alınan inputlar
x0 = input('First Guess: ')
x1 = input('Second Guess: ')
e = input('Tolerable Error: ')
i =input('Max step: ')

#float hale dönüştürülme
xl=float(x0)
xh=float(x1)
max_hata=float(e)
max_iter=int(i)

#kökün bulunup bulunmadığını sorgulama
if f(xl) * f(xh) > 0.0:
        print('Given guess values do not bracket the root.')
        print('Try Again with different guess values.')
else:
     my_regula_falsi(xl=xl,xh=xh,max_hata=max_hata,max_iter=max_iter)



      