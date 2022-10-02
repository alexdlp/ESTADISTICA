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
# Los procesos estocásticos tratan de modelizar situaciones que cambian en el tiempo y cuya evolución está sometida a las reglas del azar.
# 
# Desde un punto de vista matemático, un proceso estocástico es un conjunto de variables aleatorias $Z_t$ que pertenecen a un índice temporal $I$.
# 
# $$ \{Z_t, t \in I\} $$
# 
# Es decir, los instantes de tiempo en donde se observa el proceso están contenidos en el intervalo temporal $I$.
# 
# $Z_t$ es una variable aleatoria que puede representar:
# 
# * el número de clientes en una cola en el instante $t$
# * precio de un activo financiero en el instante $t$
# * el número de reclamaciones que recibe una compañia en el instante $t$
# 
# ````{admonition} Minirepaso del concepto de espacio probabilístico
# 
# Un espacio probabilístico  $(\Omega, \mathcal{F}, P)$  está compuesto de:
# 
# ```{margin}
# En el caso de un dado: $\Omega = \{1,2,3,4,5,6\}$
# ```
# 
# * $\Omega$: conjunto de posibles resultados de un experimento. 
# ```{margin}
# Ejemplo: $A \in \mathcal{F} $ siendo $A = \{número \hspace{1em} par\}$
# ```
# * $\mathcal{F}$: familia de subconjuntos/sucesos asociados al experimento. 
# * $P$: Función de probabilidad definida sobre la familia de sucesos. 
# 
# ```{margin}
# $A$ tiene una probabilidad asociada $P(A)$
# ```
# 
# $$\begin{split}
# P:\mathcal{F}  \rightarrow [0,1] \\
# A \rightsquigarrow P(A)
# \end{split}$$
# ````

# ### Procesos en tiempo discreto y continuo
# 
# En un proceso estocástico lo que tenemos sobre el espacio probabilístico son variables aleatorias $Z_t$ definidas sobre $\Omega$ y que toman valores en $\mathbb{R}$, habiendo una variable aleatoria $Z_t$ para cada $t \in I$
# 
# $$Z_t:\Omega \rightarrow \mathbb{R} $$ 
# 
# donde $Z_t$ es la variable que estamos observando en el instante $t$ (precio, número de personas en cola...) y que nos indica el ***estado*** del sistema en dicho instante.
# 
# El conjunto de índices $I$ suele ser un subconjunto de $[0,\infty]$. 
# 
# * Si $I$ toma valores discretos ($I = {0,1,2,...}$) se dice que es un proceso en **tiempo discreto**:
#     * $Z_t$: número de clientes atendidos en una tienda el día $t$-ésimo
#     * $Z_t$: lluvia o no eun una localidad el día $t$-ésimo
#     * $Z_t$: precio en bolsa de un activo financiero **al final** del día $t$-ésimo
# * Si $I$ toma valores continuos ($I = [0,\infty]$) se dice que es un proceso en **tiempo continuo**:
#     * $Z_t$: número de clientes esperando en una cola en el instante $t$
#     * $Z_t$: número de reclamaciones en una compañía de seguros hasta el isntante $t$
#     * $Z_t$: precio en bolsa de un activo financiero en un instante de tiempo $t$

# ```{admonition} Ejemplo sencillo de un proceso estocástico
# :class: dropdown
# Lanzo un dado 30 veces y anoto los resultados
# 
# * El espacio muestral $\Omega = \{(w_1, ..., w_{30}\}$, donde $w_t$ es el resultado del lanzamiento en el momento $t$.
# 
# * $\mathcal{F}$: familia de sucesos, partes de $\Omega$
# 
# Por ejemplo, si quisiesemos saber la probabilidad de que en todos los lanzamiento saliese un número par:
#         
# * El suceso sería: $A = \{salir \hspace{0.5em} par \hspace{0.5em} siempre\}$
# * Este suceso $A$ pertenecería a la familia de sucesos $\mathcal{F}$, $A \in \mathcal{F} $
# * El suceso $A$ tendría una probabilidad asociada $P(A)$ ( que sería igual a multiplicar $P({número \hspace{0.5em} par})$) por las veces que hayamos tirado el dado, en este caso 30. En este caso podemos hacer esto porque ***no tenemos correlación*** entre las distintas variables aleatorias $w_t$
# 
# El Proceso Estocástico sería el siguiente:
# 
# $$
# \begin{split}
# Z_t : \Omega  \Rightarrow \mathbb{R} \\
# w \Rightarrow w_t
# \end{split}
# $$
# ```

# ### Espacio de estados discretos y continuos 
# 
# El espacio de estados $E$ es el subconjunto de $\mathbb{R}$ que contiene todos los valores posibles de las variables aleatorias.
# 
# Esto *CREO* que es lo mismo que el dominio. Esta profe le llama distinto pero conceptualmente es lo mismo. En el lanzamiento de un dado, las variables aleatorias toman valores en $\mathbb{R}$, pero el espacio de estados es $\{1,2,3,4,5,6\}$
# 
# Según los valores que pueda tomar el espacoio de estados, este será discreto o continuo:
# 
# * Procesos con espacio de estados $E$ **discreto**:
#     * Número de clientes esperando en una cola: $E= 1,2,...$
#     * Registros diarios de lluvias: $E = \{0(no \hspace{0.5}em lluvia), 1 (lluvia)\}
# * Procesos con espacio de estados $E$ **continuo**:
#     * Precio en bolsa de un activo financiero: $E = [0, \infty)$
#     * Temperaturas máximas diarias en una localidad:  $E = [0, \infty)$

# ### Trayectorias de un proceso
# 
# Si estamos observando un proceso, en cada instante de tiempo, podemos anotar lo que ha sucedido.
# 
# Dado un elemento del espacio muestral $w \in \Omega$, una trayectoria del proceso está constituída por los valores concretos que que va tomando el proceso sobre ese elemento del espacio muestral para cada instante de tiempo $\{Z_t(w), t \in I\}$
# 
# También se le puede llamar función muestral o realización. Vamos con un example:
# 
# 
# IMAGEN
# 
# Para el ejemplo de la imagen, el inicio $0$ correspondería con el instante en el que abrimos la compañía. La trayectoria desde $0$ hasta $T_1$ sería de 0 reclamaciones.
# Después de que pase un tiempo aleatorio $t_1$ llega la primera reclamación, y el contador sube a 1. Se mantiene en 1 hasta que pasa otro tiempo aleatorio $t_2$ en el que llega la segunda reclamación. 
# 
# Es decir, la trayectoria asociada a este proceso que describe el número de reclamaciones hasta el instante $t$ es **una función** que va pegando saltos en instantes aleatorios dependiendo de cuando sucedan las reclamaciones.

# ### Distribuciones de probabilidad asociadas a un proceso
# 
# Cuando trabajamos con estas cosas, lo primero que tengo que hacer es definir lo que es un proceso estocástico.
# 
# Después ya puedo calcular las probabilidades asociadas a ese proceso. Para ello hay que saber:
# 
# * **Cómo se distribuyen las variables aleatorias**
# * **Cómo se relacionan entre sí**
# 
# De esta manera, un proceso estocástico se describe mediante sus distribuciones finito-dimensionales.
# Es decir, dados instantes de tiempo pertenecientes al intervalo temporal, hay que indicar la distribución de las variables $(Z_{t_1},..., Z_{t_n})$
# 
# $$(Z_{t_1},..., Z_{t_n}), \hspace{0.5em} para \hspace{0.5em} t_1,...,t_n \in I $$
# 
# Si describo la distribución de probabilidades finito-dimensionales para cualesquiera intantes de tiempoy cualesquiera variables, hayaremos las distribuciones del proceso.
# 
# Para los casos más sencillos me vale con dar la **distribución de cada $Z_t$**, (se le llama marginal-unidimensional) y **especificar las relaciones de dependencia** de las variables del proceso.
# 
# ```{admonition} Por ejemplo
# :class: dropdown
# $Z_t$ resultado de del lanzamiento del dado en el instante $t$ pues ya sé que es una variable que toma los valores $\{1,2,3,4,5,6\}$ con $P = 1/6$. Eso sería la marginal unidimensional de cada $Z_t$.
# 
# Y luego, para hacer cálculos globales que relacionen las variables del proceso, necesitaré especificar las relaciones de dependencia de las variables del proceso.
# 
# En el ejemplo del dado es sencillo porque simplemente diciendo que todas las variables del proceso son independientes podría hacer cualquier cálculo.
# 
# La probabilidad de salir par en todos los lanzamientos es igual al producto de la probabilidad de salir par en cada lanzamiento concreto. (Porque las variables son **independientes**)
# 
# Entonces, sabiendo la distribución de las variables y su relación, ya podría calcular cualquier cosa de ese proceso.
# 
# Normalmente las cosas no van a ser tan sencillas como en este ejemplo, porque las variables suelen tener relaciones de dependencia.
# ```
# 

# ## Distribuciones de un proceso. Poisson
# El proceso de Poisson es un proceso:
# * en tiempo continuo $I = [0,\infty)$
# * con espacio de estados discreto $E = 1,2,...$
# 
# Es un proceso especialmente adecuado para describir, por ejemplo, el número de reclamaciones de una compañia de seguros.
# 
# ¿Cómo lo definimos? Las variables del proceso, que serán el número de reclamaciones recibidas hasta el instante $t$ verificará:
# 
# * El incremento de reclamaciones entre dos instantes de tiempo $(Z_{t_2}-Z_{t_1})$ es una distrinbución de Poisson de parámetro $\lambda(t_1-t_2)$
# * Los incrementos del proceso son independientes
# 
# De alguna manera, el proceso de Poisson ya tiene relaciones de dependencia entre las variables, pero el hecho de que los incrementos sean independientes, me facilitará mucho la tarea de hacer cálculos.

# ### Cuestiones de existencia
# 
# A esta parte tampoco hay que hacerle mucho caso, es un poco fumada.
# 
# Una vez espacifiquemos las distribuciones del proceso hay que asegurarse de **la existencia** de ese proceso estocástico para poder estudiarlo matematicamente. Para eso debemos encontrar:
# 
# * Un espacio probabilístico $(\Omega,\mathcal{F} ,P)$
# * Sobre ese espacio probabilistico tendría que ser capaz de definir un conjunto de variables aleatorias $Z_t$ de forma que sus distribuciones finito dimensionales sean las asociadas a $(Z_{t_1},..., Z_{t_n}), \hspace{0.5em} para \hspace{0.5em} t_1,...,t_n \in I $
# 
# ¿Cómo construímos procesos estocásticos? Hay un par de maneras:
# 
# * Con construcciones ad-hoc: Procesos de Poisson, Cadenas de Markov, Movimiento Browniano
# * Resultados generales sobre la existencia: Teorema de Kolmogorov. Este teorema dice que que si asignas las probabilidades de modo consistente, viene el señor kolmogorov en persona a tu casa a garantizarte que existe un espacio probabilistico para que tu proceso estocastico se desarrolle tranquilamente. 
# 
# Pero vamos, que no es mi lucha.

# ## El proceso de Poisson
# 
# El proceso de Poisson es un proceso de recuento.
# 
# Un proceso de recuento es un proceso en tiempo continuo tal que $(N(t), t \geq 0)$
# 
# $N(t)$ puede representar:
# * número de coches que pasan por un determinado punto de una carretera
# * número de clientes que llegan a una tienda 
# * número de reclamaciones de una compañia de seguros
# 
# Es decir, un proceso de recuento es una sucesion de variables aleatorias $N(t)$ cuyo espacio de estados es $\{0,1,2,3,...\}$ porque van contando las cosas que pasan hasta un instante de tiempo.
# 
# Pare definir algo que cuente las cosas que pasan hasta un instante de tiempo, ¿cuáles son las propiedades que le vamos a requerir a ese algo?
# * $N(0) \geq 0$
# * $N(t)$ toman valores en $\mathbb{N}$, en los naturales.
# * El proceso de recuento me cuenta lo que ha sucedido hasta el instante $t$, luego si un instante $s$ tal que $s < t$, entonces $N(s) < N(t)$. (Vamos que si estoy sentado en un banco contando los coches que pasan, no pueden haber pasado 50 el primer minuto, y 10 en el siguiente, el conteo siempre es ascendente)
# * Para $s<t$, $N(t)-N(s)$ cuenta el número de sucesos que hN ocurrido en el intervalo $(s, t]$
# 
# Dado un proceso de recuento $(N(t), t \geq 0)$ vamos a hablar de dos propiedades que debe tener un proceso de Poisson, aunque estas propiedades también pueden describir un proceso estocástico general.
# 
# 1. $(N(t), t \geq 0)$ tiene **incrementos independientes** si haY independencia entre el número de sucesos ocurridos en intervalos de tiempo disjuntos. Esto es: dados cualesquiera $n$ instantes de tiempo $0 \leq t_1 < t_2 <...<t_n$, las variables $N(t_2)-N(t_1),...,N(t_n)-N(t_1)$ son independientes.

# 
