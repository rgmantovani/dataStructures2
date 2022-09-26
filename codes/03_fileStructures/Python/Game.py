# --------------------------------
# --------------------------------
class Game:
    # construtor do objeto Game
    def __init__(self, nome=None, genero=None, plataforma=None,
        ano=None, classificacao=None, preco=None, midia=None,
        tamanho=None, produtora=None):
        self.nome = nome
        self.genero = genero
        self.plataforma = plataforma
        self.ano = ano
        self.classificacao = classificacao
        self.preco = preco
        self.midia = midia
        self.tamanho = tamanho
        self.produtora = produtora

    def setNome(self, nome):
        self.nome = nome

    def getNome(self):
        return (self.nome)

# --------------------------------
# --------------------------------
