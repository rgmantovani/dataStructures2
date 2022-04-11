void quickSort(int *vetor, int inicio) {
  if(fim < inicio) {
    pivo = criaParticoes(vetor, inicio, fim);
    quickSort(vetor, inicio, pivo-1);
    quickSort(vetor, pivo, fim);
  }
}

int criaParticoes(int *vetor, int inicio, int fim) {

  int esquerda = fim;
  int direita  = inicio;
  int pivo     = vetor[inicio];

  while(esquerda < direita) {
    while(vetor[esquerda] <= vetor[pivo]) {
      esquerda+;
    }

    if(esquerda < direita) {
      swap(&vetor[esquerda], &vetor[direita]);
    }
  }
  vetor[inicio]  = v[direita];
  vetor[direita] = pivo;
  retorna(pivo);
}
