#include <stdio.h>

int main()
{
    int blockSize[20], processSize[20];
    int allocation[20];
    int nb, np, i, j, worst;

    printf("Enter number of memory blocks: ");
    scanf("%d", &nb);

    printf("Enter size of each block:\n");
    for (i = 0; i < nb; i++)
        scanf("%d", &blockSize[i]);

    printf("Enter number of processes: ");
    scanf("%d", &np);

    printf("Enter size of each process:\n");
    for (i = 0; i < np; i++)
        scanf("%d", &processSize[i]);

    for (i = 0; i < np; i++)
        allocation[i] = -1;

    for (i = 0; i < np; i++)
    {
        worst = -1;

        for (j = 0; j < nb; j++)
        {
            if (blockSize[j] >= processSize[i])
            {
                if (worst == -1 ||
                    blockSize[j] > blockSize[worst])
                {
                    worst = j;
                }
            }
        }

        if (worst != -1)
        {
            allocation[i] = worst;
            blockSize[worst] -= processSize[i];
        }
    }

    printf("\nProcess No.\tProcess Size\tBlock No.\n");

    for (i = 0; i < np; i++)
    {
        printf("%d\t\t%d\t\t", i + 1, processSize[i]);

        if (allocation[i] != -1)
            printf("%d\n", allocation[i] + 1);
        else
            printf("Not Allocated\n");
    }

    return 0;
}
