from tabuleiro import *
from PPlay.window import *
from PPlay.sprite import *


janela = Window(800, 600)
resp = True
mouse =  janela.get_mouse()
pygame.display.set_caption("Trabalho ---- ES2")

botao1j = Sprite("Sprites/botao1j.png")
botao1j.x= 100
botao1j.y= 200

botao2j = Sprite("Sprites/botao2j.png")
botao2j.x= 100
botao2j.y= 300

botaopc = Sprite("Sprites/botaopc.png")
botaopc.x= 100
botaopc.y= 400

botaoreg = Sprite("Sprites/botaoreg.png")
botaoreg.x= 100
botaoreg.y= 500

botaotit = Sprite("Sprites/nomej.png")
botaotit.x= 100
botaotit.y= 80

imagemtab = Sprite("Sprites/imagemtab.png")
imagemtab.x= 350
imagemtab.y= 330


while resp:
    janela.update()
    botao1j.draw()
    botao2j.draw()
    botaopc.draw()
    botaoreg.draw()
    botaotit.draw()
    imagemtab.draw()
    if(mouse.is_button_pressed(1) and mouse.is_over_object(botao1j) or
        mouse.is_button_pressed(1) and mouse.is_over_object(botao2j) or
        mouse.is_button_pressed(1) and mouse.is_over_object(botaopc)):
        resp = False
        janela.delay(500)



tab = Tabuleiro()

tab.inicializaMatriz()

while True:

    tab.atualiza()
    tab.selecionaPeca()
    tab.defineDisponiveis()
    tab.atualiza()
    tab.confirmaMovimento()