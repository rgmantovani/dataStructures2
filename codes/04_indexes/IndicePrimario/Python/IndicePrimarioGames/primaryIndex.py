#------------------------------------------------------
# Tabela de indice primario
#------------------------------------------------------

import os

#------------------------------------------------------
#------------------------------------------------------

class IndicePrimario:

	# atributos
	# 1. arquivo de dados (escrita/leitura), [r+]
	__arquivoDados = None 
	# 2. arquivo tabela de idx primario (escrita/leitura) []
	__arquivoIdxPrimario = None
	# 3. tabela de indices
	__tabelaIndices = list()

	#---------------------
	# A: construtor
	#---------------------
	def __init__(self):
		self.__arquivoDados = open("arqDados.txt", "r+")
		# abrir o arquivo de dados (arquivo existente)
		# arquivo de idx primario
		if(os.path.isfile("arqIdxPrimario.txt")):
			print("Existe arquivo de indice primario")
	#       - se ja existir, carrega (associa)
	#		TODO: carregar/criar tabela com base no arquivo de idx
		else:
	# 		- se nao existir, criar arquivo (vazio)
			print("Nao existe arquivo de indice primario")	
			self.__arquivoIdxPrimario = open("arqIdxPrimario.txt", "a+")
	#			- tabela de indices e vazia
	#			- percorrer o arquivo linha por linha
			RRN = 0
			for line in self.__arquivoDados.readlines()[1:]:
				print(line)
	#			- criar chave, RRN
				chave = self.criaChaveCanonica(line)
				print("-------------")
				print(chave)
				print(RRN)
				self.__tabelaIndices.append((chave, RRN))
	#               - add tupla na tabela de indices
				RRN+=1
	#       - ordenar a tabela
	#		(chave, RRN) -> tupla[0]
			self.__tabelaIndices.sort(key=lambda a: a[0])
			# print(self.__tabelaIndices)
			for i in range(0, len(self.__tabelaIndices)):
				print(self.__tabelaIndices[i])

	#---------------------
	#---------------------
	
	def criaChaveCanonica(self, registro):
		x = registro.split('|')
		print(x)
		chavePrimaria = x[0] + x[4]
		chavePrimaria = chavePrimaria.upper().replace(' ', '')
		return(chavePrimaria)

	#---------------------
	# B: destrutor
	#---------------------
	def __del__(self):
		pass
	# fecha o arquivo de dados
	# arquivo de indices
	# 	- gravar a tabela no arquivo, fecha o arquivo

	#---------------------
	# verificar se tem espaço para reuso
	#---------------------
	def consultaCabecalho(self):
		# TODO:
		# ler a primeira linha do arquivo de dados
		# obter o valor da tag TOP
		# retorna o valor de TOP
		pass

	#---------------------
	# C: Insercao (registro)
	#---------------------
	def insereRegistro(self, registro):
	#	calcular chave primaria do registro
		novaChave = self.criaChaveCanonica(registro)
		print(novaChave)
	#   procurar na tabela (RAM) se a chave ja existe
		if(self.pesquisaRegistro(registro)):
		#   se a chave ja existir: nao faz nada!
			print("Ja existe o cara")
		else:
	#       verificar se tem espaco vago no arquivo (header, TOP)
			top = self.consultaCabecalho()
	#       RRN <- se nao tiver: append
			if(top == -1):
				# add o novo registro na ultima linha do arq dados
				# RNN vai ser o tamanho da lista de tabela de indices
			else :
				# add o novo registro na posicao de reuso
				# RRN = novo valor do RRN	
			# nova tupla  = (novaChave, RRN)
			# append da nova tupla
			# reordenar a tabela

	#---------------------
	# D: Pesquisa (chave)
	#---------------------
	def pesquisaRegistro(self, chave) :
		print("---------------------")
		print("Search: " + chave + " \n")
		print("---------------------")
		
		result = [tup for tup in self.__tabelaIndices if tup[0] == chave]
		print(result)
		if(len(result) == 0):
			return [False, ] 
		else:
			# TODO: buscar valor no arquivo 
			# acessar o correspondente RRN da chave encontrada
			#   se existe na tabela (chave, RRN)
			#   vai no arquivo de dados (RRN)
			#   retorna o registro 
			# registro = self.lerRegistroComRRN(RRN)
			return [True, ]


#------------------------------------------------------
#------------------------------------------------------