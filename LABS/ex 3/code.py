#include <stdio.h>

int main() {
    int n, burst[20], wait[20] = {0}, turnaround[20];

    printf("Enter number of processes: ");
    scanf("%d", &n);

    printf("Enter burst time for each process:\n");
    for (int i = 0; i < n; i++) {
        printf("P%d: ", i + 1);
        scanf("%d", &burst[i]);
    }

    for (int i = 0; i < n; i++) {
        if (i > 0)
            wait[i] = wait[i - 1] + burst[i - 1];

        turnaround[i] = wait[i] + burst[i];
    }

    printf("\nProcess\tBurst\tWaiting\tTurnaround\n");
    for (int i = 0; i < n; i++)
        printf("P%d\t%d\t%d\t%d\n", i + 1, burst[i], wait[i], turnaround[i]);

    return 0;
}
