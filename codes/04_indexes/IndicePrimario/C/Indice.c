//------------------------------------------------------------------------------
//------------------------------------------------------------------------------

#include "Indice.h"

//------------------------------------------------------------------------------
//------------------------------------------------------------------------------

int numeroRegistros(Indice *idx) {
    char *string;
    int size, top, qtde, status;
    fseek(idx->arqDados, 0, SEEK_SET); // volta a leitura p começo do arquivo
    fscanf(idx->arqDados, "SIZE=%d TOP=%d QTDE=%d STATUS=%d\n", &size, &top,
      &qtde, &status);
    fseek(idx->arqDados, 0, SEEK_SET); // volta a leitura p começo do arquivo
    return(qtde);
}

//------------------------------------------------------------------------------
//------------------------------------------------------------------------------

void printaHeroi(Heroi *h) {
    printf("------------------\n");
    printf("Nome: %s\n", h->primeiroNome);
    printf("Sobrenome: %s\n", h->sobrenome);
    printf("Nome heroi: %s\n", h->nomeHeroi);
    printf("Poder: %s\n", h->poder);
    printf("Fraqueza: %s\n", h->fraqueza);
    printf("Cidade: %s\n", h->cidade);
    printf("Profissao: %s\n", h->profissao);
    printf("------------------\n");
}

//------------------------------------------------------------------------------
//------------------------------------------------------------------------------

Heroi quebraStringEmHeroi(char *string) {
    Heroi ret;
    char* aux = strtok(string, "|\n");
    strcpy(ret.primeiroNome, aux);
    aux = strtok(NULL, "|\n");
    strcpy(ret.sobrenome, aux);
    aux = strtok(NULL, "|\n");
    strcpy(ret.nomeHeroi, aux);
    aux = strtok(NULL, "|\n");
    strcpy(ret.poder, aux);
    aux = strtok(NULL, "|\n");
    strcpy(ret.fraqueza, aux);
    aux = strtok(NULL, "|\n");
    strcpy(ret.cidade, aux);
    aux = strtok(NULL, "|\n");
    strcpy(ret.profissao, aux);
    return (ret);
}

//------------------------------------------------------------------------------
//------------------------------------------------------------------------------

// Inicialização
void iniciaIndiceVazio(Indice *idx) {
    idx->arqDados         = fopen("arqDados.txt", "w+");
    idx->arqIdxPrimario   = fopen("arqIdxPrimario.txt", "w+");
    idx->arqIdxSecundario = fopen("arqIdxSecundario.txt", "w+");
    fprintf(idx->arqDados, "SIZE=133 TOP=-1 QTDE=0 STATUS=0\n");
}

//------------------------------------------------------------------------------
//------------------------------------------------------------------------------

char* geraChaveRegistro(char* str1, char* str2) {
    int posicao = 0;
    strcat(str1, str2);
    for(int i = 0; str1[i]; i++) {
      if(str1[i] != ' ') {
        str1[posicao++] = toupper(str1[i]);
      }
    }
    str1[posicao] = '\0';
    return(str1);
}

//------------------------------------------------------------------------------
//------------------------------------------------------------------------------

void imprimeVetorIndices(Indice *idx) {
    printf("--------------------------------\n");
    printf(" *** Vetor de Indices *** \n");
    printf("--------------------------------\n");
    int N = numeroRegistros(idx);
    for(int i = 0; i < N; i++) {
        printf("Vetor[%d] = {%s, %d}\n",
          i, idx->vetor[i].chave, idx->vetor[i].RRN);
    }
    printf("--------------\n");
}

//------------------------------------------------------------------------------
//------------------------------------------------------------------------------

void iniciaIndiceArquivo(Indice *idx, char* filename) {

    idx->arqDados = fopen(filename, "r+");
    idx->arqIdxPrimario  = fopen("arqIdxPrimario.txt", "w+");
    //TODO: criar o arquivo de indice secundario

    int N = numeroRegistros(idx);
    printf("Numero de registros = %d\n", N);
    idx->vetor = (ArrayItem*)malloc(N * sizeof(ArrayItem));

    int linhas = 0;
    Heroi heroi;
    char string[BUFFER];
    ArrayItem objeto;

    // lendo cabeçalho
    fgets(string, BUFFER, idx->arqDados);
    printf("Leitura: %s\n", string);

    while(!feof(idx->arqDados)) {
      if(fgets(string, BUFFER, idx->arqDados)!= NULL) {
        heroi = quebraStringEmHeroi(string);
        // printaHeroi(&heroi);
        char* chave = geraChaveRegistro(heroi.primeiroNome, heroi.sobrenome);
        // Jogar a informação dentro do vetor de Indices {chave, RRN}
        strcpy(objeto.chave, chave);
        objeto.RRN = linhas;
        idx->vetor[linhas] = objeto;
        linhas++;
      }
    } // voltando o cabeçote de leitura p começo do arquivo
    rewind(idx->arqDados);
}

//------------------------------------------------------------------------------
//------------------------------------------------------------------------------

void atualizaStatusHeader(Indice *idx, int status) {
    int size, top, qtde, oldStatus;
    fseek(idx->arqDados, 0, SEEK_SET); // volta a leitura p começo do arquivo
    fscanf(idx->arqDados, "SIZE=%d TOP=%d QTDE=%d STATUS=%d\n", &size, &top,
      &qtde, &oldStatus);
    fseek(idx->arqDados, 0, SEEK_SET); // volta a leitura p começo do arquivo
    fprintf(idx->arqDados, "SIZE=%d TOP=%d QTDE=%d STATUS=%d\n", size, top,
      qtde, status);
}

//------------------------------------------------------------------------------
//------------------------------------------------------------------------------

void gravaVetorIndices(Indice *idx) {
    int N = numeroRegistros(idx);
    for(int i = 0; i < N; i++) {
      ArrayItem item = idx->vetor[i];
      fprintf(idx->arqIdx, "{%s,%d}\n", item.chave, item.RRN);
    }
    atualizaStatusHeader(idx, 1);
}

//------------------------------------------------------------------------------
//------------------------------------------------------------------------------

void destroiIndice(Indice *idx) {
    gravaVetorIndices(idx);   // dump do arquivo de indice no arq aux
    free(idx->vetor);         // desalocar memoria do vetor
    fclose(idx->arqDados);    // fecha o arquivo de dados
    fclose(idx->arqIdx);      // fecha o arquivo de indice
}

//------------------------------------------------------------------------------
//------------------------------------------------------------------------------
