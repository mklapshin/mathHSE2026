import numpy as np; import matplotlib.pyplot as plt; from scipy.stats import gaussian_kde 
x = np.array(list(map(float, input("Введите выборку через пробел: ").split()))) 
kde = gaussian_kde(x) # строим ядерную оценку плотности для выборки (KDE)
xx = np.linspace(x.min(), x.max(), 200) # создаем точки по оси x для построения графика - начало диапазона, конец диапазона, количество точек
plt.plot(xx, kde(xx)); plt.xlabel("x"); plt.ylabel("f(x)"); plt.grid(); plt.show() # строим график оцененной плотности - подписи осей x, y, добавляем сетку, показываем график
