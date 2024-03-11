# Apuntes estadistica
import pandas as pd
import numpy as np
from scipy import stats
import seaborn as sns
import matplotlib.pyplot as plt
import statistics

# Media
a = pd.Series({"Madrid": 6685471, "Galicia": 2698764, "Murcia": 1494442, "Andalucia": 8446561})
b = pd.Series([8028, 29575, 11314, 87599], index = ["Madrid", "Galicia", "Murcia", "Andalucia"])

df = pd.DataFrame({"Poblacion": a,
                  "Superficie": b})
media_p = df["Poblacion"].mean()

#moda
rating_pelis = np.array([4,3,2,3,2,3,4,4,1,4,2,1,3,2,3,2,2,4,2,1,2])
moda_p = stats.mode(rating_pelis)

# mediana
x = [4,6,2,1,7,8,11,3]
statistics.median(x) # calculo de la mediana

#histograma
fig, axs = plt.subplots(1, 5, sharey=True)
fig.set_figwidth(20)

datos_1 = np.random.normal(100, 10, 2000)
datos_2 = np.random.normal(80, 30, 2000)
datos_3 = np.random.normal(90, 40, 2000)
datos_4 = np.random.lognormal(3, 1, 2000)
datos_5 = stats.gamma(3).rvs(2000)*20

# We can set the number of bins with the `bins` kwarg
axs[0].hist(datos_1, bins = 40)
axs[1].hist(datos_2, bins = 20)
axs[2].hist(datos_3, bins = 20)
axs[3].hist(datos_4, bins = 20)
axs[4].hist(datos_5, bins = 20)

axs[0].set_xlim([-20, 170])
axs[1].set_xlim([-20, 170])
axs[2].set_xlim([-20, 170])
axs[3].set_xlim([-20, 170])
axs[4].set_xlim([-20, 170])


sns.displot(datos_5, bins=10) # histograma

sns.boxplot(datos_5) # diagrama de caja
p_0 = np.percentile(x, 0) #Q0 #Min
p_25 = np.percentile(x, 25) #Q1
p_50 = np.percentile(x, 50) #Q2 #Mediana
p_75 = np.percentile(x, 75) #Q3
p_100 = np.percentile(x, 100) #Q4 #Max


data = pd.DataFrame([ 15, 1,  2,  3, 3,  4, 15, 6,  7,  8, 11, 15])
data['ranking'] = data.rank() # nos lo da de peor a mejor
data.sort_values(0)

# Como creamos un diagrama de caja
notas = pd.DataFrame({"Nota": [7, 9, 8, 9, 9, 7, 8, 9, 7, 8, 5, 9, 7, 8, 8, 3, 2, 1, 3] +
                              [4, 7, 2, 8, 5, 4, 4, 3, 6, 7, 5, 6, 4, 6, 7, 7, 5, 8, 5] ,
                      "Sexo": ['M', 'M', 'M', 'M', 'M', 'M', 'M', 'M', 'M', 'M', 'M', 'M', 'M', 'M', 'M', 'M', 'M', 'M', 'M'] +
                              ['H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H']})

plt.figure(figsize=(10,5))
sns.boxplot(x='Sexo', y='Nota', data=notas)
plt.grid(True)
plt.show() # Cuidado, hace show de todas las graficas de eeste archivo


edad_clase2 = [29,29,29,31,31,31]
np.var(edad_clase2) # la varianza

notas = pd.DataFrame({"Nota": [7, 9, 8, 9, 9, 7, 8, 9, 7, 8, 5, 9, 7, 8, 8, 3, 2, 1, 3] +
                              [4, 7, 2, 8, 5, 4, 2, 3, 6, 7, 5, 6, 4, 6, 7, 7, 5, 8, 5] ,
                      "Sexo": ['M', 'M', 'M', 'M', 'M', 'M', 'M', 'M', 'M', 'M', 'M', 'M', 'M', 'M', 'M', 'M', 'M', 'M', 'M'] +
                              ['H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H']})

notas.groupby('Sexo').mean() # Nos permite hacerlo uno por uno, aqui separara hombres y mujeres y hara la media
notas.groupby('Sexo').std() # Desviacion estandar o tipica