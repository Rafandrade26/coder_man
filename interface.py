"""Interface do Simulador"""
from graphics import *
def interface():#Vai ter toda a parte grafica da simulacao
	win = GraphWin("Escalonador de Processos", 1000, 700)
	win.setBackground("Black")
	imagem = Image(Point(450,500), "portas.png")
	imagem.draw(win)
	win.getMouse()
	win.close()

def main():#Abre o menu principal
	win = GraphWin("Escalonador de Processos", 1000, 700)
	win.setBackground("White")
	
main()
