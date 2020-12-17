import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLUT import *

LARGURA_JANELA = 640
ALTURA_JANELA = 480

xDaBola = 0
yDaBola = 0
tamanhoDaBola = 20
velocidadeDaBolaEmX = 3
velocidadeDaBolaEmY = 3

yDoJogador1 = 0
yDoJogador2 = 0

pontoJogador1 = 0
pontoJogador2 = 0

def xDoJogador1():
    return -LARGURA_JANELA / 2 + larguraDosJogadores() / 2

def xDoJogador2():
    return LARGURA_JANELA / 2 - larguraDosJogadores() / 2

def larguraDosJogadores():
    return tamanhoDaBola

def alturaDosJogadores():
    return 3 * tamanhoDaBola

def atualizar():
    global xDaBola, yDaBola, velocidadeDaBolaEmX, velocidadeDaBolaEmY, yDoJogador1, yDoJogador2, ponto, pontoJogador1, pontoJogador2
    
    xDaBola = xDaBola + velocidadeDaBolaEmX
    yDaBola = yDaBola + velocidadeDaBolaEmY

    if (xDaBola + tamanhoDaBola / 2 > xDoJogador2() - larguraDosJogadores() / 2
    and yDaBola - tamanhoDaBola / 2 < yDoJogador2 + alturaDosJogadores() / 2
    and yDaBola + tamanhoDaBola / 2 > yDoJogador2 - alturaDosJogadores() / 2):
        velocidadeDaBolaEmX = -velocidadeDaBolaEmX

    if (xDaBola - tamanhoDaBola / 2 < xDoJogador1() + larguraDosJogadores() / 2
    and yDaBola - tamanhoDaBola / 2 < yDoJogador1 + alturaDosJogadores() / 2
    and yDaBola + tamanhoDaBola / 2 > yDoJogador1 - alturaDosJogadores() / 2):
        velocidadeDaBolaEmX = -velocidadeDaBolaEmX

    if yDaBola + tamanhoDaBola / 2 > ALTURA_JANELA / 2:
        velocidadeDaBolaEmY = -velocidadeDaBolaEmY

    if yDaBola - tamanhoDaBola / 2 < -ALTURA_JANELA / 2:
        velocidadeDaBolaEmY = -velocidadeDaBolaEmY

    if xDaBola > LARGURA_JANELA / 2:
        xDaBola = 0
        yDaBola = 0
        pontoJogador1 = 1 + pontoJogador1

    if xDaBola < -LARGURA_JANELA / 2:
        xDaBola = 0
        yDaBola = 0
        pontoJogador2 = 1 + pontoJogador2

    keys = pygame.key.get_pressed()

    if keys[K_w]:
        yDoJogador1 = yDoJogador1 + 5

    if keys[K_s]:
        yDoJogador1 = yDoJogador1 - 5

    if keys[K_UP]:
        yDoJogador2 = yDoJogador2 + 5

    if keys[K_DOWN]:
        yDoJogador2 = yDoJogador2 - 5

def desenharRetangulo(x, y, largura, altura, r, g, b):
    glColor3f(r, g, b)

    glBegin(GL_QUADS)
    glVertex2f(-0.5 * largura + x, -0.5 * altura + y)
    glVertex2f(0.5 * largura + x, -0.5 * altura + y)
    glVertex2f(0.5 * largura + x, 0.5 * altura + y)
    glVertex2f(-0.5 * largura + x, 0.5 * altura + y)
    glEnd()

def desenhar():

    glViewport(0, 0, LARGURA_JANELA, ALTURA_JANELA)

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(-LARGURA_JANELA / 2, LARGURA_JANELA / 2, -ALTURA_JANELA / 2, ALTURA_JANELA / 2, 0, 1)

    glClear(GL_COLOR_BUFFER_BIT)

    desenharRetangulo(xDaBola, yDaBola, tamanhoDaBola, tamanhoDaBola, 1, 1, 0)
    desenharRetangulo(xDoJogador1(), yDoJogador1, larguraDosJogadores(), alturaDosJogadores(), 1, 0, 0)
    desenharRetangulo(xDoJogador2(), yDoJogador2, larguraDosJogadores(), alturaDosJogadores(), 0, 0, 1)

    linha_vertical(0,ALTURA_JANELA)
    placar()
    pygame.display.flip()

def linha_vertical(posicao,tamanho):
    glColor3f(1,1,1)
    glBegin(GL_LINES)
    glVertex2f(posicao, tamanho)
    glVertex2f(posicao, -tamanho)
    glEnd()

def texto(x, y, texto, r, g, b):
    glutInit()
    glColor3f(r, g, b)
    glRasterPos2f(x,y)
    for caracter in texto:    
        glutBitmapCharacter(GLUT_BITMAP_8_BY_13, ord(caracter))

def placar():
    texto(-310,210, 'Jogador 1: ', 1, 1, 1)
    texto(-210,210, str(pontoJogador1), 1, 1, 1)
    texto(180,210, 'Jogador 2: ', 1, 1, 1)
    texto(280,210, str(pontoJogador2), 1, 1, 1)

pygame.init()
pygame.display.set_mode((LARGURA_JANELA, ALTURA_JANELA), DOUBLEBUF | OPENGL)

while True:

    atualizar()
    desenhar()
    pygame.event.pump()
    pygame.time.wait(30)

