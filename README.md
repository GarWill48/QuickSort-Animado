## 📊 Quicksort Visualizer:

> Visualización animada paso a paso del algoritmo **Quicksort** usando Python con la libreria Matplotlib.

## Analista de Datos:
Durante la ejecucion observamos indicadores criticos como el pivote naranja que actua como nuestra ancla de decision estrategica, las comparaciones en azul y los intercambios amarillos que simbolizanel trafico de datos, todo mientraslas lineas de particion delimitan la carga de trabajo bajo la metodologiade divide y venceras.


## Resumen ejecutivo:
Tipo de QuickSort: Lomuto

Complejidad:
>Promedio: O(n log n)
>Peor caso: O(n²)
>Espacio: O(log n) por recursión


## Propósito del Proyecto

El objetivo de este software es proporcionar una herramienta pedagógica interactiva que ilustre el funcionamiento del algoritmo de ordenamiento Quicksort. Mediante una representación gráfica en tiempo real, el programa permite observar la mecánica de "divide y vencerás", facilitando la comprensión de conceptos abstractos como la recursión, la partición de arreglos y la selección de pivotes.
Arquitectura del Código
El sistema se divide en tres capas lógicas bien definidas:

1.- Capa de Simulación (quicksort_steps): Implementa el algoritmo de Quicksort (esquema de partición de Lomuto). A diferencia de una implementación estándar, esta función actúa como un generador de estados, capturando cada comparación e intercambio en una lista de diccionarios que sirven como "frames" para la animación.

2.- Capa de Renderizado (Matplotlib): Utiliza un gráfico de barras donde la altura de cada barra representa el valor del dato. Configura un entorno visual de alto contraste ("Dark Mode") para resaltar los elementos clave mediante un código de colores específico.

3.- Capa de Animación (FuncAnimation): Gestiona el flujo temporal de la visualización, actualizando las propiedades de las barras (altura y color) y los metadatos (mensajes informativos y barra de progreso) de forma sincronizada.

Lógica de Colores y Semántica Visual
Para mejorar la interpretabilidad, el visualizador emplea la siguiente convención:

>Naranja (P): Indica el elemento seleccionado como pivote.

>Azul: Resalta los elementos que están siendo comparados actualmente.

>Amarillo: Identifica los elementos que están siendo intercambiados de posición.

>Verde: Representa los elementos que ya han alcanzado su posición final garantizada.

>Líneas Punteadas: Delimitan el rango del subarreglo activo procesado por la recursión actual.
