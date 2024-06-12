import pickle
import os

class IndicePrimario:

	# atributos
	__arquivoDados    = None   # string
	__arquivoIndices  = None   # string
	__tabelaIndices   = list() # lista de tuplas ( CP , RRN )

	# ------------------------
	# construtor
	# ------------------------
	def __init__(self, dataFile, auxFile):
	
		# 01. abre o arquivo de dados (texto para r/w)
		# 02. percorre o arquivo (regitro por vez)
		with(open(dataFile, mode="r+") as file):
			records = file.readlines()
		records.pop(0)
	
		if(not os.path.exists(auxFile)):
			print("*** NAO EXISTE ARQUIVO")
			# if auxFile == None: # criar a estrutura
			for i in range(0, len(records)):
				auxiliar = records[i]
		
			#    a) criar chave canonica
				stringList = auxiliar.split(',')
				chave = stringList[0]
				chave = chave.replace(" ", "")
				chave = chave.upper()
				# print(chave)

			#    b) RRN (i)
			# 	 c) define a tupla (CP, RRN)
				tup = (chave, i)
			# 	 d) add lista (tabelaIndices)
				self.__tabelaIndices.append(tup)

			print(self.__tabelaIndices)
			print("\n")
			# 03. ordenar os caras pela chave
			self.__tabelaIndices.sort(key = lambda tup: tup[0])
			print(self.__tabelaIndices)

			# 04. grava a tabela de indices no arqIndices (binário)
			self.__arquivoIndices = open(auxFile, 'wb+')
			pickle.dump(self.__tabelaIndices, self.__arquivoIndices)

		else: # carregar os dados do arquivo p tabela Indices
			print("*** JA EXISTE ARQUIVO")
		#  01. abre o arquivoIndices (binario w/r)

			with open(auxFile, "rb") as f:
				unpickler = pickle.Unpickler(f)
				self.__tabelaIndices = pickle.load(f)

		#  02 leitura dos dados do arquivo e atribui p Tabela de Indices
			print(self.__tabelaIndices)

	# ------------------------
	# ------------------------


	# destrutor
	def __del__(self):
		pass

	# insercao (arquivoDados)
	def insercao(self, registro):
		# this.busca() -> True/False
		pass

	# remoção (memoria)
	def remover(self, chave):
		# this.busca() -> True/False
		pass

	# consulta (memoria)
	def busca(self, chave):
		pass

# ------------------------
# ------------------------

if __name__ == '__main__':


	tabela = IndicePrimario(dataFile = "animes.csv", auxFile = "index.dat")



























