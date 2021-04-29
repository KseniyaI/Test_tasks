from random import randrange
from math import sqrt
from math import atan2
from math import degrees
from pprint import pprint

def sort_xy(points):  
    """функция сортировки: располагает точки в порядке обхода против часов стрелки, 
    начиная с точки, ближайшей к оси у, лежащей в координатном углу I"""
    XY = []
    Z = []
    xy = points
    for elem in xy:
        XY.append( [elem[0] , elem[1] , round(degrees(atan2(elem[1],elem[0]))) ] )  #в список XY добавляем значенте угла в градусах (arctan(y/x))   
    for elem in XY:
        if elem[0]>0 and elem[1]>0 : #для 1 четверти на плоскости
            elem[2] = elem[2]+270
        elif elem[0]<=0 and elem[1]>=0 : #для 2 четверти на плоскости
            elem[2] = elem[2]-90
        elif elem[0]<=0 and elem[1]<=0 :  #для 3 четверти на плоскости
            elem[2] = elem[2]+360-90
        elif elem[0]>=0 and elem[1]<=0 : #для 4 четверти на плоскости
            elem[2] = elem[2]+360-90
    XY = (sorted(XY, key = lambda x:x[2]))   #сортировка по значению угла
    Z=[XY[-1]]+XY[0:-1]  #начало обхода с точки, ближайшей к оси Y в 1 четверти
    Z = [[elem[0],elem[1]] for elem in Z] #выводим результат без угла
    return Z

def calc_distances(spisok_koord,N):  
    """Функция находит среднее, мин., макс. расстояния точек от центра координатной плоскости (0,0)"""
    s_min = 150
    s_max = 0
    s_sum = 0
    xy = []
    n = N
    for elem in spisok_koord:
        xy.append(elem[0])
        xy.append(elem[1])
    for j in range(0,2*n-1,2):
        s = sqrt(xy[j]**2 + xy[j+1]**2)  #расстояние до центра (0,0)
        if s > s_max :   #макс. расстояние до (0,0)
            s_max = s
        if s < s_min :   #мин. расстояние до (0,0)
            s_min = s
        s_sum += s   #сумма всех расстояний
        j += 2
    distances = [round(s_max), round(s_min), round(s_sum/n)]
    return distances

xy = []   # [[x1,y1], [x2,y2],...]

n = input('Введите число точек n = ')
while not n.isdigit():
    n = input('Это не число! Введите число верно ')
n = int(n)
x = [randrange(-100, 100) for i in range(n)]  #заполнили случайными числами [x1,x2,...]
y = [randrange(-100, 100) for i in range(n)]  #заполнили случайными числами [y1,y2...]

for i in range(n):
    xy.append([x[i],y[i]])

print('Случайно заданные координаты х', x)
print('Случайно заданные координаты y', y)
print('Отсортированный список из n точек, начиная с ближней к оси У в коорд.углу I:')
pprint(sort_xy(xy))
s_max, s_min, s_sum = calc_distances(xy,n)
print('Максимальное расстояние от центра = ',s_max)
print('Минимальное расстояние от центра = ',s_min)
print('Среднее расстояние от центра = ',s_sum)
