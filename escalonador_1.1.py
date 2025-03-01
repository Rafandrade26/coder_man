#coding=UTF-8
import interface
import time
import string
from graphics import *

#################################################################
###################### Interface inicial ########################
#################################################################

win = GraphWin("Janela", 1280, 720)

bg = Rectangle (Point(0,0), Point (1280, 720))
bg.setFill(color_rgb(40, 100, 255))
bg.draw(win)

efeitoSombra = 5

while efeitoSombra > 0: #Adiciona camadas de texto cinza ligeiramente abaixo e à direita do texto de título, dando um efeito "tridimensional" ao texto.
	underTitle = Text(Point((640 + efeitoSombra), (230 + efeitoSombra)), "BEM-VINDO AO SIMULADOR DE ESCALONAMENTO")
	underTitle.setFace("arial")
	underTitle.setStyle("bold")
	underTitle.setTextColor("purple")
	underTitle.setSize(30)
	underTitle.draw(win)
	efeitoSombra = efeitoSombra - 1


title = Text (Point(640,230), "BEM-VINDO AO SIMULADOR DE ESCALONAMENTO") #Cria o título na cor preta padrão
title.setFace("arial") #Define a fonte do título (arial)
title.setStyle("bold") #Define o estilo do título (negrito)
title.setSize(30) #Define o tamanho da fonte (30)
title.draw(win) #Mostra o título do programa


#################################################################
################# Criação caixas de texto #######################
#################################################################

##### Caixa "PRÓXIMO" #####


clkBoxNextXE = 325
clkBoxNextXD = 525
clkBoxNextYS = 400
clkBoxNextYI = 440

thicker = 0

while thicker < 5:
	clickBoxNext = Rectangle(Point(clkBoxNextXE + thicker, clkBoxNextYS + thicker), Point(clkBoxNextXD - thicker, clkBoxNextYI - thicker))
	clickBoxNext.draw(win)
	thicker = thicker + 1

textNext = Text (Point (425, 420), "PRÓXIMO") 
textNext.setStyle("bold")

textNext.draw(win)

##### Caixa "ESCALONAR" #####

clkBoxEndXE = 625
clkBoxEndXD = 825
clkBoxEndYS = 400
clkBoxEndYI = 440

thicker = 0

while thicker < 5:
	clickBoxEnd = Rectangle(Point(clkBoxEndXE + thicker, clkBoxEndYS + thicker), Point(clkBoxEndXD - thicker, clkBoxEndYI - thicker))
	clickBoxEnd.draw(win)
	thicker = thicker + 1

textEnd = Text (Point (725, 420), "ESCALONAR") 
textEnd.setStyle("bold")

textEnd.draw(win)


#################################################################


letraProcesso = 1 #Define se o processo em questão é o processo A (=1), processo B (=2), processo C (=3) e assim por diante.
processosRestantesRR = 0 #Define a quantidade de processos atualmente em execução. Variável usada somente em método Round Robin.
alfabeto = string.ascii_uppercase #Cria uma lista com todas as letras maiúsculas do alfabeto
alfabetoMin = string.ascii_lowercase #Cria uma lista com todas as letras minúsculas do alfabeto

time.sleep(.5)

processos = ["nulo"]

maisEntradas = True

while maisEntradas == True:
	
	print (processos[-1])
	textoInstruc = Text(Point (540, 320), "Digite o tamanho do processo " + str(letraProcesso) + ":") 
	textoInstruc.setSize(22) #Altera o tamanho da fonte do texto de instruções
	textoInstruc.setStyle("bold") #Torna em negrito o texto das instruções
	textoInstruc.draw(win) #Mostra o texto com as instruções ao usuário

	inputBox = Entry(Point(800, 320), 3) #Cria a caixa para o usuário digitar as entradas
	inputBox.draw(win) #Mostra a caixa para digitar as entradas
	


	clickPoint = win.getMouse()
	clickX = clickPoint.getX()
	clickY = clickPoint.getY()

	if clickX > clkBoxNextXE and clickX < clkBoxNextXD and clickY > clkBoxNextYS and clickY < clkBoxNextYI:
		valorProcesso = inputBox.getText()
		
		if valorProcesso != "" and valorProcesso not in alfabetoMin and valorProcesso not in alfabeto:
			processos.append(eval(valorProcesso))
			letraProcesso = letraProcesso + 1
			processosRestantesRR = processosRestantesRR + 1

		inputBox.setText("")
		inputBox.undraw()
		inputBox.draw(win)
		textoInstruc.undraw()
	else:
		textoInstruc.undraw()
	

		if clickX > clkBoxEndXE and clickX < clkBoxEndXD and clickY > clkBoxEndYS and clickY < clkBoxEndYI:
			processos.pop(0) #Elimina o primeiro item da lista de processos
			print (processos)
			processosRestantesRR = processosRestantesRR + 1
			bg.undraw()
			bg.draw(win)

			maisEntradas = False
			inputBox.undraw()

inputBox.undraw()
##########
letraMax = letraProcesso - 1 #Define o último valor do processo (Ex: letraMax = 4 --> Processo D é o último. letraMax = 10 --> Processo J é o último, etc.)

letraProcesso = 1 #Reseta o contador de volta para o processo A.
valorTotalCiclos = 0 #Declaração inicial para a contagem de ciclos de clock total realizadas nas etapas.

print ("")

while letraProcesso <= letraMax:
	valorTotalCiclos = valorTotalCiclos + (processos[letraProcesso - 1])
	print ("O processo " + str(alfabeto[letraProcesso - 1]) + " executará " + str(processos[letraProcesso - 1]) + " ciclos.")
	letraProcesso = letraProcesso + 1
	#time.sleep(.5)
###############################################################
inputBox.undraw()

#time.sleep(1)

print ("\nAgora selecione o tipo de escalonamento. Digite:\n")
#time.sleep(1.5)
textoInstruc = Text (Point (600, 60), "Agora selecione o tipo de escalonamento. ")
textoInstruc.setSize(22) #Altera o tamanho da fonte do texto de instruções
textoInstruc.setStyle("bold") #Torna em negrito o texto das instruções
textoInstruc.draw(win) #Mostra o texto com as instruções ao usuário

### Caixa 1 ###

clkBoxFCFSXE = 150
clkBoxFCFSXD = 400
clkBoxFCFSYS = 400
clkBoxFCFSYI = 520

thicker = 0

clickBoxFCFS = Rectangle(Point(clkBoxFCFSXE + thicker, clkBoxFCFSYS + thicker), Point(clkBoxFCFSXD - thicker, clkBoxFCFSYI))
clickBoxFCFS.draw(win)

textoFCFS = Text (Point (275, 460), "FIRST COME\nFIRST SERVED")
textoFCFS.setSize(22) #Altera o tamanho da fonte do texto de instruções
textoFCFS.setStyle("bold") #Torna em negrito o texto das instruções
textoFCFS.draw(win) #Mostra o texto com as instruções ao usuário

### Caixa 2 ###

clkBoxSJFXE = 520
clkBoxSJFXD = 770
clkBoxSJFYS = 400
clkBoxSJFYI = 520

thicker = 0

clickBoxSJF = Rectangle(Point(clkBoxSJFXE + thicker, clkBoxSJFYS + thicker), Point(clkBoxSJFXD - thicker, clkBoxSJFYI))
clickBoxSJF.draw(win)

textoSJF = Text (Point (645, 460), "SHORTEST\nJOB FIRST")
textoSJF.setSize(22) #Altera o tamanho da fonte do texto de instruções
textoSJF.setStyle("bold") #Torna em negrito o texto das instruções
textoSJF.draw(win) #Mostra o texto com as instruções ao usuário

### Caixa 3 ###

clkBoxRRXE = 890
clkBoxRRXD = 1140
clkBoxRRYS = 400
clkBoxRRYI = 520

thicker = 0

clickBoxRR = Rectangle(Point(clkBoxRRXE + thicker, clkBoxRRYS + thicker), Point(clkBoxRRXD - thicker, clkBoxRRYI))
clickBoxRR.draw(win)

textoRR = Text (Point (1015, 460), "ROUND\nROBIN")
textoRR.setSize(22) #Altera o tamanho da fonte do texto de instruções
textoRR.setStyle("bold") #Torna em negrito o texto das instruções
textoRR.draw(win) #Mostra o texto com as instruções ao usuário

################

tipoDeEscalonamento = 0

clickPoint = win.getMouse()
clickX = clickPoint.getX()
clickY = clickPoint.getY()
	
if clickX > clkBoxFCFSXE and clickX < clkBoxFCFSXD and clickY > clkBoxFCFSYS and clickY < clkBoxFCFSYI:
	tipoDeEscalonamento = 1
elif clickX > clkBoxSJFXE and clickX < clkBoxSJFXD and clickY > clkBoxSJFYS and clickY < clkBoxSJFYI:
	tipoDeEscalonamento = 2
elif clickX > clkBoxRRXE and clickX < clkBoxRRXD and clickY > clkBoxRRYS and clickY < clkBoxRRYI:
	tipoDeEscalonamento = 3
	

print ('"1" para First Come First Served;')
#time.sleep(.5)
print ('"2" para Shortest Job First;')
#time.sleep(.5)
print ('"3" para Round Robin.\n')

#tipoDeEscalonamento = int(raw_input('Sua escolha: '))
print ("O progresso será mostrado a partir de parcelas de 5 ciclos de clock por vez.\n")
#time.sleep(1)

##################################################################
letraProcesso = 1
etapa = 1
ciclosRestantes = processos[letraProcesso - 1]

################# First Come First Served (FCFS) #################

bg.undraw()
bg.draw(win)

squareXE = 100
squareXD = 120
squareYS = 100
squareYI = 120

listaSquare = []
i = 0

if tipoDeEscalonamento == 1:
	#portas = Image(Point(800,600), "portas.png")
	#portas.draw(win)

	textoInstruc = Text (Point (600, 60), 'Você escolheu "First Come First Served" (FCFS). ')
	textoInstruc.setSize(22) #Altera o tamanho da fonte do texto de instruções
	textoInstruc.setStyle("bold") #Torna em negrito o texto das instruções
	textoInstruc.draw(win) #Mostra o texto com as instruções ao usuário
	
	
	portas = Image(Point(100,100), "portas.png")
	portas.draw(win)

	print ('\nVocê escolheu "First Come First Served" (FCFS).\n')
	time.sleep(.8)


	while letraProcesso	<= letraMax:
		while ciclosRestantes > 0:
			print ('Etapa ' + str(etapa) + ':')
			print ('Processo ' + str(alfabeto[letraProcesso - 1]) + ': ' + str(ciclosRestantes) + ' ciclos restantes...\n')
			ciclosRestantes = ciclosRestantes - 5
			etapa = etapa + 1
			
			square = Rectangle(Point(squareXE, squareYS), Point(squareXD, squareYI))
			listaSquare.append(square)

			listaSquare[i].draw(win)
			squareXE = squareXE + 20
			squareXD = squareXD + 20
			i = i + 1
			
			time.sleep(.9)
			
			if ciclosRestantes <= 0:
				print ('Processo concluído.\n')
				print ('######################################################\n')
				
		if letraProcesso != letraMax:
			ciclosRestantes = processos[letraProcesso]
			letraProcesso = letraProcesso + 1

			squareYS = squareYS + 20
			squareYI = squareYI + 20

		else:
			etapa = etapa - 1
			print ("Tarefa concluída em ") + str(etapa) + " etapas e " + str(valorTotalCiclos) + " ciclos de clock.\n"
			letraProcesso = letraProcesso + 1


################### Shortest Job First" (SJF) ####################

elif tipoDeEscalonamento == 2:
	print ('\nVocê escolheu "Shortest Job First" (SJF).')
	time.sleep(.8)
	processos.sort()
	ciclosRestantes = processos[0]
	time.sleep(1)

	while letraProcesso	<= letraMax:
		while ciclosRestantes > 0:
			print (('Etapa ') + str(etapa) + (':'))
			print (('Processo ') + str(alfabeto[letraProcesso - 1]) + (': ') + str(ciclosRestantes) + (' ciclos restantes...\n'))
			ciclosRestantes = ciclosRestantes - 5

			square = Rectangle(Point(squareXE, squareYS), Point(squareXD, squareYI))
			listaSquare.append(square)

			listaSquare[i].draw(win)
			squareXE = squareXE + 20
			squareXD = squareXD + 20
			i = i + 1

			etapa = etapa + 1
			time.sleep(.9)
			
			if ciclosRestantes <= 0:
				if ciclosRestantes == 0:
					print ('Processo concluído.\n')
					print ('######################################################\n')
					squareYS = squareYS + 20
					squareYI = squareYI + 20

				else:
					etapa = etapa + 1
					print ('Processo concluído.\n')
					print ('######################################################\n')
					squareYS = squareYS + 20
					squareYI = squareYI + 20
				
		if letraProcesso != letraMax:
			ciclosRestantes = processos[letraProcesso]
			letraProcesso = letraProcesso + 1
			
		else:
			etapa = etapa - 1
			print (("Tarefa concluída em ") + str(etapa) + (" etapas e ") + str(valorTotalCiclos) + (" ciclos de clock.\n"))
			letraProcesso = letraProcesso + 1
			
######################## Round Robin (RR) #########################

elif tipoDeEscalonamento == 3:
	print ('\nVocê escolheu "Round Robin".\n')
	
	time.sleep(.8)
	processosRestantesRR = processosRestantesRR - 1


	ciclosRestantes = processos[0]
	letraProcesso = letraProcesso - 1
	
	while processosRestantesRR > 0:

		while letraProcesso < letraMax:
#			print "letraMax: " + str(letraMax)
#			print "letraProcesso: " + str(letraProcesso)
			if ciclosRestantes > 0:
				print (('Etapa ') + str(etapa) + (':'))
				print ('Processo ' + str(alfabeto[letraProcesso]) + ': ' + str(ciclosRestantes) + ' ciclos restantes...\n')
			processos[letraProcesso] = ciclosRestantes - 5

			square = Rectangle(Point(squareXE, squareYS), Point(squareXD, squareYI))
			listaSquare.append(square)

			listaSquare[i].draw(win)
			squareXE = squareXE + 20
			squareXD = squareXD + 20
			i = i + 1

			etapa = etapa + 1
			time.sleep(.9)
			
			if ciclosRestantes - 1 <= 0:
				print ('Processo ' + str(alfabeto[letraProcesso]) + ' concluído.\n')
				print ('######################################################\n')
				processosRestantesRR = processosRestantesRR - 1
				letraProcesso = 0
				letraMax = letraMax - 1
		
			letraProcesso = letraProcesso + 1
			
			if letraProcesso != letraMax:
				ciclosRestantes = processos[letraProcesso]
				
			else:
				letraProcesso = 0
				ciclosRestantes = processos[0]
				processosRestantesRR = processosRestantesRR - 1
	
				squareYS = squareYS + 20
				squareYI = squareYI + 20

	print ("Tarefa concluída em " + str(etapa) + " etapas e " + str(valorTotalCiclos) + " ciclos de clock.\n")
	
	

	while processosRestantesRR > 0:
		
		print ('Etapa ' + str(etapa) + ':')
		print ('Processo ' + str(alfabeto[letraProcesso - 1]) + ': ' + str(ciclosRestantes) + ' ciclos restantes...\n')
		ciclosRestantes = ciclosRestantes - 5
		etapa = etapa + 1
		time.sleep(.9)
		
		if ciclosRestantes <= 0:
			print ('Processo concluído.\n')
			print ('######################################################\n')

		if letraProcesso != letraMax:
			ciclosRestantes = processos[letraProcesso]
			letraProcesso = letraProcesso + 1
		else:
			etapa = etapa - 1
			print ("Tarefa concluída em " + str(etapa) + " etapas e " + str(valorTotalCiclos) + " ciclos de clock.\n")
			letraProcesso = letraProcesso + 1

else:
	print ('\nComando inválido. Por favor, tente novamente a partir do início.')