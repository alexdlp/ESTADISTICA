#!/usr/bin/env python
# coding: utf-8

# 
# 
# 
# 
# ````{sidebar}
# ```{admonition} Mítico ejemplo del dado:
# 
# El espacio muestral de un dado es:
# 
# $$\Omega = \{1,2,3,4,5,6\}$$
# 
# La V.A: $X$ simboliza los posibles valores que el dado puede tomar. Osea que en caso de que $X(1) = 1$, $X(2) = 2$... y así.
# 
# Su FDP es:
# 
# $$P_X(x)= \left\{ \begin{array}{lcc}
#              \frac{1}{6} \hspace{0.5em}si\hspace{0.5em} x =1,2,3,4,5,6\\
#              \\ 0 \hspace{0.5em}en\hspace{0.5em}otro\hspace{0.5em}caso \\
#              \end{array}
#    \right.$$
# 
# ```
# 
# ```{admonition} Mítico ejemplo de la botella
# 
# Considerando el experimento de lanzar una botella al suelo y que caiga de pie. 
# 
# El espacio muestral sería: 
# 
# $$\Omega = \{éxito, fracaso\}$$
# 
# La V.A. sería 
# 
# $$X:\{éxito, fracaso\} \rightarrow \mathbb{R} $$
# y los valores $x$ que puede tomar la v.a. serían $X(éxito) = 1$ y $X(fracaso) = 0$
# 
# Su FDP es:
# 
# $$P_X(x)= \left\{ \begin{array}{lcc}
#              \frac{1}{2} \hspace{0.5em}si\hspace{0.5em} x =0,1\\
#              \\ 0 \hspace{0.5em}en\hspace{0.5em}otro\hspace{0.5em}caso \\
#              \end{array}
#    \right.$$
# ```
# ````

# 
# # Variables Aleatorias
# La idea principal del concepto de *Variable Aleatoria* es que necesitamos una herramienta que transforme los elementos del espacio muestral $\Omega$ (los posibles sucesos, como que salga cara o cruz en una moneda por ejemplo) en números con los que podamos operar.
# 
# Se representa la variable aleatoria con una letra mayúscula ($X$), y los valores que toma esa variable aleatoria con letras minúsculas ($x$).
# 
# 

# ## Espacio muestral y Dominio
# 
# El *espacio muestral* $\Omega$ es el conjunto que contiene **todos los posibles resultados/sucesos de un determinado experimento**. 
# 
# El *dominio* de una v.a. es el conjunto de todos los valores posibles que esta variable aleatoria puede tomar. Se denota:
# 
# $$D_X = \{x \in \mathbb{R} | P_X(x) > 0\}$$
# 
# El dominio de una v.a. es lo mismo que el espacio muestral ($X(\Omega) = D_X$) en caso de que los valores $x$ que pueda tomar la V.A. $X$ sean numéricos. 
# 
# Por ejemplo en el caso del dado, sí se da esa condición. Sin embargo, en el caso del experimento de la botella, su espacio muestral es $\Omega = \{éxito, fracaso\} $, pero su dominio es $D_X  = \{1,0 \}$

# # Funciones de las Variables Aleatorias
# Ahora que tenemos un chisme para transformar los **sucesos* en *números**, necesitamos otra herramienta que nos ayude a entender el **comportamiento** de esos sucesos.
# 
# ## Caso Disceto
# ````{margin}
# ```{warning}
# :class: dropdown
# Hay que andarse con ojo con estas mierdas porque entre las distintas notaciones que hay, y los distintos nombres que se les da, te puedes hacer un lio muy serio.
# A veces la podremos ver como *función de densidad de probabilidad*, o simplemente *función de densidad*. Para los ultravagos, simplemente *densidad*. Aunque para ser rigurosos, la funcion de densidad debería usarse solo para las variables continuas.
# 
# En inglés **PDF**, de *probability density function*.
# ```
# ````
# 
# ### Función de Probabilidad - caso discreto
# 
# Para el caso discreto, la *función de probabilidad* o *pdf* nos dice cual es la probabilidad de que una v.a. $X$ tome un determinado valor $x$ del dominio $D_X$. Se define:  
# 
# $$P_X(x) = P(X = x)$$
# 
# ```{admonition} Propiedades de la FDP
# :class: dropdown
# Primero en lenguaje matematicoso:
# Sea $X$ una v.a. discreta $ X:\Omega \rightarrow \mathbb{R}$ con dominio $D_X$, su función de probabilidad $P_X$ cumple lo siguiente:
# 
# * $ 0 \leq P_X(x) \leq 1 $ para todo $x \in \mathbb{R} $
# * $ \sum_{x \in D_X}P_X(x) = 1$
# 
# **En cristiano:**
# La probabilidad de que la v.a. tome uno de los valores posibles de su dominio debe estar entre 0 y 1. Lógico.
# Y el sumatorio de todas las probabilidades debe ser igual a 1. También lógico.
# ``` 
# 
# ````{margin}
# ```{warning}
# :class: dropdown
# Más nomenclature warnings. También se le llama *función de probabilidad acumulada*. O *función de distribución de probabilidad*. O función de distribución de una v.a. 
# 
# Un puto lio.
# 
# **cfd** por su acrónimo en íngles: cumulative distribution function.
# ```
# ```` 
# ### Función de distribución
# 
# La *función de distribución*  $F_X(x)$ de una v.a. $X$ representa la probabilidad de que $X$ tome un valor **menor o igual** que $x$. 
# 
# $$F_X(x) = P(X \leq x)$$
# 

# In[1]:


import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots(1, 2, figsize = (10,5))
fig.suptitle("Funciones de densidad y distribución para un dado de 6 caras", fontsize=16)
x = np.array([-2,-1,0,1,2,3,4,5,6,7,8,9])
y = np.array([0, 0, 0, 1/6, 1/6, 1/6, 1/6, 1/6, 1/6, 0, 0,0])
ysum = np.cumsum(y)

ax[0].bar(x,y,alpha = 0.8)
ax[0].set_title('Función de densidad - pdf')
ax[0].set_ylim([0, 1.05])
ax[0].set_yticks([0, 1/12, 1/6, 1/3, 1], ['0', '1/12', '1/6', '1/3', '1'])
ax[0].set_xticks([1,2,3,4,5,6], ['1','2','3','4','5','6'])
ax[0].step(x+0.5,y, color = 'r', linestyle = '--', lw = 2)
ax[0].set_xlabel('Espacio muestral - $\Omega$', )
ax[0].set_ylabel('Probabilidad  - $P(X = x)$', )

ax[1].bar(x,ysum, alpha = 0.8)
ax[1].step(x+0.53,ysum, color = 'r', linestyle = '--', lw = 2)
ax[1].set_title('Función de distribución del dado - cdf')
ax[1].set_yticks([0,1/6,2/6, 3/6,4/6,5/6, 1], ['0', '1/6', '2/6', '3/6','4/6','5/6', '1'])
ax[1].set_xticks([1,2,3,4,5,6], ['1','2','3','4','5','6'])
ax[1].set_xlabel('Espacio muestral - $\Omega$', )
ax[1].set_ylabel('Probabilidad acumulada - $P(X \leq x)$')

fig.tight_layout()
fig.subplots_adjust(top=0.82)


# **Explicación:** 
# El primer gráfico muestra como, de los valores del espacio muestral de un dado posibles ($\Omega = \{1,2,3,4,5,6\}$), la probabilidad  de que la v.a. $X$ tome uno de esos valores es de $1/6$ para cada uno de los casos ($P(X=x) = \frac{1}{6}$).
# 
# Sin embargo, el segundo de los graficos muestra cómo, la probabilidad de que la v.a. $X$ tome un valor **igual o menor** a $x$ ($P(X\leq x)$) va aumentando hasta llegar a 1. Osea que la probabilida de sacar un número menor a 2, sera de $2/6$, la de sacar un 5 será de $5/6$, y de sacar un numero menor a 10, siempre será del 100%.

# ## Caso continuo
# 
# 
# ### Función de Probabilidad - caso continuo
# 
# Igual que el caso discreto pero sobre un dominio o conjunto de valores **continuo**. Esto quiere decir que cualquier suceso único tiene probabilidad **zero** de ocurrir. 
# 
# $$P(a<X<b) = \int^{b}_{a}f_x(x)dx$$

# In[2]:


get_ipython().run_line_magic('matplotlib', 'inline')
import ipywidgets as widgets
from ipywidgets import interact

# delcaración de widgets
mu = widgets.FloatSlider(value=0,min=-5,max=5, step = 0.1, description='$\mu$:', disabled=False, continuous_update=True, orientation='horizontal',
    readout=True, readout_format='.1f')

sigma = widgets.FloatSlider(value=1,min=-5,max=5, step = 0.1, description='$\sigma$:', disabled=False, continuous_update=True, orientation='horizontal',
    readout=True,readout_format='.1f')

def plotGauss(mu = 0, sigma = 5):
    import matplotlib.pyplot as plt
    import numpy as np
    from scipy.integrate import cumulative_trapezoid
    from scipy.stats import norm
    import warnings
    warnings.simplefilter('ignore')
    
    x = np.linspace(-4,4,100)    
    y = (np.exp(-(x-mu)**2/(2*sigma**2)))/(np.sqrt(2*np.pi*sigma**2))    
 
    # z = (x-mu)/sigma; yprim = np.exp(-z**2/2)/(np.sqrt(2*np.pi)) hacer esto sería lo mismo
    
    # línea vertical 
    yvert = np.linspace(0,1.05,100)
    xvert = [mu for element in yvert]    
    
    fig, ax = plt.subplots(1, 2, figsize = (8,3))
    fig.suptitle("Funciones de densidad y distribución Gaussianas", fontsize=16)
    
    ax[0].set_xlim([-4,4])
    ax[0].set_ylim([0,1.05])
    ax[0].plot(xvert, yvert, color = 'r', linestyle = '--', alpha = 0.2)
    ax[0].set_title('Función de densidad normal - cdf')
    ax[0].plot(x, y) 
    ax[0].plot(x, norm.pdf(x)) # la de scipy, para verificar a ver si estaba bien  
    #ax[0].plot(x, yprim)

    ycdf = cumulative_trapezoid(y,x, initial=0) # cdf, la integral de pdf
    
    ax[1].set_xlim([-4,4])
    ax[1].set_ylim([0,1.05])
    ax[1].plot(xvert, yvert, color = 'r', linestyle = '--', alpha = 0.2)
    ax[1].set_title('Función de distribución normal - cdf')
    ax[1].plot(x,ycdf)
    ax[1].plot(x, norm.cdf(x)) # la de scipy, para comparar
    
    fig.tight_layout()
    fig.subplots_adjust(top=0.75)

interact(plotGauss,mu = mu, sigma=sigma);


# In[3]:


import ipywidgets as widgets
from ipywidgets import interact
get_ipython().run_line_magic('matplotlib', 'inline')
# delcaración de widgets
mu = widgets.FloatSlider(value=0,min=-5,max=5, step = 0.1, description='$\mu$:', disabled=False, continuous_update=True, orientation='horizontal',
    readout=True, readout_format='.1f')

sigma = widgets.FloatSlider(value=1,min=-5,max=5, step = 0.1, description='$\sigma$:', disabled=False, continuous_update=True, orientation='horizontal',
    readout=True,readout_format='.1f')

def plotGauss(mu = 0, sigma = 5):
    import matplotlib.pyplot as plt
    import numpy as np
    from scipy.integrate import cumulative_trapezoid
    from scipy.stats import norm
    import warnings
    warnings.simplefilter('ignore')
    
    x = np.linspace(-4,4,100)    
    y = (np.exp(-(x-mu)**2/(2*sigma**2)))/(np.sqrt(2*np.pi*sigma**2))    
 
    # z = (x-mu)/sigma; yprim = np.exp(-z**2/2)/(np.sqrt(2*np.pi)) hacer esto sería lo mismo
    
    # línea vertical 
    yvert = np.linspace(0,1.05,100)
    xvert = [mu for element in yvert]    
    
    fig, ax = plt.subplots(1, 2, figsize = (8,3))
    fig.suptitle("Funciones de densidad y distribución Gaussianas", fontsize=16)
    
    ax[0].set_xlim([-4,4])
    ax[0].set_ylim([0,1.05])
    ax[0].plot(xvert, yvert, color = 'r', linestyle = '--', alpha = 0.2)
    ax[0].set_title('Función de densidad normal - cdf')
    ax[0].plot(x, y) 
    ax[0].plot(x, norm.pdf(x)) # la de scipy, para verificar a ver si estaba bien  
    #ax[0].plot(x, yprim)

    ycdf = cumulative_trapezoid(y,x, initial=0) # cdf, la integral de pdf
    
    ax[1].set_xlim([-4,4])
    ax[1].set_ylim([0,1.05])
    ax[1].plot(xvert, yvert, color = 'r', linestyle = '--', alpha = 0.2)
    ax[1].set_title('Función de distribución normal - cdf')
    ax[1].plot(x,ycdf)
    ax[1].plot(x, norm.cdf(x)) # la de scipy, para comparar
    
    fig.tight_layout()
    fig.subplots_adjust(top=0.75)

interact(plotGauss,mu = mu, sigma=sigma);


# In[ ]:





# In[ ]:





# In[ ]:





# |       |   Discreta   |   Continua   |
# | :------------ | :-------------: |:-------------: |
# |        Distribución      |     $x_n \rightarrow p_n$          |        $f(x)$     |
# |     F(X)     |      $\sum^{n}_{i=1}p_i = 1 $     |     $ \int^{\infty}_{-\infty}f(x)dx = 1 $  |
# |     Media $\mu$     |      $\sum^{n}_{i=1}x_ip_i    $  |      $\int^{\infty}_{-\infty}xf(x)dx  $   |
# |     Varianza $\sigma^2$     |      $\sum^{n}_{i=1}(x_i-\mu)^2p_i    $   |     $ \int^{\infty}_{-\infty}(x_\mu)^2f(x)dx  $      |
