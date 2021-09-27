#include<stdlib.h>
#include<stdio.h>
#define M 2
#define MM  (M * 2)
#define FALSE 0
#define TRUE  1

typedef long TipoChave;
typedef struct TipoRegistro {
  TipoChave Chave;
  /*outros componentes*/
} TipoRegistro;
typedef struct TipoPagina* TipoApontador;
typedef struct TipoPagina {
  short n;
  TipoRegistro r[MM];
  TipoApontador p[MM + 1];
} TipoPagina;

void Inicializa(TipoApontador *Dicionario)
{  *Dicionario = NULL; }

void Pesquisa(TipoRegistro *x, TipoApontador Ap)
{ long i = 1;
  if (Ap == NULL) 
  { printf("TipoRegistro nao esta presente na arvore\n");
    return;
  }
  while (i < Ap->n && x->Chave > Ap->r[i-1].Chave) i++;
  if (x->Chave == Ap->r[i-1].Chave) 
  { *x = Ap->r[i-1];
    return;
  }
  if (x->Chave < Ap->r[i-1].Chave) 
  Pesquisa(x, Ap->p[i-1]);
  else Pesquisa(x, Ap->p[i]);
} 

void InsereNaPagina(TipoApontador Ap, 
                    TipoRegistro Reg, TipoApontador ApDir)
{ short NaoAchouPosicao;
  int k;
  k = Ap->n;  NaoAchouPosicao = (k > 0);
  while (NaoAchouPosicao) 
    { if (Reg.Chave >= Ap->r[k-1].Chave) 
      { NaoAchouPosicao = FALSE;
        break;
      }
      Ap->r[k] = Ap->r[k-1];
      Ap->p[k+1] = Ap->p[k];
      k--;
      if (k < 1) NaoAchouPosicao = FALSE;
    }
  Ap->r[k] = Reg; 
  Ap->p[k+1] = ApDir;
  Ap->n++;
} 

void Ins(TipoRegistro Reg, TipoApontador Ap, short *Cresceu, 
         TipoRegistro *RegRetorno,  TipoApontador *ApRetorno)
{ long i = 1; long j;
  TipoApontador ApTemp;
  if (Ap == NULL) 
  { *Cresceu = TRUE; (*RegRetorno) = Reg; (*ApRetorno) = NULL;
    return;
  }
  while (i < Ap->n && Reg.Chave > Ap->r[i-1].Chave)  i++;
  if (Reg.Chave == Ap->r[i-1].Chave) 
  { printf(" Erro: Registro ja esta presente\n"); *Cresceu = FALSE;
    return;
  }
  if (Reg.Chave < Ap->r[i-1].Chave) i--;
  Ins(Reg, Ap->p[i], Cresceu, RegRetorno, ApRetorno);
  if (!*Cresceu) return;
  if (Ap->n < MM)   /* Pagina tem espaco */
    { InsereNaPagina(Ap, *RegRetorno, *ApRetorno);
      *Cresceu = FALSE;
      return;
    }
  /* Overflow: Pagina tem que ser dividida */
  ApTemp = (TipoApontador)malloc(sizeof(TipoPagina));
  ApTemp->n = 0;  ApTemp->p[0] = NULL;
  if (i < M + 1) 
  { InsereNaPagina(ApTemp, Ap->r[MM-1], Ap->p[MM]);
    Ap->n--;
    InsereNaPagina(Ap, *RegRetorno, *ApRetorno);
  } 
  else InsereNaPagina(ApTemp, *RegRetorno, *ApRetorno);
  for (j = M + 2; j <= MM; j++) 
    InsereNaPagina(ApTemp, Ap->r[j-1], Ap->p[j]);
  Ap->n = M;  ApTemp->p[0] = Ap->p[M+1];
  *RegRetorno = Ap->r[M];  *ApRetorno = ApTemp;
}

void Insere(TipoRegistro Reg, TipoApontador *Ap)
{ short Cresceu;
  TipoRegistro RegRetorno;
  TipoPagina *ApRetorno, *ApTemp;
  Ins(Reg, *Ap, &Cresceu, &RegRetorno, &ApRetorno);
  if (Cresceu)  /* Arvore cresce na altura pela raiz */
  { ApTemp = (TipoPagina *)malloc(sizeof(TipoPagina));
    ApTemp->n = 1; 
    ApTemp->r[0] = RegRetorno;
    ApTemp->p[1] = ApRetorno;
    ApTemp->p[0] = *Ap;  *Ap = ApTemp;
  }
}

void Reconstitui(TipoApontador ApPag, TipoApontador ApPai, 
                 int PosPai, short *Diminuiu)
{ TipoPagina *Aux;  long DispAux, j;
  if (PosPai < ApPai->n)  /* Aux = TipoPagina a direita de ApPag */
  { Aux = ApPai->p[PosPai+1];  DispAux = (Aux->n - M + 1) / 2;
    ApPag->r[ApPag->n] = ApPai->r[PosPai];
    ApPag->p[ApPag->n + 1] = Aux->p[0];  ApPag->n++;
    if (DispAux > 0)  /* Existe folga: transfere de Aux para ApPag */
    { for (j = 1; j < DispAux; j++)
        InsereNaPagina(ApPag, Aux->r[j-1], Aux->p[j]);
      ApPai->r[PosPai] = Aux->r[DispAux-1];  Aux->n -= DispAux;
      for (j = 0; j < Aux->n; j++) Aux->r[j] = Aux->r[j + DispAux];
      for (j = 0; j <= Aux->n; j++) Aux->p[j] = Aux->p[j + DispAux];
      *Diminuiu = FALSE;
    }
    else /* Fusao: intercala Aux em ApPag e libera Aux */
      { for (j = 1; j <= M; j++)
          InsereNaPagina(ApPag, Aux->r[j-1], Aux->p[j]);
        free(Aux);
        for (j = PosPai + 1; j < ApPai->n; j++) 
          { ApPai->r[j-1] = ApPai->r[j]; 
	    ApPai->p[j] = ApPai->p[j+1]; 
	  }
        ApPai->n--;
        if (ApPai->n >= M) *Diminuiu = FALSE;
      }
  }
  else /* Aux = TipoPagina a esquerda de ApPag */
    { Aux = ApPai->p[PosPai-1]; DispAux = (Aux->n - M + 1) / 2;
      for (j = ApPag->n; j >= 1; j--) ApPag->r[j] = ApPag->r[j-1];
      ApPag->r[0] = ApPai->r[PosPai-1];
      for (j = ApPag->n; j >= 0; j--) ApPag->p[j+1] = ApPag->p[j];
      ApPag->n++;
      if (DispAux > 0) /* Existe folga: transf. de Aux para ApPag */
      { for (j = 1; j < DispAux; j++)
          InsereNaPagina(ApPag, Aux->r[Aux->n - j], 
	                 Aux->p[Aux->n - j + 1]);
        ApPag->p[0] = Aux->p[Aux->n - DispAux + 1];
        ApPai->r[PosPai-1] = Aux->r[Aux->n - DispAux];
        Aux->n -= DispAux;  *Diminuiu = FALSE;
      }
      else /* Fusao: intercala ApPag em Aux e libera ApPag */
        { for (j = 1; j <= M; j++)
            InsereNaPagina(Aux, ApPag->r[j-1], ApPag->p[j]);
          free(ApPag);  ApPai->n--;
          if (ApPai->n >= M)  *Diminuiu = FALSE;
        }
    }
}

void Antecessor(TipoApontador Ap, int Ind, 
                TipoApontador ApPai, short *Diminuiu)
{ if (ApPai->p[ApPai->n] != NULL) 
  { Antecessor(Ap, Ind, ApPai->p[ApPai->n], Diminuiu);
    if (*Diminuiu) 
    Reconstitui(ApPai->p[ApPai->n], ApPai, (long)ApPai->n, Diminuiu);
    return;
  }
  Ap->r[Ind-1] = ApPai->r[ApPai->n - 1]; 
  ApPai->n--;  *Diminuiu = (ApPai->n < M);
} 

void Ret(TipoChave Ch, TipoApontador *Ap, short *Diminuiu)
{ long j, Ind = 1;
  TipoApontador Pag;
  if (*Ap == NULL) 
  { printf("Erro: registro nao esta na arvore\n"); *Diminuiu = FALSE;
    return;
  }
  Pag = *Ap;
  while (Ind < Pag->n && Ch > Pag->r[Ind-1].Chave) Ind++;
  if (Ch == Pag->r[Ind-1].Chave) 
  { if (Pag->p[Ind-1] == NULL)   /* TipoPagina folha */
    { Pag->n--;
      *Diminuiu = (Pag->n < M);
      for (j = Ind; j <= Pag->n; j++) 
        { Pag->r[j-1] = Pag->r[j];  Pag->p[j] = Pag->p[j+1]; }
      return;
    }
    /* TipoPagina nao e folha: trocar com antecessor */
    Antecessor(*Ap, Ind, Pag->p[Ind-1], Diminuiu);
    if (*Diminuiu) 
    Reconstitui(Pag->p[Ind-1], *Ap, Ind - 1, Diminuiu);
    return;
  }
  if (Ch > Pag->r[Ind-1].Chave) Ind++;
  Ret(Ch, &Pag->p[Ind-1], Diminuiu);
  if (*Diminuiu) Reconstitui(Pag->p[Ind-1], *Ap, Ind - 1, Diminuiu);
}  

void Retira(TipoChave Ch, TipoApontador *Ap)
{ short Diminuiu;
  TipoApontador Aux;
  Ret(Ch, Ap, &Diminuiu);
  if (Diminuiu && (*Ap)->n == 0)  /* Arvore diminui na altura */
  { Aux = *Ap;   *Ap = Aux->p[0]; 
    free(Aux);
  }
}  

void ImprimeI(TipoApontador p, int nivel)
{ long i;
  if (p == NULL) return;
  printf("Nivel %d : ", nivel);
  for (i = 0; i < p->n; i++)
    printf("%ld ",(long)p->r[i].Chave);
  putchar('\n');
  nivel++;
  for (i = 0; i <= p->n; i++)
    ImprimeI(p->p[i], nivel);
} 

void Imprime(TipoApontador p)
{ int  n = 0; ImprimeI(p, n); } 

void TestaI(TipoApontador p, int pai, short direita)
{ int i;
  int antecessor = 0;
  if (p == NULL) return;
  if (p->r[0].Chave > pai && direita == FALSE) 
  { printf("Erro: filho %12ld maior que pai %d\n", p->r[0].Chave, pai);
    return;
  }
  for (i = 0; i < p->n; i++) 
    { if (p->r[i].Chave <= antecessor) 
      { printf("Erro: irmao %ld maior que irmao a esquerda %d\n",
        (long)p->r[i].Chave, antecessor);
        return;
      }
      antecessor = p->r[i].Chave;
    }
  for (i = 0; i < p->n; i++) 
    TestaI(p->p[i], p->r[i].Chave, FALSE);
  TestaI(p->p[p->n], p->r[i].Chave, TRUE);
}

void Testa(TipoApontador p)
{ int i;
  if (p == NULL) return;
  for (i = 0; i < p->n; i++) 
    TestaI(p->p[i], p->r[i].Chave, FALSE);
  TestaI(p->p[p->n], p->r[i].Chave, TRUE);
}

int main(int argc, char *argv[])
{ TipoRegistro x;
  TipoPagina *D;
  Inicializa(&D);
  printf("Chave: ");
  scanf("%ld%*[^\n]", &x.Chave);
  getchar();
  while (x.Chave != 0) 
    { Insere(x, &D);
      Imprime(D); printf("Chave: ");
      scanf("%ld%*[^\n]", &x.Chave);
      getchar();
    }
  Testa(D);
  printf("Chave: ");
  scanf("%ld%*[^\n]", &x.Chave);
  getchar();
  while (x.Chave != 0) 
    { Retira(x.Chave, &D);
      Imprime(D);
      printf("Chave: ");
      scanf("%ld%*[^\n]", &x.Chave);
      getchar();
    }
  Testa(D);
  return 0;
}
