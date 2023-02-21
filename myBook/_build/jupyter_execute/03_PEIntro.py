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
# Esto *CREO* que es lo mismo que el dominio. Esta profe le llama distinto pero conceptualmente es lo mismo. En el lanzamiento de un dado, las variables aleatorias toman valores en $\mathbb{R}$, pero el espacio de estados es $\{1,2,3,4,5,6\}$.
# 
# Según los valores que pueda tomar el espacoio de estados, este será discreto o continuo:
# 
# * Procesos con espacio de estados $E$ **discreto**:
#     * Número de clientes esperando en una cola: $E= 1,2,...$
#     * Registros diarios de lluvias: $E = \{0(no \hspace{0.5em} lluvia), 1 (lluvia)\}$
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

# ````{admonition}
# 
# ```{figure} ./images/plot1.jpg
# ---
# scale: 90%
# align: left
# ---
# ```{sidebar}
# Para el ejemplo de la imagen, el inicio $0$ correspondería con el instante en el que abrimos la compañía. La trayectoria desde $0$ hasta $T_1$ sería de 0 reclamaciones.
# Después de que pase un tiempo aleatorio $t_1$ llega la primera reclamación, y el contador sube a 1. Se mantiene en 1 hasta que pasa otro tiempo aleatorio $t_2$ en el que llega la segunda reclamación. 
# 
# Es decir, la trayectoria asociada a este proceso que describe el número de reclamaciones hasta el instante $t$ es **una función** que va pegando saltos en instantes aleatorios dependiendo de cuando sucedan las reclamaciones.
# ```
# 
# ````

# ```{sidebar}
# Para el ejemplo de la imagen, el inicio $0$ correspondería con el instante en el que abrimos la compañía. La trayectoria desde $0$ hasta $T_1$ sería de 0 reclamaciones.
# Después de que pase un tiempo aleatorio $t_1$ llega la primera reclamación, y el contador sube a 1. Se mantiene en 1 hasta que pasa otro tiempo aleatorio $t_2$ en el que llega la segunda reclamación. 
# 
# Es decir, la trayectoria asociada a este proceso que describe el número de reclamaciones hasta el instante $t$ es **una función** que va pegando saltos en instantes aleatorios dependiendo de cuando sucedan las reclamaciones.
# ```

# ```{figure} ./images/plot1.jpg
# ---
# scale: 90%
# align: left
# ---
# ola?
# ```

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
# Si describo la distribución de probabilidades finito-dimensionales para cualesquiera intantes de tiempo y cualesquiera variables, hayaré las distribuciones del proceso.
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
# ¿Cómo lo definimos? Las variables del proceso, que serán el número de reclamaciones recibidas hasta el instante $t$, verificará:
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

# ### El proceso de Poisson
# 
# Un proceso de Poisson es un proceso  **de recuento** en tiempo continuo tal que $(N(t), t \geq 0)$
# 
# $N(t)$ puede representar:
# * número de coches que pasan por un determinado punto de una carretera
# * número de clientes que llegan a una tienda 
# * número de reclamaciones de una compañia de seguros
# 
# Es decir, un proceso de recuento es una sucesion de variables aleatorias $N(t)$ cuyo espacio de estados es $\{0,1,2,3,...\}$ porque van contando las cosas que pasan hasta un instante de tiempo.
# 
# Si lo que quiero es definir las cosas que pasan hasta un instante de tiempo, ¿Qué propiedades le voy a requerir a ese algo?
# * $N(0) \geq 0$
# * $N(t)$ toman valores en $\mathbb{N}$, en los naturales.
# * El proceso de recuento me cuenta lo que ha sucedido hasta el instante $t$. Luego, si un instante $s$ tal que $s < t$, entonces $N(s) < N(t)$. (Vamos que si estoy sentado en un banco contando los coches que pasan, no pueden haber pasado 50 hasta el primer minuto, y 25 hasta el minuto 2. El conteo siempre es ascendente)
# * Para $s<t$, $N(t)-N(s)$ cuenta el número de sucesos que han ocurrido en el intervalo $(s, t]$
# 
# Dado un proceso de recuento $(N(t), t \geq 0)$ vamos a hablar de dos propiedades que debe tener un proceso de Poisson, aunque estas propiedades también pueden describir un proceso estocástico general.
# 

# ````{admonition} Propiedades de un proceso de Poisson
# 1. $(N(t), t \geq 0)$ tiene **incrementos independientes** si hay independencia entre el número de sucesos ocurridos en intervalos de tiempo disjuntos. Esto es: dados cualesquiera $n$ instantes de tiempo $0 \leq t_1 < t_2 <...<t_n$, las variables $N(t_2)-N(t_1),...,N(t_n)-N(t_1)$ son independientes.
# 
# 2. Un proceso estocástico, o un proceso de recuento particular $(N(t), t \leq 0)$ tiene **incrementos estacionarios** si la distribución del número de sucesos ocurridos en un intervalor de tiempo depende de la longitud de ese intervalo, pero **no** del instante de observación.
# 
# Es decir, si tomo in instante de tiempo $s \leq 0$, que es el origen de la observación, y un intervalo de tiempo $t > 0$, la distribución de la variable $N(t+s)-N(s)$ (el número de sucesos que han ocurrido entre $s$ y $t$) va a coincidir con la distribución de de los incrementos si tomase $s = 0$, $N(t)-N(0)$
# 
# Decimos que los incrementos son estacionarios porque independientemente del instante en el que yo empiezo a observar, voy a observar los incrementos con la misma distribución.
# 
# 
# ```{warning}
# :class: dropdown
# 
# En algunos libros se utiliza una definición más general de incrementos estacionarios:
# 
# Se dice que un proceso tiene incrementos estacionarios si la distribución del número de sucesos ocurridos en intervalos de tiempo disjuntos depende, en todo caso, de la longitud de estos, pero no del instante inicial de observación. 
# 
# Osea que si tomo un instante de tiempo arbitrario $ s \leq 0$, que será el instante en el que empiezo a observar los incrementos del proceso, y tengo tiempos $0 \leq t_1< t_2<...<tn$, los cuales me darán las longitudes de los intervalos de tiempo que quiero observar, y considero la distribución de la variable $n$-dimensional de incrementos $N(t_2 + s)-N(t_1 + s),...,N(t_n +s)-N(t_{n-1}+s)$ (es decir, estoy observando los incrementos del procesopero comenzando en un instante arbitrario $s$), esta distribución coincidirá con la distribución de los incrementos **si tomase $s = 0$**
# 
# $$ N(t_2 + s)-N(t_1 + s),...,N(t_n +s)-N(t_{n-1}+s) = N(t_2)-N(t_1),...,N(t_n)-N(t_{n-1}) $$
# 
# Es decir, si $s = 0$, lo que yo observo desde aquí será lo mismo, en cuanto a cálculo de probabilidades que si yo me pusiese a observar el proceso a partir de un instante arbitrario $s$.
# 
# ```
# Bajo la condición de incrementos independientes, ambas definiciones de incrementos estacionarios (la de fuera del warning y la de dentro) son equivalentes.
# ````

# ## Proceso de Poisson
# ```{admonition} Repaso distribución de Poisson
# :class: dropdown
# Si tomamos $X$ una v.a., decimos que $X$ es un variable de Poisson de parámetro $\lambda$ si verifica:
# 
# $$P(X=k) = \frac{e^{-k}\lambda^{k}}{k!}, k= 0,1,...$$
# 
# Es una v.a. adecuada para contar el número de sucesos (llamadas telefónicas por ejemplo) en un intervalo de tiempo.
# 
# Algunas propiedades:
# 
# * Valor esperado: $E[X] = \sum^{\infty}_{k = 0}kP(X=k)=\lambda$
# * Varianza: $Var[X] = \lambda$
# 
# Si quiesiéramos calcular momentos que no fuesen ni la esperanza ni la varianza, podríamos recurrir a la función generatriz de momentos para la variable de Poisson.
# 
# $$\psi(t) = Ee^{tX} = \sum^{\infty}_{k = 0}e^{tk}P(X=k) = e^{\lambda(e^t - 1)}, t \in \mathbb{R}$$
# 
# Los momentos de una v.a. pueden calcularse a partir de la función generatriz de momentos (si esta existe en un entorno de origen) ya que se tiene que el valor esperado de $X^k$ se puede obtener derivando la función generatriz de momentos $k$ veces y aplicando la derivada en $t=0$.
# 
# $$EX^k = \left. \frac{d^k}{dt^k}\psi(t) \right|_{t=0}, k= 1,2,...$$
# 
# Si tenemos una función generatriz de momentos sencilla, podemos calcular los momentos de una v.a sin necesidad de hacer excesivos cálculos.
# 
# ```

# Mucho ojo a todo esto porque se viene roca.
# 
# Vamos a partir de las definiciones del libro de Ross, Capitulo 2. Aquí se presentan dos definiciones. Vamos con la primera:
# 
# El proceso de Poisson es un proceso de recuento $(N(t), t \leq 0)$. Diremos que es un proceso de Poisson de tasa $\lambda$ si:
# 
# 1. Comienza en el origen $(N(0) = 0)$
# 2. Tiene incrementos independientes
# 3. Si tomo instantes de tiempo arbitrarios $s$ tal que $t \leq 0$, entonces la distribución de los incrementos $N(t+s)-N(s)$ va a tener distribución de Poisson de parámetro $\lambda t$. (multiplico el parámetro $\lambda$ por la longitud del intervalo de tiempo de los incrementos). Esto es
# 
# $$P(N(t+s)-N(s) = n) = \frac{e^{-\lambda t}(\lambda t)^n}{n!}, n = 0,1,...$$
# 
# La probabilidad de que un incremento de magnitud $t$ valga $n$ viene dada por la distribución de Poisson de parámetro $\lambda$
# 
# ```{admonition} Observaciónes
# :class: dropdown
# La propiedad 3 verifica que el proceso de Poisson tiene la propiedad de incrementos estacionarios ya que los incrementos del proceso solo dependen de la magnitud del intervalo y no del instante inicial de observación.
# 
# También por la propiedad 3 conozco el valor esperado del número de sucesos hasta el instante $t$:
# 
# $$EN(t) = \lambda t $$
# 
# De ahí que se llame *tasa* a $\lambda$ (número medio de sucesos por unidad de tiempo).
# 
# Si $\lambda = 1$, llamamos a $(N(t), t \leq 0)$ proceso de Poisson estándar.
# ```
# Para determinar si un proceso de recuento arbitrario es en realidad un proceso de Poisson, debemos demostrar que se satisfacenm als condiciones 1, 2 y 3. La condición 1, que simplemente establece que el recuento de eventos comienza en el momento $t=0$, y la condición 2 generalmente se pueden verificar a partir de nuestro conocimiento del proceso. Pero no está del todo claro cómo determinamos el cumplimiento de la condición 3 y por esa razón es útil una definición equivalente de un proceso de Poisson.
# 
# Ahí va la senda definición que presenta el Ross ~~este de los huevos~~
# 

# ### Definición a través de sus incrementos infinitesimales
# El proceso de Poisson también se puede definir de la siguiente manera. Tenemos un proceso de recuento $(N(t), t \leq 0)$. Podría decir que este proceso es un proceso de Poisson de tasa $\lambda$ si verifica:
# 
# 
# ```{margin}
# Dada una función $f$, diré que $f$ es una $o(h)$ si  $\lim_{h\to 0}\frac{f(h)}{h}=0$
# A $o(h)$ le llama una o pequeña de h. Muy bien. Todo ok.
# $N(h)$: incremento infinitesimal
# ```
# 1. $N(0) = 0$
# 2. El proceso tiene incrementos estacionarios e independientes
# 3. $P(N(h) = 1) = \lambda h + o(h)$
# 4. $P(N(h) \leq 2) = o(h)$
# 
# La propiedad 3 nos cuantifica la probabilidad de la ocurrencia de *un* suceso en un incremento infinitesimal, mientras que la propiedad 4 nos cuantifica la probabilidad de que ocurran *dos* sucesos en un incremento infinitesimal. Entonces, en un incremento infinitesimal, o puede pasar una cosa o pueden pasar cero cosas. La probabilidad de que sucedan más cosas es irrelevante.
# 
# Osea, si soy capaz de entender esto, la prob 4 quiere decir que en un incremento infinitesimal $N(h)$, la prob de que ocurran 2 o más sucesos es irrelevante? ¿$o(h)$ es la notación para describir irrelevante? ¿NO VALE EL 0 O QUÉ? Enfin. Me están poniendo negro ya. ~~Puta peña.~~
# 
# Dicho de otro modo: las propiedades 3 y 4 nos indican que los incrementos infinitesimales del proceso son de magnitud 0 o 1.

# Vale pues ahora Ross nos dice que ambas definiciones son EQUIVALENTES. Y que una implica la otra y viceversa.
# 
# Para eso define:
# 
# $$P_n(t) = P(N(t) = n)$$
# 
# Sin más que esto no es nada en principio, solo otra manera de llamar a la probabilidad de que en el instante $t$, $N(t) = n$
# 
# Entonces, empezamos con el caso de n = 0, y te plasma lo siguiente en el libro sin explicación alguna:
# 
# $$P_0(t+h) = P(N(t+h) = 0)$$
# 
# ¿Qué tiene que pasar para que o cosas en este intervalo?
# 
# ![Drag Racing](incrementos.png)
# 
# Pues que tienen que pasar 0 cosas desde 0 a $t$ ($N(t)=0$), y otras 0 cosas desde $t$ ahsta $t+h$ ($N(t+h)-N(t) = 0$). Vale pues entonces :
# 
# $$P_0(t+h) = P(N(t+h) = 0) = P(N(t)=0,N(t+h)-N(t) = 0)$$
# 
# Ahora, por la propiedad de incrementos independientes digo:
# 
# $$P(N(t)=0,N(t+h)-N(t) = 0) = P(N(t)=0)P(N(t+h)-N(t) = 0)$$
# 

# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# 

# 

# 
