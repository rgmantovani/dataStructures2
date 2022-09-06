//----------------------------
//----------------------------

#include <stdio.h>
#include "Indice.h"

//----------------------------
//----------------------------

int main(int argc, const char * argv[]) {
  Indice ed;
  // iniciaIndiceVazio(&ed);
  iniciaIndiceArquivo(&ed, "heroi.txt");

  imprimeVetorIndices(&ed);

  gravaVetorIndices(&ed);

  destroiIndice(&ed);

  printf("Indice destruido\n");

  return 0;
}

//----------------------------
//----------------------------
