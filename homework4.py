import numpy as np; from scipy.stats import skew, kurtosis
sample = np.array(input("Введите выборку через пробел: ").split(), float) # ввод значений выборки
expectation = sample.mean() # Вычисляем выборочное среднее — оценку математического ожидания
print("Мат. ожидание:", expectation)
print("Медиана:", np.median(sample)) # Вычисляем и выводим медиану выборки
for ddof in (0, 1): # Перебираем два варианта расчёта дисперсии: со смещением и без смещения
    variance = np.var(sample, ddof=ddof) # Вычисляем дисперсию: ddof=0 — деление на n, ddof=1 — на n-1
    print(f"Дисперсия (ddof={ddof}):", variance)
    print(f"СКО (ddof={ddof}):", np.sqrt(variance))
print("Асимметрия (несмещённая): ", skew(sample, bias=False)) # Вычисляем и выводим скорректированный коэффициент асимметрии
print("Эксцесс (несмещённый): ", kurtosis(sample, bias=False)) # Вычисляем и выводим скорректированный эксцесс
