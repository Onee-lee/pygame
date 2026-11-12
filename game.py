import pygame
import pgzrun
import random


pontos = 0
derrotas = 0
start = 0
dificult = 0
rota_patrulha=[(100,100), (600,100)]
WIDTH=800
HEIGHT=600
TITLE="Jogo teste1"

def dificuldade_texto():
    if start==1 and dificult==0:
        screen.draw.text(f"escolha uma dificuldade:", (150,100), fontsize=60, color="Gray")
        screen.draw.text(f"Fácil", center=(WIDTH//2, HEIGHT//3), fontsize=50, color="Gray")
        screen.draw.text(f"Difícil", center=(WIDTH//2,HEIGHT//2), fontsize=50, color="Gray")

def game_over_texto():
    if dificult==1:
        if derrotas >= 10:
            screen.draw.text(f"Game Over", center=(WIDTH//2,HEIGHT//2), fontsize=100, color="Red")
            screen.draw.text(f"pressione espaço para continuar", center=(WIDTH//2,400), fontsize=50, color="White")

    if dificult==2:
        if derrotas >= 5:
            screen.draw.text(f"Game Over", center=(WIDTH//2,HEIGHT//2), fontsize=100, color="Red")
            screen.draw.text(f"pressione espaço para continuar", (130,400), fontsize=50, color="White")

def vitoria_texto():
    if dificult==1:
        if pontos == 5:
            screen.draw.text(f"Parabens, você venceu",center=(WIDTH//2,HEIGHT//2), fontsize=70, color="Blue")
            screen.draw.text(f"pressione espaço para continuar", (130,400), fontsize=50, color="White")

    if dificult==2:
        if pontos == 10:
            screen.draw.text(f"Parabens, você venceu",center=(WIDTH//2,HEIGHT//2), fontsize=70, color="Blue")
            screen.draw.text(f"pressione espaço para continuar", (130,400), fontsize=50, color="White")

def teleporte():
    heroi.x=random.randint(0,800)
    heroi.y=random.randint(0,600)

def reinicio():
    heroi.x = WIDTH // 2
    heroi.y = HEIGHT // 2
    vilao.x = random.randint(0, WIDTH)
    vilao.y = random.randint(0, HEIGHT)
    moeda.x = random.randint(30,700)
    moeda.y = random.randint(50,500)

def kill():
    heroi.x=1000
    heroi.y=1000
    vilao.x=2000
    vilao.y=2000
    moeda.x=3000
    moeda.y=3000
    pontos=0
    derrotas=0

def dash():    
    if keyboard.z and keyboard.up:
        heroi.y = heroi.y - 10
    if keyboard.z and keyboard.down:
        heroi.y = heroi.y + 10 
    if keyboard.z and keyboard.left:
        heroi.x = heroi.x - 10
    if keyboard.z and keyboard.right:
        heroi.x = heroi.x + 10     

def movimento():
    if dificult==1:
        if keyboard.right:
            heroi.x = heroi.x + 1
        if keyboard.left:
            heroi.x = heroi.x - 1
        if keyboard.up:
            heroi.y = heroi.y - 1
        if keyboard.down:
            heroi.y = heroi.y + 1

    if dificult==2:
        if keyboard.right:
            heroi.x = heroi.x + 1.5
        if keyboard.left:
            heroi.x = heroi.x - 1.5
        if keyboard.up:
            heroi.y = heroi.y - 1.5
        if keyboard.down:
            heroi.y = heroi.y + 1.5

def movimento_vilao():
    if dificult == 1:
        if derrotas <= 9 and pontos <= 4:
            if heroi.x > vilao.x:
                vilao.x=vilao.x + 1.5
            if heroi.x < vilao.x:
                vilao.x=vilao.x - 1.5
            if heroi.y < vilao.y:
                vilao.y=vilao.y - 1.5
            if heroi.y > vilao.y:
                vilao.y=vilao.y + 1.5
    if dificult == 2:
        if derrotas <= 4 and pontos <= 9:
            if heroi.x > vilao.x:
                vilao.x=vilao.x + 3
            if heroi.x < vilao.x:
                vilao.x=vilao.x - 3
            if heroi.y < vilao.y:
                vilao.y=vilao.y - 3
            if heroi.y > vilao.y:
                vilao.y=vilao.y + 3

def atulizar_ia_guarda():
    global estado_guarda, indice_rota, estado_jogo

    dx = heroi.x - guarda.x
    dy = heroi.y - guarda.y
    distancia.qd = dx**2 + dy**2

#    if guarda.x < heroi.x: guarda.x +=


heroi=Actor("heroi", (WIDTH // 2, HEIGHT // 2))
moeda=Actor("moeda", (WIDTH // 4, HEIGHT // 4))
vilao=Actor("vilao", (WIDTH // 7 , HEIGHT // 7))
vilao2=Actor("vilao2", (255, 270)) 
botao=Actor("botao", (WIDTH//2, HEIGHT//3))
botao2=Actor("botao", (WIDTH//2, HEIGHT//2))                                                                               


def draw():
    global pontos
    global start
    
    screen.fill((30,30,30))
   
    heroi.draw()
    moeda.draw()
    vilao.draw()
  
    if start==1 and dificult==0:
        botao.draw()
        botao2.draw()
   
    if start==0:
        vilao2.draw()

    if start ==0:
        screen.draw.text(f"The eye", (525,255), fontsize=80, color="Gray")
        screen.draw.text(f"aperte espaço\npara começar", (550,355), fontsize=40, color="Gray")


    if start == 1 and dificult==1:    
        screen.draw.text(f"Pontos: {pontos}/5", (20,20), fontsize=40, color="white")
        screen.draw.text(f"Derrotas : {derrotas}/10", (20,60), fontsize=40, color="white")

    if start == 1 and dificult==2:    
        screen.draw.text(f"Pontos: {pontos}/10", (20,20), fontsize=40, color="white")
        screen.draw.text(f"Derrotas : {derrotas}/5", (20,60), fontsize=40, color="white")
    
    game_over_texto()

    vitoria_texto()

    dificuldade_texto()


def update():
    global pontos
    global derrotas
    global start

    dash()

    movimento()

    movimento_vilao()

    if keyboard.escape:
        global dificult, start

        kill()
        dificuldade_texto()
        dificult=0
        start=0
        derrotas=0
        pontos=0


    if start==0:
       if keyboard.space:
        start=1
        reinicio()

    if start==0 or dificult==0:
        kill()


    if heroi.colliderect(moeda):
        pontos = pontos + 1
        moeda.x = random.randint(30,700)
        moeda.y = random.randint(50,500)
    if dificult==1:
        if derrotas == 10:
            kill()

        if pontos == 5:
            kill()
    if dificult==2:
        if derrotas == 5:
            kill()
        if pontos == 10:
            kill()
    if dificult == 1:
        if derrotas == 10:
            if keyboard.space:
                derrotas=0
                reinicio()

        if pontos == 5:
            if keyboard.space:
                pontos=0
                derrotas=0
                reinicio()
    if dificult == 2:
        if derrotas == 5:
            if keyboard.space:
                derrotas=0
                reinicio()

        if pontos == 10:
            if keyboard.space:
                pontos=0
                derrotas=0
                reinicio()

    if heroi.colliderect(vilao):
        heroi.x = WIDTH // 2
        heroi.y = HEIGHT // 2
        vilao.x = random.randint(0, WIDTH)
        vilao.y = random.randint(0, HEIGHT)
        pontos = 0
        derrotas = derrotas + 1
 

def on_mouse_down(pos):
    global dificult
    if botao.collidepoint(pos):
        dificult=1
        reinicio()
    if botao2.collidepoint(pos):
        dificult=2
        reinicio()


pgzrun.go()