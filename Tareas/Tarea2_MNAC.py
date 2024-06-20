#!/usr/bin/env python
# coding: utf-8

# # Daniel Rojo Mata 

# # Problema 1

# In[3]:


def tablas_señor(tablas):

    #Esta es la condición de que el arreglo de entrada solo debe contener a lo más 10 elementos
    if len(tablas)<11:
        lista = []
        #Se selecciona el número mínimo de la lista
        num = min(tablas)
        #Mientras el numero no sea el máximo de la lista dada agregamos un valor al número mínimo
        #y si el número no se encuentra se agrega a la lista 
        while num!=max(tablas):
            num+=1
            if num not in tablas:
                lista.append(num)
        #Finalmente se regresa el número de elementos de la lista
        return len(lista)
    
    else: 
        print("El arreglo de entrada debe contener, a lo más, 10 elementos")


# In[7]:


tablas1=[7,3,4,9]
tablas2 = [0,2]
tablas3 = [i for i in range(50)]
tablas_señor(tablas3)


# # Problema 2
# 
# 

# In[63]:


#Se hace una función que recibe 2 strings
def en_comun(string1, string2):
    #Se hace una lista que contenga los elementos de la string2
    s2 = [elemento for elemento in string2]
    contador = 0
    #Iteramos em los elementos de la primera lista 
    for elemento in string1:
        #Si el elemento de la primera lista está en la segunda removemos ese elemento
        #Cada elemento que se remueve es un elemento compartido en las listas
        if elemento in s2:
            s2.remove(elemento)
            #Cada vez que se remueva el elemento, al contador se le suma 1
            contador += 1
            
    #El contador registra el número de letras que hay en común
    return contador


# In[66]:


string1 = "ccell"
string2 = "czlcc,"
en_comun(string1, string2)


# # Problema 3.

# In[60]:


#Se define la función que se pide 
def buen_dia(numero):

    #Se guardan los números en una lista
    lista_numeros = [int(i) for i in str(numero)]
    
    #Esta es la condición de que se de un número par de dígitos
    #Además está la condición de que se tenga un número menos a 10^6
    if len(lista_numeros)%2 == 0 and len(lista_numeros) < 10**6:
        n = int(len(lista_numeros)/2)
        #Estas son las mitades de los números.
        primera_mitad = lista_numeros[:n]
        segunda_mitad = lista_numeros[n:]
        #Contadores para la suma de las mitades
        suma1, suma2 = 0,0
        #Se calcula la suma de los elementos en las mitades
        for numeros in primera_mitad:
            suma1+=numeros
        for numeros in segunda_mitad:
            suma2+=numeros
        #Se hace el comparativo de las sumas
        if suma1 == suma2:
            print("Tendrá un buen día")
            return True 
        else: 
            print("Tendrá un mal día")
            return False
    #Esta condición asegura que se tiene que ingresar un número par de dígitos
    #Además asegura que se tiene que introducir un número mayor a 10 
    else:
        print("Debes ingresar un número con un número par de digitos")
    


# In[61]:


n1 = 2341
n2= 284028
n3 = 0
buen_dia(n3)


# # Problema 4

# In[58]:


def Tarros(tarros):
    
    #Esta es la lista inicial
    lista_final = tarros[:]
    #Se ordenan de menor a mayor los elementos que no son -1
    numeros = sorted([n for n in tarros if n!= -1]) #[15, 19,17,16,18]
    
    #enumerate nos da resultados de la forma (a,b) en donde "a" representa la posición (índice) del elemento "b"
    for indice, elemento in enumerate(tarros):
    #[(0, -1), (1, 15), (2, 19), (3, 17), (4, -1), (5, -1), (6, 16), (7, 18)]
    
        #Filtramos los elementos que no son -1 de la lista dada
        if elemento != -1:
            #En esta parte, a la lista inicial se le agrega el valor de los números que no son -1
            #Agregamos el primer elemento de los números, y ya están ordenados
            lista_final[indice] = numeros[0]
            #A la lista de los números ordenados le removemos el primer elemento 
            numeros.remove(numeros[0])
        
    return lista_final


# # Problema 6.

# In[129]:


#Se define la función requerida
#El argumento solo es una string
def espacios_por_guiones(string):
    #Las palabras de la string se separan por: " " y se juntan en una lista
    new_string = string.split(" ")
    #Esta es la condicion de que la string debe tener a lo más 10 palabras
    if len(new_string) < 11:
        #Aqui se están cambiando los espacios por guiones y se regresa el resultado
        return "-".join(new_string)
    else:
        #Esto es lo que se imprime en caso de que no se tengan las 10 palabras
        print("La string debe contener menos de 10 palabras, please")


# In[132]:


s1 = "Esto es una string con mas de diez palabras jaja que malo"
s2 = "Esto es una string con menos de diez palabras"
s3 = " "

espacios_por_guiones(s2)


# # Problema 10 
# 
# Me di cuenta muuuuy tarde de que el programa lo pude simplificar xd, pero ya no me dio tiempo de modificar 😬

# ### Se grafica la función del problema 16
# 
# $f(x) = 230x^4 + 18x^3 + 9x^2 -221x -9$

# In[100]:


import numpy as np
import matplotlib.pyplot as plt

#Se define la función 
def f16(x):
    f = 230*(x**4) + 18*(x**3)+9*(x**2)-221*x-9
    return f

#Se define el intervalo con el cual la función será evaluada 
x = np.linspace(-2,2,100)

#Se grafica
fig = plt.subplots(1,2, figsize = (18, 5))

#Se está graficando la función de tal manera que se pueda ver cómo es 
plt.subplot(1,2,1)
#Esta es la gráfica del polinomio con todo el dominio dado por x
plt.plot(x,f16(x), color = "Blue", label="$f(x) = 230x^4 + 18x^3 + 9x^2 -221x -9$" )
#Se grafica la función f(x)=0, para observar los cortes con la gráfica
plt.axhline(0, color='red', linestyle='--', label = "f(x) = 0")
plt.ylim(-200, 1000)
#Título de la gráfica y en los ejes
plt.title("Grafica del problema 16. 'Gráfica completa.' ",fontdict={'fontname': "Comic Sans MS", "fontsize": 15})
plt.xlabel("x",fontdict={'fontname': "Comic Sans MS", "fontsize": 15})
plt.ylabel("f(x)", fontdict={'fontname': "Comic Sans MS", "fontsize": 15})

plt.grid()
plt.legend()


plt.subplot(1,2,2)
#Se grafica la función pero haciendo "zoom" en donde están las raíces
plt.plot(x,f16(x), color = "Blue", label="$f(x) = 230x^4 + 18x^3 + 9x^2 -221x -9$" )
#Se grafica la función f(x)=0, para observar los cortes con la gráfica
plt.axhline(0, color='red', linestyle='--', label = "f(x) = 0")
#Título de la gráfica y en los ejes
plt.title("Grafica del problema 16. 'Gráfica con zoom.' ", fontdict={'fontname': "Comic Sans MS", "fontsize": 15})
plt.xlabel("x",fontdict={'fontname': "Comic Sans MS", "fontsize": 15})
plt.ylabel("f(x)", fontdict={'fontname': "Comic Sans MS", "fontsize": 15})
#Limites de los ejes
plt.xlim(-.4,1.2)
plt.ylim(-150, 150)

plt.legend()
plt.grid()
plt.show()


# ### Se grafica la función del problema 17
# $f(x) = tan(\pi x) - 6$

# In[99]:


import numpy as np
import matplotlib.pyplot as plt


#Se define la función 
def f17(x):
    f =np.tan(np.pi*x)-6
    return f


#Se define el intervalo con el cual la función será evaluada 
x = np.linspace(-2,2,100)

#Se grafica
fig = plt.subplots(1,2, figsize = (18, 5))

#Se está graficando la función de tal manera que se pueda ver cómo es 
plt.subplot(1,2,1)
#Esta es la gráfica de la función trigonométrica con todo el dominio dado por x
plt.plot(x,f17(x),  color = "Green", label="$f(x) = tan(\pi x) - 6$" )
#Se grafica la función f(x)=0, para observar los cortes con la gráfica
plt.axhline(0, color='red', linestyle='--', label = "f(x) = 0")
#Límites de graficación
plt.ylim(-75, 10)
plt.xlim(0.3, 0.6)
#Título de la gráfica y en los ejes
plt.title("Grafica del problema 17 en el intervalo [0.3, 0.6]. ", fontdict={'fontname': "Comic Sans MS", "fontsize": 15})
plt.xlabel("x",fontdict={'fontname': "Comic Sans MS", "fontsize": 15})
plt.ylabel("f(x)", fontdict={'fontname': "Comic Sans MS", "fontsize": 15})

plt.grid()
plt.legend()

plt.subplot(1,2,2)
#Se grafica la función pero haciendo "zoom" en donde están las raíces
plt.plot(x,f17(x), color = "Green", label="$f(x) = tan(\pi x) - 6$" )
#Se grafica la función f(x)=0, para observar los cortes con la gráfica
plt.axhline(0, color='red', linestyle='--', label = "f(x) = 0")
#Título de la gráfica y en los ejes
plt.title("Grafica del problema 17. 'Gráfica con zoom.' ", fontdict={'fontname': "Comic Sans MS", "fontsize": 15})
plt.xlabel("x",fontdict={'fontname': "Comic Sans MS", "fontsize": 15})
plt.ylabel("f(x)", fontdict={'fontname': "Comic Sans MS", "fontsize": 15})
#Límites de graficación
plt.xlim(0.43,0.48)
plt.ylim(-5, 5)

plt.legend()
plt.grid()
plt.show()


# # Problema 11.
# 
# ### No estoy muy seguro, pero creo que necesitábos la masa y la constante del resorte (la k), esto porque en la energía cinética y en la potencial se usan.
# 
# ### Cuando los necesitaba, los tomé como 1, y ese es el caso que presento. Vemos que hay conservación de la energía, pero en otros casos no es muy claro.

# In[1]:


import numpy as np
import matplotlib.pyplot as plt

#Oscilador armónico 
class oscilador():
    """
    Clase que genera un movimiento oscilatorio 
    """
    
    #Se definen los principales atributos del oscilador
    def __init__(self, xm , omega , phi): 
        #Amplitud:
        self.xm = xm
        #Frecuencia:
        self.omega = omega
        #Fase:
        self.phi = phi
    
    #Se define la función de la posición
    def posicion(self, t):
        pos = self.xm*np.cos(self.omega*t + self.phi)
        return pos
    
    #Se define la energia cinética
    #Para ello se derivó la función de posición
    def energia_cinetica(self, t):
        vx = -self.xm*self.omega*np.sin(self.omega*t + self.phi)
        #Aquí fue en donde hice la masa igual a 1
        cinetica = (0.5)*vx**2
        return cinetica
    
    #Se define la energia potencial
    #Se hizo el factor k = 1
    def energia_potencial(self, pos):
        pot = (0.5)*(pos)**2
        return pot
    
    #Se define la energía mecánica
    def energia_mecanica(self, cinetica, potencial):
        mecanica = cinetica + potencial
        return mecanica
    
    #Se grafica la posición
    def grafica_posicion(self, pos):
        fig = plt.subplots( figsize = (18, 5))
        plt.plot(t, pos, color = "Orange",
                label = f"$\omega$ = {self.omega}")
        plt.title("Posición",fontdict={'fontname': "Comic Sans MS", "fontsize": 15})
        plt.xlabel("$t \ [s]$",fontdict={'fontname': "Comic Sans MS", "fontsize": 15})
        plt.ylabel("$x(t) \ [m]$",fontdict={'fontname': "Comic Sans MS", "fontsize": 15})
        plt.grid()
        plt.legend()
    
    #Se grafican las energías
    def graficas_energias(self, cinetica, potencial, mecanica):
        
        fig = plt.subplots(1,3, figsize = (18, 5))
        plt.subplot(1, 3, 1)
        plt.plot(t, cinetica, color = "Blue",
                 label = f"$\omega$ = {self.omega}")
        plt.title("Energía Cinética",fontdict={'fontname': "Comic Sans MS", "fontsize": 15})
        plt.xlabel("$t \ [s]$",fontdict={'fontname': "Comic Sans MS", "fontsize": 15})
        plt.ylabel("$KE \ [Joules]$",fontdict={'fontname': "Comic Sans MS", "fontsize": 15})
        plt.grid()
        plt.legend()
        
        plt.subplot(1, 3, 2) 
        plt.plot(t,potencial, color = "Red", 
                 label = f"$\omega$ = {self.omega}")
        plt.title("Energía Potencial",fontdict={'fontname': "Comic Sans MS", "fontsize": 15})        
        plt.xlabel("$x \ [m]$",fontdict={'fontname': "Comic Sans MS", "fontsize": 15})
        plt.ylabel("$PE \ [Joules]$",fontdict={'fontname': "Comic Sans MS", "fontsize": 15})
        plt.grid()
        plt.legend()

        plt.subplot(1, 3, 3) 
        plt.plot(t, mecanica, color = "Green",
                label = f"$\omega$ = {self.omega}")
        plt.title("Energía Mecánica",fontdict={'fontname': "Comic Sans MS", "fontsize": 15})
        plt.xlabel("$t \ [s]$", fontdict={'fontname': "Comic Sans MS", "fontsize": 15})
        plt.ylabel("$EM \ [Joules]$", fontdict={'fontname': "Comic Sans MS", "fontsize": 15})
        plt.grid()
        plt.legend()

#En esta función se hace lo de calcular 3 diferentes frecuencias
def frecuencias(t, frecuencias, xm, phi):
    plt.figure(figsize=[18,6])
    for omega in frecuencias:
        p = oscilador(xm, omega, phi)
        y = p.posicion(t)
        plt.plot(t, y, label = f"$\omega$ = {omega}")
    plt.title("Oscilador armónico, distintas frecuencias",fontdict={'fontname': "Comic Sans MS", "fontsize": 15})
    plt.xlabel("$t \ [s]$", fontdict={'fontname': "Comic Sans MS", "fontsize": 15})
    plt.ylabel("$x(t)\ [m]$", fontdict={'fontname': "Comic Sans MS", "fontsize": 15})
    plt.grid()
    plt.legend()
    plt.show()       
            

#Este es un parámetro de tiempo
def tiempo(t0, tf, bins):
    t = np.linspace(t0, tf , bins)
    return t


# In[2]:


t = tiempo(t0=0, tf=5, bins=1000)

#Se define nuestro objeto
p1 = oscilador(xm=3, omega=1, phi=0)

#función posición
pos = p1.posicion(t)
#Energía cinética
cinetica = p1.energia_cinetica(t)
#Energía potencial
potencial = p1.energia_potencial(pos)
#Energía mecánica
mecanica = p1.energia_mecanica(cinetica, potencial)

#Cabe recalcar que solo se están haciendo las gráficas de la energía de un objeto
p1.graficas_energias(cinetica, potencial, mecanica)
#Gráfica de la posición de nuestro objeto
p1.grafica_posicion(pos)
#Estas son las gráficas de distintos objetos con distintas frecuencias
frecuencias(t,[1,2,3], xm=2, phi=0)


# # Problema 12

# In[200]:


import numpy as np 
import matplotlib.pyplot as plt 
from scipy.optimize import fsolve


# ## $x − 2x − 5 = 0 \ en \ [1, 4]$

# In[156]:


def raices(f, intervalo):
    solucion = fsolve(f, intervalo)
    return solucion

def grafica(f,x,raices, intervalo, titulo):
    
    #plt.figure(figsize=[10,6])
    fig = plt.subplots(1,2, figsize = (18, 5))
    
    plt.subplot(1,2,1)
    #Esta es la gráfica de la función trigonométrica con todo el dominio dado por x
    plt.plot(x,f(x),  color = "Green", label=titulo )
    #Se grafica la función f(x)=0, para observar los cortes con la gráfica
    plt.axhline(0, color='red', linestyle='--', label = "f(x) = 0")
    #Límites de graficación
    #Título de la gráfica y en los ejes
    plt.title("f(x)", 
              fontdict={'fontname': "Comic Sans MS", "fontsize": 15})
    plt.xlabel("x",fontdict={'fontname': "Comic Sans MS", "fontsize": 15})
    plt.ylabel("f(x)", fontdict={'fontname': "Comic Sans MS", "fontsize": 15})
    plt.grid()
    plt.legend()

    plt.subplot(1,2,2)
    plt.plot(x, f(x), color="blue", label = titulo)
    plt.axhline(0, color ="r", linestyle = "--", label = "f(x)=0")
    plt.plot(raices[0], 0 ,color = "Green", marker = "o", label = f"Raices: {raices}")
    plt.title("Raices de f(x)", fontdict={'fontname': "Comic Sans MS", "fontsize": 15})
    plt.xlabel("x", fontdict={'fontname': "Comic Sans MS", "fontsize": 15})
    plt.ylabel("f(x)", fontdict={'fontname': "Comic Sans MS", "fontsize": 15})
    plt.xlim(intervalo[0], intervalo[1])
    plt.grid()
    plt.legend()


# In[140]:


f1 = lambda x: x - 2*x -5
x = np.linspace(-10,5,100)
intervalo = [1,4]
root = raices(f1, intervalo)
grafica(f1,x,root,intervalo,titulo="$f(x)=x-2x - 5$")


# ## $x - cos(x) \ en \ \left[0,\displaystyle\frac{\pi}{2} \right]$

# In[141]:


f2 = lambda x: x - np.cos(x)
x = np.linspace(-10,5,100)
intervalo = [0,(np.pi)/2]
root2 = raices(f2,intervalo)
grafica(f2,x,root2, intervalo, titulo = "$f(x) = x - Cos(x)$" )


# ## $x + 3x − 1 = 0 \ en \ [−3, −2]$

# In[142]:


f3 = lambda x: x +3*x -1
x = np.linspace(-10,5,100)
intervalo = [-3,-2]
root3 = raices(f3,intervalo)
grafica(f3,x,root3,intervalo, titulo = "$f(x)= x + 3x -1$")


#  ## $x − 0.8 − 0.2 sin x = 0 \ en \ [0, π/2] $

# In[143]:


f4 = lambda x: x -0.8-0.2*np.sin(x)
x = np.linspace(-10,5,100)
intervalo = intervalo = [0,(np.pi)/2]
root4 = raices(f4,intervalo)
grafica(f4,x,root4,intervalo, titulo = "$f(x)=x - 0.8 -0.2Sin(x)$")


# # Pregunta 14

# ## $4x Cos(2x) - (x-2) = 0 \ en \ [0,8]$

# In[210]:


import numpy as np 
import matplotlib.pyplot as plt 
#Se usará el método de Newton
from scipy.optimize import newton


#Se define la función a la que queremos encontrar las raíces
f = lambda x: 4*x*np.cos(2*x)-(x-2)
#Se debe definir la derivada de la función
fprime = lambda x: -8*x*np.sin(2*x) + 4*np.cos(2*x)-1
#Este es el dominio
x = np.linspace(0,8,200)

#Esta es la presición
error = 10**-5
#Estos son los valores de x0 en donde el método inicia 
#Se itera en estos para aproximar las soluciones
intervalo = [1, 2, 4, 6, 7]

#Se grafica la función
plt.figure(figsize=[18,6])
#Para encontrar las soluciones se itera en distintas condiciones iniciales
for x0 in intervalo:
    #Se aplica el método de Newton
    solucion = newton(f,x0,fprime,tol=error)
    print(f"Una raíz es: {solucion} ")
    #Se grafican las raíces
    plt.plot(solucion, 0, marker = "s",label=f"raiz: {solucion}")

#Se grafica la función 
plt.plot(x,f(x), color="blue", label = "$f(x)=4xCos(2x) - (x-2)$")
plt.title("Gráfica problema 14", fontdict={'fontname': "Comic Sans MS", "fontsize": 15})
plt.axhline(0, color = "green", linestyle ="--")
plt.xlim(0,8)
plt.xlabel("x",fontdict={'fontname': "Comic Sans MS", "fontsize": 15})
plt.ylabel("f(x)", fontdict={'fontname': "Comic Sans MS", "fontsize": 15})
plt.grid()
plt.legend()
plt.show()

