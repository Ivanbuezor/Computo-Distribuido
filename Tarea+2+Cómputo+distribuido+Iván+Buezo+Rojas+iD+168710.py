
# coding: utf-8

# # Tarea 2 Cómputo distribuido Iván Buezo Rojas ID 168710

# ## Cortes consistentes

# Con los relojes vectoriales, el timestamp de eventos es un vector. Cada proceso conoce su posicion en el vector.

# ![Relojes vectoriales](https://www.cs.rutgers.edu/~pxk/rutgers/notes/clocks/images/clocks-vector.png)

# Si hacemos un corte en la imagen despues de los eventos c,j y l pero antes de los eventos d y m tenemos los relojes vectoriales (3,1,0),(2,2,0) y (0,0,1). Podemos ver que este corte es consistente, no hay eventos que hayan pasado y no esten en el corte. 
# Sinembargo si hacemos el corte despues de los eventos f,j y l pero antes de los eventos g k y m tenemos los relojes vectoriales (5,1,2),(2,2,0),(0,0,1) podemos ver que el corte es inconsistente, ya que el evento f depende del evento m, pero el evento m no ah pasado en el corte.

# Podemos escribir una función que nos permita saber si un corte es consistente o no con los relojes vectoriales de los eventos en la frontera del corte como input

# In[61]:


import numpy as np


# In[73]:


def corte(x):
    v=np.transpose(x)
    y=np.diag(v) #diagonal de la matriz que contiene los relojes
    lon = len(v[1]) #tamaño de los vectores
    for i in range(0,lon): 
        a = np.array(v[i] <= y[i]) #Comparamos los valores de los relojes
        if ((a==True).all() != True): #Si detecta inconsistencias
            message="el corte no es consistente"
            value=False
            break
        else:
            if i == (lon-1):#Si no detecta inconsistencias
                    message="el corte es consistente"
                    value=True
    return(message) #,value)


# In[74]:


relojes = np.array([(3,1),(0,2)])
corte(relojes)


# In[75]:


relojes = np.array([(6,3),(0,2)])
corte(relojes)


# In[76]:


relojes = np.array([(3,1,0),(2,2,0),(0,0,1)])
corte(relojes)


# In[77]:


relojes = np.array([(5,1,2),(2,2,0),(0,0,1)])
corte(relojes)

