#!/usr/bin/env python
# coding: utf-8

# # Tarea 1. Daniel Rojo Mata. 

# ## Problema 1
# ### Para convertir grados celcius a Fahrenheit se hace: 
# ### $T_{F} = \displaystyle\frac{9}{5} T_{C} + 32° $
# ### En donde $T_{F}$ y $T_{C}$ hacen referencia a la temperatura en grados Fahrenheit y Celsius, respectivamente.

# In[60]:


def celsius_a_fahrenheit(T_c):
    T_f = (9/5)*T_c + 32
    return T_f


# In[62]:


celsius_a_fahrenheit(23.4)


# ## Problema 5

# In[38]:


def buscar(lista, numero):
    if numero in lista:
        print(numero)
    else:
        print("El número no está en la lista.")


# In[45]:


lista_1 = [i for i in range(0,100)]
buscar(lista_1, 21)


# In[46]:


lista_2 = [i for i in range(0,100)]
buscar(lista_2, 2001)


# ## Problema 7
# ### Sabemos que el área de un círculo es de la forma: $A = \pi \ r^2 $
# ### En donde $r$ es el radio del círculo.

# In[48]:


#Se importa el valor de "pi".
from math import pi 

def area_circulo(radio):
    A = pi*(radio**2)
    return A


# In[49]:


area_circulo(radio=3)


# ## Pregunta 11 
# ### Se define la distancia entre dos vectores, $x$ & $y$, como: 
# ### $d_{xy} = \displaystyle\sqrt{\displaystyle\sum_{i} (x_i - y_i )^2}$ 

# In[55]:


#Se define una función que encuentra la distancia entre dos puntos.
def distancia(vector_1, vector_2):
    #Los vectores tienen que tener la misma dimensión:
    if len(vector_1) == len(vector_2):
        norma_cuadrada = 0
        for indice in range(0, len(vector_1)):
            #Se define la norma al cuadrado como: Σ(xi - yi)^2
             norma_cuadrada += (vector_1[indice]-vector_2[indice])**2
        #En esta parte se le saca la raíz cuadrada a la norma.
        resultado = (norma_cuadrada)**(1/2)        
        return resultado
    else: 
        print("Las dimensiones no coinciden, vuelve a intentar.")


# In[56]:


vector_1 = [1,2,3]
vector_2 = [3,2,1]
distancia(vector_1, vector_2)


# In[58]:


vector_1 = [0,0]
vector_2 = [0,0,0]
distancia(vector_1, vector_2)


# ## Problema 15

# In[51]:


def factorial(n):
    #El factorial de cero es uno, se debe escribir esta parte al inicio.
    if n == 0: 
        return 1
    #Aquí se escribe la condición de n<=20, que es equivalente a n<21.
    elif n < 21: 
        #Se usa un contador, pero debe iniciar en uno, si se inicia en 0 todo sería 0.
        factorial = 1
        for numero in range(1, n+1):
            factorial *= numero
        return factorial
    #Si se ingresa un número mayor a 20, no calcula nada, es una restricción que se pedía.
    else:
        print("Escoge un número menor o igual a 20, por fa")


# In[52]:


factorial(7)


# In[53]:


factorial(21)


# ## Problema 17

# In[51]:


def ordenar(cadena):    
    
    #Se hace uso de las siguientes strings como guías
    MINUSCULAS = "abcdefghijklmnñopqrstuvwxyz"
    MAYUSCULAS = MINUSCULAS.upper()
    NUMEROS = "0123456789"
    
    #Las restricciones que se piden son los if, elif y else.
    
    if len(cadena) == 0:
        print("Dame otra string con más elementos, please.")
        
    elif len(cadena) < 1000:
        #Se hace una lista de comprensión en donde se almacenan las letras mínusculas.
        #En todos los casos se hizo uso de la función "sorted()" la cual ordena alfabéticamente.
        minusculas = sorted([char for char in cadena if char in MINUSCULAS])
        #Se hace una lista de comprensión y se guardan las letras mayúsculas.
        #De igual forma se usa "sorted()"
        mayusculas = sorted([char for char in cadena if char in MAYUSCULAS])
        #En esta lista se guardan los números que hay en la cadena. 
        numeros_cadena = [char for char in cadena if char in NUMEROS ]
        #Se separan los números pares, se ordenan con "sorted()".
        pares = sorted([numero for numero in numeros_cadena if int(numero)%2 ==0 ])
        #Se separan los números impares y se guardan.
        impares = sorted([numero for numero in numeros_cadena if int(numero)%2 !=0 ])
        #En este paso se concatenan todas las listas anteriores
        cadena_ordenada = minusculas + mayusculas + impares + pares
        #Se usa ".join()" para juntar todos los elementos de la cadena final obteniendo el resultado que se pide.
        cadena_final = "".join(cadena_ordenada)
        
        print(cadena_final)
    
    else:
        print("Ya te pasaste de elementos krnal")


# In[52]:


cadena = "cLAse2021864"
ordenar(cadena)


# In[53]:


ordenar("AaAaA DAniEL 987456322150")

