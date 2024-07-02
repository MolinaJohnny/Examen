import pygame
from biblioteca import *
from pygame.locals import *
import json
from datos import lista
'''     
Segundo examen parcial de PROGRAMACION
Nombre: Jhonny Molina Rea
Dni: 44260390
Division: 212

'''


pygame.init()     #Inicio del programa

#    Variables y contadores
font = pygame.font.SysFont("Arial Narrow", 30)
screen = pygame.display.set_mode([720, 520])
posicion_text_a = (90, 365)
posicion_text_b = (300,365)
posicion_text_c = (520,365)
puntaje = 0
pregunta = -1
errores = 0

#   Banderas
running = True
menu = True
esta_jugando = False
cargar_submenu = False
carga_juego = False
carga_menu = False
pantalla_scores = False
error = False
correcta = None
escribiendo = False
mostrar_scores = False
sonido_fondo_play = False
#    Sonidos
pygame.mixer.init()
sonido_fondo = pygame.mixer.Sound("clase/mijuego/sonidos/endingelevator-152337.mp3")
sonido_fondo.set_volume(0.2)
sonido_correcto = pygame.mixer.Sound("clase/mijuego/sonidos/correcto_sonido.mp3")
sonido_correcto.set_volume(0.4)
#   SCORES
scores = {}
lista_scores =[]


while running:
    text_puntaje = font.render(f"PUNTAJE: {puntaje}", True, (0,0,0))

    for event in pygame.event.get():    #Las interacciones que puede realizar el usuario
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if menu == True and carga_menu == True: # Se verifica que hayan sido creados los rect para interactuar
                if rect_jugar.collidepoint(event.pos):
                    menu = False
                    mostrar_scores= False
                    puntaje = 0
                    nombre = ""
                if rect_scores.collidepoint(event.pos):
                    mostrar_scores = True
                    
                if rect_salir.collidepoint(event.pos):
                    running = False
            if mostrar_scores ==True and pantalla_scores == True: # se verifica que se hayan creado los rect
                if boton_menu.collidepoint(event.pos):
                    menu = True
                    puntaje = 0
                    pregunta = -1
                    mostrar_scores = False
            if cargar_submenu == True:  # se verifica que se haya cargado los rect
                if boton_pregunta.collidepoint(event.pos):                
                    esta_jugando = True
                    errores = 0
                    pregunta += 1
                    error = False
                    correcta = None
                if boton_menu.collidepoint(event.pos):
                    menu = True
                    puntaje = 0
                    pregunta = -1
                if boton_reiniciar.collidepoint(event.pos):
                    pregunta = -1
                    esta_jugando = False
                    puntaje = 0
            if esta_jugando == True and carga_juego == True: # Se verifica que se haya cargado los rect
                match respuesta:
                    case "a": # Caso en el que la respuesta correcta sea A
                        if boton_a.collidepoint(event.pos):
                            puntaje += 10
                            esta_jugando = False
                            correcta = boton_a
                            datos_correcta = presiono_correcta(r_a, posicion_text_a)
                        if boton_b != None and boton_b.collidepoint(event.pos):
                            errores +=1
                            error = presiono_error( "b")
                            boton_b = None

                        if boton_c != None and boton_c.collidepoint(event.pos):
                            errores +=1  
                            error = presiono_error( "c")
                            boton_c = None    
                    case "b": # Caso en el que la respuesta correcta sea B
                        if boton_b.collidepoint(event.pos):
                            puntaje += 10
                            esta_jugando = False
                            correcta = boton_b
                            datos_correcta = presiono_correcta(r_b, posicion_text_b)
                        if boton_a != None and boton_a.collidepoint(event.pos):
                            errores +=1    
                            error = presiono_error("a")
                            boton_a = None
                        if boton_c != None and boton_c.collidepoint(event.pos):
                            errores +=1 
                            boton_c = None
                            error = presiono_error( "c")
                    case "c": # Caso en el que la respuesta correcta sea C
                        if boton_c.collidepoint(event.pos):
                            puntaje += 10
                            esta_jugando = False
                            correcta = boton_c
                            datos_correcta = presiono_correcta(r_c, posicion_text_c)
                        if boton_b != None and boton_b.collidepoint(event.pos):
                            errores +=1    
                            error = presiono_error( "b")
                            boton_b = None
                        
                        if boton_a != None and boton_a.collidepoint(event.pos):
                            errores +=1    
                            error = presiono_error("a")
                            boton_a = None
                            
    cargar_imagen("clase/mijuego/imagenes/fondo_1.jpg", (0,0), (720, 520), screen)
    lista_preguntas = acomodar_datos(lista)
    # Si el usuario cometio 2 errores en la misma pregunta se pasara a la siguiente pregunta reiniciando el contador de errores.
    if errores == 2:
        errores = 0 
        pregunta +=1
        error = False
    # El menu principal que se muestra una vez iniciado el programa y al ingresar el nombre una vez finalizar la secuencia de preguntas
    elif mostrar_scores == True:
        lista_scores = ordenar_lista(lista_scores)
        crear_dibujar_rect((180, 100, 200, 300), screen, (255,0,0))
        boton_menu = crear_dibujar_rect((580, 470, 130, 40), screen, (255,0,0))
        crear_texto("MENU", (0,0,0), (615, 479 ), screen)
        if len(lista_scores) == 1:
            crear_texto(f"{lista_scores[0]["nombre"]} : {lista_scores[0]["puntaje"]}", (0,0,0), (220,160), screen)
        elif len(lista_scores) == 2:
            crear_texto(f"{lista_scores[1]["nombre"]} : {lista_scores[1]["puntaje"]}", (0,0,0), (220,190), screen)
            crear_texto(f"{lista_scores[0]["nombre"]} : {lista_scores[0]["puntaje"]}", (0,0,0), (220,160), screen)
        elif len(lista_scores) ==3 :
            crear_texto(f"{lista_scores[2]["nombre"]} : {lista_scores[2]["puntaje"]}", (0,0,0), (220,220), screen)
            crear_texto(f"{lista_scores[1]["nombre"]} : {lista_scores[1]["puntaje"]}", (0,0,0), (220,190), screen)
            crear_texto(f"{lista_scores[0]["nombre"]} : {lista_scores[0]["puntaje"]}", (0,0,0), (220,160), screen)
        pantalla_scores = True


    elif menu == True:
        
        rect_jugar = crear_dibujar_rect((80, 220, 200, 50), screen, (255,0,0))
        rect_scores= crear_dibujar_rect((450, 220, 200, 50), screen, (255,0,0))
        rect_salir = crear_dibujar_rect((270, 450, 200, 50 ), screen, (255,0,0))
        crear_texto("JUGAR", (0,0,0), (140, 235), screen)
        crear_texto("VER PUNTAJES", (0,0,0), (470, 235), screen)
        crear_texto("SALIR", (0,0,0), (330, 465), screen)
        carga_menu = True
    # Luego de llegar a la pregunta final se le pide al usuario ingresar su nombre.
    elif esta_jugando == True:

        if pregunta == len(lista_preguntas): #se verifica que el valor de la pregunta actual no sea mayor
                                             # que la cantidad de preguntas.
            escribiendo = True
            while escribiendo:
                pressed_keys = pygame.key.get_pressed()
                
                for event in pygame.event.get():
                    crear_dibujar_rect((250, 240, 300, 60), screen, (255,0,0))
                    crear_texto(f"Ingresa tu nombre: {nombre}", (0,0,0), (272, 262), screen)                  
                    if event.type == pygame.TEXTINPUT:
                        nombre += event.text
                        print(nombre)
                    elif event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_BACKSPACE:
                            nombre = nombre[:-1]

                    if True in pressed_keys:
                        if pressed_keys[K_RETURN]:
                            scores = ({"nombre":nombre, "puntaje":puntaje})
                            lista_scores.append(scores)
                            escribiendo = False
                            menu = True
                            esta_jugando = True
                            pregunta = 0

                    pygame.display.flip()
            guardar_json(lista_scores, "scores")
            
        pregunta_actual = lista_preguntas[pregunta]
        respuesta = pregunta_actual[2]

        boton_pregunta = crear_dibujar_rect((250, 40, 220, 60), screen, (255,0,0))
        boton_reiniciar = crear_dibujar_rect((250, 430, 220, 60), screen, (255,0,0))

        # Al mostrar una pregunta se deben mostrar todas las respuestas posibles.
        if error == False:
            boton_a = crear_dibujar_rect((50, 350, 200, 50), screen, (255, 0 ,0))
            boton_b = crear_dibujar_rect((270, 350, 200, 50), screen, (255,0,0))
            boton_c = crear_dibujar_rect((490, 350, 200, 50), screen, (255,0,0))
            r_a = crear_texto(pregunta_actual[1][0], (0,0,0), (posicion_text_a), screen)
            r_b = crear_texto(pregunta_actual[1][1], (0,0,0), (posicion_text_b), screen)
            r_c = crear_texto(pregunta_actual[1][2], (0,0,0), (posicion_text_c), screen)
        
        # Si el usuario ingreso una respuesta incorecta esta no se mostrara y debera elegir otra.
        elif error != False:
            match error:
                case "a":
                    boton_b = crear_dibujar_rect((270, 350, 200, 50), screen, (255,0,0))
                    boton_c = crear_dibujar_rect((490, 350, 200, 50), screen, (255,0,0))
                    crear_texto(pregunta_actual[1][1], (0,0,0), (300,365), screen)
                    crear_texto(pregunta_actual[1][2], (0,0,0), (520,365), screen)
                case "b":
                    boton_c = crear_dibujar_rect((490, 350, 200, 50), screen, (255,0,0))
                    boton_a = crear_dibujar_rect((50, 350, 200, 50), screen, (255, 0 ,0))
                    crear_texto(pregunta_actual[1][0], (0,0,0), (90, 365), screen)
                    crear_texto(pregunta_actual[1][2], (0,0,0), (520,365), screen)
                case "c":
                    boton_a = crear_dibujar_rect((50, 350, 200, 50), screen, (255, 0 ,0))
                    boton_b = crear_dibujar_rect((270, 350, 200, 50), screen, (255,0,0))
                    crear_texto(pregunta_actual[1][0], (0,0,0), (90, 365), screen)
                    crear_texto(pregunta_actual[1][1], (0,0,0), (300,365), screen)
            
        crear_texto("PREGUNTA", (0,0,0), (302, 62), screen)
        crear_texto("REINICIAR", (0,0,0), (305, 453), screen)
        screen.blit(text_puntaje, (550, 50))
        crear_texto(pregunta_actual[0], (220, 17, 17), (100,260), screen)

        carga_juego = True #Se verifica que primero haya cargado la pantalla 
                            #y luego podra realizar eventos en ella

    elif esta_jugando == False :    # El submenu que se acede una vez presionado Jugar y al que se vuelve
                                    # cada vez que el usuario responde una pregunta de manera correcta o incorrecta
        
        boton_pregunta = crear_dibujar_rect((250, 40, 220, 60), screen, (255,0,0))
        boton_reiniciar = crear_dibujar_rect((250, 430, 220, 60), screen, (255,0,0))
        boton_menu = crear_dibujar_rect((580, 470, 130, 40), screen, (255,0,0))
        crear_texto("PREGUNTA", (0,0,0), (302, 62), screen)
        crear_texto("REINICIAR", (0,0,0), (305, 453), screen)
        crear_texto("MENU", (0,0,0), (615, 479 ), screen)
        screen.blit(text_puntaje, (550, 400))

        if correcta != None:   #Si el usuario elige la opcion correcta solo se mostrara esa y volvera al submenu
            pygame.draw.rect(screen, (255,0,0),correcta , border_radius= 15)
            screen.blit(datos_correcta[0], datos_correcta[1])
                
        cargar_submenu = True # Se verifica que primero hayan sido dibujados los rect
                                # para luego poder interactuar con ellos
    if sonido_fondo_play == False :
        sonido_fondo.play(-1)
        sonido_fondo_play = True
    pygame.display.flip()

pygame.quit()   #Fin del programa
