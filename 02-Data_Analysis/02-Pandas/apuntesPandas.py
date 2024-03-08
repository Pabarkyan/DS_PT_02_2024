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

#data = pd.read_csv('/url') # Leer un CSV
data = {'California': 38332521,
                   'Texas': 26448193,
                   'New York': 19651127,
                   'Florida': 19552860,
                   'Illinois': 12882135}
data = pd.Series(population_dict)
data.head() # Salen los 5 primeros, vale para cualquier tabla, no tiene porque ser CSV si o si

data.columns = [""] # Para cambiar sus columnas (los titulos)
data.keys() # a pesar de no ser un diccionario, podemos aplicar keys
list(data.items())


# Cuando estamos en pandas el "and" lo tenemos que sustituir poru n "&"
# idem con el or y | y not con  ~ (Alt Gr + 4)

data = pd.Series([0.25, 0.5, 0.75, 1.0],
                 index=['a', 'b', 'c', 'd'])
data[(data > 0.3) & (data < 0.8)]
data[(data>0.5)&(data<=1)]
data[(data==0.5)|(data==1)]
data[data.isin([1, 0.5])] # idem al de arriba, ns como es

data.loc # Permite la indexacion y el corte que siempre hace referencia al indice explicito
data.iloc # Permite indexar y slicing que siempre hace referencia al indice implicito estilo Python

###
area = pd.Series({'California': 423967, 'Texas': 695662,
                  'New York': 141297, 'Florida': 170312,
                  'Illinois': 149995})
pop = pd.Series({'California': 38332521, 'Texas': 26448193,
                 'New York': 19651127, 'Florida': 19552860,
                 'Illinois': 12882135})

data = pd.DataFrame({'area':area, 'pop':pop})

data['area'] # es equivalente a data.area aunque  esta ultima forma es muy mala practica
# CUIDADO con poner nombres que igualan a metodos (pop)
data.pop # Uqtilizamos mejor data['pop']


# Generacion de columnas
data['density'] = data['pop'] / data['area']
print(data.T) # Traspuesta de la matriz

print(data.loc["Texas":"New York", "pop":"density"]) #Podemos elegir de esta manera lo que sacar
print(data.loc[data.density > 100, ["pop", "density"]])

# Mostrar el area de los estados cuya poblacion sea mas de 20 millones de habitantes
print(data.loc[data['pop'] > 20_000_000, ["area"]]) # No utilizamos el .pop para que no lo confunda con el metodo
print(data[data['pop'] > 20_000_000]['area'])
# La diferencia es que uno devuvlve un type serie y otro devuelve un dataframe

# El iloc no se usa demasiado