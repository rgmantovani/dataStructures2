#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

#define BUFFER 150
//----------------------------
//----------------------------

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
  FILE *arqDados; // arquivo de dados (r+)
  FILE *arqIdx;   // arquivo de indices (r+)
  ArrayItem *vetor;  // vetor de pares ordenados {chave, RRN}
  // TODO: adicionar
  // int numeroRegistros
  // bool/int status
} Indice;

//----------------------------
//----------------------------

int numeroRegistros(Indice *idx) {
  char *string;
  // fgets(string, 100, idx->arqDados);
  int size, top, qtde, status;

  fseek(idx->arqDados, 0, SEEK_SET); // volta a leitura p começo do arquivo
  fscanf(idx->arqDados, "SIZE=%d TOP=%d QTDE=%d STATUS=%d\n", &size, &top,
    &qtde, &status);
  // DEBUG
  printf("SIZE=%d TOP=%d QTDE=%d STATUS=%d\n", size, top, qtde, status);
  fseek(idx->arqDados, 0, SEEK_SET); // volta a leitura p começo do arquivo
  // SIZE=133 TOP=-1 QTDE=0 STATUS=0
  return(qtde);
}

// ---------------------------------------
// ---------------------------------------

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

// ---------------------------------------
// ---------------------------------------
// string = Barry|Allen|Flash|correr|cadarço|Star city|policial forense
Heroi quebraStringEmHeroi(char *string) {
  Heroi ret; // retorno
  char* aux = strtok(string, "|\n");
  // acessar todos os campos
  // strcpy(destino, source)
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
  // printf("Debugão: .....\n");
  // printaHeroi(&ret);
  return (ret);
}

// ---------------------------------------
// ---------------------------------------

// 1. inicialização
//   - arqDados (pode existir ou não)
//      * se ele existir: carregar as informações p criar o vetor
//      * se ele não existir: cria um arquivo em branco (só add header)
//   - arqIdx
//   - vetor (criador com base no arqDados)
void iniciaIndiceVazio(Indice *idx) {
    idx->arqDados = fopen("arqDados.txt", "w+");
    idx->arqIdx   = fopen("arqIdx.txt", "w+");
    //vetor
    // escrever o header no arqDados
    fprintf(idx->arqDados, "SIZE=133 TOP=-1 QTDE=0 STATUS=0\n");
}

// ---------------------------------------
// ---------------------------------------
//  str1, str2
//  chave = str1 + str2 -> letra maiuscula
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

// ---------------------------------------
// ---------------------------------------

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

// ---------------------------------------
// ---------------------------------------

void iniciaIndiceArquivo(Indice *idx, char* filename) {
  idx->arqDados = fopen(filename, "r+");
  idx->arqIdx   = fopen("arqIdx.txt", "w+");

  // N = qtde de registros (arq)
  int N = numeroRegistros(idx);
  printf("Numero de registros = %d\n", N);
  idx->vetor = (ArrayItem*)malloc(N * sizeof(ArrayItem));

  // percorrer o arqDados
  int linhas = 0;
  Heroi heroi;
  char string[BUFFER];
  ArrayItem objeto;

  // lendo cabeçalho
  fgets(string, BUFFER, idx->arqDados);
  printf("Leitura: %s\n", string);

  // for(int i = 0; i < 4; i++) {
  while(!feof(idx->arqDados)) {
    if(fgets(string, BUFFER, idx->arqDados)!= NULL) {
      printf("Reg: %s", string);
      // Barry|Allen|Flash|correr|cadarço|Star city|policial forense
      // str -> obj (Heroi)
      heroi = quebraStringEmHeroi(string);
      printaHeroi(&heroi);
      //    - gerar a chave e o RRN
      char* chave = geraChaveRegistro(heroi.primeiroNome, heroi.sobrenome);
      printf("CHAVE = %s\n", chave);
      printf("RRN = %d\n", linhas);
      printf("----------\n");

      // Jogar a informação dentro do vetor de Indices
      //    - vetor[i] = {chave, RNN}
      strcpy(objeto.chave, chave);
      objeto.RRN = linhas;
      printf("RRN do objeto = %d\n", objeto.RRN);
      printf("CHAVE do objeto = %s\n", objeto.chave);
      idx->vetor[linhas] = objeto;
      linhas++;
    }
  } // voltando o cabeçote de leitura p começo do arquivo
  rewind(idx->arqDados);
}

// ---------------------------------------
// ---------------------------------------

void destroiIndice(Indice *idx) {
  // atualizarIdxAux(idx);     // TODO: dump do arquivo de indice no arq aux
  // free(idx->vetor);         // desalocar memoria do vetor
  fclose(idx->arqDados);    // fecha o arquivo de dados
  fclose(idx->arqIdx);      // fecha o arquivo de indice
}

//----------------------------
//----------------------------

// 2. inserir (registro) -> arqDados -> vetor
//    - Se existe posição p ser reutilizada:
//        insere com reuso
//    - Senão: add no final do arquivo (append)
//    - Atualiza o cabeçalho p falso (entrou informação)
//    - Add {chave, RRN} do novo registro no vetor
//    - Ordena
//    - Passa p arquivo de Indice (coloca true no cabeçalho do arquivo de dados)

// 3. Remoção (registro) -> arqDados (chave)
//    - remove do arquivo de dados (invalida - *)
//        atualiza no cabeçalho do arq dados (pilha lógica)
//    - remove do vetor (busca binária)
//    - reordena o indice
//    - passa p arquivo de indice (coloca true na flag do header do arqDados)

// 4. Pesquisar (chave)
//    - vai no indice (memoria) e procura pela chave
//      busca binaria
//    - se não achou? retorna falso (não achou)
//    - se achou? pegar o RRN da chave consultada no vetor/lista
//        - usa o RRN p ler o registro la do arqDados
//        - retorna o registro todo p usuario

// 5. Grava/Salva o Indice (vetor) no arqIdx
//      - percorre o vetor/lista posição por posição
//            - para cada posicao (elemento)
//            - gravar no arqIdx

// 6. Ler/Carregar o Indice de um arquivo (arqIdx)
//      - percorrer o arquivo (linha/linha) pos/pos
//            - para valor lido (elemento)
//            - add no Indice (vetor/lista)

// 7. Destruir a estrutura
//     - Destruir a lista (salvar o Indice no arqdIdx)
//     - vetor: desalocar memoria, lista: destruir Lista
//     - fechar os arquivos (arqDados, arqIdx)

// 8. Numero Registros
//     - acessa o arqDados
//     - faz a leitura do cabecalho (header)
//     - identifica a quantidade de registros
//     - retorna p user/programa

// 9. Atualizar o cabeçalho arqDados (flag)
//    - sobreescreve o valor da flag no header
//    - se é true vira false, se é false vira true

//----------------------------
//----------------------------

void atualizaStatusHeader(Indice *idx, int status) {
  // TODO: Otimizar (pensando em string replace)
  int size, top, qtde, oldStatus;
  // garantir que estamos acessando a primeira linha do arquivo
  fseek(idx->arqDados, 0, SEEK_SET); // volta a leitura p começo do arquivo
  // frpintf(status)
  fscanf(idx->arqDados, "SIZE=%d TOP=%d QTDE=%d STATUS=%d\n", &size, &top,
    &qtde, &oldStatus);
  fseek(idx->arqDados, 0, SEEK_SET); // volta a leitura p começo do arquivo
  fprintf(idx->arqDados, "SIZE=%d TOP=%d QTDE=%d STATUS=%d\n", size, top,
    qtde, status);
  fseek(idx->arqDados, 0, SEEK_SET); // volta a leitura p começo do arquivo
}

//----------------------------
//----------------------------

void gravaVetorIndices(Indice *idx) {
  // gravar no arquivo de Indices
  int N = numeroRegistros(idx);
  for(int i = 0; i < N; i++) {
    ArrayItem item = idx->vetor[i];
    fprintf(idx->arqIdx, "{%s,%d}\n", item.chave, item.RRN);
  }
  atualizaStatusHeader(idx, 1);
}

//----------------------------
//----------------------------


int main(int argc, const char * argv[]) {
  Indice ed;
  // iniciaIndiceVazio(&ed);
  // printf("Criei indice vazio\n");
  iniciaIndiceArquivo(&ed, "heroi.txt");
  printf("Criei indice de arquivo\n");
  imprimeVetorIndices(&ed);
  gravaVetorIndices(&ed);
  destroiIndice(&ed);
  printf("Indice destruido\n");
  return 0;
}



















//----------------------------
//----------------------------
