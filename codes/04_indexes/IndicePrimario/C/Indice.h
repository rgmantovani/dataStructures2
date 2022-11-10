//------------------------------------------------------------------------------
//------------------------------------------------------------------------------

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>
#include <stdbool.h>

#define BUFFER 150

//------------------------------------------------------------------------------
//------------------------------------------------------------------------------

typedef struct {
  char primeiroNome[BUFFER];
  char sobrenome[BUFFER];
  char nomeHeroi[BUFFER];
  char poder[BUFFER];
  char fraqueza[BUFFER];
  char cidade[BUFFER];
  char profissao[BUFFER];
} Heroi;


typedef struct {
  char chave[BUFFER];   // chave é a chave canonica de um registro
  int RRN;              // é a referencia p leitura/gravação do registro
} ArrayItemPrimario;

typedef struct {
  char chavePrimaria[BUFFER];   // chave primeira em forma canonica
  char chaveSecundaria[BUFFER]; // chave secundaria em formato canonico (maiusc)
} ArrayItemSecundario;

//Indice
typedef struct {
  FILE *arqDados;              // arquivo de dados (r+)
  FILE *arqIdxPrimario;        // arquivo de indice primario (r+)
  FILE *arqIdxSecundario;      // arquivo de indice secundario (r+)
  ArrayItemPrimario *idxPrimario;    // vetor de pares ordenados {chave, RRN}
  ArrayItemSecundario *idxSecundario; // idx secundário
  int numeroRegistros; // guardar o numero de registros na memoria
  bool status;         // status de escrita do arquivo
} Indice;

//------------------------------------------------------------------------------
//------------------------------------------------------------------------------

int numeroRegistros(Indice *idx);
void printaHeroi(Heroi *h);
Heroi quebraStringEmHeroi(char *string);

void iniciaIndiceVazio(Indice *idx);
void iniciaIndiceArquivo(Indice *idx, char* filename);
char* geraChaveRegistro(char* str1, char* str2);

void imprimeVetorIndices(Indice *idx);
void gravaVetorIndices(Indice *idx);
void atualizaStatusHeader(Indice *idx, int status);
void destroiIndice(Indice *idx);

bool adicionarRegritro(Indice *idx);
bool procurarRegistro(Indice *idx);
bool deletaRegistro(Indice *idx);

//------------------------------------------------------------------------------
//------------------------------------------------------------------------------
