from random import randrange
from math import sqrt
from math import atan2
from math import degrees
from pprint import pprint
from pylab import * 

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
        if s > s_max :
            s_max = s
            x_max = xy[j]
            y_max = xy[j+1]
        if s < s_min :
            s_min = s
            x_min = xy[j]
            y_min = xy[j+1]
        s_sum += s   #сумма всех расстояний
        j += 2
    distances = [round(s_max), round(s_min), round(s_sum/n), x_max, y_max, x_min, y_min]
    return distances

xy = []   # [[x1,y1], [x2,y2],...]
X = []
Y = []

n = input('Введите число точек n = ')
while not n.isdigit():
    n = input('Это не число! Введите число верно ')
n = int(n)
x = [randrange(-100, 100) for i in range(n)]  #заполнили случайными числами [x1,x2,...]
y = [randrange(-100, 100) for i in range(n)]  #заполнили случайными числами [y1,y2...]

for i in range(n):
    xy.append([x[i],y[i]])

fig = plt.figure() 
fig.set_size_inches(10, 10)  #размер графика в дюймах
ax = fig.add_subplot(111)     
scatter(x,y, s=20 ,marker='o')  #рисуем точки на графике

arrow( -100, 0, 200, 0, length_includes_head = True, head_width = 5 )   # ось Х
plt.text(100, 2, "X", size = 16)  #подпись оси Х
arrow( 0, -100, 0, 200, length_includes_head = True, head_width = 5 )   # ось Y
plt.text(2, 100, "Y",size = 16)  #подпись оси Y

x_max, y_max, x_min, y_min = calc_distances(xy,n)[3:]
arrow(0, 0, x_max, y_max, lw = 0.5, ec='r')  #максимальное расстояние на графике
arrow(0, 0, x_min, y_min, lw = 0.5, ec='g')  #минимальное расстояние на графике


for elem in sort_xy(xy):
        X.append(elem[0])
        Y.append(elem[1])
for i in range(n):              #подписываем точку на графике с учетом сортировки 
    plt.text(X[i],Y[i], i+1, size = 14)

grid()  #сетка
show() 

print('Случайно заданные координаты х', x)
print('Случайно заданные координаты y', y)
print('Отсортированный список из n точек:')
pprint(sort_xy(xy))
s_max, s_min, s_sum, *rest = calc_distances(xy,n)
print('Максимальное расстояние от центра = ',s_max)
print('Минимальное расстояние от центра = ',s_min)
print('Среднее расстояние от центра = ',s_sum)
