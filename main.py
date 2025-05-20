# ---------------------------------------------------------------------------------
#  Lenguajes de Interfaz en TECNM Campus ITT
#  Autor: Jennifer Nicole Macedo Cruz  
#  Fecha: 2025-05-14  
#  Descripción: Práctica - Animaciones en pantalla OLED con Raspberry Pi Pico W.
#               El programa se conecta a una pantalla OLED vía I2C y muestra una
#               animación cíclica de diferentes estados del clima.
# ---------------------------------------------------------------------------------

from machine import Pin, I2C
from ssd1306 import SSD1306_I2C
import framebuf, sys
import utime

pix_res_x = 128
pix_res_y = 64

def init_i2c(scl_pin, sda_pin):
    i2c_dev = I2C(1, scl=Pin(scl_pin), sda=Pin(sda_pin), freq=200000)
    i2c_addr = [hex(ii) for ii in i2c_dev.scan()]
    
    if not i2c_addr:
        print('No I2C Display Found')
        sys.exit()
    else:
        print("I2C Address      : {}".format(i2c_addr[0]))
        print("I2C Configuration: {}".format(i2c_dev))
    
    return i2c_dev

def mostrar_clima(oled, etiqueta, dibujo):
    oled.fill(0)
    oled.text(etiqueta, 0, 0)
    for i, linea in enumerate(dibujo):
        oled.text(linea, 0, 15 + i * 10)
    oled.show()
    utime.sleep(2)

def animacion_clima(oled):
    climas = [
        ("Soleado", [
            "   \\   |   /",
            "    .---.  ",
            " - (     ) -",
            "    `---'  ",
            "   /  |  \\ "
        ]),
        ("Parcial", [
            "     .--.   ",
            "  .-(    ). ",
            " (___.__)__) ",
            "     \\ | /  ",
            "      ---   "
        ]),
        ("Nublado", [
            "   .--. .--.",
            "  (    Y    )",
            " (___.-.___)",
            "            ",
            "            "
        ]),
        ("Lluvia", [
            "    .--.    ",
            " .-(    ).  ",
            "(___.__)__) ",
            "  '  '  '   ",
            " '  '  '    "
        ]),
        ("Tormenta", [
            "   .--.     ",
            " (    ).    ",
            "(___.__)__ )",
            "   ⚡⚡⚡     ",
            "  ' ' '     "
        ])
    ]

    while True:
        for clima in climas:
            mostrar_clima(oled, clima[0], clima[1])

def main():
    i2c_dev = init_i2c(scl_pin=27, sda_pin=26)
    oled = SSD1306_I2C(pix_res_x, pix_res_y, i2c_dev)
    animacion_clima(oled)

if __name__ == '__main__':
    main()
