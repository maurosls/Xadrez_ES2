from tabuleiro import *
from PPlay.window import *
from PPlay.sprite import *
import ctypes
import webbrowser


janela = Window(800, 600)
resp = True
mouse = janela.get_mouse()
pygame.display.set_caption("Xadrez ES2 ")

botao1j = Sprite("Sprites/botao1j.png")
botao1j.x= 100
botao1j.y= 200

botao2j = Sprite("Sprites/botao2j.png")
botao2j.x= 100
botao2j.y= 300

botaoPC = Sprite("Sprites/botaopc.png")
botaoPC.x= 100
botaoPC.y= 400

botaoRegras = Sprite("Sprites/botaoreg.png")
botaoRegras.x= 100
botaoRegras.y= 500
url = "http://baquara.com/xadrez/movimentos.htm"

imagemTitulo = Sprite("Sprites/nomej.png")
imagemTitulo.x= 100
imagemTitulo.y= 80

imagemTabuleiro = Sprite("Sprites/imagemtab.png")
imagemTabuleiro.x= 350
imagemTabuleiro.y= 330


while resp:
    janela.update()
    botao1j.draw()
    botao2j.draw()
    botaoPC.draw()
    botaoRegras.draw()
    imagemTitulo.draw()
    imagemTabuleiro.draw()
    tipoJogo = None
    if(mouse.is_button_pressed(1) and mouse.is_over_object(botao1j)):
        resp = False
        janela.delay(300)
        tipoJogo = "1j"
    elif(mouse.is_button_pressed(1) and mouse.is_over_object(botao2j)):
        resp = False
        janela.delay(300)
        tipoJogo = "2j"
    elif(mouse.is_button_pressed(1) and mouse.is_over_object(botaoPC)):
        ctypes.windll.user32.MessageBoxW(0, "Modo de Jogo não Disponível!", "Aviso!", 0)
        #resp = False
        #janela.delay(500)
    elif(mouse.is_button_pressed(1) and mouse.is_over_object(botaoRegras)):
        webbrowser.open(url, new=0,autoraise=True)



tab = Tabuleiro(tipoJogo)

tab.inicializaMatriz()

loop = True

while loop:
    tab.atualiza()
    tab.selecionaPeca()
    tab.defineDisponiveis()
    tab.atualiza()
    if(tab.selecao != "vazio" and tab.selecao != None):
        tab.confirmaMovimento()

    if(tab.checkM == True):
        loop = False


