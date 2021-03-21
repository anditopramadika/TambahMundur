# Input User untuk 2 Angka
x = input('Masukkan angka 1 : ')
y = input('Masukkan angka 2 : ')

#Pembuatan def function tambahMundur
def tambahMundur(x,y):
    # Filter Inputan User hanya untuk Integer dan kurang dari 359999 : 
    if (x.isnumeric() or y.isnumeric()) and (0<int(x)<359999 or 0<int(y)<359999) :
        a = 0                               #sisa angka untuk looping angka dibalik di input x
        b = 0                               #sisa angka untuk looping angka dibalik di input y 
        c = 0                               #sisa angka untuk looping reversed x+y
        while (int(x) > 0):                 # loop saat x lebih dari 0
    # Membalikkan integer di input x    
            rev_x = int(x) % 10          
            a = (a * 10) + rev_x  
            x = int(x) // 10  

        while (int(y) > 0):  
    # Membalikkan integer di input y         
            rev_y = int(y) % 10  
            b = (b * 10) + rev_y  
            y = int(y) // 10
    
    #menambahkan hasil reversed x (a) + reversed y (b)
        d = a+b   

        while (int(d) > 0):  
    #membalikkan hasil reversed x (a) + reversed y (b)        
            rev_xy = int(d) % 10  
            c = (c * 10) + rev_xy  
            d = int(d) // 10
        print('Hasil tambah mundurnya :',c)     #print hasil dari tambahMundur 

    else:
        print('Invalid Input!')
        
tambahMundur(x, y)