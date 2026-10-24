#include <stdio.h>
#include <pthread.h>
#include <semaphore.h>
#include <unistd.h>

#define N 5

sem_t forks[N];
sem_t room;

void *philosopher(void *arg)
{
    int id = *(int *)arg;

    printf("Philosopher %d is thinking\n", id + 1);

    sem_wait(&room);

    sem_wait(&forks[id]);
    sem_wait(&forks[(id + 1) % N]);

    printf("Philosopher %d is eating\n", id + 1);
    sleep(1);

    sem_post(&forks[id]);
    sem_post(&forks[(id + 1) % N]);

    printf("Philosopher %d finished eating\n", id + 1);

    sem_post(&room);

    return NULL;
}

int main()
{
    pthread_t threads[N];
    int id[N];
    int i;

    // Initialize forks
    for (i = 0; i < N; i++)
    {
        sem_init(&forks[i], 0, 1);
    }

    // Allow at most four philosophers to compete
    sem_init(&room, 0, N - 1);

    // Create philosopher threads
    for (i = 0; i < N; i++)
    {
        id[i] = i;
        pthread_create(&threads[i], NULL, philosopher, &id[i]);
    }

    // Wait for all philosophers to finish
    for (i = 0; i < N; i++)
    {
        pthread_join(threads[i], NULL);
    }

    // Destroy semaphores
    for (i = 0; i < N; i++)
    {
        sem_destroy(&forks[i]);
    }

    sem_destroy(&room);

    printf("All philosophers have finished eating.\n");

    return 0;
}
