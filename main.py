import pygame
 
 
# Definimos algunos colores
NEGRO = (0, 0 ,0)
BLANCO = (255, 255, 255)
VERDE = (0, 255, 0)
ROJO = (255, 0, 0)
AZUL = (0, 0, 255)
VIOLETA = (98, 0, 255)
  
pygame.init()
   
# Establecemos las dimensiones de la pantalla [largo,altura]
dimensiones = [700,500]
pantalla = pygame.display.set_mode(dimensiones) 
pygame.display.set_caption("Mi Primer juego en Informática")
  
#El bucle se ejecuta hasta que el usuario hace click sobre el botón de cierre.
 
hecho = False

#para darle movimiento al rectagulo comenzamos dandole una variable
rect_x = 50
rect_y = 50

#hacemos una variable para modificar en cuantos pixeles se mueve
rect_cambio_x = 5
rect_cambio_y = 5
  
# Se usa para establecer cuan rápido se actualiza la pantalla
 
reloj = pygame.time.Clock()
  
# -------- Bucle principal del Programa -----------
while not hecho:
    # --- Bucle principal de eventos
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT: 
            hecho = True

     
    # Primero, limpia la pantalla con blanco. No vayas a poner otros comandos de dibujo encima 
    # de esto, de otra forma serán borrados por este comando:
    pantalla.fill(NEGRO)  

    #dibujamos un cuadrado blanco en la ubicacion [50, 50], [x,y]y tendra 50 pixelesde largo
    # y 50 pixeles de alto estos dos son los ultimos dos numeros
    pygame.draw.rect(pantalla, BLANCO, [rect_x, rect_y, 50, 50])
    #dibujamos un cuadrado rojo dentro del blanco pero mas chico y para que quede en el centro le damos el mismo valor que el blanco
    pygame.draw.rect(pantalla, ROJO, [rect_x + 10, rect_y + 10 , 30, 30])
    rect_x += rect_cambio_x
    rect_y += rect_cambio_y
    # para que el cuadrado rebote tenemos que hacer que rect_cambio_x cambio de 5 a -5
    # eso lo hacemos con if si rect_x es mayor a 450 oes menos a 0 que rect_cambio_x multiplique su valor por -1
    # asi se vuelve negativo
    if rect_y > 450 or rect_y < 0:
        rect_cambio_y = rect_cambio_y * -1
    if rect_x > 650 or rect_x < 0:
        rect_cambio_x = rect_cambio_x *-1
     
    # --- Avanzamos y actualizamos la pantalla con lo que hemos dibujado.
    pygame.display.flip()
 
    # --- Limitamos a 60 fotogramas por segundo (frames per second)
    reloj.tick(60)
     
# Cerramos la ventana y salimos.
# Si te olvidas de esta última línea, el programa se 'colgará'
# al salir si lo hemos estado ejecutando desde el IDLE.
pygame.quit()