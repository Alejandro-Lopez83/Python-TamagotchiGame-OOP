
# Python-TamagotchiGame-OOP 🐱 🐶 🐭

[![English](https://img.shields.io/badge/lang-English-blue.svg)](#english) [![Español](https://img.shields.io/badge/lang-Espa%C3%B1ol-red.svg)](#español)

## English

### Description
A Python console-based Tamagotchi game implementing Object-Oriented Programming principles. Create and take care of virtual pets (dogs, cats, mice) with unique characteristics and interactions. The project serves as a practical example of OOP concepts including inheritance, polymorphism, and encapsulation.

### Features
- Create multiple pets of different species (Dog, Cat, Mouse)
- Interact with your pets through various actions:
  - Feed them to increase their hunger level
  - Make them speak (bark, meow, or squeak) to increase happiness
  - Let them rest to recover energy
- Monitor your pets' status:
  - Happiness level
  - Hunger level
  - Energy level
- All stats are capped at 150 points and can't go below 0

### How to Play
1. Run the game
2. Choose from the following options:
   - Create a new Tamagotchi
   - Play with your Tamagotchi
   - Check your Tamagotchi's stats
   - Exit the game
3. Create your first pet by choosing a species and giving it a name
4. Interact with your pet through various actions
5. Keep an eye on their stats to ensure they stay happy and healthy!

### Technical Details
The game demonstrates key OOP principles in Python:
- **Inheritance**: Species-specific classes inherit from base `Tamagotchi` class
- **Encapsulation**: Properties and behaviors are encapsulated within appropriate classes
- **Polymorphism**: Each species implements its own versions of speak() and rest()
- **Class Structure**:
  - Base `Tamagotchi` class with common attributes and methods
  - Specialized subclasses for each species (Dog, Cat, Mouse)
  - Game management through `Tamagotchi_Fantasy` class

### Installation
1. Clone this repository
2. Make sure you have Python installed
3. Run the script:
```bash
python tamagotchi_fantasy.py
```

---

## Español

### Descripción
Un juego de Tamagotchi basado en consola implementado en Python utilizando principios de Programación Orientada a Objetos. Crea y cuida mascotas virtuales (perros, gatos, ratones) con características e interacciones únicas. El proyecto sirve como ejemplo práctico de conceptos de POO incluyendo herencia, polimorfismo y encapsulamiento.

### Características
- Crea múltiples mascotas de diferentes especies (Perro, Gato, Ratón)
- Interactúa con tus mascotas mediante varias acciones:
  - Alimentarlas para aumentar su nivel de hambre
  - Hacerlas hablar (ladrar, maullar o chillar) para aumentar su felicidad
  - Dejarlas descansar para recuperar energía
- Monitorea el estado de tus mascotas:
  - Nivel de felicidad
  - Nivel de hambre
  - Nivel de energía
- Todas las estadísticas están limitadas a 150 puntos y no pueden bajar de 0

### Cómo Jugar
1. Ejecuta el juego
2. Elige entre las siguientes opciones:
   - Crear un nuevo Tamagotchi
   - Jugar con tu Tamagotchi
   - Revisar las estadísticas de tu Tamagotchi
   - Salir del juego
3. Crea tu primera mascota eligiendo una especie y dándole un nombre
4. Interactúa con tu mascota mediante diferentes acciones
5. ¡Mantén un ojo en sus estadísticas para asegurarte de que se mantengan felices y saludables!

### Detalles Técnicos
El juego demuestra principios clave de POO en Python:
- **Herencia**: Las clases específicas de especies heredan de la clase base `Tamagotchi`
- **Encapsulamiento**: Propiedades y comportamientos encapsulados en clases apropiadas
- **Polimorfismo**: Cada especie implementa sus propias versiones de speak() y rest()
- **Estructura de Clases**:
  - Clase base `Tamagotchi` con atributos y métodos comunes
  - Subclases especializadas para cada especie (Perro, Gato, Ratón)
  - Gestión del juego a través de la clase `Tamagotchi_Fantasy`

### Instalación
1. Clona este repositorio
2. Asegúrate de tener Python instalado
3. Ejecuta el script:
```bash
python tamagotchi_fantasy.py
```
