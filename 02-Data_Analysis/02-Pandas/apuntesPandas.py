# Apuntes pandas, manipulacion de datos tabulares

import pandas as pd # es la convencion para abreviar pandas
import numpy as np

data = pd.Series([1.5, 1.6, 1.75, 1.80]) # serie de datos. de forma tabular

data.values # te devuelve solo los valores
data.index # te de vuelve los indices

data = pd.Series([1.5, 1.6, 1.75, 1.80], 
                 index=['Jane', 'Joe', 'Susan', 'Mike']) # Para modificar los indices
data['Jane']

population_dict = {'California': 38332521,
                   'Texas': 26448193,
                   'New York': 19651127,
                   'Florida': 19552860,
                   'Illinois': 12882135}
population = pd.Series(population_dict) # transformar un diccionario a una serie
population['California':'Florida']

pd.Series({2:'a', 1:'b', 3:'c'}) # otra forma
pd.Series({2:'a', 1:'b', 3:'c'}, index=[3, 2])
pd.Series(5, index=[100, 200, 300])

# Data frames
area_dict = {'California': 423967, 'Texas': 695662, 'New York': 141297,
             'Florida': 170312, 'Illinois': 149995}
area = pd.Series(area_dict)

states = pd.DataFrame({'population': population,
                       'area': area}) # serie de series (dataframe)

print(states.index) # Nos devuvlve los indices
print(states.columns) # Nos devuelve las columnas
print(states.values) # Nos devuelve los valores

states['area']

pd.DataFrame(data=population, columns=['population'])
print(pd.DataFrame(data=population, columns=['population']).reset_index()) # Reseteamos el index

x = pd.DataFrame(np.random.rand(3, 2), # Combinamos numpy con pandas
             columns=['Columna_1', 'Columna_2'],
             index=['a', 'b', 'c'])


ind = pd.Index([2, 3, 5, 7, 11]) # array especial para identificar cada una de las filas que tiene el dataframe

# Podemos aplicar todo lo de numpy, size, shape, ndim, dtype, slicing de cadenas, etc...


indA = pd.Index([1, 3, 5, 7, 9])
indB = pd.Index([2, 3, 5, 7, 11])

indA.intersection(indB) # Este si
indA.union(indB) # union
indA.difference(indB)  # symmetric difference

data = pd.read_csv('/url') # Leer un CSV
data.head() # Salen los 5 primeros, vale para cualquier tabla, no tiene porque ser CSV si o si

data.columns = [""] # Para cambiar sus columnas (los titulos)