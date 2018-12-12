#include <stdio.h>
#include <stdlib.h>
#define MAX 26 // change for max chars in word
#define LINES 250 // known number from file length

int countCommon(char input_1[], char input_2[]);

int main(){

  FILE *filename;
  char * words[LINES];
  filename = fopen("d2-p1.txt", "r");
  int count = LINES;
  int i,j, result;

  for (i=0; i < count; i++){
    words[i] = malloc(26);
    fscanf(filename, "%s", words[i]);
  }

  for (i=0; i<count; i++){
    for (j=0; j<count; j++){
      printf("Comparing: %s and %s ", words[i], words[j]);
      result = countCommon(words[i], words[j]);
      printf("Result: %d\n", result);
    }
  }

  fclose(filename);
  for (i=0; i<count; i++){
    free (words[i]);
  }
  printf("Got to end.\n");
  return 0;
}

int countCommon(char input_1[], char input_2[]){
  int i;
  int score = 0;

  for (i = 0; i < MAX; i++){
    if (input_1[i] == input_2[i]) {
      score++;
    }
  }
  return score;
}
