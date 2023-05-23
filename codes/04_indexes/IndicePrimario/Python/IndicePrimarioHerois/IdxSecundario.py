
# class IdxSecundario
# TODO: fazer herança da classe IdxPrimario
#      * arqDados
#      * tabelaIndicesPrimario
#      * arqIndicesPrimario
#      * tabelaIndicesSecundario
#      * arqIndicesSecundario

# Pesquisa(query - chaveSecundaria):
#    retorno: 0 ou + registros (list, vetor)
#      1. pesquisar se a chave (query) existe na tabela de idx IdxSecundario
#           - Se não encontrar nada: lista vazia (none)
#      temos informção na tabela secundaria
#      [1+ chaves secundarias correspondentes a query]
#      2. Percorrer todas as posicoes da tabela de indice secundario cujo
#       valor da chave é query (laço/for/iteracao/iteration)
#           aux = elemento iteracao
#           3. Procurar na tabela de Indice Primario, qual é o RRN do registro
#           4. Leitura do registro com base no RRN
#           5. append(registro) na lista de retorno
#      6. retorna (lista de registros)

# Construtor
#      1. Abrir o arquivos de dados
#      2. Para cada registro no arquivo de dados:
#          3. cria a chave canonica primaria do registro
#          4. pega o RRN do registro
#          5. Append (chave 1a, RRN) na tabela de indices Primario
#          6. cria/pega a chave secundaria
#          7. Append (chave 2a, chave 1a) na tabela de Indices Secundaria
#       8. Ordena a tabela de indices primario (Chave 1a)
#       9. Ordena a tabela de indices secundario (Chave 2a)
