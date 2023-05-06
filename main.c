#include <stdio.h>
#include <stdlib.h>
#include <time.h>

static unsigned short int WON, LOST, LENGTH;
static char HYPHEN = '-';

static char* repeatChar(char symbol, short int repeat) {
    char* result = (char*)malloc(repeat + 1);
    for (int i = 0; i < repeat; i++) {result[i] = symbol;}
    result[repeat] = '\0';
    return result;
}

static char* getInput(char* message) {
    printf(message);
    char* result;
    scanf("%s", &result);
    return result;
}

int main(void) {
    const char* SEPARATOR = repeatChar(HYPHEN, 80);
    int choice;
    WON = LOST = LENGTH = 0;
    srand(time(0));
    printf("casino game\n");
    printf("choose a color (red / black), number, odd / even: \n");
    scanf("%s", &choice);
    printf("%s", &choice);
    //printf("%s", SEPARATOR);
    return 0;
}