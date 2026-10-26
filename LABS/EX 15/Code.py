#include <stdio.h>
#include <string.h>

struct Directory
{
    char dirname[30];
    char files[20][30];
    int count;
};

int main()
{
    struct Directory dir[10];
    char dname[30], fname[30];
    int nd = 0, choice, i, j, found;

    while (1)
    {
        printf("\n--- Two Level Directory ---\n");
        printf("1. Create Directory\n");
        printf("2. Create File\n");
        printf("3. Display Files\n");
        printf("4. Search File\n");
        printf("5. Exit\n");
        printf("Enter your choice: ");
        scanf("%d", &choice);

        switch (choice)
        {
            case 1:
                printf("Enter directory name: ");
                scanf("%29s", dname);

                found = 0;
                for (i = 0; i < nd; i++)
                {
                    if (strcmp(dir[i].dirname, dname) == 0)
                    {
                        found = 1;
                        break;
                    }
                }

                if (found)
                    printf("Directory already exists!\n");
                else if (nd < 10)
                {
                    strcpy(dir[nd].dirname, dname);
                    dir[nd].count = 0;
                    nd++;
                    printf("Directory created successfully.\n");
                }
                else
                    printf("Directory limit reached.\n");
                break;

            case 2:
                printf("Enter directory name: ");
                scanf("%29s", dname);

                found = 0;
                for (i = 0; i < nd; i++)
                {
                    if (strcmp(dir[i].dirname, dname) == 0)
                    {
                        found = 1;
                        break;
                    }
                }

                if (!found)
                {
                    printf("Directory not found!\n");
                    break;
                }

                printf("Enter file name: ");
                scanf("%29s", fname);

                for (j = 0; j < dir[i].count; j++)
                {
                    if (strcmp(dir[i].files[j], fname) == 0)
                        break;
                }

                if (j < dir[i].count)
                    printf("File already exists!\n");
                else if (dir[i].count < 20)
                {
                    strcpy(dir[i].files[dir[i].count], fname);
                    dir[i].count++;
                    printf("File created successfully.\n");
                }
                else
                    printf("Directory is full.\n");
                break;

            case 3:
                if (nd == 0)
                    printf("No directories found.\n");

                for (i = 0; i < nd; i++)
                {
                    printf("\nDirectory: %s\n", dir[i].dirname);

                    if (dir[i].count == 0)
                        printf("No files.\n");

                    for (j = 0; j < dir[i].count; j++)
                        printf("%s\n", dir[i].files[j]);
                }
                break;

            case 4:
                printf("Enter directory name: ");
                scanf("%29s", dname);

                found = 0;
                for (i = 0; i < nd; i++)
                {
                    if (strcmp(dir[i].dirname, dname) == 0)
                    {
                        found = 1;
                        break;
                    }
                }

                if (!found)
                {
                    printf("Directory not found!\n");
                    break;
                }

                printf("Enter file name to search: ");
                scanf("%29s", fname);

                found = 0;
                for (j = 0; j < dir[i].count; j++)
                {
                    if (strcmp(dir[i].files[j], fname) == 0)
                    {
                        found = 1;
                        break;
                    }
                }

                if (found)
                    printf("File found in directory %s.\n", dname);
                else
                    printf("File not found.\n");
                break;

            case 5:
                return 0;

            default:
                printf("Invalid choice!\n");
        }
    }
}
