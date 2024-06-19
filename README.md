# Sistema-de-recomendación-de-viajes

## **Introduccion**
El turismo ha experimentado una transformación significativa con la integración de la tecnología, lo que ha permitido a los viajeros acceder a información y recomendaciones personalizadas de manera eficiente. En este contexto, los sistemas expertos se han convertido en herramientas cruciales para facilitar la planificación de viajes, ofreciendo sugerencias basadas en las preferencias y necesidades individuales de los usuarios.

## **Objetivo**

El objetivo del sistema de recomendación de viajes es proporcionar recomendaciones personalizadas de destinos de viaje a los usuarios basándose en sus preferencias y necesidades específicas. Al hacer preguntas sobre características clave como el clima, seguridad, transporte, preferencias alimentarias, tipo de atracciones, y otros factores importantes para la experiencia de viaje, el sistema será capaz de sugerir los destinos más adecuados que se alineen con los intereses y condiciones del viajero.

## **Requisitos no funcionales**

| Requisito no funcional | Descripción |
|------------------------|-------------|
| Usabilidad             | La interfaz del sistema debe ser intuitiva y fácil de usar, permitiendo a los usuarios navegar y completar el cuestionario sin dificultades. |
| Rendimiento            | El sistema debe ser capaz de procesar las respuestas del cuestionario y generar recomendaciones rápidamente, asegurando tiempos de respuesta cortos. |
| Escalabilidad          | El sistema debe ser capaz de manejar un aumento en la cantidad de destinos sin degradar el rendimiento, permitiendo su crecimiento sin problemas. |
| Mantenibilidad         | El código del sistema debe estar bien documentado y estructurado, facilitando su mantenimiento y actualización por parte de los desarrolladores. |


## **Requisitos funcionales**

| Requisito funcional           | Descripción                                                                                                                                               |
|-------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------|
| Cuestionario de Preferencias  | El sistema debe presentar un cuestionario estructurado a los usuarios para recolectar información sobre sus preferencias en diversas categorías como clima, seguridad, transporte, comida, atracciones, etc. |
| Base de Datos de Destinos     | Debe existir una base de datos completa y actualizada de destinos de viaje con detalles específicos relacionados con las preguntas del cuestionario.        |
| Motor de Recomendación        | El sistema debe incluir un motor que utilice las respuestas del cuestionario para calcular las puntuaciones de los destinos y recomendar los más adecuados para el usuario. |
| Información Detallada del Destino | Para cada destino recomendado, el sistema debe proporcionar información adicional sobre actividades disponibles, atracciones principales, opciones de transporte y consejos de viaje. |

### **Estructura de Proyecto**

