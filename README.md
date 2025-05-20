# 🌤️ Animación de Clima en Pantalla OLED con Raspberry Pi Pico W

Este proyecto muestra una animación cíclica de diferentes estados del clima en una pantalla OLED conectada a un Raspberry Pi Pico W usando MicroPython.

> ✨ **Realizado por:** Jennifer Nicole Macedo Cruz  
> 🏫 TECNM Campus Tijuana - Lenguajes de Interfaz  
> 📅 Fecha: 14 de mayo de 2025

---

## 🧾 Descripción

El objetivo del proyecto es desplegar distintas animaciones relacionadas con el clima (soleado, nublado, lluvia, etc.) en una pantalla OLED 128x64 mediante conexión I2C, usando MicroPython y la Raspberry Pi Pico W. 

La simulación fue realizada utilizando la plataforma Wokwi.

---

## 🛠️ Hardware utilizado

- Raspberry Pi Pico W
- Pantalla OLED SSD1306 (I2C)
- Conexiones I2C:
  - `SCL`: GP27
  - `SDA`: GP26
  - `VCC`: 3V3_EN
  - `GND`: GND

---

## 🔗 Diagrama de conexión

El siguiente diagrama fue generado en [Wokwi](https://wokwi.com):

> Puedes abrir y simular este proyecto desde aquí:  
> [🌐 Simulación en Wokwi](https://wokwi.com/projects/430988774320576513)

📄 Archivo: `diagram.json`

---

## 🧠 Funcionamiento

El script en `main.py`:
1. Inicializa la pantalla OLED mediante el bus I2C.
2. Recorre una lista de representaciones ASCII de climas.
3. Muestra cada animación por 2 segundos antes de pasar a la siguiente en bucle.

---

## ▶️ Ejecución

### Requisitos

- MicroPython cargado en la Raspberry Pi Pico W.
- Librería `ssd1306.py` (debe estar en la misma carpeta del script).

### Pasos

1. Copia el archivo `main.py` a tu Raspberry Pi Pico W.
2. Asegúrate de tener la librería `ssd1306.py` disponible.
3. Corre el script desde Thonny o cualquier entorno compatible con MicroPython.

---

## 🧾 Archivos

| Nombre               | Descripción                                            |
|----------------------|--------------------------------------------------------|
| `main.py`            | Código principal que muestra las animaciones           |
| `diagram.json`       | Diagrama de conexión en formato Wokwi                  |
| `wokwi-project.txt`  | Enlace al proyecto simulado en Wokwi                   |

---

## 📸 Vista previa
![image](https://github.com/user-attachments/assets/f8297047-c798-4a03-b250-1b020a1df877)

