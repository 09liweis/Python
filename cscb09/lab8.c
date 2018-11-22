#include <stdio.h>
#include <stdlib.h>

int main(int argc, char **argv)
{
    FILE *fp;
    char c;

    if (argc < 2) {
        printf("Please run program with file\n");
        exit(1);
    } else {
        fp = fopen(argv[1], "r+");
        if (fp == NULL) {
            perror(fp);
            return(-1);
        }
        while ((c = getc(fp)) > 0) {
            putchar(c);
        }
        fclose(fp);   
    }

    return 1;
}