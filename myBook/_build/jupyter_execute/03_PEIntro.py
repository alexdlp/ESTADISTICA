#!/usr/bin/env python
# coding: utf-8

# # Procesos estocásticos
# 
# * Introducción 2h
# * Procesos de Poisson 6h
# * Procesos de renovación 6h
# * Cadenas de Markov en tiempo discreto 6h
# * Cadenas de Markov en tiempo continuo 6h
# 

# ## Introducción a los procesos estocásticos
# 
# Los procesos estocásticos tratan de modelizar situaciones que cambian en el tiempo y que están sometidas a las regas del azar. Este tipo de situaciones en las que interviene el azar tratamos de describirlas desde un punto de vista matemático.
# 
# Desde un punto de vista matemático, un proceso estocástico es un conjunto de variables aleatorias que pertenecen a un índice temporal.
# $$ \{Z_t, t \in I\} $$
# 
# Es decir, los instantes de tiempo en donde se observa el proceso están contenidos en el intervalo temporal $I$.
# 
# $Z_t$ puede representar:
# 
# * el número de clientes en una cola en el instante $t$
# * precio de un activo financiero en el instante $t$
#   
# ### Procesos en tiempo discreto y continuo
# $(\Omega, \mathcal{F}, P)$ : Espacio Probabilístico
# 
# * $\Omega$: conjunto de posibles resultados de un experimento. En el caso de un dado: $\Omega = \{1,2,3,4,5,6\}$
# * $\mathcal{F}$: familia de subconjuntos/sucesos asociados al experimento. Ejemplo: $A \in \mathcal{F} $ siendo $A = \{número \hspace{1em} par\}$
# * $P$: Función de probabilidad definida sobre la familia de sucesos. $P.\mathcal{F} \rightarrow [0,1]$, $ A \rightsquigarrow P(A)$ ($A$ tiene una probabilidad asociada $P(A)$)
# 
# Lo que tenemos sobre el espacio probabilístico son variables aleatorias $Z_t$, habiendo una variable aleatoria $Z_t$ para cada $t \in I$ definida sobre $\mathbb{R}$ 
# 
# $$Z_t:\Omega \rightarrow \mathbb{R} $$ 
# 
# donde $Z_t$ es la variable que estamos observando en el instante $t$ (precio, número de personas en cola...) y que nos indica el *estado* del sistema en dicho instante.
# 
# El conjunto de índices $I$ suele ser un subconjunto de $[0,\infty]$. Los casos más importantes: APUNTES
# 
# Ejemplo sencillo de un proceso estocástico:
# Lanzo un dado 30 veces y anoto los resultados
# $\Omega = \{(w_1, ..., w_30\}$, donde $w_t$ es el resultado del lanzamiento en el momento $t$.
# $\mathcal{F}$: familia de sucesos, partes de $\Omega$
# Proceso estocástico:
# $$\begin{equation}
# \begin{split}
# Z_t : \Omega  \Rightarrow \mathbb{R} \\
# w \Rightarrow w_t
# \end{split}
# \end{equation}$$
# 
# 

# 
