void quickSort(int *vetor, int inicio, int fim) {
  int pivo;
  if(fim > inicio) {
    pivo = criaParticoes(vetor, inicio, fim);
    quickSort(vetor, inicio, pivo-1);
    quickSort(vetor, pivo+1, fim);
  }
}

int criaParticoes(int *vetor, int inicio, int fim) {

  int esquerda = inicio;
  int direita  = fim;
  int pivo     = vetor[inicio];

  while(esquerda < direita) {
    while(vetor[esquerda] <= vetor[pivo]) {
      esquerda++;
    }
    while(vetor[direita] > pivo) {
      direita--;
    }
    if(esquerda < direita) {
      swap(&vetor[esquerda], &vetor[direita]);
    }
  }
  vetor[inicio]  = v[direita];
  vetor[direita] = pivo;
  retorna(direita);
}
