import pygame
import sys

# Inicializar Pygame
pygame.init()

# Configurar la pantalla
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Entrada de Texto con Pygame")

# Configurar fuente
font = pygame.font.Font(None, 36)

# Variable para almacenar el texto ingresado
input_text = ""

# Iniciar la entrada de texto
pygame.key.start_text_input()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        # Capturar eventos de teclado
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                print("Texto ingresado:", input_text)
                input_text = ""
            elif event.key == pygame.K_BACKSPACE:
                input_text = input_text[:-1]
            else:
                input_text += event.unicode

    # Dibujar la pantalla
    screen.fill((255, 255, 255))
    text_surface = font.render(input_text, True, (0, 0, 0))
    screen.blit(text_surface, (50, 200))

    pygame.display.flip()

# Detener la entrada de texto
pygame.key.stop_text_input()

# Salir de Pygame
pygame.quit()
sys.exit()
