import numpy as np; import matplotlib.pyplot as plt
x = np.sort(list(map(float, input().split()))) # ввод и сортировка выборки
if (0 <= (p := float(input("Введите вероятность p (от 0 до 1): "))) <= 1):  # ввод вероятности p и проверка корректности введенного значения
    F = np.arange(1, len(x) + 1) / len(x) # построение выборочной функции распределения F_n(x)
    plt.step(x, F, where='post'); plt.xlabel("x"); plt.ylabel("F_n(x)"); plt.grid(); plt.show()
    print("Выборочная квантиль: ", np.quantile(x, p, method='inverted_cdf')) # вычисление и вывод выборочной квантили
