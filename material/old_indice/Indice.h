#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

#define BUFFER 150
#define SIZESTRING 100

//----------------------------
//----------------------------

typedef struct {
  char primeiroNome[SIZESTRING];
  char sobrenome[SIZESTRING];
  char nomeHeroi[SIZESTRING];
  char poder[SIZESTRING];
  char fraqueza[SIZESTRING];
  char cidade[SIZESTRING];
  char profissao[SIZESTRING];
} Heroi;

typedef struct {
  char chave[SIZESTRING]; // chave é a chave canonica de um registro
  int RRN;                // é a referencia p leitura/gravação do registro
} ArrayItem;

//Indice
typedef struct {
  FILE *arqDados; // arquivo de dados (r+)
  FILE *arqIdx;   // arquivo de indices (r+)
  ArrayItem *vetor;  // vetor de pares ordenados {chave, RRN}
  // TODO: adicionar
  // int numeroRegistros
  // bool/int status
} Indice;

//----------------------------
//----------------------------

int numeroRegistros(Indice *idx);
void printaHeroi(Heroi *h);
Heroi quebraStringEmHeroi(char *string);
void iniciaIndiceVazio(Indice *idx);
char* geraChaveRegistro(char* str1, char* str2);
void imprimeVetorIndices(Indice *idx);
void iniciaIndiceArquivo(Indice *idx, char* filename);
void destroiIndice(Indice *idx);
void atualizaStatusHeader(Indice *idx, int status);
void gravaVetorIndices(Indice *idx);

//----------------------------
//----------------------------
