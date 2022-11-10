#include <stdio.h>
#include "Indice.h"

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
