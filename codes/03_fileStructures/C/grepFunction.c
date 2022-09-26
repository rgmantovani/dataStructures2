/* --------------------------------------------------- */
/* --------------------------------------------------- */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define BUFFER_LENGTH 1001

/* --------------------------------------------------- */
/* --------------------------------------------------- */

char** findPatterns(FILE *file, char *word, int *count) {
   
  *count = 0;
  char lineBuffer[BUFFER_LENGTH+1];
  
  /* find all the occurences and count them */
  while(!feof(file)) {
    fgets(lineBuffer, BUFFER_LENGTH, file);
    if(strstr(lineBuffer, word))
      (*count)++;
  }
  
  /* dinamically allocates memory to the char matrix */
  char **strings = (char**)malloc(*count * sizeof(char*));
  for(int i = 0; i < (*count); i++) {
    strings[i] = (char*)malloc(1000 * sizeof(char));
  }
  
  /* rewind file */
  rewind(file);
   
  *count = 0;
  while(!feof(file)) {
    fgets(lineBuffer, BUFFER_LENGTH, file);
    if(strstr(lineBuffer, word)) {
      strcpy(strings[*count], lineBuffer);
      (*count)++;
    }
  }
  return strings;
}

/* --------------------------------------------------- */
/* --------------------------------------------------- */

int main(int argc, char *argv[]) {
  
  if(argc < 3){
    fprintf( stderr, "A string pattern and a file name are required\n");
    return EXIT_FAILURE;
  }
  
  FILE* file = fopen(argv[2],"r");
  if(!file){
    fprintf( stderr, "Error - unable to open %s\n", argv[2]);
    return EXIT_FAILURE;
  }

  int count = 0;
  char **strings = findPatterns(file, argv[1], &count);

  for(int i = 0; i < count; i++) {
    printf("%s", strings[i]);
  }
  
  fclose(file);
  printf("found %d occurrences\n", count);

  return EXIT_SUCCESS;
}

/* --------------------------------------------------- */
/* --------------------------------------------------- */
