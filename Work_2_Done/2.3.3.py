import pandas as pd


df = pd.read_csv("adult.csv")

print(df)

print("Взглянем на первые строки: ")
print(df.head(2), "\n")

print("Взглянем на последние строки: ")
print(df.tail(3))

print("Взглянем на кол-во строк и столбцов: ")
print("Строк:", df.shape, "Столбцов", '\n')

print("Получим описательную статистику для любых числовых столбцов: ")
print(df.describe, '\n')


print("Выберите инидвидуальные данные или срезы фрейма данных: ")
print(df.iloc[1:4])

