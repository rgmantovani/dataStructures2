#------------------------------------------------------
#------------------------------------------------------

from primaryIndex import IndicePrimario

#------------------------------------------------------
# funcao main no python
#------------------------------------------------------

if __name__ == "__main__":

    # construtor 
	estrutura = IndicePrimario()
	
	# existe a chave
	res = estrutura.pesquisaRegistro(chave="HADES2019")
	print(res)

	# nao existe a chave
	res = estrutura.pesquisaRegistro(chave="HAVEANICEDEATH2022")
	print(res)
	
	newRegistro = "Have a nice Death|Magic Design Studios|Rogue-like|Multiplataforma|2022|Teen|61.99|Digital|2.00"
	estrutura.insereRegistro(newRegistro)

	#estrutura.removeRegistro(chave)
	# destruir (chamado implicitamente pelo python)


#------------------------------------------------------
#------------------------------------------------------
