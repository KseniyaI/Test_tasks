number = ['A123AA159', 'V123CC12', 'AA123A159', 'B123BBB12', 'T1596MM23', 'E555ET89', 'H984BO159', '1236TT78', 'TRR12345', 'K789MM']
L = ['A','B','C','E','H','K','O','P','T','Y','M','X']
for a in number:
    if a[0] in L and a[4] in L and a[5] in L :
        if len(a) in [8,9] :

            print(a)

    '''try:
        if int(a[1:4]) in range(1,1000) :   #проверка цифр номера
            print('a')
    except:  
        pass
    
    try:
        if int(a[6:9]) in range(1,1000) :   #проверка номера региона 3 цифры
            print(a[6:9])
        elif int(a[6:8]) in range(1,100) :    #проверка номера региона 2 цифры
            print(a[6:8])
    except:  
        pass'''
    
    #if len(a) == 8 or 9 :  #проверка длины номера 8 или 9 символов
      #  print('***')
