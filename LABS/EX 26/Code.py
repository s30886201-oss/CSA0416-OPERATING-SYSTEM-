#include <stdio.h>

int main()
{
    FILE *fp;
    char filename[50], text[200];
    int choice;
    char ch;

    while (1)
    {
        printf("\n--- File Management Operations ---\n");
        printf("1. Create File\n");
        printf("2. Write to File\n");
        printf("3. Read File\n");
        printf("4. Append to File\n");
        printf("5. Delete File\n");
        printf("6. Exit\n");
        printf("Enter your choice: ");
        scanf("%d", &choice);

        if (choice == 6)
            break;

        printf("Enter file name: ");
        scanf("%49s", filename);

        switch (choice)
        {
            case 1:
                fp = fopen(filename, "w");
                if (fp != NULL)
                {
                    printf("File created successfully.\n");
                    fclose(fp);
                }
                else
                    printf("Unable to create file.\n");
                break;

            case 2:
                fp = fopen(filename, "w");
                if (fp != NULL)
                {
                    printf("Enter text: ");
                    scanf(" %199[^\n]", text);
                    fprintf(fp, "%s\n", text);
                    fclose(fp);
                    printf("Data written successfully.\n");
                }
                else
                    printf("Unable to open file.\n");
                break;

            case 3:
                fp = fopen(filename, "r");
                if (fp != NULL)
                {
                    printf("File contents:\n");
                    while ((ch = fgetc(fp)) != EOF)
                        putchar(ch);
                    fclose(fp);
                }
                else
                    printf("File not found.\n");
                break;

            case 4:
                fp = fopen(filename, "a");
                if (fp != NULL)
                {
                    printf("Enter text to append: ");
                    scanf(" %199[^\n]", text);
                    fprintf(fp, "%s\n", text);
                    fclose(fp);
                    printf("Data appended successfully.\n");
                }
                else
                    printf("Unable to open file.\n");
                break;

            case 5:
                if (remove(filename) == 0)
                    printf("File deleted successfully.\n");
                else
                    printf("Unable to delete file.\n");
                break;

            default:
                printf("Invalid choice.\n");
        }
    }

    return 0;
}
