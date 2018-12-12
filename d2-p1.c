#include <stdio.h>
#include <stdlib.h>
#define MAX 26 // change
#define LINES 250

int countTwice(char[]);
int countThree(char[]);

int main(){

  FILE *filename;
  char input[MAX];

  filename = fopen("d2-p1.txt", "r");
  int count = LINES;
  int i;
  int Threes = 0;
  int Twos = 0;
  int Threes_count = 0;
  int Twos_count = 0;

  for (i=0; i<count; i++){
    fscanf(filename, "%s", input);
    printf("\n%s\n", input);
    Twos = countTwice(input);
    printf("Twice: %d\n", Twos);
    Threes = countThree(input);
    printf("Three: %d\n", Threes);
    if (Twos) {Twos_count++;}
    if (Threes) {Threes_count++;}
  }

  printf("\nTwos total: %d\n", Twos_count);
  printf("Threes total: %d\n", Threes_count);
  printf("Checksum: %d\n", Twos_count * Threes_count);

  fclose(filename);
  printf("Got to end.\n");
  return 0;
}

int countTwice(char input[]){
  int i, bin;
  int count = 0;
  int dist[255]; //ASCII MAX char set

  //printf("%s", input);

  // zero the freq distribution
  for (i=0;i<255;i++){
    dist[i] = 0;
  }

  // increatement the freq
  for (i=0;i<MAX;i++){
    bin = input[i];
    dist[bin]++;
    printf("Incr char: %d\n", bin);
  }

  // start at 1 to avoid counting the null char
  for (i=1;i<255;i++){
    if (dist[i] == 2) {
      printf("Bin %d, %d\n", i, dist[i] );
      count++;
    }
  }
  return count;
}

int countThree(char input[]){
  int i, bin;
  int count = 0;
  int dist[255]; //ASCII MAX char set

  //printf("%s", input);

  // zero the freq distribution
  for (i=0;i<255;i++){
    dist[i] = 0;
  }

  // increatement the freq
  for (i=0;i<MAX;i++){
    bin = input[i];
    dist[bin]++;
    printf("Incr char: %d\n", bin);
  }

  // start at 1 to avoid counting the null char
  for (i=1;i<255;i++){
    if (dist[i] == 3) {
      printf("Bin %d, %d\n", i, dist[i] );
      count++;
    }
  }
  return count;
}
