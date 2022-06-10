#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>
#include <stdbool.h>
#define MAX_SIZE_PK 40              // tamanho maximo de chave primaria

typedef struct{
  int size;
  int top;
  int qtde;
  int status;
} HeaderInfo;

typedef struct {
  char ano[5];    // XXXX
  char duracao[6]; // XX:XX
  char titulo[31];
  char artista[21];
  char genero[12];
  char idioma[12];
} Musica;

typedef struct {
  char chavePrimaria[MAX_SIZE_PK];  // chavePrimaria (titulo + artista)
  int RRN;       // RRN
} ItemArrayPrimario;

typedef struct {
  char chavePrimaria[MAX_SIZE_PK];
  char chaveSecundaria[15];
} ItemArraySecundario;

typedef struct {
  FILE *arqDados;         // arquivo com os dados (brutos/reais)
  FILE *arqIdxPrimario;   // arquivo de dump do indice primario
  FILE *arqIdxSecundario; // arquivo de dump do indice secundario (generos)
  ItemArrayPrimario *arrayPrimario;     //arrayPrimario
  ItemArraySecundario *arraySecundario; //arraySecundario
} IndiceSecundario;

// -----------------------------------------
// -----------------------------------------

char* criarChavePrimaria(char* titulo, char* artista) {
  // concatena, maiusculo
  char* chave = malloc(MAX_SIZE_PK * sizeof(char));
  strcpy(chave, titulo);
  strcat(chave, artista);
  // printf("Merge = %s\n", chave);
  for(int i = 0; i < strlen(chave); i++) {
    chave[i] = toupper(chave[i]);
  }
  return(chave);
}

// -----------------------------------------
// -----------------------------------------

char* criarChaveSecundaria(char* genero) {
  for (int i = 0; i < strlen(genero); i++) {
    genero[i] = toupper(genero[i]);
  }
  return(genero);
}

// -----------------------------------------
// -----------------------------------------

// leitura da quantidade de registros (cabecalho)
HeaderInfo numeroRegistrosCabecalho(IndiceSecundario *idx) {
  // garante: cabeçote está no começo do arquivo
  fseek(idx->arqDados, 0, SEEK_SET);
  HeaderInfo ret;
  fscanf(idx->arqDados, "SIZE=%d TOP=%d QTDE=%d STATUS=%d\n", &ret.size,
    &ret.top, &ret.qtde, &ret.status);
  return(ret);
}

// -----------------------------------------
// -----------------------------------------

Musica quebraStringEmMusica(char *linha) {

  Musica music;
  char *pch;
  pch = strtok(linha,"|\n");
  strcpy(music.ano, pch);
  pch = strtok(NULL,"|\n");
  strcpy(music.duracao, pch);
  pch = strtok(NULL,"|\n");
  strcpy(music.titulo, pch);
  pch = strtok(NULL,"|\n");
  strcpy(music.artista, pch);
  pch = strtok(NULL,"|\n");
  strcpy(music.genero, pch);
  pch = strtok(NULL,"|\n");
  strcpy(music.idioma, pch);

  return(music);
}

// -----------------------------------------
// -----------------------------------------


// ordernar indice primario
// ordernar indice secundario
// atualizar o status do arqDados
// leitura de registro -> Musica (artista, titulo, genero)
// gravar indice primario no arquivo primario
// gravar indice secundario no arquivo secundario

// -----------------------------------------
// -----------------------------------------


void iniciaIndiceSecundario(IndiceSecundario *ds, char* nomeArquivo) {

  // abrir os arquivos
  ds->arqDados         = fopen(nomeArquivo, "r+");
  ds->arqIdxPrimario   = fopen("indicePrimario.txt", "w+");
  ds->arqIdxSecundario = fopen("IndiceSecundario.txt", "w+");

  // descobrir qtde de registros no arquivo de arqDados
  HeaderInfo info = numeroRegistrosCabecalho(ds);
  printf("Numero de Registros: %d\n", info.qtde);

  // alocar memoria do arrayPrimario
  ds->arrayPrimario   = malloc(info.qtde * sizeof(ItemArrayPrimario));
  // alocar memoria do arraySecundario
  ds->arraySecundario = malloc(info.qtde * sizeof(ItemArraySecundario));

  // Percorre o arquivo (laço):
  char linha[info.size+1];
  char keyP[MAX_SIZE_PK], keyS[MAX_SIZE_PK];
  Musica registro;
  int RRN = 0;
  ItemArrayPrimario iap;
  ItemArraySecundario ias;

  while(fgets(linha, info.size, ds->arqDados) != NULL) {
    // iteração = registro (ano|duracao|titulo|artista|...)
    registro = quebraStringEmMusica(linha);
    // criar chave canonica primaria
    strcpy(keyP, criarChavePrimaria(registro.titulo, registro.artista));
    //     criar chave canonica secundaria (Genero)
    strcpy(keyS,criarChaveSecundaria(registro.genero));
    printf("==========================\n");
    // insere no array primario: (chave primaria | RNN)
    strcpy(iap.chavePrimaria, keyP);
    iap.RRN = RRN;
    ds->arrayPrimario[RRN] = iap;
    //     insere no array secundario (chave secundaria | chave primaria)
    strcpy(ias.chavePrimaria, keyP);
    strcpy(ias.chaveSecundaria, keyS);
    printf("keyP = %s\n", ias.chavePrimaria);
    printf("keyS = %s\n", ias.chaveSecundaria);
    ds->arraySecundario[RRN] = ias;
    RRN++;
  }

  // Ordena:
  //     ordena arraySecundario (se tiver chaves iguais, considerar a primaria)
  //     ordena arrayPrimario
  // Abrir/Criar os arquivos de dump
  //      grava o indice primario (arqIdxPrimario)
  //      grava o indice secundario (arqIdxSecundario)
  // Atualiza o STATUS do header (arq Dados) -> TRUE
}
// -----------------------------------------
// -----------------------------------------

void imprimeIndiceSecundario(IndiceSecundario *ds) {
  // int N = sizeof(ds->arraySecundario)/sizeof(ds->arraySecundario[0]);
  int N = numeroRegistrosCabecalho(ds).qtde;
  // percorrer e imprimir as posicoes dos vetores
  ItemArrayPrimario iap;
  ItemArraySecundario ias;
  printf("====================================\n");
  printf(" IDX PRIM | IDX SEC\n");
  printf("====================================\n");
  printf("N = %d\n", N);
  for(int i = 0; i < N; i++) {
    iap = ds->arrayPrimario[i];
    ias = ds->arraySecundario[i];
    printf("%d: [%s | %d] [%s | %s]\n", i, iap.chavePrimaria, iap.RRN,
      ias.chaveSecundaria, ias.chavePrimaria);
  }
  printf("====================================\n");

}

// -----------------------------------------
// -----------------------------------------

void destroiIndiceSecundario(IndiceSecundario *ds) {
    // verifica se não está atualizado no arquivo
    //      gravar os indices nos arquivos de dump
    // desalocar os vetores (arrayPrimario, arraySecundario)
    // fechar os arquivos (dumps, dados)
}

// -----------------------------------------
// -----------------------------------------

int main(int argc, char *argv[]) {
  IndiceSecundario secondIdx;
  // Inicia Indice Secundario baseado no arquivo já existente
  iniciaIndiceSecundario(&secondIdx, "arqMusicas.txt");
  imprimeIndiceSecundario(&secondIdx);
  // destroiIndiceSecundario(&secondIdx);

  return 0;
}

// -----------------------------------------
// -----------------------------------------
