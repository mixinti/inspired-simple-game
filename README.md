# Sistema de Combate por Turnos en Consola

Aplicación de simulación de combate por turnos desarrollada en Python utilizando programación orientada a objetos y librerías nativas.

## Características Técnicas

* **Arquitectura Modular por Capas:** Separación limpia entre la lógica de negocio (dominio), el controlador de flujos (motor) y la interfaz de usuario.
* **Diseño Orientado a Objetos Avanzado:** Uso estricto de clases abstractas y métodos obligatorios para garantizar la consistencia de las entidades.
* **Encapsulamiento Completo:** Control estricto del estado de los personajes (puntos de vida, maná y ataque) mediante propiedades de acceso controlado.
* **Polimorfismo Estructural:** Motor de juego genérico capaz de ejecutar acciones y resoluciones de combate dinámicamente según la entidad activa.

## Arquitectura del Proyecto

* `main.py`: Punto de entrada único que inicializa y ejecuta la aplicación.
* `domain/`: Contiene las clases base, entidades de héroes, enemigos, habilidades físicas y el catálogo de hechizos mágicos.
* `engine/`: Administra el flujo del bucle principal del juego, la validación de condiciones de victoria o derrota y el orden secuencial de los turnos.
* `ui/`: Gestiona de forma exclusiva las entradas y salidas de texto a través de la terminal de comandos.
