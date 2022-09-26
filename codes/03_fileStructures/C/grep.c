/* --------------------------------------------------- */
/* --------------------------------------------------- */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define BUFFER_LENGTH 1001

/* --------------------------------------------------- */
/* --------------------------------------------------- */

int main(int argc, char * argv[]) {

  char lineBuffer[BUFFER_LENGTH+1];
  int count = 0;
  
  if(argc < 3){
    fprintf( stderr, "A string pattern and a file name are required\n");
    return EXIT_FAILURE;
  }

  FILE* file = fopen(argv[2],"r");
  if(!file){
    fprintf( stderr, "Error - unable to open %s\n", argv[2]);
    return EXIT_FAILURE;
  }

  while(fgets(lineBuffer, BUFFER_LENGTH, file)) {
    if(strstr(lineBuffer, argv[1])){
      printf("%s", lineBuffer);
      count++;
    }
  }
  
  fclose(file);
  printf("found %d occurrences\n", count);
  return EXIT_SUCCESS;
}

/* --------------------------------------------------- */
/* --------------------------------------------------- */
