#include <stdio.h>
#include <string.h>

int main()
{
    char files[20][30];
    char name[30];
    int n = 0, choice, i, found;

    while (1)
    {
        printf("\n--- Single Level Directory ---\n");
        printf("1. Create File\n");
        printf("2. Display Files\n");
        printf("3. Search File\n");
        printf("4. Delete File\n");
        printf("5. Exit\n");
        printf("Enter your choice: ");
        scanf("%d", &choice);

        switch (choice)
        {
            case 1:
                printf("Enter file name: ");
                scanf("%29s", name);

                found = 0;
                for (i = 0; i < n; i++)
                {
                    if (strcmp(files[i], name) == 0)
                    {
                        found = 1;
                        break;
                    }
                }

                if (found)
                    printf("File already exists!\n");
                else if (n < 20)
                {
                    strcpy(files[n], name);
                    n++;
                    printf("File created successfully.\n");
                }
                else
                    printf("Directory is full.\n");
                break;

            case 2:
                if (n == 0)
                    printf("Directory is empty.\n");
                else
                {
                    printf("Files in directory:\n");
                    for (i = 0; i < n; i++)
                        printf("%s\n", files[i]);
                }
                break;

            case 3:
                printf("Enter file name to search: ");
                scanf("%29s", name);

                found = 0;
                for (i = 0; i < n; i++)
                {
                    if (strcmp(files[i], name) == 0)
                    {
                        found = 1;
                        break;
                    }
                }

                if (found)
                    printf("File found.\n");
                else
                    printf("File not found.\n");
                break;

            case 4:
                printf("Enter file name to delete: ");
                scanf("%29s", name);

                found = 0;
                for (i = 0; i < n; i++)
                {
                    if (strcmp(files[i], name) == 0)
                    {
                        found = 1;
                        break;
                    }
                }

                if (found)
                {
                    for (; i < n - 1; i++)
                        strcpy(files[i], files[i + 1]);

                    n--;
                    printf("File deleted successfully.\n");
                }
                else
                    printf("File not found.\n");
                break;

            case 5:
                return 0;

            default:
                printf("Invalid choice.\n");
        }
    }
}
