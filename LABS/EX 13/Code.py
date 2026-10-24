
#include <stdio.h>

#define MAX 100

void firstFit(int blocks[], int m, int process[], int n)
{
    int allocation[MAX];
    int i, j;

    for (i = 0; i < n; i++)
        allocation[i] = -1;

    for (i = 0; i < n; i++)
    {
        for (j = 0; j < m; j++)
        {
            if (blocks[j] >= process[i])
            {
                allocation[i] = j;
                blocks[j] -= process[i];
                break;
            }
        }
    }

    printf("\nFirst Fit Allocation:\n");
    printf("Process\tSize\tBlock\n");

    for (i = 0; i < n; i++)
    {
        printf("%d\t%d\t", i + 1, process[i]);

        if (allocation[i] != -1)
            printf("%d\n", allocation[i] + 1);
        else
            printf("Not Allocated\n");
    }
}

void bestFit(int blocks[], int m, int process[], int n)
{
    int allocation[MAX];
    int i, j, best;

    for (i = 0; i < n; i++)
        allocation[i] = -1;

    for (i = 0; i < n; i++)
    {
        best = -1;

        for (j = 0; j < m; j++)
        {
            if (blocks[j] >= process[i])
            {
                if (best == -1 || blocks[j] < blocks[best])
                    best = j;
            }
        }

        if (best != -1)
        {
            allocation[i] = best;
            blocks[best] -= process[i];
        }
    }

    printf("\nBest Fit Allocation:\n");
    printf("Process\tSize\tBlock\n");

    for (i = 0; i < n; i++)
    {
        printf("%d\t%d\t", i + 1, process[i]);

        if (allocation[i] != -1)
            printf("%d\n", allocation[i] + 1);
        else
            printf("Not Allocated\n");
    }
}

void worstFit(int blocks[], int m, int process[], int n)
{
    int allocation[MAX];
    int i, j, worst;

    for (i = 0; i < n; i++)
        allocation[i] = -1;

    for (i = 0; i < n; i++)
    {
        worst = -1;

        for (j = 0; j < m; j++)
        {
            if (blocks[j] >= process[i])
            {
                if (worst == -1 || blocks[j] > blocks[worst])
                    worst = j;
            }
        }

        if (worst != -1)
        {
            allocation[i] = worst;
            blocks[worst] -= process[i];
        }
    }

    printf("\nWorst Fit Allocation:\n");
    printf("Process\tSize\tBlock\n");

    for (i = 0; i < n; i++)
    {
        printf("%d\t%d\t", i + 1, process[i]);

        if (allocation[i] != -1)
            printf("%d\n", allocation[i] + 1);
        else
            printf("Not Allocated\n");
    }
}

int main()
{
    int blocks[MAX], process[MAX];
    int b1[MAX], b2[MAX], b3[MAX];
    int m, n, i, choice;

    printf("Enter number of memory blocks: ");
    scanf("%d", &m);

    printf("Enter sizes of memory blocks:\n");
    for (i = 0; i < m; i++)
        scanf("%d", &blocks[i]);

    printf("Enter number of processes: ");
    scanf("%d", &n);

    printf("Enter sizes of processes:\n");
    for (i = 0; i < n; i++)
        scanf("%d", &process[i]);

    do
    {
        printf("\n--- Memory Allocation Strategies ---\n");
        printf("1. First Fit\n");
        printf("2. Best Fit\n");
        printf("3. Worst Fit\n");
        printf("4. Exit\n");
        printf("Enter your choice: ");
        scanf("%d", &choice);

        for (i = 0; i < m; i++)
        {
            b1[i] = blocks[i];
            b2[i] = blocks[i];
            b3[i] = blocks[i];
        }

        switch (choice)
        {
            case 1:
                firstFit(b1, m, process, n);
                break;

            case 2:
                bestFit(b2, m, process, n);
                break;

            case 3:
                worstFit(b3, m, process, n);
                break;

            case 4:
                printf("Exiting program.\n");
                break;

            default:
                printf("Invalid choice!\n");
        }

    } while (choice != 4);

    return 0;
}
