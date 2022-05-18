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
} ArrayItem;


//Indice
typedef struct {
  FILE *arqDados;      // arquivo de dados (r+)
  FILE *arqIdx;        // arquivo de indices (r+)
  ArrayItem *vetor;    // vetor de pares ordenados {chave, RRN}
  int numeroRegistros; // guardar o numero de registros na memoria
  bool status;         // status de escrita do arquivo
} Indice;

//------------------------------------------------------------------------------
//------------------------------------------------------------------------------

int numeroRegistros(Indice *idx);
void printaHeroi(Heroi *h);
Heroi quebraStringEmHeroi(char *string);
void iniciaIndiceVazio(Indice *idx);
char* geraChaveRegistro(char* str1, char* str2);
void imprimeVetorIndices(Indice *idx);
void iniciaIndiceArquivo(Indice *idx, char* filename);
void atualizaStatusHeader(Indice *idx, int status);
void gravaVetorIndices(Indice *idx);
void destroiIndice(Indice *idx);

//------------------------------------------------------------------------------
//------------------------------------------------------------------------------
