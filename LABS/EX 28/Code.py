#include <stdio.h>
#include <string.h>

int main()
{
    FILE *fp;
    char filename[100];
    char pattern[100];
    char line[500];
    int found = 0;

    printf("Enter file name: ");
    scanf("%99s", filename);

    printf("Enter word to search: ");
    scanf("%99s", pattern);

    fp = fopen(filename, "r");

    if (fp == NULL)
    {
        printf("Unable to open file.\n");
        return 1;
    }

    while (fgets(line, sizeof(line), fp) != NULL)
    {
        if (strstr(line, pattern) != NULL)
        {
            printf("%s", line);
            found = 1;
        }
    }

    if (!found)
        printf("Pattern not found.\n");

    fclose(fp);

    return 0;
}
